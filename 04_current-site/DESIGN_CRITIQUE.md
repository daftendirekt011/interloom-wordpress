# Design Critique — Current interloom.com.pe vs. 2026 Brand Standards
> Captured: May 7, 2026
> Inputs: `03_assets/BRAND_SUMMARY.md` (Manual de Marca 2026 by Anita) + `04_current-site/SITE_AUDIT.md` + screenshots in `04_current-site/screenshots/`
> Method: `/design-critique` — first-impression, usability, hierarchy, consistency, accessibility — applied page by page, with each finding paired to the exact replacement that comes from the new brand system.

---

## Brand Standards Recap (the bar everything must clear)

The Manual de Marca 2026 sets six rules that every page below is being measured against:

1. **80% white minimum.** Every layout must read as predominantly white/off-white. Color (green especially) is an accent, never the field.
2. **Typography system is fixed.** Playfair Display for headings, Lexend Light for body. Recoleta is logo-only, never UI text. All-caps display type is not part of the system.
3. **Color palette is restrained.** Near-black `#1D1D1B`, forest green `#2E7B37`, dark brown `#4A3625`, warm tan `#9F8A73`. Bright `#009E3C` and yellow-green `#C9CC3D` exist only inside the clover gradient, not as UI fills.
4. **Logo placement rules.** White, light, or subtle-texture backgrounds only. No saturated or dark backgrounds, no busy photo overlays.
5. **Six tonal principles.** Formalidad, solidez operativa, cercanía al campo sin clichés, sostenibilidad operativa, claridad y orden, modernidad atemporal, "cool con identidad de campo".
6. **System, not pages.** Header, footer, type scale, spacing, and components must work as one flexible system across web, presentations, signatures, and merch.

**Net of these:** the current site fails the brand at the foundation level — type, color, density, and hierarchy — before any individual page is even considered. Most page-level findings below are downstream consequences of three system-level failures that have to be fixed first.

---

## Three System-Level Failures (fix these once, every page improves)

### 1. Type system is wrong everywhere

| Where it shows up | What's wrong | What replaces it |
|---|---|---|
| Page titles ("NOSOTROS", "MERCADO LOCAL", "EXPORTACION", "PLANTAS DE PROCESAMIENTO") | Heavy all-caps sans, theme default, white-on-black | **Playfair Display Regular**, sentence case ("Nosotros", "Mercado local"), `#1D1D1B` on white, ~64–80px desktop |
| Section headings ("UNIDADES DE NEGOCIO", "PRODUCTOS", "EQUIPO MERCADO EXPORTACIONES", "GERENCIA") | All-caps green sans, identical weight to product labels | **Playfair Display Regular**, sentence case, ~36–44px, `#1D1D1B`. Green reserved for a small eyebrow label or rule |
| Product names ("QUINUA BLANCA", "FRIJOL CASTILLA"…) | All-caps, tiny tracking, green | **Lexend Light** at ~16–18px, sentence case, `#1D1D1B`. Optional Playfair italic for the species/Latin name |
| Body paragraphs (Nosotros copy, facility descriptions) | Theme sans, justified, low contrast | **Lexend Light** ~17px / 1.6 line-height, left-aligned, `#1D1D1B` on white |
| Nav items ("HOME · NOSOTROS · UNIDADES DE NEGOCIO · CONTACTO") | All-caps with underline-on-active | **Lexend Light** sentence case, ~14–15px, current page indicated by green underline rule, not weight |

The all-caps habit is the single most "2022 Bridge theme" tell on the site, and it violates *claridad y orden* (caps reduce reading speed) and *modernidad atemporal* (caps + sans = generic corporate, the opposite of "elegante con identidad de campo").

### 2. Color usage is close on volume, wrong on shade and placement

The site's overall white-to-color ratio is roughly in the right zone — most content sits on white and color use is restrained. The failure isn't volume, it's three specific things: (a) a handful of concentrated dark elements in the most visible places on every page, (b) the wrong *shade* of green used for UI, and (c) pure black instead of the warmer near-black the brand specifies.

