using './main.bicep'

param environmentName = readEnvironmentVariable('AZURE_ENV_NAME', 'MY_ENV')
param resourceGroupName = readEnvironmentVariable('AZURE_RESOURCE_GROUP', '')
param location = readEnvironmentVariable('AZURE_LOCATION', 'eastus2')
param principalId = readEnvironmentVariable('AZURE_PRINCIPAL_ID', '')
param openAiName = readEnvironmentVariable('AZURE_OPENAI_NAME', '')
param createRoleForUser = bool(readEnvironmentVariable('CREATE_ROLE_FOR_USER', 'true'))
// the following params apply to the deployment of a frontend static app, for testing purposes
// the application has Template Framework Documentation
param deployExampleStaticFrontend = bool(readEnvironmentVariable('FRONTEND_DEPLOY', 'true'))
// param frontendUrl = readEnvironmentVariable('FRONTEND_URI')
param frontendAppName = readEnvironmentVariable('FRONTEND_APP_NAME', '')
