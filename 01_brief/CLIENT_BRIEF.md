# Client Brief — Interloom

**Last updated:** May 6, 2026  
**Status:** Active — first version due Friday May 9

---

## Client Info

- **Company:** Interloom (Grupo Interloom)
- **Website (current):** www.interloom.com.pe
- **Primary contact:** via Mazor (PM)
- **Email:** contacto@interloom.com.pe
- **Phone:** (511) 311 – 1730
- **Address:** Av. Jorge Basadre 310, Oficina 504, San Isidro, Lima – Perú
- **Social:** Facebook, Instagram

---

## Who They Are

Interloom is a Peruvian agrotrading group with **+30 years of experience** in local and international food commercialization. They operate across several business divisions:

- **DEL CAMPO** — Consumer brand, local market (rice, oils, lard)
- **División de Ingredientes** — B2B local (sugar, potato starch, glutamate, others)
- **División de Secos** — Export (quinoa & andean grains, own plant in Callao)
- **División de Frescos** — Export (ginger, turmeric, avocado, cacao, own plant in Satipo, Junín)
- **Greenclover Naturals LLC** — US subsidiary (local distribution + pallet sales with traceability)

**Key stats:** Top 10 exporter of Andean grains, top 5 in quinoa, 8,000+ tons exported in last 4 years. Certifications: USDA Organic, EU Bio, BRC Food, Kiwa, Kosher, SMETA.

---

## Project Scope (from RFQ)

This project is part of a larger 4-deliverable engagement. **Our scope is the website (Deliverable 3)** but context on the other deliverables matters:

1. **Corporate presentation** — 15–20 slides (PowerPoint/Google Slides). Sets the look & feel.
2. **Commercial brochure** — PDF for DEL CAMPO + Export divisions.
3. **🌐 Web corporativa (our deliverable)** — WordPress redesign, bilingual, by divisions.
4. **Logo refresh** — modernize typography/proportions; logo files + brand guide.

**Note:** Deliverables 1 and 4 are being done by Anita. The brand manual she delivered is the reference for our web work.

---

## Website Requirements

### Must-haves
- WordPress (recycling the existing installation at interloom.com.pe)
- **No-code / low-code only** (client wants to self-manage after delivery)
- **Bilingual: Spanish + English** (currently using TranslatePress plugin)
- **Responsive** (mobile-first)
- Contact forms → auto-send to contacto@interloom.com.pe
- **DEL CAMPO section**: WhatsApp Business direct contact button
- Structured by business divisions

### Site Architecture (from RFQ)
```
INTERLOOM
├── Home
├── Acerca de Nosotros
├── Nuestras Divisiones
│   ├── DEL CAMPO (Mercado Local – marca propia)
│   │   ├── Arroces importados
│   │   ├── Aceites
│   │   └── Manteca
│   ├── División de Ingredientes (Mercado Local – B2B)
│   │   ├── Azúcar, Almidón de papa, Glutamato, Otros
│   ├── División de Secos (Exportación)
│   │   ├── Quinua y granos andinos
│   │   └── Planta propia – Callao
│   ├── División de Frescos (Exportación)
│   │   ├── Jengibre y cúrcuma, Palta fresca, Cacao en grano
│   │   └── Planta propia – Satipo, Junín
│   └── Greenclover Naturals LLC (USA)
│       ├── Comercialización local en EE.UU.
│       └── Ventas por pallets con trazabilidad
├── Sostenibilidad y Certificaciones
├── Clientes
└── Contacto (formularios con envío automático)
```

Each section should include: product description, markets, logistics capabilities, certifications.

---

## Design Direction

- **Style:** Minimalist, clean, modern — "cool with a field identity"
- **Tone:** Professional but not cold. Formal + approachable.
- **Background:** ~80% white minimum (per brand manual)
- **Avoid:** Dark/strong background colors, cluttered images behind logo

### Brand Colors
| Name | Hex | Use |
|------|-----|-----|
| Near-black | `#1D1D1B` | Primary text |
| Bright green | `#009E3C` | Logo gradient, accents (use sparingly) |
| Yellow-green | `#C9CC3D` | Logo gradient (very sparingly) |
| Dark brown | `#4A3625` | Secondary text, details |
| Warm beige/tan | `#9F8A73` | Backgrounds, subtle accents |
| Forest green | `#2E7B37` | Secondary green accents |

### Typography
| Role | Font |
|------|------|
| Logo wordmark | Recoleta Regular |
| Headings/titles | Playfair Display |
| Body text | Lexend Light |

---

## Reference Sites (Client-approved)

| Site | What the client liked |
|------|-----------------------|
| [cono-group.com/es/sustentabilidad](https://www.cono-group.com/es/sustentabilidad) | Overall look. Would reduce text in paragraphs. |
| [ldc.com/product/animal-feed-pet-food/](https://www.ldc.com/product/animal-feed-pet-food/) | Product section layout specifically. |
| [globenatural.com](https://globenatural.com/) | Visual/style benchmark |
| [peruviannature.com](https://peruviannature.com/) | Visual/style benchmark |

Client note: *"Son estilos súper distintos, pero ambos han hecho un buen trabajo visual en sus webs."*

---

## Team

| Person | Role |
|--------|------|
| Mazor | PM (our contact) |
| Anita | Brand designer (logo + brand manual — done) |
| Cami | Web design lead (us) |

---

## Timeline

| Date | Milestone |
|------|-----------|
| May 6 | Setup & asset organization |
| May 7 | Site audit, design analysis, WP strategy |
| May 9 (Fri) | First version to show (internal) |
| TBD | Client review |

---

## Technical Notes

- Hosting: **SiteGround** ✅ confirmed (Security Optimizer + Speed Optimizer are SiteGround plugins; "Purge SG Cache" in admin bar)
- WordPress: 6.9.4
- Active theme: **Bridge** by Qode Interactive — keeping it. Bridge controls header/footer via Qode Options; Elementor Pro handles all page content
- Page builder: **Elementor Free 3.25.2 + Elementor Pro 3.25.4** — ⚠️ Pro license needs to be verified/activated
- E-commerce: **WooCommerce** active — product catalog is a WooCommerce shop
- Translation: **TranslatePress 2.6.4** (not WPML — earlier note was incorrect)
- Other active plugins: LayerSlider (no license), Slider Revolution, WPForms, Duplicator Pro, ACF, JetSmartFilters
- **Staging**: SiteGround → Site Tools → WordPress → Staging → Create Staging (Mazor can do this in 2 min)
- Backup: Duplicator Pro installed — last backup Feb 2025, run fresh before starting
- Current copyright footer: "INTERLOOM 2022" (outdated)
