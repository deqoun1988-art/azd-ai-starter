import importlib.util
import os
from pathlib import Path
import types


MODULE_PATH = Path(__file__).resolve().parents[1] / ".github" / "validator" / "validator.py"
SPEC = importlib.util.spec_from_file_location("validator_module", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_valid_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / ".github" / "workflows").mkdir(parents=True)
    (repo / "infra").mkdir()
    (repo / ".devcontainer").mkdir()

    write_file(
        repo / "README.md",
        """
# Sample Project

## Features

## Getting Started

## Guidance

## Resources
""".strip(),
    )
    write_file(repo / "LICENSE", "MIT License")
    write_file(repo / "SECURITY.md", "# Security")
    write_file(repo / ".github" / "CODE_OF_CONDUCT.md", "# Code of Conduct")
    write_file(repo / "CONTRIBUTING.md", "# Contributing")
    write_file(repo / ".github" / "ISSUE_TEMPLATE.md", "# Issue")
    write_file(repo / "azure.yaml", "name: demo\nservices: {}\n")
    write_file(
        repo / ".github" / "workflows" / "pr-gate.yml",
        """
name: validation
on: [pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: microsoft/security-devops-action@v1
      - uses: github/codeql-action/upload-sarif@v3
""".strip(),
    )
    write_file(
        repo / ".github" / "workflows" / "azure-dev.yml",
        """
name: deploy
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/setup-azd@v1.0.0
""".strip(),
    )
    return repo


def test_check_topic_existence_requires_expected_topics():
    success, success_message = validator.check_topic_existence(
        "azd-templates,ai-azd-templates",
        validator.expected_topics,
    )
    assert success is True
    assert "azd-templates" in success_message

    failure, failure_message = validator.check_topic_existence(
        "azure,examples",
        validator.expected_topics,
    )
    assert failure is False
    assert "ai-azd-templates" in failure_message
    assert "missing" in failure_message


def test_check_file_existence_validates_required_h2_sections(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "# Demo\n\n## Features\n\n## Getting Started\n\n## Guidance\n\n## Resources\n",
        encoding="utf-8",
    )

    success, success_message = validator.check_file_existence(
        str(tmp_path),
        "README.md",
        validator.readme_h2_tags,
    )
    assert success is True
    assert "README.md File" in success_message

    readme_path.write_text(
        "# Demo\n\n## Features\n\n## Getting Started\n",
        encoding="utf-8",
    )

    failure, failure_message = validator.check_file_existence(
        str(tmp_path),
        "README.md",
        validator.readme_h2_tags,
    )
    assert failure is False
    assert "Guidance" in failure_message


def test_check_msdo_result_handles_missing_scan_file_and_security_errors(monkeypatch):
    missing_result, missing_message = validator.check_msdo_result(None)
    assert missing_result is False
    assert "missing" in missing_message.lower()

    class FakeSarif:
        @staticmethod
        def get_records_grouped_by_severity():
            return {
                "error": [
                    {"Code": "AZR-000283", "Description": "Known issue to ignore."},
                    {"Code": "AZR-000999", "Description": "Real security problem."},
                ],
                "warning": [{"Code": "WARN-01", "Description": "Warning only."}],
            }

    monkeypatch.setattr(validator.loader, "load_sarif_file", lambda _: FakeSarif())
    monkeypatch.setattr(validator.os.path, "isfile", lambda _: True)

    result, message = validator.check_msdo_result("fake-results.sarif")
    assert result is False
    assert "AZR-000999" in message
    assert "warning" in message.lower()


def test_check_for_actions_in_workflow_file_flags_missing_security_steps(tmp_path):
    repo = tmp_path / "repo"
    workflow_dir = repo / ".github" / "workflows"
    workflow_dir.mkdir(parents=True)
    write_file(
        workflow_dir / "pr-gate.yml",
        """
name: validation
jobs:
  validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo 'no security action here'
""".strip(),
    )

    result, message = validator.check_for_actions_in_workflow_file(
        str(repo),
        ".github/workflows/pr-gate.yml",
        validator.security_actions,
    )
    assert result is False
    assert "microsoft/security-devops-action" in message
    assert "github/codeql-action/upload-sarif" in message


def test_check_for_azd_commands_restores_cwd(monkeypatch, tmp_path):
    start_dir = tmp_path / "start"
    start_dir.mkdir()
    target_dir = tmp_path / "target"
    target_dir.mkdir()

    original = os.getcwd()
    os.chdir(start_dir)

    try:
        calls = []

        def fake_run(command, capture_output, text, check, shell):
            calls.append((os.getcwd(), command))
            return types.SimpleNamespace(stdout="ok")

        monkeypatch.setattr(validator.subprocess, "run", fake_run)

        success, message = validator.check_for_azd_up(str(target_dir))
        assert success is True
        assert "azd up" in message
        assert calls[0][0] == str(target_dir)
        assert calls[0][1] == "azd up --no-prompt"

        success, message = validator.check_for_azd_down(str(target_dir))
        assert success is True
        assert "azd down" in message
        assert calls[1][0] == str(target_dir)
        assert calls[1][1] == "azd down --force --purge"

        assert os.getcwd() == str(start_dir)
    finally:
        os.chdir(original)


def test_internal_validator_passes_for_valid_repo(monkeypatch, tmp_path):
    repo = build_valid_repo(tmp_path)

    monkeypatch.setattr(
        validator,
        "check_msdo_result",
        lambda _: (True, "<details><summary>Security scan passed.</summary></details>"),
    )

    passed, message = validator.internal_validator(
        str(repo),
        False,
        False,
        "azd-templates,ai-azd-templates",
        "unused.sarif",
    )

    assert passed is True
    assert "Repository Management:" in message
    assert "Source code structure and conventions:" in message
    assert "Functional Requirements:" in message
    assert "Security Requirements:" in message