| Element | Current | Replacement |
|---|---|---|
| Top utility bar | Solid black, full-bleed — small in area but anchored at the top of every page so it dominates first impression | Remove entirely, or ultra-thin `#F7F5F1` (off-white) bar with `#1D1D1B` text |
| Page-title hero banner (Nosotros, Plantas, Mercado Local, Exportación) | Dark photo overlay with white all-caps title — the loudest single block on every subpage | White section, Playfair Display title in `#1D1D1B`, optional small image to the right (editorial split) — never overlay |
| Division/"Unidades de negocio" cards on home | Dark photo cards with white all-caps labels overlaid — also breaks the rule that the logo and brand voice can't sit on busy/dark backgrounds | White cards with Playfair title in near-black, small product photo on light backdrop |
| Section-heading green ("UNIDADES DE NEGOCIO", "PRODUCTOS", "EQUIPO MERCADO EXPORTACIONES") | `#009E3C` lime/bright green — that's the *clover gradient* color, not the UI green | Forest `#2E7B37` reserved for links/eyebrows only. Section titles themselves go to `#1D1D1B` Playfair sentence case |
| Near-black usage | Mostly pure `#000000` (top bar, page banner overlays, footer text) | Warmer `#1D1D1B` everywhere — small change, big difference in tone |
| CTA buttons ("VER TODOS", "Send") | Mid-gray pill, dark gray rectangle | Forest `#2E7B37` solid with Lexend Light label, or near-black ghost outline. One primary style across the site |
| Section background variation | White only — sections separated by dark photo bands instead of subtle background flips | Add `#FAF8F4` (off-white) or warm tan at low opacity as a secondary section background, so the layout breathes without needing dark bands |

### 3. Layout has no spacing or hierarchy system

Every screenshot shows the same pattern: blocks stacked tight to one another, identical weight, no eyebrow/title/body rhythm, no editorial splits, no rule lines, no breathing room. There is no 8/12-pt spacing scale visible — sections are separated only by background color flips. This produces the "everything at the same weight" feeling called out in the audit.

**Replacement:** an 8pt spacing scale (8/16/24/32/48/64/96/128), 12-column grid with generous gutters, a clear three-tier type scale (Display / Section / Body), and an alternating section pattern (white → off-white → white) instead of black-to-white flips.

---

## Header & Top Bar (cross-cutting — visible on every screenshot)

**What fails**

- **Black "Bienvenidos a INTERLOOM" + phone bar** is full-bleed black, putting the page below the brand's 80% white floor before the user has scrolled. The welcome message itself is filler copy, not utility.
- **Logo lockup is the pre-Anita version** — the clover sits next to "INTERLOOM" in a generic bold sans, not the Recoleta wordmark with the new gradient clover specified in the manual.
- **Nav is all-caps Bridge default** with red US-flag language switcher (TranslatePress), then a hamburger icon next to the desktop menu — two nav patterns conflicting in the same row.
- **No sticky behavior**, so on long product pages the nav scrolls away.
- **Cart icon hidden via custom CSS** (per audit) — the right pattern, but the underlying WooCommerce header template is doing work the design doesn't want.

**What replaces it**

- Remove the black welcome bar. If Mazor wants email + phone visible above the fold, put them as a thin off-white (`#FAF8F4`) bar with `#1D1D1B` Lexend Light text, right-aligned, ~12px. No "Bienvenidos a INTERLOOM" copy.
- Swap to the new horizontal logo lockup (clover gradient + Recoleta "INTERLOOM"), sized at ~36–40px tall, anchored left.
- Nav in Lexend Light sentence case, with the new five-division architecture: **Inicio · Nosotros · Divisiones ▾ · Sostenibilidad · Clientes · Contacto**, plus an ES/EN toggle as a text switch ("ES / EN") rather than a flag.
- Sticky header on scroll, white background, 1px `#EAE6DE` bottom border to anchor it.
- Bridge header builder + Qode Options used to configure the new header. Elementor Pro handles page content.

---

## Footer (cross-cutting — visible on home, nosotros, mercado local, etc.)

**What fails**

