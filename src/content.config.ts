import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
	// Load Markdown and MDX files in the `src/content/blog/` directory.
	loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
	// Type-check frontmatter using a schema
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string(),
			// Transform string to Date object
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			draft: z.boolean().optional(),
			unlisted: z.boolean().optional(),
			category: z.string().optional(),
			heroImage: image().optional(),
		}),
});

const books = defineCollection({
	loader: glob({ base: './src/content/books', pattern: '**/*.{md,mdx}' }),
	schema: z.object({
		title: z.string(),
		description: z.string(),
		lang: z.enum(['zh', 'en']),
		book: z.string(),
		bookTitle: z.string(),
		pageSlug: z.string(),
		translationKey: z.string(),
		kind: z.enum(['landing', 'guide', 'toc', 'preface', 'chapter', 'appendix']),
		order: z.number(),
		chapterNumber: z.number().optional(),
		partTitle: z.string().optional(),
		draft: z.boolean().optional(),
		unlisted: z.boolean().optional(),
	}),
});

export const collections = { blog, books };
