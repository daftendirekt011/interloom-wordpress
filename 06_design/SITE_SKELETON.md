# Interloom — Site Skeleton (As Built)
> Updated May 22, 2026 — reflects final approved mockups in `docs/`
> Previous version was a planning doc. This version matches the HTML release exactly.

---

## Page Index & URLs

| Page | HTML file (docs/) | WP URL | Template |
|------|-------------------|--------|----------|
| Home | `home-version-a.html` | `/` | Custom — Elementor |
| Nosotros | `nosotros.html` | `/nosotros/` | Custom — Elementor |
| **Del Campo** | `del-campo.html` | `/del-campo/` | Unique — own layout (not division template) |
| **Ingredientes** | `division-ingredientes.html` | `/divisiones/ingredientes/` | Division template |
| **Secos** | `division-secos.html` | `/divisiones/secos/` | Division template |
| **Frescos** | `division-frescos.html` | `/divisiones/frescos/` | Division template |
| **Greenclover Naturals** | `division-greenclover.html` | `/divisiones/greenclover/` | Division template |
| Sostenibilidad | `sostenibilidad.html` | `/sostenibilidad/` | Custom — Elementor |
| Clientes | `clientes.html` | `/clientes/` | Custom — Elementor |
| Contacto | `contacto.html` | `/contacto/` | Custom — Elementor |

> ⚠️ Del Campo URL changed: `/divisiones/del-campo/` → `/del-campo/` (top-level, not under Divisiones)

---

## Navigation Structure

### Header (Bridge — Qode Options + custom CSS)

```
[LOGO]   Nosotros  |  Del Campo  |  Divisiones ▾  |  Sostenibilidad  |  Clientes  |  Contacto   ES | EN
```

**Key change vs original plan:** Del Campo is now a **top-level nav item** — separate from Divisiones.

**Divisiones dropdown — 4 items only (Del Campo is NOT in this dropdown):**
```
División de Ingredientes    → /divisiones/ingredientes/
División de Secos           → /divisiones/secos/
División de Frescos         → /divisiones/frescos/
Greenclover Naturals LLC    → /divisiones/greenclover/
```

**Utility bar (above nav):**
```
contacto@interloom.com.pe    |    (511) 311-1730    [Facebook] [Instagram]
```
Height: 32px · Background: `#FAF8F5` · Font: Lexend Light 12px

**Dropdown panel specs:**
- Width: 280px, left-aligned below "Divisiones"
- Background: white, 1px `#EDEAE3` border
- Item padding: 14px 24px, border-left 3px transparent (active/hover: `#2E7B37`)
- Hover: text `#2E7B37` + background `#FAF8F5` + left border `#2E7B37`

### Footer (5 columns — Bridge Footer widget areas)
```
Col 1: Brand block (logo 90px height + descriptor text + social icons)
Col 2: Divisiones (5 division links — including Del Campo)
Col 3: Empresa (Nosotros, Sostenibilidad, Clientes, Contacto)
Col 4: Contacto (address, phone, email, WhatsApp for Del Campo)
Col 5: Certificaciones (6 cert marks, 2-col grid, 44px height each)
```
Background: `#FAF8F5` · Top border: 1px `#EDEAE3` · Padding: 96px 80px 48px

---

## Design Tokens (from mockup CSS — use these everywhere)

```css
--text-primary:       #1D1D1B;
--text-secondary:     #4A3625;
--accent-warm:        #9F8A73;
--accent-green:       #2E7B37;
--accent-green-hover: #256328;
--surface-warm:       #FAF8F5;
--hairline:           #EDEAE3;
--white:              #FFFFFF;

--max-width:          1480px;
--gutter-desktop:     80px;
--gutter-tablet:      48px;
--gutter-mobile:      20px;
```

**Del Campo only — extra token:**
```css
--dc-blue:   #1B3D87;
--dc-yellow: #F5C518;   /* CTA hover accent */
```

---

## Page-by-Page Content (As Built)

### Home `/`

