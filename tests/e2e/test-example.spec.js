// test-example.spec.js
import { test, expect } from '@playwright/test';

test('Check if application was deployed to provisioned service URL', async ({ page }) => {
    const url = process.env.FRONTEND_URL ?? 'http://localhost:4321';
    console.log(url, '### URL');
    if (!url) {
      throw new Error("URL wasn't retrieved or service not provisioned");
    }
    
    await page.goto(url);
    const azureLocator = 'body[data-artifact="Azure Default Service Page"]';
    // Services like Azure Container Apps and Azure Static Web Apps will render this data-attribute
    // in the body of their default page
    const isVisible = await page.isVisible(azureLocator);
    // We can assume the application not to have been deployed if the data-attribute is present
    expect(isVisible).toBe(false); 
  });
  