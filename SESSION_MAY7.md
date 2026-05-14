# Session Brief — Updated May 10, 2026
**Goal:** Understand Bridge capabilities → full site mockup (Version A locked) → staging → build
**Deadline:** First internal version Friday May 8 → MISSED → new target: this week

---

## ✅ Already done (completed May 6)

- [x] Full project workspace organized
- [x] SITE_AUDIT.md — complete with plugin inventory, page inventory, menu structure, WP strategy
- [x] BRAND_SUMMARY.md — extracted from Anita's brand manual
- [x] REFERENCE_SITES.md — 4 reference sites analyzed
- [x] DESIGN_DIRECTION.md — locked design decisions for every component (Opus)
- [x] DESIGN_CRITIQUE.md — current site critiqued page by page against brand standards (Opus)
- [x] Elementor Pro confirmed Active (kikegaona@me.com)
- [x] SiteGround confirmed, staging request sent to Mazor
- [x] Theme decision: keep Bridge (header/footer via Qode Options, pages via Elementor Pro)
- [x] Bridge capabilities researched → BRIDGE_CAPABILITIES.md (07_wordpress/)
- [x] Mega menu revised: Bridge has no native mega menu → simplified standard dropdown (5 stacked items)
- [x] Hero decision: **Version A locked** — full-bleed photo with headline overlay. Version B explored and discarded.

---

## Start here (5 min)

- [ ] Check if Mazor confirmed SiteGround staging
- [ ] If yes → ask him to create it before touching anything on prod
- [ ] Run Duplicator Pro backup on prod regardless (last one was Feb 2025)

---

## What we know going in

**Stack:** WordPress 6.9.4 · Bridge theme (Qode) · Elementor Pro (active, kikegaona@me.com) · WooCommerce (catalog only, cart hidden) · TranslatePress (ES/EN) · SiteGround hosting

**Bridge owns:** header, footer, global typography defaults  
**Elementor owns:** all page content + WooCommerce product/archive templates  
**Custom CSS:** hides WooCommerce cart from header — keep this

**Design direction:** White-dominant (80%+), Playfair Display headings, Lexend Light body, #1D1D1B text, #2E7B37 green accents, #9F8A73 warm secondary. Full-bleed editorial photography.

**New architecture:**
Home → Acerca de Nosotros → Nuestras Divisiones (DEL CAMPO / Ingredientes / Secos / Frescos / Greenclover) → Sostenibilidad y Certificaciones → Clientes → Contacto

---

## Session agenda

### Block 1 — HTML mockups (Sonnet, two separate conversations)
Design direction and critique are done — go straight to building mockups.

**Mockup A — Home page, Version A (full-bleed hero)**
Read: DESIGN_DIRECTION.md + CLIENT_BRIEF.md + BRAND_SUMMARY.md
Save to: `06_design/mockups/home-version-a.html`

**Mockup B — Home page, Version B (editorial split hero)**  
Same files, same design system, only the hero section changes.
Save to: `06_design/mockups/home-version-b.html`

Both must be buildable in Elementor Pro + Bridge. Use real Google Fonts. Color blocks for photography placeholders. Real content from CLIENT_BRIEF.md.

### Block 2 — Division page mockup (Sonnet)
One HTML mockup of the division page template (use División de Secos as the example).
Read: DESIGN_DIRECTION.md (Division/Product Page section) + CLIENT_BRIEF.md
Save to: `06_design/mockups/division-template.html`

### Block 3 — WordPress setup on staging (if Mazor confirms)
- Run Duplicator Pro backup first
- Set Elementor Global Colors (6 tokens from DESIGN_DIRECTION.md)
- Set Elementor Global Fonts (Playfair Display + Lexend Light)
- Configure Bridge header: Header Type 1, sticky, white, new logo, utility bar
- Create new pages for new site architecture
- Remove LayerSlider + Slider Revolution

---

## Skills to use tomorrow

| Task | Skill / Model |
|------|--------------|
| Analyzing reference sites, design decisions | **Opus** (complex reasoning) |
| Creating wireframe documents | `docx` skill + **Opus** |
| Writing page content drafts | **Sonnet** |
| Building HTML mockups | **Sonnet** |
| Documenting decisions | **Sonnet** |
| Any presentations for client | `pptx` skill |

---

## Key files to reference
- [CLIENT_BRIEF.md](01_brief/CLIENT_BRIEF.md)
- [BRAND_SUMMARY.md](03_assets/BRAND_SUMMARY.md)
- [SITE_AUDIT.md](04_current-site/SITE_AUDIT.md)
- [REFERENCE_SITES.md](05_inspiration/REFERENCE_SITES.md)
- Current site screenshots: `04_current-site/screenshots/`

---

## Open questions (not blocking)
- Mazor: LDC product section — exactly what did the client like? (ask Mon/Tue)
- Client: Do they want to keep the FAQ page? Request a Quote form?
- Assets still needed: product photos, hero imagery, certification logos hi-res, content per division
