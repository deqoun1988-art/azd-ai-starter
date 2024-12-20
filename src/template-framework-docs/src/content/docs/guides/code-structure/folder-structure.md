---
title: Folder structure
description: A comprehensive guide to building templates.
---

- [C# and .NET project folder structure](#c-and-net-project-folder-structure)
- [Java project folder structure](#java-project-folder-structure)
- [JavaScript project folder structure](#javascript-project-folder-structure)
- [Python project folder structure](#python-project-folder-structure)

## C# and .NET project folder structure

The following guidelines and the folders included, represent the conventional structure for a C#/.NET standard application.

```bash
~root
│
├── .devcontainer
│    ├── devcontainer.json
│    └── post-create-command.sh
│      
├── .github/
│   └── workflows/
│       ├── workflow1.yml
│       ├── workflow2.yml
│       └── ...                     
│
├── infra/
│   ├── main.bicep
│   ├── main.parameters.bicep
│   ├── abbreviations.json
│   └── ...                         
│
├── src/
│   ├── ProjectName.Core/
│   │   ├── Models/
│   │   ├── Services/
│   │   ├── Repositories/
│   │   └── ...
│   ├── ProjectName.Web/
│   │   ├── Controllers/
│   │   ├── Views/
│   │   ├── wwwroot/
│   │   └── ...
│   ├── ProjectName.Tests/
│   │   ├── Unit/
│   │   ├── Integration/
│   │   └── ...
│   └── ProjectName.sln
│
├── *docs/
│   └── ...
│
├── tools/
│
├── scripts/
│
├── .gitignore
├── azure.yaml
└── README.md

```
* optional additional docs folder for extended documentation files

# Recommended coding styleguide

C# AZD templates follow the [common C# code conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) used for documentation & samples.

## Java project folder structure

The following guidelines and the folders included, represent the conventional structure for a Java standard application.

```bash

~root
│
├── .devcontainer
│    ├── devcontainer.json
│    └── post-create-command.sh
├── .github/
│   └── workflows/
│       ├── workflow1.yml
│       ├── workflow2.yml
│       └── ...                     
│
├── infra/
│   ├── main.bicep
│   ├── main.parameters.bicep
│   ├── abbreviations.json
│   └── ...
│
├── azure.yaml
├── pom.xml
├── README.md
├── src/                            
│   ├── main/                       
│   │   ├── java/                   
│   │   │   ├── com/                
│   │   │   │   ├── projectname/    
│   │   │   │   │   ├── controllers/ 
│   │   │   │   │   ├── services/    
│   │   │   │   │   ├── models/      
│   │   │   │   │   └── ...
│   │   │   │   └── ...
│   │   │   └── ...
│   │   └── resources/              
│   │
│   └── test/                       
│
├── *docs/
|   └── ...                          
│
├── build/                          
│
├── lib/                            
│
└── scripts/                        


```
* optional additional docs folder for extended documentation files

# Recommended coding styleguide

TBD

C# AZD templates follow the [common C# code conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) used for documentation & samples.

## JavaScript project folder structure

The following guidelines and the folders included, represent the conventional structure for a JavaScript or TypeScript standard application, as an npm package.

```bash

~root
│
├── .devcontainer
│    ├── devcontainer.json
│    └── post-create-command.sh              
├── azure.yaml                      
│
├── .github/
│   └── workflows/
│       ├── workflow1.yml           
│       ├── workflow2.yml           
│       └── ...                     
│
├── infra/
│   ├── main.bicep                  
│   ├── main.parameters.bicep       
│   ├── abbreviations.json          
│   └── ...                         
│
├── src/                            
│   ├── app/                        
│   │   ├── components/             
│   │   ├── services/               
│   │   ├── models/                 
│   │   └── ...
│   ├── styles/                     
│   ├── assets/                     
│   ├── utils/                      
│   └── core/
│   
├── (1)packages/
│       ├── app/ 
│       ├── module/
│       └── ...
├── public/                         
│
├── tests/                          
│   └── ...                         
│
├── * docs/                           
│   └── ...                         
│
├── package.json                    
├── README.md                       

```
* optional additional docs folder for extended documentation files
(1) /packages to be used in a monorepo context

## Additional recommendations

- TypeScript is preferred over vanilla JavaScript

- 3rd party dependencies will be used to a minimum and Web Platform APIs are preferred

- Except in the cases when we're showcasing a specific framework, vanilla over frameworks is preferred to reduce maintenance efforts

- Server side JavaScript will be written for the latest Node.js LTS version

- When writing serverless APIs to be deployed to Azure Functions, they should use the model v4 when possible/supported

- REST is preferred over GraphQL to avoid Apollo conflict resolution across packages

- Preferred package manager and monorepo tool is npm 

- Prettier and ESLint configuration should be in place 


# Recommended code style guidelines 

The following styles and conventions are not strictly mandatory but highly recommended. Large deltas from this recommendations may block a template from being added to the gallery.

[TS Style Guide](https://ts.dev/style/#identifiers)

[Guidelines for writing JavaScript code examples - The MDN Web Docs project | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide/Code_style_guide/JavaScript)
 

 ## Python project folder structure

The following guidelines and the folders included, represent the conventional structure for a Python standard application.

```bash

~root
│
├── .devcontainer
│    ├── devcontainer.json
│    └── post-create-command.sh              
├── azure.yaml                      
│
├── .github/
│   └── workflows/
│       ├── workflow1.yml           
│       ├── workflow2.yml           
│       └── ...                     
│
├── infra/
│   ├── main.bicep                  
│   ├── main.parameters.bicep       
│   ├── abbreviations.json          
│   └── ...                         
│
├── src/                            
│   ├── projectname/                
│        ├── __init__.py             
│        ├── core/                            
│        └── ...
│                      
│
├── tests/                          
│   └── ...                         
│
├── *docs/                           
│   └── ...                         
│
├── requirements-dev.txt                
├── README.md                       
└── .gitignore                      
             

```
* optional additional docs folder for extended documentation files

