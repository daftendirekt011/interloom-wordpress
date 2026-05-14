# Current Site Audit — Interloom
> Captured: May 6, 2026 | URL: www.interloom.com.pe
> ⚠️ Corrected May 6 after full-page screenshots — several findings from initial WP admin session were wrong (admin bar / JS interference)

---

## Tech Stack

| Component | Details |
|-----------|---------|
| CMS | WordPress 6.9.4 |
| Theme | **Bridge** by Qode Interactive (heavy multipurpose theme) |
| Page builder | **Elementor Free 3.25.2 + Elementor Pro 3.25.4** — Pro installed but ⚠️ license may not be active ("Activate it here" prompt) |
| E-commerce | **WooCommerce** — active; product catalog is a WooCommerce shop |
| Slider | LayerSlider (active, **no license** — can't update) + Slider Revolution (active) |
| Forms | WPForms |
| Translation | **TranslatePress - Multilingual 2.6.4** (NOT WPML — earlier doc was wrong) |
| Hosting | **SiteGround** ✅ confirmed — "Purge SG Cache" in admin bar, Security Optimizer + Speed Optimizer plugins are SiteGround's own |
| Backup | Duplicator Pro — last backup Feb 5, 2025 (⚠️ over a year ago — run fresh backup before touching anything) |
| Top bar | Email + phone number shown above nav |
| Copyright footer | "INTERLOOM 2022" — 4 years old |

---

## Page Inventory

| Page | Status | Notes |
|------|--------|-------|
| Home (Front Page) | ✅ Published | Hero slider working |
| Home (Draft) | 🟡 Draft | Last modified May 4, 2026 — someone was editing recently |
| nosotros | ✅ Published | Has team section |
| Plantas de Procesamiento | ✅ Published | Sub-item under Nosotros in menu |
| Exportacion | ✅ Published | WooCommerce Shop Page — product catalog |
| Equipo de exportaciones | ✅ Published | Separate team page (Aug 2023) |
| Mercado local | ✅ Published | Product page |
| Equipo mercado local | ✅ Published | Separate team page (Aug 2023) |
| Contacto | ✅ Published | Map working |
| FAQ PAGE | ✅ Published | Elementor |
| Request a Quote | ✅ Published | |
| Products | ✅ Published | WooCommerce products listing |
| Blog | ✅ Published | |
| Cart / Checkout / My Account | ✅ Published | WooCommerce pages |
| Privacy Policy | 🟡 Draft | |
| Quote Received / Quotes List | 🟡 Draft | |
| Refund and Returns Policy | 🟡 Draft | |

**Total: 23 pages (18 published, 5 drafts)**

### Current Menu Structure
```
Home
Nosotros
  └── Plantas de Procesamiento (sub-item)
Unidades de negocio (Custom Link — no real page, that's why /unidades-de-negocio/ is 404)
  ├── Exportacion (sub-item)
  └── Mercado local (sub-item)
Catálogo (Custom Link — points to WooCommerce catalog)
Contacto
Idioma opuesto (Language Switcher — TranslatePress)
```

---

## Full Plugin Inventory

| Plugin | Status | Action |
|--------|--------|--------|
| **Elementor** (3.25.2) | Active | Keep |
| **Elementor Pro** (3.25.4) | Active ⚠️ license unconfirmed | Keep — verify license with client |
| **WooCommerce** | Active | Keep — product catalog depends on it |
| **WPForms** | Active | Keep |
| **TranslatePress - Multilingual** (2.6.4) | Active | Keep (this is the translation plugin, not WPML) |
| **ACF (Advanced Custom Fields)** | Active | Keep — likely used for custom fields |
| **Bridge Core** | Active | Remove with theme switch |
| **Qi Addons for Elementor** | Active | Remove with theme switch |
| **Qi Blocks** | Active | Remove with theme switch |
| **Qode Instagram Widget** | Active | Remove |
| **Qode Twitter Feed** | Active | Remove |
| **LayerSlider** | Active, no license | Remove — replace hero with Elementor/CSS |
| **Slider Revolution** | Active | Remove |
| **Security Optimizer** (SiteGround) | Active | Keep |
| **Speed Optimizer** (SiteGround) | Active | Keep |
| **Duplicator Pro** | Active | Keep — run fresh backup before work starts |
| **JetSmartFilters** | Active | Evaluate — used for product filtering? |
| **WBW Product Filter PRO** | Active | Evaluate — duplicate of JetSmartFilters? |
| **Premium Starter Templates** (Elementor) | Active | Can remove |
| **Duplicate Page** | Active | Keep (useful during build) |
| **Better Search Replace** | Active | Keep (useful during build) |
| **All in One WP Migration** | Active | Keep (useful for staging push) |
| **Export Media Library** | Active | Optional |
| **Content Aware** | Active | Evaluate |
| **Envato Market** | Active | Can remove if Bridge license not needed |
| **WP File Manager** | Active | Keep (useful) |
| **Custom Content Addon Stickers** | Active | Remove |

---

## Page-by-Page Notes

### Home
- **Top bar:** Shows email (contacto@interloom.com.pe) and phone ((511) 311-1730)
- **Hero:** Working slider with full-bleed food photography — wooden spoons with colorful legumes/grains (red beans, black beans, green mung beans, peanuts). Warm, rich composition.
- **Certifications bar:** SMETA, GlobalGAP, Kosher K, USDA Organic (4 visible in screenshots; may be more)
- **Unidades de Negocio section:** 2 image cards — "EXPORTACION" and "MERCADO LOCAL"
- **Productos section:** 4 featured products — Quinua Blanca, Frijol Castilla, Jengibre Orgánico Fresco, Azúcar Rubia — with "VER TODOS" CTA
- **Footer:** Logo, address, email, phone, Facebook + Instagram icons

### Nosotros
- Full-width hero banner with warehouse photo + "NOSOTROS" title overlay
- Company description block (centered, grey background)
- Sustainability paragraph + team photo (hands together)
- International markets paragraph + world map illustration
- **Team section:** "EQUIPO MERCADO EXPORTACIONES" — Aranzazu Muelle, Juan Jose Zevallos; "GERENCIA" — Antonio Cook Hardy (CEO), Alexia Cook Hardy (CEO)
- Content is solid — team names/photos + company story can be reused/adapted

### Mercado Local (product page)
- Left sidebar navigation with categories: Arroz, Azúcar, Aceites y grasas, Conservas, Menestras
- 4-column product grid with product images and names
- Products visible: Quinua Blanca, Quinua Tricolor, Aceite Vegetal, Arroz, Arveja Verde Partida, Azúcar Blanca, Azúcar Rubia, Frijol Canario, Frijol Panamito, Garbanzos, Lentejas, Maíz Pop Corn, Pallares
- ⚠️ This page covers what will become DEL CAMPO + División de Ingredientes in the new architecture

### Exportacion (product page)
- Left sidebar navigation with categories: Congelados, Secos, Granos, Legumbres, Otros commodities, Frescos y derivados
- Large product grid — richer catalog than Mercado Local
- Products visible: Quinua Roja, Quinua Negra, Quinua Tricolor, Arroz, Azúcar Blanca, Cacao en Grano, Cacao en Polvo, Jengibre Orgánico Fresco, Cúrcuma Orgánica Fresca, Palta Fresca, Jengibre Deshidratado, Cúrcuma en Polvo, Chia, and more
- ⚠️ This covers División de Secos + División de Frescos in the new architecture

### Plantas de Procesamiento
- Two facility sections:
  - **Quinoa Facility (Callao)** — grains/legumes processing plant
  - **Ginger Operation (Satipo, Junín)** — fresh produce plant
- Certification logos shown: Kosher, USDA Organic, EU Bio, BRC Food
- ⚠️ Content from here can move into the respective division pages in the new site

### Contacto
- Google Map IS loading (San Isidro, Lima visible) ✅
- A popup/overlay panel appears with contact info + product image
- 3 columns: Llámenos (phone) | Chat (WhatsApp icon) | Envíenos un Mensaje (form)
- Form fields: Name, Email, Teléfono, Mensaje

---

## Design Issues (for tomorrow's analysis)

### Critical (broken)
- [ ] Hero slider is working but uses **LayerSlider** — heavy, slow, should be replaced with clean static/CSS section
- [ ] "Unidades de Negocio" as a nav item needs restructuring (currently dropdown to flat subpages; new architecture has 5 divisions)
- [ ] ~~Google Map on Contacto not loading~~ — **Map IS working** ✅

### Design / UX
- [ ] Overall design feels dated — basic layout, generic feel (2022 era)
- [ ] Typography not using brand fonts (Playfair Display / Lexend)
- [ ] Logo in header — check if this is pre-Anita refresh (likely yes, since brand manual is from 2026)
- [ ] All-caps headings everywhere — heavy and hard to read
- [ ] Navigation structure too flat for the new multi-division architecture (currently: Home, Nosotros, Unidades de Negocio dropdown, Contacto — needs to expand)
- [ ] No sticky header
- [ ] Product pages use a sidebar + grid layout (LDC-style) — this is actually solid and directionally correct for the new site
- [ ] Footer minimal — copyright 2022, no rich content
- [ ] No "Sostenibilidad" or "Clientes" sections (required by new site map)
- [ ] Not utilizing brand color palette properly
- [ ] No visual hierarchy — everything at same weight
- [ ] Top bar (email + phone) is useful — keep this pattern or integrate into header

### Content gaps (vs. new site map)
- [ ] No individual pages per division — currently grouped as "Mercado Local" + "Exportacion" (5 new divisions needed: DEL CAMPO, Ingredientes, Secos, Frescos, Greenclover)
- [ ] No Sostenibilidad y Certificaciones page
- [ ] No Clientes section
- [ ] Greenclover Naturals LLC not represented at all
- [ ] English version exists via TranslatePress — needs audit for completeness
- [ ] Certification logos on Plantas page (Kosher, USDA Organic, EU Bio, BRC Food) — need hi-res versions for new Sostenibilidad page

---

## What's Worth Keeping

- **Content from Nosotros** — company story, sustainability text, market reach, team section with real names and photos (Antonio Cook Hardy CEO, Alexia Cook Hardy CEO, Aranzazu Muelle, Juan Jose Zevallos)
- **Product structure** — sidebar + grid layout on Mercado Local / Exportacion pages is directionally aligned with new design (LDC-style); can refine rather than rebuild from scratch
- **Product catalog content** — full list of products across both pages is good source material for division pages
- **Plantas de Procesamiento content** — facility descriptions for Callao (Secos) and Satipo (Frescos) can move into division pages
- **Hero food photography** — warm, well-shot food imagery is usable; evaluate quality at full resolution
- **Certification logos** — USDA Organic, EU Bio, BRC Food, Kiwa, Kosher, SMETA (need hi-res versions)
- **Contact form structure** — WPForms can be restyled
- **WPML** — translation plugin already set up (carry forward)
- **SiteGround hosting** — staging tool available for safe dev

---

## WordPress Strategy Notes

### Theme Decision
**Keeping Bridge** — it was a deliberate purchase, it's already paired with Elementor Pro, and the timeline doesn't justify a theme switch. Bridge controls the header and footer; Elementor Pro handles all page content. This is the intended workflow for Bridge.

Header/footer will be configured through **Bridge's header builder + Qode Options**, not Elementor Theme Builder (which currently only handles the WooCommerce product templates).

### Page Builder Decision
Stick with **Elementor Pro** — already installed, licensed (kikegaona@me.com, Active ✅), and the right tool for no-code client self-management after delivery.

⚠️ **Elementor Pro license needs to be verified** — the dashboard shows "Activate it here." Ask the client if they have an active Elementor Pro subscription (elementor.com account). If not, they'll need to renew (~$59/year). This unlocks Theme Builder (global header/footer), dynamic content, and more.

### WooCommerce
The product catalog is built on WooCommerce. This is worth keeping — product categories are already set up, the filtering plugins (JetSmartFilters, WBW Product Filter) handle the sidebar. For the redesign we restyle the shop templates with Elementor Pro rather than rebuilding the catalog from scratch.

### Staging Environment
Ask Mazor to go to **SiteGround → Site Tools → WordPress → Staging → Create Staging**. Takes 2 minutes. No technical knowledge needed. Do this before any design work on the live site.

### Before Starting Any Work — Checklist
- [ ] Run Duplicator Pro backup (last one was Feb 2025!)
- [ ] Set up SiteGround staging
- [ ] Verify Elementor Pro license is active
- [ ] Check the "Home — Draft" page (modified May 4, 2026) — what is it?

### Custom CSS (Appearance → Customize → Additional CSS)
Three rules, all hiding the WooCommerce cart from the header:
```css
.shopping_cart_header .header_cart.cart_icon:before { visibility: hidden; display: none; }
span.header_cart_span { visibility: hidden; display: none; }
.shopping_cart_header { visibility: hidden; display: none; }
```
**Why:** They use WooCommerce for the product catalog structure but it's not a real storefront — no public cart/checkout. Keep this CSS in the redesign.

### Plugins to Remove (after staging is set up)
- LayerSlider, Slider Revolution → replace hero with Elementor section or CSS
- Custom Content Addon Stickers → unnecessary
- Qode Instagram, Qode Twitter → not used in redesign
- Note: Bridge Core, Qi Addons, Qi Blocks stay — they're part of the Bridge ecosystem we're keeping

---

## Contact Info Extracted (for content reuse)
- **Address:** Av. Jorge Basadre 310, Oficina 504, San Isidro, Lima – Perú
- **Email:** contacto@interloom.com.pe
- **Phone:** (511) 311 – 1730
- **Social:** Facebook, Instagram
