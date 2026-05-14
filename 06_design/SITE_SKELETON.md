# Interloom — Site Skeleton (Locked)
> May 10, 2026 — reference for all mockup and build work

---

## Page Index & URLs

| Page | URL | WP Status | Template |
|------|-----|-----------|----------|
| Home | `/` | Front Page | Custom — Elementor |
| Nosotros | `/nosotros/` | Publish | Custom — Elementor |
| **DEL CAMPO** | `/divisiones/del-campo/` | Create | Division template |
| **Ingredientes** | `/divisiones/ingredientes/` | Create | Division template |
| **Secos** | `/divisiones/secos/` | Create (from Exportacion) | Division template |
| **Frescos** | `/divisiones/frescos/` | Create (from Exportacion) | Division template |
| **Greenclover Naturals** | `/divisiones/greenclover/` | Create | Division template |
| Sostenibilidad | `/sostenibilidad/` | Create | Custom — Elementor |
| Clientes | `/clientes/` | Create | Custom — Elementor |
| Contacto | `/contacto/` | Publish (restyle) | Custom — Elementor |
| *Plantas de Procesamiento* | *(content moves into Secos + Frescos)* | Redirect or retire | — |
| *Mercado Local* | *(content moves into DEL CAMPO + Ingredientes)* | Redirect or retire | — |
| *Exportacion* | *(content moves into Secos + Frescos)* | Redirect or retire | — |

---

## Navigation Structure

### Header (Bridge — Qode Options)
```
[LOGO]    Nosotros  |  Divisiones ▾  |  Sostenibilidad  |  Clientes  |  Contacto    ES | EN
```

**Divisiones dropdown (5 items):**
```
DEL CAMPO                    → /divisiones/del-campo/
División de Ingredientes     → /divisiones/ingredientes/
División de Secos            → /divisiones/secos/
División de Frescos          → /divisiones/frescos/
Greenclover Naturals LLC     → /divisiones/greenclover/
```

**Utility bar above nav:**
```
contacto@interloom.com.pe    [phone] (511) 311-1730  [Facebook] [Instagram]
```

### Footer (5 columns)
```
Col 1: Brand block (logo + tagline + social)
Col 2: Divisiones (5 division links)
Col 3: Empresa (Nosotros, Sostenibilidad, Clientes, Contacto)
Col 4: Contacto (address, phone, email, WhatsApp for DEL CAMPO)
Col 5: Certificaciones (6 logo marks, grayscale)
```

---

## User Flows

### Flow 1 — Export buyer (primary)
Home → `Divisiones ▾` → División de Secos or Frescos → Product list (sidebar nav by category) → `Solicitar cotización` → Contacto form

### Flow 2 — Local retail / consumer (DEL CAMPO)
Home → `Divisiones ▾` → DEL CAMPO → Products → **WhatsApp Business CTA**

### Flow 3 — B2B Ingredient buyer
Home → `Divisiones ▾` → División de Ingredientes → Products → `Solicitar cotización` → Contacto

### Flow 4 — US market inquiry
Home → `Divisiones ▾` → Greenclover Naturals → Contact block → Contacto

### Flow 5 — Certification / compliance check
Home → `Sostenibilidad` → Certificate details → Download or contact

### Flow 6 — Who are you? (new visitor)
Home → `Nosotros` → Story + Team → `Nuestras Divisiones` section → Division of interest

---

## Page-by-Page Content Outline

### Home `/`
1. **Utility bar** — email left, phone + social right
2. **Fixed header** — logo + nav
3. **Hero** — full-bleed photo (Version A locked), Playfair H1, Lexend sub-headline, green CTA
4. **Certifications strip** — 6 logos at 28% opacity on `#FAF8F5`, 80px height
5. **Nuestras Divisiones** — Playfair H2, 5-column image card grid, each card → division page
6. **Quiénes somos** — 2-column: text left (Playfair lead + Lexend body, "30 years" story), editorial photo right, CTA → /nosotros/
7. **Sostenibilidad teaser** — full-width `#FAF8F5` band, Playfair italic pull quote + link → /sostenibilidad/
8. **Contacto CTA** — centered, Playfair H2 "¿Trabajamos juntos?", form or link → /contacto/
9. **Footer**

