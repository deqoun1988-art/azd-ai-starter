// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Template Authoring Frameowork Docs',
			social: {
				github: 'https://github.com/Azure-Samples/azd-template-artifacts',
			},
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Publishing Guidelines', slug: 'guides/publishing-guidelines' },
					],
				},
				{
					label: 'Development Guidelines',
					autogenerate: { directory: 'guides/development-guidelines' },
				},
				{
					label: 'Code Structure',
					autogenerate: { directory: 'guides/code-structure' },
				},
				{
					label: 'Standard Files',
					autogenerate: { directory: 'standard-files' },
				},
			],
		}),
	],
});
