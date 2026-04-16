# The 0.5 Chronicles / 《地球文明0.5编年史》

`The 0.5 Chronicles` is a bilingual, volume-based historical writing project about how ordinary life crossed from the late mechanical age into the AI era.

It is not a flat blog. The repo combines a public Astro site, structured chapter files, editorial notes, and manuscript material that is still being shaped into publishable volumes.

## Scope

- Retrospective volumes rebuilding the transition years from 1980 onward
- `Now Records` preserving the present tense as future source material
- Bilingual publication in English and Chinese
- A historical lens focused on work, tools, habits, coordination, media, and ordinary life

## Current Public Structure

- Volume I (1980-1995): `Digital Eve / 数字前夜`
- Volume II (1996-2010): `The Age of Connection / 连接的年代`
- Volume III (2011-2020): `The Platform Age / 平台时代`
- Volume IV (2021-2025): `Machine Collaborators / 机器合作者`
- `Now Records / 当下记录`
- Method, project notes, launch notes, and editorial roadmaps

## Repository Layout

```text
.
├── manuscripts/              # working notes and raw manuscript material
├── public/                   # static assets shipped as-is
├── src/
│   ├── assets/               # local images used by pages/posts
│   ├── components/           # shared Astro components
│   ├── content/blog/         # published and semi-published content entries
│   ├── layouts/              # page/post layouts
│   ├── pages/                # route entry points and volume landing pages
│   ├── consts.ts             # site title, description, tagline
│   └── content.config.ts     # Astro content collection schema
├── tools/                    # content-generation helpers and migration scripts
├── astro.config.mjs
└── package.json
```

## Content States

This repo uses three practical content states:

- Public: listed in archive/index pages and linked normally
- Unlisted: built as routable pages, but intentionally omitted from archive/index/RSS
- Draft: excluded from the site build

Volume landing pages may point to unlisted chapter drafts when those chapters are meant to be readable in sequence but not yet promoted into the main archive.

## Structure Migration

The repo went through a structural cleanup in April 2026 to retire the misleading `vol-0-1980-1995` and
`vol-1-digital-eve` namespaces and replace them with the current canonical volume layout.

See:

- `STRUCTURE_MIGRATION_2026-04.md`

## Local Development

Install dependencies first:

```sh
npm ci
```

Run the dev server:

```sh
npm run dev
```

Create a production build:

```sh
npm run build
```

Preview the production build locally:

```sh
npm run preview
```

## Editorial Workflow

1. Draft or revise chapter material in `src/content/blog/` or `manuscripts/`.
2. Decide whether the entry should be `public`, `unlisted`, or `draft`.
3. Wire chapter access from the relevant volume page in `src/pages/volumes/`.
4. Keep project-level framing pages up to date when a new volume or structural change becomes public.

## Deployment

The site deploys through GitHub Pages via the workflow in `.github/workflows/deploy.yml`.

Canonical site configuration currently points to:

- `https://www.0500005.xyz`

## Notes

- This repo is the canonical source for the published site structure.
- Volume pages are curated entry points; the archive is not the authoritative map of the project.