- Says "© INTERLOOM 2022" — four-year-old copyright tells visitors the site is abandoned.
- A single column with logo, address, email, phone, two social icons. No site map, no division links, no certifications, no newsletter, no language toggle, no Greenclover Naturals LLC presence (which the new architecture requires).
- Pure white background with a faint top border — visually disappears, gives no closing weight to the page.
- Phone formatted inconsistently with the header ("(511) 311 – 1730" vs. "(511) 311-1730").

**What replaces it**

- Multi-column footer on a warm tan `#9F8A73` at low opacity (or `#F7F5F1` off-white) background with `#1D1D1B` text:
  - Col 1: Logo (vertical lockup), short positioning line, address
  - Col 2: Divisiones — links to all five
  - Col 3: Compañía — Nosotros, Sostenibilidad, Clientes, Contacto
  - Col 4: Greenclover Naturals LLC contact block (US presence)
  - Col 5: Newsletter signup (Lexend Light label, near-black ghost button)
- Bottom strip: certifications row (USDA Organic, EU Bio, BRC, Kosher, SMETA, GlobalGAP) in a single rule-bordered band, monochrome treatment so they read as a system, not a logo wall.
- Copyright auto-year ("© Interloom 2026") + "Hecho en Lima, Perú".
- Social icons monochrome `#1D1D1B`, hover forest green.

---

## Home

**Screenshot:** dark-photo hero (red beans, blueberries, peanuts, mung beans on wood) with no headline overlay → 4 monochrome certification logos on a tan strip → "UNIDADES DE NEGOCIO" with two dark photo cards (Exportación / Mercado Local) → "PRODUCTOS" with 4 product images and a gray "VER TODOS" pill → minimal footer.

**First impression (2-second test).** Eye lands on the hero photo, then bounces because there is no headline, no value prop, no CTA — the page's purpose is not stated. The red US flag in the header is more visually loud than anything else in the layout, which is wrong.

**What fails**

| # | Finding | Severity |
|---|---|---|
| H1 | Hero is photo-only — no headline, no positioning line, no CTA. User can't tell what Interloom *does* | Critical |
| H2 | LayerSlider rendering hero — heavy plugin, no licence, slow LCP | Critical |
| H3 | "UNIDADES DE NEGOCIO" still reflects old 2-bucket architecture (Exportación / Mercado Local). New architecture has 5 divisions | Critical |
| H4 | Section heading uses lime-green all-caps sans, off-brand | Moderate |
| H5 | Two division cards are dark photos with white all-caps labels — logo + brand can't sit on dark/busy backgrounds | Moderate |
| H6 | Featured products row is decorative-only; no link to products, no category context, no SKU/origin info | Moderate |
| H7 | "VER TODOS" CTA is a low-contrast gray pill — fails as primary action | Moderate |
| H8 | No Sostenibilidad / Clientes / Greenclover blocks anywhere on the home page | Critical |
| H9 | Certifications strip is on a tan band with mismatched logo treatments (some color, some mono) | Minor |

**What replaces it**

- **Hero (white background, editorial split):** Playfair Display H1 in `#1D1D1B` ("Cadenas de suministro agrícolas, hechas en Perú" or similar — final copy from Mazor), Lexend Light supporting line, primary CTA "Conocer divisiones" forest-green. Right side: a single high-quality product/field photo with generous margin — *never* full-bleed under the title. Hero rendered in Elementor (no LayerSlider).
- **Trust bar (right under hero):** 6 monochrome certification marks on a single off-white band, equally spaced, with a small "Certificaciones y estándares" eyebrow — one consistent treatment.
- **Divisiones grid (replaces "UNIDADES DE NEGOCIO"):** five cards in a 3-2 or 5-up grid — DEL CAMPO, Ingredientes, Secos, Frescos, Greenclover. Each card: white background, near-black Playfair title, one-line Lexend Light descriptor, small forest-green arrow link. Optional small product photo per card on a *light* background. No dark photo overlays.
- **Sostenibilidad block:** new section, image left / text right, Playfair Display title, Lexend Light paragraph, link to /sostenibilidad.
- **Clientes / "Trabajamos con":** logo wall (monochrome, single tone) of B2B clients, with a "Conocer clientes" link.
- **Featured products → optional:** if kept, render as a horizontal scroller with proper product cards (image, sentence-case name, division tag, link to product) — *not* as four floating images.
- **Contacto closing block:** simple two-column block (address / form) above the footer.

