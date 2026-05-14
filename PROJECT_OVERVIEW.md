# Interloom — WordPress Redesign

**Client:** Interloom (Grupo Interloom, Lima – Perú)  
**Project type:** WordPress redesign — minimalist, modern, bilingual  
**Kicked off:** May 6, 2026  
**Status:** 🟡 Setup done — Design analysis starts May 7

---

## The Brief in One Paragraph

Interloom is a 30+ year Peruvian agrotrading group with 5 business divisions. Their current WordPress site is outdated (2022 design, 2022 copyright), uses the wrong fonts and colors, has no brand hierarchy, and doesn't reflect their new brand identity (designed by Anita). We're rebuilding it — cleaner, minimalist, organized by divisions — using no-code tools (Elementor + Bridge) so they can self-manage. Bilingual (ES/EN). First version to show internally on Friday May 9.

---

## Team

| Person | Role |
|--------|------|
| Mazor | PM — our point of contact |
| Anita | Brand designer — delivered logo + Manual de Marca 2026 |
| Cami | Web design lead |

---

## Timeline

| Date | What |
|------|------|
| **May 6** ✅ | Setup, asset organization, current site review |
| **May 7** | Site audit deep-dive, WP strategy, start wireframes |
| **May 9 (Fri)** | First version to show (internal) |
| TBD | Client review |
| TBD | Development begins on staging |
| TBD | Go-live |

---

## Folder Structure

```
interloom/
├── PROJECT_OVERVIEW.md         ← you are here
├── 01_brief/
│   ├── CLIENT_BRIEF.md         ← full project brief, requirements, contact info
│   └── RFQ Web Interloom.pdf   ← original client RFQ document
├── 02_research/                ← competitor analysis, notes
├── 03_assets/
│   ├── BRAND_SUMMARY.md        ← colors, fonts, logo rules (extracted from manual)
│   ├── Manual_marca_2026.pdf   ← Anita's full brand manual
│   ├── logos/                  ← ⚠️ NEED: SVG + PNG files from Anita
│   ├── fonts/                  ← ⚠️ NEED: Recoleta Regular file from Anita
│   ├── images/                 ← ⚠️ NEED: product + hero photos from client
│   └── icons/
├── 04_current-site/
│   ├── SITE_AUDIT.md           ← full current site audit (bugs, gaps, tech stack)
│   ├── screenshots/            ← home, nosotros, contacto captured May 6
│   └── content/
├── 05_inspiration/
│   └── REFERENCE_SITES.md      ← analysis of 4 client-approved reference sites
├── 06_design/
│   ├── wireframes/
│   ├── mockups/
│   └── components/
├── 07_wordpress/
│   ├── theme/
│   ├── plugins/
│   └── notes/
└── 08_deliverables/
```

---

## What We Know (Key Decisions)

### WordPress Stack
- **Hosting:** SiteGround ✅ confirmed — staging request sent to Mazor
- **Theme:** Bridge (Qode) — keeping it. Header/footer via Qode Options, pages via Elementor Pro
- **Page builder:** Elementor Pro ✅ active (kikegaona@me.com)
- **E-commerce:** WooCommerce — keeping for product catalog (cart hidden via CSS)
- **Translation:** TranslatePress (not WPML)
- **Remove:** LayerSlider + Slider Revolution — replace hero with Elementor section
- **Keep:** WPForms, TranslatePress, ACF, JetSmartFilters, Duplicator Pro, SiteGround plugins

### Design Direction
- **White-dominant** (80%+ per brand manual) — generous white space
- **Typography-led** — Playfair Display for headings, Lexend Light for body
- **Colors:** `#1D1D1B` text, `#2E7B37` green accents, `#9F8A73` warm secondary
- **Full-bleed hero** with clean editorial photography
- **Division cards** for the main navigation to business units
- **Product section:** LDC-style sidebar navigation for divisions/products
- **DEL CAMPO:** WhatsApp Business CTA button

### New Site Architecture
Home → Acerca de Nosotros → Nuestras Divisiones (5) → Sostenibilidad y Certificaciones → Clientes → Contacto

### What the Client Likes
- Cono Group: structure, confidence, typography
- LDC: product section ("la parte de producto" — exact aspect TBD, confirm with Mazor)
- Globenatural: warm organic aesthetic
- Peruvian Nature: editorial boldness, bilingual approach

---

## Assets Still Needed

- [x] **Logo files from Anita** — .ai, .pdf, horizontal PNG, transparent PNG, isologo PNG ✅
- [x] **Recoleta font file** — Recoleta-RegularDEMO.otf ✅
- [ ] **Product photography** — from client (they have existing photos)
- [ ] **Hero/section imagery** — existing or stock aligned with brand
- [ ] **Certification logos** — high-res versions (USDA, EU Bio, BRC, Kiwa, Kosher, SMETA)
- [ ] **Content per division** — product descriptions, markets, capacidades logísticas

---

## Key Docs
- [CLIENT_BRIEF.md](01_brief/CLIENT_BRIEF.md) — full requirements + site map
- [BRAND_SUMMARY.md](03_assets/BRAND_SUMMARY.md) — colors, fonts, logo rules
- [SITE_AUDIT.md](04_current-site/SITE_AUDIT.md) — current site bugs + tech stack
- [REFERENCE_SITES.md](05_inspiration/REFERENCE_SITES.md) — reference analysis
