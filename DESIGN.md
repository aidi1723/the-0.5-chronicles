# Design Notes

## Visual Direction

This site is an editorial archive with a warm paper-like surface, restrained accent color, and bilingual labels. New book pages should feel like part of the same reading system rather than a separate product area.

## Rules

- Use the existing global tokens in `src/styles/global.css` for color, text, border, radius, and shadow.
- Keep layouts semantic and light: Astro pages, server-rendered content, no client JavaScript unless needed.
- Use clear bilingual navigation where it helps orientation: English first for site-level labels, Chinese first inside Chinese book content.
- Cards should be used for repeated book/chapter entries and entry panels only.
- Reading pages should stay narrow, quiet, and scannable, with visible language switching and previous/next movement.
- The homepage book entrance should be prominent enough to find, but it must not replace the existing 0.5 Chronicles volume architecture.
