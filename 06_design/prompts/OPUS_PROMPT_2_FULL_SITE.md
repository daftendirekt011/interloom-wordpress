# Opus Prompt 2 — Full Site UX Prototype
> Copy everything below the horizontal rule into a fresh Claude Opus conversation (Cowork mode).
> You have access to the interloom workspace folder. Read the files listed below before starting.
> Run this AFTER Prompt 1 is complete — the design language is already established there.

---

You are a senior web designer and front-end developer working on a website redesign for **Grupo Interloom**, a Peruvian agrotrading company.

## STEP 1 — Read these files first (in this order)

Use the Read tool on each file before doing anything else:

1. `C:\Users\DCPor\OneDrive\Documentos\interloom\SESSION_MAY7.md` — session context, stack decisions
2. `C:\Users\DCPor\OneDrive\Documentos\interloom\05_inspiration\DESIGN_DIRECTION.md` — all locked design decisions
3. `C:\Users\DCPor\OneDrive\Documentos\interloom\01_brief\CLIENT_BRIEF.md` — company info, all 5 divisions, products, team, contact
4. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\SITE_SKELETON.md` — full page index, URLs, user flows, division-specific content table
5. `C:\Users\DCPor\OneDrive\Documentos\interloom\07_wordpress\BRIDGE_CAPABILITIES.md` — Bridge constraints (header/footer = Bridge via Qode Options; all page content = Elementor Pro)

Also check if `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\home-version-a.html` exists — if it does, read the CSS custom properties block and the header/footer markup from it, and reuse them exactly across all pages for consistency.

Do not start building until all files are read.

---

## STEP 2 — What you're building

A complete, navigable HTML prototype — all 10 pages linked together with working internal navigation. This is a **UX completeness exercise**: every page must exist, every division must show its real products, every link must work within the prototype. Structural completeness over pixel-perfect polish.

**Output folder:** `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\`

**File structure — save exactly like this:**
```
06_design/mockups/
  index.html                      ← Home (Version A hero — locked)
  nosotros.html                   ← Nosotros / About
  sostenibilidad.html             ← Sostenibilidad y Certificaciones
  clientes.html                   ← Clientes
  contacto.html                   ← Contacto
  divisiones/
    del-campo.html                ← DEL CAMPO
    ingredientes.html             ← División de Ingredientes
    secos.html                    ← División de Secos
    frescos.html                  ← División de Frescos
    greenclover.html              ← Greenclover Naturals LLC
```

All internal `<a href="...">` links must work when opened from the file system. Use relative paths (from `divisiones/` pages, use `../` to reach root pages).

---

## STEP 3 — Key constraints (read the files for full detail)

**Stack:**
- Bridge controls header + footer (page content is Elementor Pro — the middle of every page)
- No mega menu — Divisiones uses a standard 5-item CSS dropdown
- 5-column division card grid on home page is Elementor content → fully supported, no issue
- No sliders, no dark sections, no all-caps body text

**Fonts:** Playfair Display (headings 400 Regular + italic) + Lexend (300 Light + 400 Regular). Google Fonts only.

**Colors:** `#1D1D1B` `#4A3625` `#9F8A73` `#2E7B37` `#FAF8F5` `#EDEAE3` + pure white. Use CSS custom properties. Forest green = punctuation only (CTAs, hover, active states).

**Division-specific CTAs (from SITE_SKELETON.md):**
- DEL CAMPO → WhatsApp Business button (`#25D366` background — only non-brand color allowed)
- All other divisions → "Solicitar cotización" green button → contacto.html

**Photos:** CSS gradient placeholders everywhere, labeled clearly. Dark gradient for heroes, warm-brown for field/editorial, muted green for plant, per-division colors for cards.

**Navigation paths** — from `divisiones/` files, paths are:
- Root pages: `../nosotros.html`, `../sostenibilidad.html`, `../contacto.html`, `../index.html`
- Division pages: `del-campo.html`, `secos.html` (relative within `divisiones/`)
- Footer links: same `../` prefix

---

## STEP 4 — Page content sources

All product names, descriptions, team names, certifications, contact info, and division details are in `CLIENT_BRIEF.md` and `SITE_SKELETON.md`. Use the real content — don't invent anything. Key details:

**Team:** Antonio Cook Hardy (CEO), Alexia Cook Hardy (CEO), Aranzazu Muelle (Exportaciones), Juan Jose Zevallos (Exportaciones)

**Certifications:** USDA Organic, EU Bio, BRC Food, Kiwa, Kosher, SMETA

**Contact:** Av. Jorge Basadre 310, Of. 504, San Isidro, Lima – Perú | (511) 311-1730 | contacto@interloom.com.pe

**Stats:** +30 años · 8,000+ toneladas · 25+ mercados · Top 5 quinua · 5 divisiones

---

## STEP 5 — Build order

Build one file at a time, save it, then move to the next. Confirm each file is saved before continuing.

Order:
1. `index.html` (home)
2. `nosotros.html`
3. `divisiones/del-campo.html`
4. `divisiones/ingredientes.html`
5. `divisiones/secos.html`
6. `divisiones/frescos.html`
7. `divisiones/greenclover.html`
8. `sostenibilidad.html`
9. `clientes.html`
10. `contacto.html`

After all 10 are saved: open `index.html` and verify that clicking through Divisiones → any division page → back works via the breadcrumb and nav links.

Begin by reading the five files listed in Step 1.
