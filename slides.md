---
marp: true
title: Product Documentation — Marp Demo
author: Technical Writer (sudip-06)
theme: default     # Using default + local styles below
paginate: true
footer: "© 2025 | Contact: 23f3004246@ds.study.iitm.ac.in"
description: "Maintainable product docs in Markdown, exported to HTML/PDF/PPTX via Marp CLI."
---

<!-- Custom theme specification (save as themes/product-docs.css to use with --theme)
```css
/* @theme product-docs
 * Usage: marp --theme themes/product-docs.css slides.md -o dist/slides.html
 */
:root {
  --accent: #2563eb;
  --text: #0f172a;
}<img width="117" height="154" alt="image" src="https://github.com/user-attachments/assets/6113da87-48a0-4588-b95b-37d47d1702c1" />

section {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  color: var(--text);
  padding: 60px;
}
h1, h2, h3 { color: var(--accent); }
section::after {
  /* Page numbers (alternative to paginate: true) */
  content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  position: absolute; right: 24px; bottom: 18px; font-size: 0.8rem; color: #64748b;
}