**What works (keep, restyle):**
- The food photography itself is warm and well-shot — keep the assets, but use them in editorial frames, not as full-bleed dark overlays.

---

## Nosotros

**Screenshot:** dark hero banner with "NOSOTROS" all-caps overlay → three editorial blocks (clover icon + paragraph; team-hands photo + sustainability paragraph; world map illustration + markets paragraph) → certification row (USDA Organic, EU Bio, BRC Food, Kiwa) → "EQUIPO MERCADO EXPORTACIONES" with two name cards (Aranzazu Muelle, Juan Jose Zevallos) → "GERENCIA" with two name cards (Antonio Cook Hardy, Alexia Cook Hardy) → footer.

**First impression.** This is the strongest page in terms of *content* (real story, real team, real markets) and the weakest in *presentation* — every well-written paragraph is buried in default Bridge styling.

**What fails**

| # | Finding | Severity |
|---|---|---|
| N1 | Hero banner is full-bleed dark photo with white all-caps "NOSOTROS" — same problem as every other page banner | Critical |
| N2 | Body copy is theme sans, justified, mid-gray on light gray box — low contrast and visually inert | Moderate |
| N3 | Clover icon used as illustration is the *old* logo, not the new gradient version | Moderate |
| N4 | Team cards have **no photos** — just a bordered box with the name in Playfair-ish all-caps, a generic bio, and a tiny LinkedIn-blue square | Critical |
| N5 | Two team sections ("Equipo Mercado Exportaciones" + "Gerencia") are identical components — no hierarchy between leadership and operating team | Moderate |
| N6 | Certification logos are at random sizes and color treatments (USDA in green, EU Bio in green, BRC in green check, Kiwa in red) — reads as a sticker collection, not a system | Moderate |
| N7 | World-map illustration is a stock green-blob graphic — undermines "modernidad atemporal" | Minor |
| N8 | No timeline / no facility map / no values block — the page reads as text-and-photos with no structural backbone | Moderate |

**What replaces it**