1. **Utility bar** — email left, phone + social icons right
2. **Fixed/sticky header** — logo + nav + lang toggle + hamburger
3. **Hero (Version A — locked)** — full-bleed photo (`assets/hero.jpg`), dark gradient left mask, content bottom-left
   - Eyebrow: "GRUPO INTERLOOM · LIMA, PERÚ"
   - H1: "Agro con trazabilidad real."
   - Sub: "+30 años exportando granos andinos, frescos e ingredientes a más de 25 países..."
   - CTA: "Conoce nuestras divisiones" → `#divisiones`
4. **Certifications strip** — `#FAF8F5` background, "Certificaciones" label left, 6 cert logos right (real images at 36px height, opacity 0.55)
   - Files: `cert-usda.jpg`, `cert-eubio.jpg`, `cert-brc.jpg`, `cert-smeta.jpg`, `cert-kosher.png`, `cert-kiwa.jpg`
5. **Nuestras Divisiones** (`id="divisiones"`) — white background, padding 128px
   - Section head: eyebrow "NUESTRAS DIVISIONES" + H2 "Una marca local y cuatro divisiones de exportación." + subtitle
   - **Del Campo featured band** — 2-col (1.05fr / 1fr), photo left (`assets/division-delcampo.jpg`), content right:
     - Eyebrow: "MARCA PROPIA · MERCADO LOCAL"
     - H3: "Del Campo" + italic tagline "Lo natural a tu mesa"
     - Description paragraph
     - CTAs: WhatsApp button (#25D366) + outline "Conocer la marca →"
   - **Sub-header B2B**: eyebrow "B2B · EXPORTACIÓN" + H4 "Cuatro divisiones para mercados internacionales"
   - **4-column export grid** — Ingredientes, Secos, Frescos, Greenclover
     - Each card: 4:5 ratio photo + H3 Playfair 20px + desc Lexend 13px + green arrow "→"
     - Hover: photo scales 1.03, arrow moves 4px right
6. **About teaser** — 2-col (1.05fr / 1fr): copy left + photo right (`assets/nosotros_equipo.jpg`)
   - Eyebrow: "QUIÉNES SOMOS"
   - H2: "Tres décadas conectando campo y mercado."
   - Lead paragraph (Playfair 24px) + body paragraph (Lexend 16px)
   - Link: "Conoce nuestra historia →" (green underline)
7. **Stats band** — `#FAF8F5` bg, 4-column grid, Playfair 64px green numbers:
   - +30 / años exportando agro
   - 25+ / países atendidos en cuatro continentes
   - 8,000t / exportadas en los últimos 4 años
   - Top 5 / exportador de quinua
8. **Sostenibilidad teaser** — `#FAF8F5` bg, centered, Playfair italic blockquote 32px:
   - *"Toda la cadena, una sola firma — del productor andino al cliente internacional."*
   - Link: "Conoce nuestras prácticas →"
9. **Contacto CTA** — white, centered, Playfair H2 "¿Trabajamos juntos?", subtitle, green CTA → `/contacto`
10. **Footer**

---

### Nosotros `/nosotros/`

1. Utility bar + Header (Nosotros active)
2. **Page hero** — full-bleed (`assets/hero_nosotros.jpg` or `hero_nosotros_manos.jpg`), H1 "Nosotros", eyebrow "GRUPO INTERLOOM"
3. **Historia** — 3-col grid layout (head + extended body): eyebrow "NUESTRA HISTORIA" + H2 "Tres décadas de agro peruano." + 3 paragraphs (company origin → growth → today)
4. **Stats band** — same 4 stats as home (shared component)
5. **Operaciones** — (from original skeleton — 2 plants: Callao + Satipo with photos)
6. **Sostenibilidad excerpt** — `#FAF8F5` centered, Playfair italic blockquote (different from home) + link → `/sostenibilidad/`
7. **Mercados** — 2-col: left (eyebrow + H2 + body + 2-col market list), right (map placeholder)
   - Market list items separated by hairline borders
8. **Equipo** — `#FAF8F5` bg, 2 groups with hairline separator:
   - Liderazgo: Antonio Cook Hardy (CEO), Alexia Cook Hardy (CEO) — 132×132 photo + name + role (green) + bio
   - Exportaciones: Aranzazu Muelle, Juan Jose Zevallos — smaller cards (104×104)
   - Photos: `team_antonio.jpg`, `team_alexia.jpg`, `team_aranzazu.jpg`, `team_juanjose.jpg`
9. **Contacto CTA** — same shared component as home
10. Footer

---

### Del Campo `/del-campo/`
> ⚠️ Unique page — completely different layout and visual identity from the 4 export division pages

**Visual identity overrides:**
- Accent color: `--dc-blue: #1B3D87` (replaces green for eyebrows and labels)
- Footer: dark (`#1D1D1B` bg), not the warm beige footer
- No "Divisiones" sidebar — product catalog shows as full-width cards

**Sections:**
1. Utility bar + Header (Del Campo active)
2. **Hero "marquee infinito"** — 2 rows of product packaging scrolling in opposite directions (CSS animation, infinite loop). No full-bleed photo. Head: eyebrow + H1 "Del Campo". Foot: "Dónde comprar" button + "Ver catálogo →" outline button
   - Row 1 images (→): dc-arroz-delcampo, dc-aceite-900, dc-arroz-rico, dc-girasol-900, dc-manteca, dc-arroz-celeste, dc-aceite-5lt, dc-arroz-embolsado
   - Row 2 images (←): dc-arroz-olimar, dc-aceite-fritura, dc-arroz-parbolizado, dc-girasol-20lt, dc-aceite-3-5lt, dc-azucar, dc-duraznos, dc-manteca
3. **Intro** — 2-col (story + text) + 3 animated counter stats:
   - 30+ / Años de Grupo Interloom respaldando la marca
   - 25+ / Mercados internacionales con nuestro estándar
   - 5 / Líneas de producto para el hogar y la pastelería
4. **Catálogo** (`id="productos"`) — centered head "Cinco líneas." + 5 product line cards. Each card: info col (line number label + H3 + description + presentaciones) + posters col (3-4 product images with 3D tilt effect on hover):
   - Línea 01 — Arroces (arroz-delcampo, arroz-rico, arroz-celeste, arroz-embolsado)
   - Línea 02 — Aceites (aceite-900, aceite-5lt, aceite-fritura, girasol-900)
   - Línea 03 — Manteca Vegetal
   - Línea 04 — (pending content)
   - Línea 05 — (pending content)
5. **Dónde comprar** (`id="donde-comprar"`) — distribution channel cards (4 channels in grid)
6. **Por qué Del Campo** — 3-column brand value blocks
7. **CTA** — WhatsApp Business button + "Conocer Grupo Interloom" link
8. Dark footer (simplified: copyright left + links right)

---

### División pages (template — used 4×: Ingredientes, Secos, Frescos, Greenclover)

1. Utility bar + Header (Divisiones active)
2. **Breadcrumb** — "Inicio > Divisiones > [Division Name]"
3. **Division hero** — 60vh full-bleed photo, dark overlay, H1 overlay
4. **Intro band** — Playfair lead paragraph (35-50 words)
5. **Two-column product body** — padding 32px 80px 120px:
   - Sidebar (280px sticky, top: 120px): category nav links + certifications 2×3 grid
   - Main content: content heading (Playfair 32px) + product rows separated by hairlines
   - Each product row: 280×280 image (white bg, 1px border, 24px padding) + H3 + description + meta (certifications · presentations)
6. **Closing band** — 50vh full-bleed photo, dark overlay, centered Playfair italic blockquote
7. Footer (standard warm beige)

**Division-specific content:**

| Division | URL | Products | Plant | Hero | CTA |
|----------|-----|----------|-------|------|-----|
| Ingredientes | `/divisiones/ingredientes/` | Azúcar Rubia, Azúcar Blanca, Almidón de Papa, Glutamato | — | `division-ingredientes.jpg` | Solicitar cotización |
| Secos | `/divisiones/secos/` | Quinua Blanca, Q. Roja, Q. Tricolor, Q. Negra, Chía, Kiwicha, Maíz Mote, Maíz Cusco, Pallar, Frijol Canario, Sésamo, Harina de Quinua | Callao | `hero_secos.jpg` / `division-secos.jpg` | Solicitar cotización |
| Frescos | `/divisiones/frescos/` | Jengibre Orgánico, Cúrcuma Fresca, Palta Fresca, Cacao en Grano, Jengibre Deshidratado, Cúrcuma en Polvo, Cacao en Polvo | Satipo, Junín | `division-frescos.jpg` | Solicitar cotización |
| Greenclover | `/divisiones/greenclover/` | US distribution, pallet sales with traceability | USA | `division-greenclover.jpg` | Contacto / Quote |

---

### Sostenibilidad `/sostenibilidad/`

1. Utility bar + Header (Sostenibilidad active)
2. **Page hero** — full-bleed (`assets/hero_sostenibilidad.jpg`), H1 "Sostenibilidad y Certificaciones"
3. **Intro** — eyebrow "NUESTRO ENFOQUE" + lead + body paragraph (sustainability as operational principle)
4. **Certificaciones section** — 2-col head (eyebrow + H2 "Verificadas por terceros, válidas en cada mercado.") + certs-cards grid. Each cert card: logo placeholder + H3 + description + "Aplica a: [divisions]":
   - USDA Organic → Secos · Frescos · Greenclover
   - EU Bio → Secos · Frescos · Greenclover
   - BRC Food → Secos · Frescos
   - Kiwa → Secos · Frescos
   - Kosher → Secos
   - SMETA → Secos · Frescos
5. **Prácticas** — 3-column: Trazabilidad · Plantas propias · Cadena de origen
6. **Contacto CTA** — shared component
7. Footer

---

### Clientes `/clientes/`

1. Utility bar + Header
2. Page hero H1 "Clientes"
3. Markets section — world map placeholder + destination country list
4. Client logos wall — monochrome (pending client delivery)
5. Optional testimonial / case study
6. Contacto CTA
7. Footer

---

### Contacto `/contacto/`

1. Utility bar + Header (Contacto active)
2. **Page hero** — full-bleed (`assets/hero_contacto.jpg`), H1 "Contacto"
3. **Contact body** — 2-col (form left, contact cards right... or left=cards, right=form — confirm in HTML):
   - 4 segmented contact cards: Comercial · Exportación · Prensa · Trabaja con nosotros (each with email)
   - WPForms restyled (floating labels, "Enviar mensaje" CTA)
4. **Map** — full-width 420px height, hatch-pattern placeholder, green pin at San Isidro location
5. **Offices strip** — `#FAF8F5` bg, 2-col: Lima office + Greenclover US
   - Lima: Av. Jorge Basadre 310, Of. 504, San Isidro, Lima – Perú · (511) 311-1730 · contacto@interloom.com.pe
   - Greenclover: US address (TBD)
6. Footer

---

## Assets Inventory (docs/assets/)

### Photos — confirmed present
| File | Used in |
|------|---------|
| `hero.jpg` | Home hero |
| `hero_nosotros.jpg` / `hero_nosotros_manos.jpg` | Nosotros hero |
| `hero_kion_aerial.jpg` | Home hero alternative |
| `hero_kion_field.jpg` | (available) |
| `hero_secos.jpg` | Secos hero |
| `hero_sostenibilidad.jpg` | Sostenibilidad hero |
| `hero_contacto.jpg` | Contacto hero |
| `hero_planta_2.jpg` | (available) |
| `nosotros_equipo.jpg` | Home about teaser |
| `nosotros_editorial.jpg` | (available) |
| `nosotros_cosecha.jpg` | (available) |
| `nosotros_planta.jpg` | (available) |
| `sostenibilidad_mano.jpg` | (available) |
| `delcampo_hero.jpg` | (available) |
| `division-delcampo.jpg` | Home featured band |
| `division-ingredientes.jpg` | Ingredientes card |
| `division-secos.jpg` | Secos card |
| `division-frescos.jpg` | Frescos card |
| `division-greenclover.jpg` | Greenclover card |
| `team_antonio.jpg` | Nosotros equipo |
| `team_alexia.jpg` | Nosotros equipo |
| `team_aranzazu.jpg` | Nosotros equipo |
| `team_juanjose.jpg` | Nosotros equipo |
| `card_secos.jpg` / `card_secos_alt.jpg` | Secos division card |

### Product photos — confirmed present
| Files | Division |
|-------|----------|
| `prod_quinoa_blanca.jpg`, `prod_quinua_roja.jpg`, `prod_quinua_tricolor.jpg`, `prod_quinua_negra.jpg` | Secos |
| `prod_chia.jpg`, `prod_kiwicha.jpg`, `prod_sesamo.jpg` | Secos |
| `prod_maiz_mote.jpg`, `prod_maiz_cusco.jpg`, `prod_pallar.jpg`, `prod_frijol_canario.jpg` | Secos |
| `prod_harina_quinua.jpg` | Secos |
| `prod_kion.jpg`, `prod_kion_deshidratado.jpg` | Frescos |
| `prod_curcuma.jpg`, `prod_curcuma_polvo.jpg` | Frescos |
| `prod_palta.jpg` | Frescos |
| `prod_cacao_grano.jpg`, `prod_cacao_polvo.jpg` | Frescos |
| `prod_azucar_rubia.jpg`, `prod_azucar_blanca.jpg`, `prod_almidon.jpg` | Ingredientes |
| `dc-arroz-*.jpg` (8 files), `dc-aceite-*.jpg` (4 files), `dc-girasol-*.jpg` (2 files), `dc-manteca.jpg`, `dc-azucar.jpg`, `dc-duraznos.jpg` | Del Campo |
| `delcampo_aceite.jpg`, `delcampo_arroz_rico.jpg`, `delcampo_manteca.jpg`, `delcampo_girasol.jpg` | Del Campo |
| `hoja_aceite.jpg`, `hoja_girasol.jpg`, `hoja_arroz.jpg`, `hoja_manteca.jpg` | Del Campo (background / decoration) |

### Certification logos — confirmed present
`cert-usda.jpg`, `cert-eubio.jpg`, `cert-brc.jpg`, `cert-smeta.jpg`, `cert-kosher.png`, `cert-kiwa.jpg`

### Still missing
- [ ] Kosher cert image (currently `cert-kosher.png` — check resolution)
- [ ] Client logos (for Clientes page — from client)
- [ ] Greenclover US address
- [ ] Del Campo copy (Líneas 04 and 05 content in HTML still uses Lorem Ipsum)
- [ ] Nosotros operaciones photos (Callao plant, Satipo plant — check if `nosotros_planta.jpg` covers this)

---

## User Flows (final)

### Flow 1 — Export buyer
Home → Divisiones ▾ → Secos or Frescos → product list (sidebar nav) → "Solicitar cotización" → Contacto

### Flow 2 — Local retail / consumer
Home → Del Campo featured band → WhatsApp CTA  
OR  
Home → "Del Campo" nav → Del Campo page → WhatsApp / "Dónde comprar"

### Flow 3 — B2B Ingredient buyer
Home → Divisiones ▾ → Ingredientes → products → "Solicitar cotización" → Contacto

### Flow 4 — US market
Home → Divisiones ▾ → Greenclover → Contact → Contacto

### Flow 5 — Certification check
Home → Sostenibilidad → cert cards → Contacto

### Flow 6 — New visitor / brand
Home → Nosotros → Historia + Equipo → Nuestras Divisiones CTA

---

## What's NOT in scope
- Blog (exists, leave as-is)
- Request a Quote / Quotes List (leave as draft)
- FAQ Page (client to decide)
- My Account / Cart / Checkout (WooCommerce — hidden via CSS)