### Nosotros `/nosotros/`
1. Header
2. **Hero** — full-bleed warehouse/field photo, H1 "Nosotros"
3. **Historia** — 2-column: Playfair lead paragraph + Lexend body (company story, 30 years)
4. **Números** — Bridge counter section: 30+ años · 8,000+ tons · 25+ mercados · 5 divisiones (animated count-up)
5. **Operaciones** — 2-up: Planta Callao + Planta Satipo (photo + Lexend caption + link → division pages)
6. **Sostenibilidad excerpt** — teaser, link → /sostenibilidad/
7. **Mercados** — world map illustration + destination countries
8. **Equipo Liderazgo** — 2-up cards: Antonio Cook Hardy (CEO), Alexia Cook Hardy (CEO) — photo required
9. **Equipo Exportaciones** — 2-up smaller: Aranzazu Muelle, Juan Jose Zevallos — photo required
10. Footer

### División pages (template — used 5×)
1. Header
2. **Breadcrumb** — Home > Divisiones > [Division Name]
3. **Hero** — 60vh full-bleed division photo, H1 overlay
4. **Intro band** — Playfair lead paragraph, 35-50 words
5. **Two-column body** — sticky sidebar (product categories + certifications) + scrolling product rows
6. **Closing band** — full-bleed photo + Playfair Italic pull quote
7. Footer

**Division-specific content:**

| Division | URL | Products | Plant | CTA | Special |
|----------|-----|----------|-------|-----|---------|
| DEL CAMPO | /del-campo/ | Arroces importados, Aceites, Manteca | — | WhatsApp Business | Consumer brand, local market |
| Ingredientes | /ingredientes/ | Azúcar, Almidón de papa, Glutamato, Otros | — | Solicitar cotización | B2B local |
| Secos | /secos/ | Quinua Blanca, Q. Roja, Q. Tricolor, Q. Negra, Chia, otros granos andinos | Callao | Solicitar cotización | Top 5 quinoa exporter |
| Frescos | /frescos/ | Jengibre orgánico, Cúrcuma fresca, Palta fresca, Cacao en grano, Jengibre deshidratado, Cúrcuma en polvo, Cacao en polvo | Satipo, Junín | Solicitar cotización | Own processing plant |
| Greenclover | /greenclover/ | US distribution, pallet sales with traceability | USA | Contacto / Quote | US subsidiary |

### Sostenibilidad `/sostenibilidad/`
1. Header
2. **Hero** — field/certification photo, H1 "Sostenibilidad y Certificaciones"
3. **Intro** — Playfair lead, sustainability as operating principle (not decoration)
4. **Certificaciones** — 6 cards, one per cert (USDA Organic, EU Bio, BRC Food, Kiwa, Kosher, SMETA): logo + name + what it means + which divisions hold it
5. **Prácticas** — 3-column: Trazabilidad · Plantas propias · Cadena de origen — Lexend body
6. **CTA** → Contacto

### Clientes `/clientes/`
1. Header
2. **Hero** — H1 "Clientes"
3. **Markets served** — world map, destination countries listed
4. **Client logos** — monochrome, single-tone wall (once client provides)
5. **Testimonial or case study** — optional, if available
6. **CTA** → Contacto

### Contacto `/contacto/`
1. Header
2. **H1** "Contacto" — white section
3. **2-column** — Left: 4 segmented contact cards (Comercial · Exportación · Prensa · Trabaja con nosotros), each with email. Right: WPForms restyled (floating labels, Enviar mensaje CTA)
4. **Map** — full-width Google Maps embed, custom dark style, green pin
5. **Offices strip** — Lima office + Greenclover US
6. Footer

---

## Bridge-specific features to use

| Feature | Where | Why |
|---------|-------|-----|
| Parallax background | Hero sections (Home, all division pages) | Adds depth to full-bleed photos |
| Scroll animations (fade up) | Division cards, certifications logos, team cards | Polished entrance without JS overhead |
| Counter section (animated) | Nosotros — 30 años / 8000 tons / 25 markets | High-impact, Bridge-native |
| Fixed header (type: Fixed) | Global | Utility bar + nav always visible |
| Header Top Area (utility bar) | Global | Email + phone always accessible |
| Parallax row | Closing band on division pages | Full-bleed photo with depth |
| Sticky sidebar | Division pages (Elementor Pro sticky widget) | LDC-style product navigation |
| Footer widget areas | Global | 5-column footer via Bridge footer builder |
| TranslatePress language switcher widget | Header top right area | ES/EN toggle |

---

## What's NOT in scope (this project)
- Blog (exists as a page, leave as-is)
- Request a Quote / Quotes List (leave as draft)
- FAQ Page (leave as-is, client to decide)
- My Account / Cart / Checkout (WooCommerce — hidden via CSS, leave as-is)
