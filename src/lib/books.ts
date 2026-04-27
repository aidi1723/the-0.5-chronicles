import { getCollection, type CollectionEntry } from 'astro:content';

export type BookEntry = CollectionEntry<'books'>;
export type BookLang = 'zh' | 'en';

export const BOOKS = {
	'the-code-of-all-things': {
		slug: 'the-code-of-all-things',
		title: 'The Code of All Things',
		titleZh: '万物代码',
		subtitle: "From the Universe's Primary Rules to a New Agent Civilization",
		subtitleZh: '从宇宙主规则到 Agent 新文明',
		description:
			'A bilingual book project about rules, civilization, Agent systems, and the boundary between human judgment and executable language.',
		descriptionZh:
			'一部关于底层规则、文明反编译、Agent 执行系统，以及人类判断与可执行语言边界的双语书。',
	},
} as const;

export type BookSlug = keyof typeof BOOKS;

export function isBookSlug(slug: string): slug is BookSlug {
	return slug in BOOKS;
}

export function getBookMeta(slug: BookSlug) {
	return BOOKS[slug];
}

export async function getPublishedBookEntries() {
	return (await getCollection('books'))
		.filter((entry) => !entry.data.draft)
		.sort((a, b) => a.data.order - b.data.order);
}

export async function getEntriesForBook(book: string, lang?: BookLang) {
	const entries = await getPublishedBookEntries();
	return entries.filter((entry) => entry.data.book === book && (!lang || entry.data.lang === lang));
}

export function getBookPagePath(entry: BookEntry) {
	return `/books/${entry.data.book}/${entry.data.lang}/${entry.data.pageSlug}/`;
}

export function getBookLangPath(book: string, lang: BookLang) {
	return `/books/${book}/${lang}/`;
}

export function getAlternateEntry(entry: BookEntry, entries: BookEntry[]) {
	return entries.find(
		(candidate) =>
			candidate.data.book === entry.data.book &&
			candidate.data.translationKey === entry.data.translationKey &&
			candidate.data.lang !== entry.data.lang,
	);
}

export function getSiblingEntries(entry: BookEntry, entries: BookEntry[]) {
	const visible = entries
		.filter(
			(candidate) =>
				candidate.data.book === entry.data.book &&
				candidate.data.lang === entry.data.lang &&
				!candidate.data.unlisted,
		)
		.sort((a, b) => a.data.order - b.data.order);
	const index = visible.findIndex((candidate) => candidate.id === entry.id);

	return {
		previous: index > 0 ? visible[index - 1] : undefined,
		next: index >= 0 && index < visible.length - 1 ? visible[index + 1] : undefined,
	};
}