- **Hero:** white section, Playfair Display "Nosotros" left-aligned at ~80px, Lexend Light positioning line below ("30 años llevando productos peruanos al mundo, con estándar operativo y trazabilidad"), one editorial photo right (warehouse, field, or team — *not* overlaid).
- **Story block:** two-column editorial layout — Playfair eyebrow ("Nuestra historia") + Lexend Light paragraphs. Replace clover-icon-as-illustration with either a real archive photo or an abstract textured panel.
- **Sostenibilidad excerpt:** kept here as a teaser, with a "Ver más sobre sostenibilidad" link to the new dedicated page (so this page doesn't carry the whole topic).
- **Mercados block:** replace the green-blob world map with a clean line-art world map in `#1D1D1B` with destination markets dotted in forest green. Lexend Light caption listing the countries.
- **Operaciones strip:** small visual block — "2 plantas, Callao y Satipo" — with link to the new Plantas page.
- **Liderazgo (was "Gerencia"):** large 2-up cards with **real photos** of Antonio Cook Hardy and Alexia Cook Hardy, Playfair name, Lexend Light role + bio, optional LinkedIn icon (monochrome). Photos are non-negotiable for credibility on a B2B site.
- **Equipo (was "Equipo Mercado Exportaciones"):** smaller 4-up grid, photo + name + role, same component template at a different scale. Add Aranzazu Muelle, Juan Jose Zevallos with photos.
- **Certificaciones strip:** moved to its own Sostenibilidad page; on Nosotros only a single "Trabajamos bajo estándares internacionales" line + link.

**What works (keep, restyle):**
- Real names and bios are gold — keep verbatim, restyle the wrapper.
- The story-then-team narrative arc is correct; only the components need to be replaced.

---

## Plantas de Procesamiento (operaciones.png)

**Screenshot:** dark hero with "PLANTAS DE PROCESAMIENTO" all-caps overlay → two text-only cards ("QUINOA FACILITY" and "GINGER OPERATION") with a tiny "INTERLOOM" eyebrow → row of certifications (Kosher, USDA Organic, EU Bio, BRC Food) → minimal footer.

**First impression.** A page about physical infrastructure has zero photographs of physical infrastructure. The two facility cards are bordered text boxes — they could describe anything.

**What fails**

| # | Finding | Severity |
|---|---|---|
| O1 | No facility photographs whatsoever — no exterior, no interior, no equipment, no team-on-site | Critical |
| O2 | Page-title banner is the same dark photo overlay pattern, off-brand | Critical |
| O3 | Facility names in English ("Quinoa Facility", "Ginger Operation") while the rest of the site is Spanish — inconsistent without an obvious reason | Moderate |
| O4 | "INTERLOOM" eyebrow above each card is meaningless and adds visual noise | Minor |
| O5 | No location map, no capacity/throughput numbers, no certifications mapped to which plant has which | Moderate |
| O6 | Certification row at the bottom is identical to the one on Nosotros — duplicated, no context | Moderate |
| O7 | Page lives at a flat URL ("Plantas de Procesamiento") but the new architecture wants this content to live inside the relevant division pages (Secos = Callao, Frescos = Satipo) | Moderate |

**What replaces it**

- **Hero:** white section, Playfair "Operaciones" or "Nuestras plantas", Lexend supporting line.
- **Two facility blocks** as full editorial sections, each with:
  - **Wide photograph** of the actual plant (exterior or processing line)
  - Playfair section title in Spanish: "Planta Callao — Granos y legumbres" / "Planta Satipo — Frescos y derivados"
  - Lexend Light copy (current copy is reusable, just rewritten for hierarchy)
  - **Specs strip** below: location, area (m²), throughput, certifications applicable to *this* plant, year operational
  - Small line-art map showing location in Peru
- **Architecture call:** content from this page splits into the new Secos and Frescos division pages per the audit. This page can either (a) become a single "Operaciones" overview that links to each division for the deep dive, or (b) be deprecated entirely. Recommendation: **keep as overview**, since visitors arriving from "Sostenibilidad" or "Nosotros" benefit from a single operational summary.
- Drop the "INTERLOOM" eyebrows — they're a Bridge-theme template artifact.

**What works (keep, restyle):**
- Existing copy describing each facility is solid B2B language — keep, reformat into specs.

---

## Mercado Local

**Screenshot:** dark hero with "MERCADO LOCAL" all-caps overlay → left sidebar with category filter (Arroz, Azúcar, Aceites y grasas, Conservas, Menestras) → 4-column product grid (Quinua Blanca, Quinua Tricolor, Aceite Vegetal, Arroz, Arveja Verde Partida, Azúcar Blanca, Azúcar Rubia, Frijol Canario, Frijol Panamito, Garbanzos, Lentejas, Maíz Pop Corn, Pallares) → footer.

**First impression.** This is the most directionally correct page on the site — sidebar + grid is a real B2B catalog pattern. But every individual component is unstyled.

**What fails**

| # | Finding | Severity |
|---|---|---|
| M1 | Page banner same dark overlay pattern | Critical |
| M2 | Sidebar is unstyled list of category names — no counts, no active state, no hover, no icons | Moderate |
| M3 | Product cards are an image floating on white with an all-caps green name underneath — no card structure, no border, no division/category tag, no presentation format, no link affordance | Critical |
| M4 | Product images are inconsistent — some on white, some on tan, some with shadows, some without — clearly different photo shoots glued together | Moderate |
| M5 | "Mercado Local" as a *page* doesn't survive the new architecture — its products split between DEL CAMPO and División de Ingredientes | Critical |
| M6 | No product-detail destination — clicking a product goes to a default WooCommerce template (per audit), which the brand doesn't control | Critical |
| M7 | No filter beyond category — no search, no presentation/format filter, no certification filter | Moderate |

**What replaces it**

- **Page-level:** retire "Mercado Local" as a top-level page. Its products redistribute into the new division pages (DEL CAMPO and División de Ingredientes). The catalog *pattern* (sidebar + grid) is reused on each division page.
- **Hero:** white, Playfair Display title ("DEL CAMPO" or "División de Ingredientes" — sentence case), Lexend Light positioning line specific to that division.
- **Sidebar:** Lexend Light category list, sentence case, with product count beside each label `Menestras (12)`, active item indicated by forest-green left rule + slight bold. Add filters: Presentación (granel / consumo / industrial), Certificación, Origen (when relevant).
- **Product card (new component, used on every catalog page):**
  - Square product photo on `#FAF8F4` off-white (one consistent backdrop across all photography — re-shoot or color-correct existing assets)
  - Product name in Lexend Light sentence case, near-black
  - Latin/scientific name in Playfair italic, smaller, optional
  - Tiny tag row below: `Granel · Orgánico · USDA` in Lexend Light, near-black
  - Whole card is the link target — hover lifts card with soft shadow + faint forest-green border
- **Product detail:** restyle the WooCommerce single-product template via Elementor Pro Theme Builder. White background, generous margins, tabbed content (Descripción · Especificaciones · Presentaciones · Certificaciones · Origen · Solicitar muestra). "Solicitar cotización" CTA in forest green replaces the hidden cart button.
- **Photo system:** mandate a single photo treatment — same backdrop, same lighting, same crop ratio — across all 60+ products. This is the highest-leverage visual upgrade on the site.

**What works (keep, restyle):**
- Sidebar + grid is the right pattern.
- Product list is solid source content.
- Existing JetSmartFilters / WBW Product Filter wiring can power the new filter UI.

---

## Exportación

**Screenshot:** identical pattern to Mercado Local — dark "EXPORTACION" banner → sidebar (Congelados, Secos, Granos, Legumbres, Otros commodities, Frescos y derivados) → richer 4-column product grid with quinoas, cacao, ginger, turmeric, avocado, chia, beans, etc. → minimal footer.

**First impression.** Same pattern, same problems, slightly richer catalog. The category sidebar conflates form (Congelados, Secos, Frescos) with type (Granos, Legumbres) — a taxonomy issue, not just a styling one.

**What fails**

| # | Finding | Severity |
|---|---|---|
| E1 | All catalog/styling failures from Mercado Local apply identically | Critical |
| E2 | Category taxonomy mixes processing state (Congelados / Secos / Frescos) with botanical type (Granos / Legumbres) — confusing and inconsistent | Critical |
| E3 | "Exportación" as a page doesn't survive the new architecture either — it splits into División de Secos and División de Frescos | Critical |
| E4 | Product photography is more inconsistent than Mercado Local — backdrops range from white to wood to dark, scales vary | Moderate |
| E5 | No origin/destination context, despite this being the export catalog — no "this product ships from Callao to EU/US" markers | Moderate |
| E6 | No B2B-specific affordances — no MOQ, no Incoterms, no "request sample" / "request quote" CTA on the listing | Critical |

**What replaces it**

- **Page-level:** retire "Exportación" as a top-level page. Products split into División de Secos (Callao plant) and División de Frescos (Satipo plant), each with its own catalog using the unified sidebar + grid + card pattern. "Otros commodities" likely becomes Greenclover Naturals (US-based commodity trading) and gets its own division page.
- **Sidebar taxonomy:** within each division, sidebar lists by *type* only (Granos, Legumbres, Cacao, Especias, Aceites, etc.) — processing state is implicit in the division. Add filters for presentación / certificación / destino.
- **Product card (B2B variant):** same component as Mercado Local, plus optional tag for "Disponible para exportación" or destination flags (single-color line-art) for the principal markets.
- **Catalog header on each division page:** small infographic strip — `2 plantas · X SKUs · Y mercados · Z certificaciones` in Lexend Light — replaces the generic dark hero.
- **CTA pattern:** "Solicitar cotización" / "Solicitar muestra" available both at the catalog level and on each product detail.

**What works (keep, restyle):**
- The catalog is genuinely deep — keep every product.
- Sidebar + grid pattern survives.
- Filtering plugins are already in place (per audit).

---

## Contacto + Contacto sidebar popup

**Screenshot:** dark "CONTACTO" banner (implied by header pattern) → Google Map with pin in San Isidro → three columns (Llámenos / Chat / Envíenos un Mensaje) with phone, generic green WhatsApp icon, and a 4-field form (Name, Email, Teléfono, Mensaje, "Send" button) → footer.
**Sidebar popup (contacto-sidebar.png):** a slide-in panel with logo, a small dark photo of red/orange/yellow grains, "Póngase en contacto con nosotros y lo atenderemos lo antes posible.", address, email, phone — over a dimmed page.

**First impression.** Two contact patterns running at once (page + sidebar popup) and neither is on-brand. The popup behaves like a dismissable ad, not a contact aid.

**What fails**

| # | Finding | Severity |
|---|---|---|
| C1 | Sidebar popup interrupts reading on every page (per the screenshot pattern), darkens the page, and partially repeats the same info as the Contacto page | Critical |
| C2 | "Send" button on the form is dark gray rectangle in English ("Send") on a Spanish-language site | Moderate |
| C3 | Form fields are theme-default thin-outlined inputs — no labels, only placeholders, which fails accessibility (when text is typed the placeholder vanishes and the user loses context) | Critical |
| C4 | Generic green WhatsApp logo dropped in the middle column with no styling — feels pasted in | Moderate |
| C5 | Hours info ("LUN-VIE: 9am to 6pm") is in English on a Spanish page | Moderate |
| C6 | No segmented contact paths — same form regardless of whether visitor is press, customer, supplier, applicant | Moderate |
| C7 | Map is a default Google Maps embed without brand color treatment | Minor |
| C8 | Map is *inside* a column layout that breaks at narrow widths — collapses awkwardly | Moderate |

**What replaces it**

- **Kill the sidebar popup entirely.** Contact info already lives in the header utility bar and the footer; a dismissable overlay is unnecessary friction and breaks the brand's "claridad y orden" principle.
- **Hero (Contacto page):** white, Playfair "Contacto", Lexend Light line ("Comercial, exportación, prensa o trabajo con nosotros — escríbanos").
- **Two-column layout:**
  - **Left:** segmented contact options as four small cards — Comercial / Exportación / Prensa / Trabaja con nosotros — each with its own email + relevant phone extension
  - **Right:** clean form with proper floating labels, four fields (Nombre, Empresa, Email, Mensaje), single primary CTA "Enviar mensaje" in forest-green Lexend Light. WPForms restyled.
- **Map block:** below the columns, full-width with a `#1D1D1B` near-black tint applied to the Google Map style (custom map style JSON), forest-green pin, address overlay card in white with Lexend Light text.
- **Office strip:** small two-up section — "Oficina Lima · Av. Jorge Basadre 310, Of. 504, San Isidro" + "Greenclover Naturals LLC · [US address]" — reinforces the multi-entity story.
- **Hours + WhatsApp:** consolidated into a small footer-of-page strip in Spanish ("Lun–Vie · 9:00 a 18:00"), WhatsApp as a monochrome icon with text link, not the green sticker.

**What works (keep, restyle):**
- Address, phone, email, map embed are all correct content — only the wrappers fail.

---

## Cross-cutting accessibility findings

| Issue | Where | Replacement |
|---|---|---|
| Placeholder-only form fields | Contact form | Floating labels (visible label that animates above the input on focus) |
| All-caps display type at heading sizes | Every page banner and section heading | Sentence case in Playfair Display — also restores Spanish accents (NOSOTROS → Nosotros, EXPORTACION → Exportación) |
| Low-contrast green-on-white for headings (`#009E3C` on white = ~3.4:1, fails WCAG AA for normal text) | Section headings, product names | Use near-black `#1D1D1B` for body + headings; reserve green for forest `#2E7B37` (~5.5:1) on white for links/eyebrows only |
| White text on dark photo overlays in page banners | Every secondary page | Replaced by white-section text-only headers — no overlay needed |
| Touch targets on filter sidebar | Mercado Local, Exportación | Min 44×44px hit area, Lexend Light 16px label, 12px vertical padding |
| Form button labels in English | "Send" on Contacto | "Enviar mensaje" in Spanish (Lexend Light) |
| Mixed Spanish/English copy | "Quinoa Facility", "Ginger Operation", "LUN-VIE: 9am to 6pm" | Spanish on the .pe site, parallel English version via TranslatePress for the English locale |
| Logo on dark/photo backgrounds | Header (against dark top bar), division cards (logo near dark photos) | Logo only on white, off-white, or fine-texture backgrounds per brand manual |

---

## Priority Recommendations

1. **Replace the global type and color system before doing any page work.** Set Elementor Global Colors (6 brand tokens) and Elementor Global Fonts (Playfair Display + Lexend Light) on day one. Configure Bridge's global typography in Qode Options to match. Every page improves by ~70% as a side effect of this single change.
2. **Build one product card and one section component, then replicate.** The single most repeated element across the site is the product image + name. Build it once (off-white backdrop, Lexend Light name, optional Playfair italic species, tag row) and apply it to all 60+ products in WooCommerce — including consistent photo retouching to a single backdrop. Same logic for the catalog sidebar and the page hero.
3. **Restructure the page architecture before redesigning Mercado Local / Exportación.** The new five-division architecture (DEL CAMPO, Ingredientes, Secos, Frescos, Greenclover) supersedes the current 2-bucket split. Don't redesign the old buckets — design the new divisions and migrate content. Add the missing pages (Sostenibilidad, Clientes, Greenclover) alongside.
4. **Kill the dark bands and overlays in concentrated places.** The site is already mostly white, so this isn't a global rebalance — it's surgical: remove the black top welcome bar, replace every dark page-title banner with a white section + Playfair title, and lighten the dark division cards on home. These are small in area but disproportionately loud, and removing them is what makes the site finally read as on-brand.
5. **Re-shoot or color-correct product photography to a single backdrop.** Inconsistent product photography is the most visible "off-brand" symptom on the catalog pages and the cheapest to fix at the asset level (no code).
6. **Add real photos to the Liderazgo + Equipo blocks on Nosotros.** A B2B trust page without faces undercuts every other claim on the site.
7. **Remove the contact sidebar popup.** It violates the entire "claridad y orden" principle and provides no information that isn't in the header/footer/contact page.

---

## Summary table — what survives, what's replaced, what's new

| Element | Verdict |
|---|---|
| Bridge theme | **Keep** — header/footer via Bridge + Qode Options; page content via Elementor Pro |
| LayerSlider + Slider Revolution + unused Qode plugins | **Remove** — replace hero with Elementor section or CSS |
| Pre-Anita logo lockup | **Replace** — new horizontal lockup (gradient clover + Recoleta wordmark) |
| All-caps theme typography | **Replace** — Playfair Display + Lexend Light, sentence case |
| Black top bar + black page banners + dark photo overlays | **Remove** — white sections with Playfair titles |
| Product catalog (sidebar + grid pattern) | **Keep, restyle** with new card + photo system |
| Product photography | **Color-correct or re-shoot** to a single off-white backdrop |
| Nosotros narrative + team names | **Keep copy, redesign components**, add real team photos |
| Plantas de Procesamiento copy | **Keep copy, redistribute** content into Secos + Frescos divisions, add real facility photos |
| Mercado Local / Exportación as pages | **Retire** — content migrates to the five new division pages |
| Contact form | **Restyle** WPForms — floating labels, Spanish CTA, forest-green primary |
| Contact sidebar popup | **Remove entirely** |
| Footer | **Replace** — multi-column off-white footer with full nav, Greenclover block, certifications strip, dynamic year |
| Sostenibilidad page | **New** — required by new site map |
| Clientes page | **New** — required by new site map |
| Greenclover Naturals LLC presence | **New** — currently absent on the site |
| WPForms / WooCommerce / TranslatePress / SiteGround / JetSmartFilters | **Keep** — restyle templates only |
