// From https://github.com/jupyter-book/blog/blob/main/plugins/blog.mjs

import { globSync } from "glob";
import { readFileSync } from "node:fs";
import { extname, basename, join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { getFrontmatter } from "myst-transforms";
import { genRSS } from './rss.mjs';
import yaml from 'js-yaml';

// Get the directory of the current module
const __dirname = dirname(fileURLToPath(import.meta.url));

// Track if RSS has been generated
let rssGenerated = false;

function generateRSSFeed(ctx) {
  if (rssGenerated) return;  // Only generate once
  
  const paths = globSync("blog/**/*.md").sort().reverse();
  const rssItems = paths.map(path => {
    const content = readFileSync(path, { encoding: "utf-8" });
    const ast = ctx.parseMyst(content);
    const frontmatter = getFrontmatter({}, ast).frontmatter;
    const ext = extname(path);
    
    return {
      title: frontmatter.title,
      description: frontmatter.description || '',
      date: frontmatter.date,
      link: `/${path.toString().slice(0, -ext.length)}`,
      content: content
    };
  });

  const mystConfig = yaml.load(readFileSync(join(__dirname, '..', 'myst.yml'), 'utf8'));
  genRSS({
    title: mystConfig.project.blog?.title || mystConfig.project.title,
    description: mystConfig.project.blog?.description || '',
    link: mystConfig.project.blog?.url || '',
    items: rssItems
  });
  
  rssGenerated = true;
}

const blogPostsDirective = {
  name: "blog-posts",
  doc: "Display preview cards for documents.",
  options: {
    limit: { type: Number, doc: "Number of posts." },
  },
  run(data, vfile, ctx) {
    // Generate RSS feed on first run
    generateRSSFeed(ctx);
    
    const size = data.options.limit ?? 3;
    const paths = globSync("blog/**/*.md").sort().reverse();
    
    const nodes = paths.map((path) => {
      const ext = extname(path);
      const name = basename(path, ext)
      const content = readFileSync(path, { encoding: "utf-8" });
      const ast = ctx.parseMyst(content);
      const frontmatter = getFrontmatter(vfile, ast).frontmatter;

      const descriptionItems = frontmatter.description
        ? ctx.parseMyst(frontmatter.description).children
        : [];
      const subtitleItems = frontmatter.subtitle
        ? ctx.parseMyst(frontmatter.subtitle).children
        : [];
      const footerItems = frontmatter.date
        ? [
            {
              type: "footer",
              children: [ctx.parseMyst(`**Date**: ${frontmatter.date}`)["children"][0]],
            },
          ]
        : [];
      return {
        type: "card",
        children: [
          {
            type: "cardTitle",
            children: ctx.parseMyst(frontmatter.title).children,
          },
          ...subtitleItems,
          ...descriptionItems,
          ...footerItems,
        ],
        url: `/${path.toString().slice(0, -ext.length)}`,
      };
    });

    return Array.from(nodes).slice(0, size);
  },
};

const plugin = { name: "Blog posts", directives: [blogPostsDirective] };

export default plugin;