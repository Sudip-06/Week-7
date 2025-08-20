---
marp: true
title: Product Documentation — Marp Demo
author: Technical Writer (sudip-06)
theme: default           # Using default plus local CSS below
paginate: true
footer: "© 2025 • Contact: 23f3004246@ds.study.iitm.ac.in"
description: "Maintainable product docs in Markdown, exportable to HTML/PDF/PPTX via Marp."
---

<!--
Custom theme specification (save as themes/product-docs.css to use with --theme)
```css
/* @theme product-docs
 * Usage:
 *   marp --theme themes/product-docs.css slides.md -o dist/index.html
 */
:root {
  --accent: #2563eb;   /* Indigo */
  --text: #0f172a;     /* Slate-900 */
}
section {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  color: var(--text);
  padding: 60px;
}
h1, h2, h3 { color: var(--accent); letter-spacing: .3px; }
blockquote { color: #334155; }
section::after {
  /* Explicit page number overlay (alternative to paginate: true) */
  content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  position: absolute; right: 24px; bottom: 18px; font-size: .8rem; color: #64748b;
}
