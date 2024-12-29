import { writeFileSync } from 'node:fs';

export function genRSS({ title, description, link, items }) {
  const rss = `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>${escapeXml(title)}</title>
  <description>${escapeXml(description)}</description>
  <link>${escapeXml(link)}</link>
  <atom:link href="${escapeXml(link)}/rss.xml" rel="self" type="application/rss+xml" />
  ${items.map(item => `
    <item>
      <title>${escapeXml(item.title)}</title>
      <description>${escapeXml(item.description)}</description>
      <link>${escapeXml(link + item.link)}</link>
      <guid>${escapeXml(link + item.link)}</guid>
      ${item.date ? `<pubDate>${new Date(item.date).toUTCString()}</pubDate>` : ''}
    </item>
  `).join('\n')}
</channel>
</rss>`;

  writeFileSync('_build/html/rss.xml', rss);
}

function escapeXml(unsafe) {
  if (!unsafe) return '';
  return unsafe.replace(/[<>&'"]/g, c => {
    switch (c) {
      case '<': return '&lt;';
      case '>': return '&gt;';
      case '&': return '&amp;';
      case '\'': return '&apos;';
      case '"': return '&quot;';
    }
  });
}
