import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const badClaimPatterns = [
  /\blicensed\b/i,
  /\bcertified\b/i,
  /\binsured\b/i,
  /\bguarantee(?:d|s)?\b/i,
  /\b24\/7\b/i,
  /\bemergency\b/i,
  /\b\d+\s*(?:active\s*)?crew(?:\s*units?)?\b/i,
  /under\s+45\s+minutes/i,
  /prompt response/i,
  /will be dispatched/i,
  /transmitted/i,
  /fully licensed/i,
  /average\s+joplin\s+dispatch/i,
  /(?:\d+|[<>]\s*\d+(?:\.\d+)?)\s*(?:mins?|hours?|hrs?)/i,
  /\d+\s*crews?\b/i,
  /automated dispatch/i,
  /field unit assigned/i,
  /will assign/i,
  /fastest response/i,
  /response times? under/i,
  /localized area dispatch/i,
  /dispatch online/i,
  /transmit/i,
];
const skipDirs = new Set(['.git', '.vercel', 'node_modules', 'dist']);
function walk(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (skipDirs.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...walk(full));
    else out.push(full);
  }
  return out;
}
const htmlFiles = walk(root).filter((f) => f.endsWith('.html'));
if (!htmlFiles.length) throw new Error('No HTML routes found');
const allFiles = new Set(walk(root).map((f) => path.resolve(f)));
let errors = [];
for (const file of htmlFiles) {
  const rel = path.relative(root, file);
  const html = fs.readFileSync(file, 'utf8');
  if (!/<title>[^<]{8,}<\/title>/i.test(html)) errors.push(`${rel}: missing meaningful title`);
  if (!/<meta\s+name=["']description["']\s+content=["'][^"']{40,}["']/i.test(html)) errors.push(`${rel}: missing meaningful meta description`);
  if (!/<h1[\s>]/i.test(html)) errors.push(`${rel}: missing h1`);
  for (const pat of badClaimPatterns) {
    const match = html.match(pat);
    if (match) errors.push(`${rel}: unverified/forbidden claim pattern: ${match[0]}`);
  }
  const attrPattern = /\b(?:href|src)=["']([^"']+)["']/gi;
  let m;
  while ((m = attrPattern.exec(html))) {
    const raw = m[1];
    if (/^(https?:|mailto:|tel:|data:)/i.test(raw)) continue;
    if (raw.startsWith('#')) {
      const id = raw.slice(1);
      if (id && !new RegExp(`id=["']${id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']`).test(html)) errors.push(`${rel}: missing same-page anchor ${raw}`);
      continue;
    }
    const [beforeHash, hash] = raw.split('#');
    const targetPart = beforeHash.split('?')[0];
    const target = path.resolve(path.dirname(file), targetPart || rel);
    if (!allFiles.has(target)) {
      errors.push(`${rel}: broken local reference ${raw}`);
      continue;
    }
    if (hash && target.endsWith('.html')) {
      const targetHtml = fs.readFileSync(target, 'utf8');
      if (!new RegExp(`id=["']${hash.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']`).test(targetHtml)) errors.push(`${rel}: broken anchor ${raw}`);
    }
  }
}
for (const required of ['robots.txt', 'sitemap.xml', 'styles.css']) {
  if (!fs.existsSync(path.join(root, required))) errors.push(`missing ${required}`);
}
const sitemap = fs.readFileSync(path.join(root, 'sitemap.xml'), 'utf8');
const routeCount = (sitemap.match(/<loc>/g) || []).length;
if (routeCount < 10) errors.push(`sitemap too small: ${routeCount} routes`);
if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}
console.log(`Check passed: ${htmlFiles.length} HTML routes, sitemap ${routeCount} URLs, no broken local refs, no forbidden fake-claim patterns.`);
