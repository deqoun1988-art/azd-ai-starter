// playwright.config.js
import { defineConfig, devices } from '@playwright/test';

const useLocalServer = true;

export default defineConfig({
  testDir: './tests/e2e',
  testMatch: '*.spec.Js',
  timeout: 180000,
  expect: { timeout: 5000 },
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:4321',
    browserName: 'chromium',
    trace: 'on-first-retry',
    headless: true,
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
  webServer: [
    {
      command: 'cd src/template-framework-docs && npm install && npm run dev',
      url: 'http://localhost:4321',
      reuseExistingServer: useLocalServer,
    }
],
});
