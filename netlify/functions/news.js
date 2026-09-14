const sources = [
  ['Ciencia y tecnología', 'México ciencia tecnología innovación'],
  ['Cultura y sociedad', 'México cultura sociedad'],
  ['Actualidad', 'México actualidad'],
];

function escapeXml(value) {
  return value.replace(/[<>&'\"]/g, (char) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', "'": '&apos;', '"': '&quot;' }[char]));
}

function decodeEntities(value = '') {
  return value.replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, '$1')
    .replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'")
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>');
}

function tag(item, name) {
  const match = item.match(new RegExp(`<${name}[^>]*>([\\s\\S]*?)</${name}>`, 'i'));
  return match ? decodeEntities(match[1]).trim() : '';
}

async function getFeed(label, query) {
  const url = `https://news.google.com/rss/search?q=${encodeURIComponent(query)}&hl=es-419&gl=MX&ceid=MX:es-419`;
  const response = await fetch(url, { headers: { 'User-Agent': 'OyeLoMex/1.0 news reader' } });
  if (!response.ok) throw new Error(`Feed ${label} returned ${response.status}`);
  const xml = await response.text();
  return [...xml.matchAll(/<item>([\s\S]*?)<\/item>/gi)].slice(0, 5).map((match) => {
    const item = match[1];
    return { title: tag(item, 'title'), link: tag(item, 'link'), pubDate: tag(item, 'pubDate'), source: tag(item, 'source'), category: label };
  }).filter((item) => item.title && item.link);
}

exports.handler = async function handler() {
  const results = await Promise.allSettled(sources.map(([label, query]) => getFeed(label, query)));
  const articles = results.flatMap((result) => result.status === 'fulfilled' ? result.value : []);
  articles.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));
  const unique = articles.filter((article, index, all) => all.findIndex((other) => other.title === article.title) === index).slice(0, 12);
  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'public, max-age=900, s-maxage=900' },
    body: JSON.stringify({ updatedAt: new Date().toISOString(), articles: unique }),
  };
};
