import type { APIRoute } from 'astro';

export const GET: APIRoute = () => {
  const body = `User-agent: *\nAllow: /\n\nSitemap: https://www.0500005.xyz/sitemap-index.xml\n`;
  return new Response(body, {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'public, max-age=300',
    },
  });
};
