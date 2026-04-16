# Structure Migration 2026-04

This note records the April 2026 cleanup that turned the project from an early drafting namespace into a clearer publication structure.

## Canonical Repository

The canonical repo is:

- `/Users/aidi/.openclaw/workspace/the-0.5-chronicles`

An older local copy also exists at:

- `/Users/aidi/.openclaw/workspace/0500005-blog`

That older copy is no longer the authoritative source for routing, content organization, or deployment.

## Why The Migration Happened

Two early namespaces had become misleading:

- `vol-0-1980-1995` mixed together formal volume chapters, early archive drafts, and later speculative notes.
- `vol-1-digital-eve` duplicated material that now belongs inside the formal Volume I namespace.

Keeping those names in active use made the repo harder to understand and made URLs look less intentional than the actual editorial structure.

## Canonical Content Layout

Published and semi-published volume material now lives under:

- `src/content/blog/volumes/vol-1-1980-1995`
- `src/content/blog/volumes/vol-2-1996-2010`
- `src/content/blog/volumes/vol-3-2011-2020`
- `src/content/blog/volumes/vol-4-2021-2025`

Supporting non-canonical lines live under:

- `src/content/blog/volumes/vol-0-early-archive`
  Legacy draft archive retained for writing history, abandoned chapter lines, and earlier framing passes.
- `src/content/blog/volumes/vol-open-2026-2029`
  Open-ended forward notes that are not yet presented as a closed formal volume.

## Retired Namespaces

The following content namespaces are retired:

- `src/content/blog/volumes/vol-0-1980-1995`
- `src/content/blog/volumes/vol-1-digital-eve`

They should not receive new content.

## Compatibility Strategy

Old incoming blog links are still preserved:

- `/blog/volumes/vol-0-1980-1995/...`
- `/blog/volumes/vol-1-digital-eve/...`

Those routes now resolve through compatibility redirect pages to the current canonical post URLs.

The landing page `/volumes/vol-0-1980-1995/` is intentionally kept, but it is now a legacy archive hub rather than a formal volume page.

## Content State Rules

The site uses three practical states:

- `public`: listed in archive/index pages and normal site navigation
- `unlisted`: routable and readable, but intentionally omitted from archive/index/RSS
- `draft`: excluded from the site build

Volume landing pages may link to `unlisted` entries when a chapter should be readable in sequence before it is promoted into broader discovery surfaces.

## Working Rule Going Forward

When adding or revising chapter material:

1. Put formal historical chapters into the correct canonical volume namespace.
2. Use `vol-0-early-archive` only for preserved legacy drafts.
3. Use `vol-open-2026-2029` only for open-ended forward material that has not been locked into a formal published volume.
4. Preserve redirects when renaming any public-facing path that might already have been shared.
