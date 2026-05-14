# Interloom — Design Direction (Locked)

**Decided:** May 6, 2026 · **For build session:** May 7, 2026
**Lens:** White-dominant (80%+), minimalist, "cool con identidad de campo" — professional but warm. Not generic corporate. Not rustic agricultural.

> **Theme: Bridge (Qode Interactive) — keeping it.** Header and footer are configured through Bridge's header builder + Qode Options. Elementor Pro handles all page content. All design decisions in this document are valid regardless of theme choice.

> This document is decisions, not options. Every section below tells you exactly what to build.

---

## Reference Sites — What We're Actually Borrowing

The four references resolve cleanly when filtered through Interloom's brand. Here's how each one contributes — and what we explicitly discard.

**Cono Group (cono-group.com/es/sustentabilidad)** — borrow the structural confidence: simple top-aligned nav with logo left, links right, language toggle far right, underline on the active nav item. Borrow the breadcrumb pattern (`Home > Sustentabilidad`) for all interior pages. Borrow the full-bleed editorial photo header followed by a single H1 + short intro. **Discard** the long-paragraph treatment — the client called this out and we're cutting body copy into shorter passages with visual breaks.

**LDC (ldc.com/product/animal-feed-pet-food/)** — borrow the product page layout almost verbatim: persistent left sidebar with category list (active item gets a light gray fill), right column intro paragraph in serif, then product rows that pair a square white-bg product photo (~280px) with serif name + 2-3 line description and a hairline divider between rows. **Discard** the global-corporate-enterprise temperature — Interloom needs a warmer face than LDC. Use brand photography (real Peruvian crops, real plants in Callao/Satipo) rather than studio-on-white.

**Globe Natural (globenatural.com)** — borrow the warm-but-clean tone and the simple top-nav structure (Inicio · Nosotros · Servicios · Productos · Sostenibilidad · Contacto) — that pattern maps almost 1:1 to Interloom's information architecture. **Discard** the cream-band header and the centered-logo-with-hand-drawn-flourishes treatment. That reads boutique/feminine; Interloom is corporate-warm. Also discard the slow hero animation — keep things lean.

**Peruvian Nature (peruviannature.com)** — borrow the editorial confidence and oversized headline behavior on Nosotros and division pages — large type that owns the section. Borrow the sticky dark header pattern (we'll execute it lighter — see below). **Discard** the full-viewport color blocks (orange, lime, navy backgrounds) and the condensed display sans-serif. That language is the opposite of Interloom's white-dominant brand rule. We use scale and serif weight for confidence, not color blocking.

**The composite:** Cono's frame + LDC's product page + Globe's category structure + Peruvian Nature's typographic confidence — all in white space with serif headlines and forest-green accents.

---

## Header / Navigation — Locked

**Bridge header style:** Header Type 1 (standard horizontal). Not transparent. Not centered. Sticky on scroll with a slight white background blur and a 1px hairline border at the bottom (`#EDEAE3` — a 10% tint of the warm tan).

**Layout (desktop, left to right):**
- Horizontal Interloom logo (`logo_horizontal_transparent.png`), 40px tall, anchored ~32px from left
- Primary nav, right-aligned, ~32px from right edge: **Nosotros · Divisiones ▾ · Sostenibilidad · Clientes · Contacto**
- After the nav, a thin vertical divider (`#E6E2DA`, 1px, 16px tall), then language toggle **ES | EN** (active = `#1D1D1B`, inactive = `#9F8A73`)

**Top utility bar** (above the main header, full width, 32px tall, `#FAF8F5` background with `#1D1D1B` 12px Lexend Light text): keep the existing pattern — `contacto@interloom.com.pe` left, `(511) 311-1730` and Facebook + Instagram icons right. This bar disappears on scroll; only the main header remains sticky.

**Divisiones dropdown:** standard dropdown panel (Bridge does not support mega menus natively — no plugin needed). White background, 280px wide, left-aligned below "Divisiones". 5 items stacked: **DEL CAMPO · División de Ingredientes · División de Secos · División de Frescos · Greenclover Naturals**. Lexend Light 14px `#1D1D1B`, 16px vertical padding per item, 1px `#EDEAE3` divider between items. Hover: text shifts to `#2E7B37`. Active page: `#2E7B37` text + 3px left border. Clean, fast, no JS complexity.

**Mobile:** logo left, hamburger right. Drawer slides from the right, full-height white, links stacked in Playfair Display 22px with 24px vertical rhythm. Language toggle pinned at the bottom of the drawer.

**Nav typography:** Lexend Light, 14px, `#1D1D1B`, letter-spacing 0.02em, all caps optional only on the utility bar — primary nav stays sentence-case. Active page gets a 2px underline in `#2E7B37`, 4px below the baseline.

---

## Hero Section — Home Page — TWO VERSIONS FOR CLIENT REVIEW

> **Decision pending:** Build two mockups for Monday — Version A (full-bleed photo with overlay, Cono Group pattern) and Version B (white background editorial split, text left / photo right). Client picks one. Everything else in the design is identical between versions.

### Version A — Full-bleed photo with overlay

**Pattern:** full-bleed editorial photograph + headline overlay (Cono Group's structure, not Peruvian Nature's color block). Single fixed image, no slider, no LayerSlider — that plugin gets removed.

**Dimensions:** 100vw × 78vh on desktop (min 600px, max 720px), 70vh on tablet, 60vh on mobile.

**Image:** one of the warm editorial food/field shots from the existing asset library — first preference is a wide horizontal of crops in field (quinoa, ginger, cacao) shot in soft late-light. Avoid the wooden-spoons-with-grains hero from the current site (too still-life, too Pinterest). If we don't have a strong field shot, use a clean portrait of an open hand holding raw grain. Image gets a 30% black-to-transparent gradient on the left third (mask, not solid overlay) so the headline reads cleanly without darkening the whole photo. Logo readability is preserved per brand manual — image must not be busy behind the headline area.

**Headline copy:** "Agro peruano con trazabilidad real." (placeholder — copywriter to refine; structure stays). Playfair Display Regular, 64px desktop / 44px tablet / 32px mobile, line-height 1.1, color `#FFFFFF`. Anchored bottom-left, 80px from left edge, 96px from bottom.

**Sub-headline** below the H1: "+30 años exportando granos andinos, frescos e ingredientes a más de 25 países." Lexend Light, 18px, `#FFFFFF`, max-width 520px, line-height 1.5.

**Single CTA button** below sub-headline, 32px gap: "Conoce nuestras divisiones" — solid `#2E7B37` background, `#FFFFFF` text in Lexend Regular 14px, 14px × 28px padding, 2px corner radius, no shadow. Hover: background darkens to `#256328`. This is one of only two places forest green appears as a fill on the home page.

**No carousel, no slider dots, no scroll indicator.** Single confident image. Cono Group's logic.

### Version B — Editorial split (white background)
**Pattern:** White section, no photo overlay. Headline left, photo right. Safer from a brand-rules standpoint (logo and text never float on a photo).

**Layout:** 2-column, 60/40 split. Left: Playfair Display H1 + Lexend Light sub-headline + forest-green CTA button, anchored vertically center. Right: one high-quality editorial photo (4:5 portrait crop) with ~40px white margin so it floats, not bleeds. Section height ~85vh desktop.

**Background:** pure white `#FFFFFF`. Top of the left column gets a small eyebrow in `#9F8A73` Lexend Light uppercase: "GRUPO INTERLOOM · LIMA, PERÚ".

**Headline:** same copy as Version A — "Agro peruano con trazabilidad real." Same size, same color, but on white not on photo.

**Why Version B matters:** it's 100% aligned with Anita's logo-on-light-backgrounds rule with zero workarounds, and it scales better to mobile (stack: text above, photo below). Tradeoff is it's less visually dramatic than the full-bleed.

---

## Division Cards — Home Page — Locked

**Section anchor:** below the hero and a thin certifications strip (USDA Organic, EU Bio, BRC Food, SMETA, Kosher, Kiwa — logos at 28% opacity, 48px tall, evenly spaced on `#FAF8F5`, 80px section height). The certifications strip is the visual handshake before the divisions.

**Pattern:** **image cards, not typographic tiles.** Five cards, one per division. Decision rationale: typographic-only tiles would feel cold for a brand that lives in real fields and plants; image cards establish "field identity" without slipping into rustic. Globe Natural's warm-image approach wins here over Peruvian Nature's bare typography blocks.

**Layout:**
- Section heading: "Nuestras Divisiones" — Playfair Display Regular, 40px, `#1D1D1B`, centered, 96px top padding
- Section subheading: one line in Lexend Light 16px `#4A3625`, centered, max-width 560px
- 64px gap, then a 5-column grid on desktop (each card ~280px wide), 2 columns on tablet, 1 column on mobile. Cards do **not** wrap onto a 2/3 split — five even columns, even if cramped — because parity of divisions matters editorially.

**Card anatomy:**
- Top: 4:5 portrait photo, full-bleed inside the card (no padding around the image). Real-context photography only — DEL CAMPO = a hand placing a bag of rice in a kitchen; Ingredientes = bulk sugar texture; Secos = quinoa close-up; Frescos = ginger root in Satipo; Greenclover = a US warehouse pallet shot. No stock images.
- Below image: 24px white padding zone
- Division name in Playfair Display Regular, 22px, `#1D1D1B` (e.g., "DEL CAMPO," "División de Secos") — note: title-case for "División de…" entries; "DEL CAMPO" stays uppercase per existing brand convention
- One-line descriptor in Lexend Light 13px `#4A3625`, max 12 words ("Granos andinos certificados, exportación global.")
- Small `→` arrow in `#2E7B37`, Lexend Light 14px, 12px below descriptor, indicating click-through

**Card behavior:** entire card is the link target. Hover state — image scales 1.03 over 400ms ease-out, descriptor stays still, arrow shifts 4px to the right. No drop shadows, no border, no background fill. Cards float on white.

---

## Division / Product Page Layout — Locked

**Pattern:** LDC's left-sidebar + right-content scaffold, refined for Interloom. This template serves all five divisions identically — variation comes from content, not layout.

**Page structure (top to bottom):**

1. **Breadcrumb bar** — `Home > Divisiones > [Division Name]` — full-width, `#FAFAFA` background, 48px tall, Lexend Light 13px. Active crumb in `#2E7B37`, others in `#9F8A73` with `>` separators in `#9F8A73` at 60% opacity. (Cono Group pattern.)

2. **Page hero** — 60vh full-bleed photo of the division's actual operation (the Callao plant for Secos, Satipo facility for Frescos, etc.). H1 overlay anchored bottom-left, same 80px / 96px insets as the home hero, but 48px Playfair Display instead of 64px. No sub-headline at this level — the photo and H1 carry it.

3. **Intro band** — 100% width, white background, 96px top + 64px bottom padding. Single Playfair Display Regular paragraph, 24px, `#1D1D1B`, line-height 1.5, max-width 720px, left-aligned not centered. This is the "what this division does" paragraph — 35-50 words max. (LDC's intro paragraph treatment.)

4. **Two-column body** — sticky left sidebar + scrolling right content. Sidebar is 280px wide, content area max 880px, 96px gap between. Outer page padding 80px desktop / 32px mobile.

   **Sidebar (sticky, top offset 120px to clear the header):**
   - Heading "Productos" in Playfair Display Regular 16px, `#9F8A73`, letter-spacing 0.06em, uppercase, 16px bottom margin
   - Vertical list of product categories — Lexend Light 15px `#1D1D1B`, 14px vertical rhythm, 12px left padding, 4px left border in `#FFFFFF` (transparent)
   - Active category: 4px left border `#2E7B37`, background `#FAF8F5` (subtle warm tan tint at 10%), text weight stays Light
   - Hover: text shifts to `#2E7B37`
   - Below the product list, a 32px gap, then a small block titled "Certificaciones de esta división" with 4 small black logo marks at 32px tall — this anchors trust on every division page

   **Content area (scrolling right column):**
   - Section heading "Productos" — Playfair Display Regular 32px `#1D1D1B`, 64px bottom margin
   - Product rows — vertically stacked, each row is a 12-column grid: 4 columns image, 8 columns text, 48px column gap
     - Image cell: 280px square, white background (`#FFFFFF`), 1px border in `#EDEAE3`, product photo centered with ~32px internal padding so the product floats — same logic as LDC
     - Text cell: product name in Playfair Display Regular 26px `#1D1D1B`, 12px gap, 2-3 line description in Lexend Light 15px `#4A3625` at line-height 1.6, max 60 words
     - Below description: a metadata strip — "Origen: Callao, Perú · Presentación: 25kg · Certificación: USDA Organic" — Lexend Light 12px `#9F8A73`, 24px top margin
   - 1px hairline divider between rows in `#EDEAE3`, 56px vertical padding around each divider
   - At the end of the product list: a single CTA — "Solicitar cotización" — same forest-green button as the home hero. For DEL CAMPO division specifically, replace this with a WhatsApp button (`#25D366` background — the only non-brand color allowed, justified by platform recognition) that links to the WhatsApp Business number.

5. **Closing band** — full-bleed photo (50vh) of the plant, team, or field, with one Playfair Display Italic 28px pull quote overlaid (e.g., "Toda la cadena, una sola firma."). Bottom of the page before the footer.

**No tabs, no accordion product navigation.** Sidebar is the navigation. Reasoning: with 5 divisions × 4-12 products each, the catalog scales better as scrolling rows than as nested tabs, and the LDC pattern is the one the client liked.

---

## Typography Treatment — Locked

**Type system (set as Elementor Global Fonts on day one):**

| Token | Font | Weight | Size (desktop) | Size (mobile) | Line-height | Color | Usage |
|---|---|---|---|---|---|---|---|
| H1 — hero | Playfair Display | Regular 400 | 64px | 32px | 1.1 | `#FFFFFF` over photo / `#1D1D1B` on white | Home hero, top of major pages |
| H1 — page | Playfair Display | Regular 400 | 48px | 28px | 1.15 | `#1D1D1B` | Interior page titles when no hero photo |
| H2 — section | Playfair Display | Regular 400 | 40px | 26px | 1.2 | `#1D1D1B` | "Nuestras Divisiones," "Productos," etc. |
| H3 — card / product | Playfair Display | Regular 400 | 26px | 22px | 1.3 | `#1D1D1B` | Division cards, product rows |
| H4 — small heading | Playfair Display | Regular 400 | 18px | 18px | 1.4 | `#1D1D1B` | Footer columns, sidebar items |
| Eyebrow / kicker | Playfair Display | Regular 400 | 16px | 14px | 1.4 | `#9F8A73` (uppercase, letter-spacing 0.06em) | "Productos," "Sostenibilidad" labels |
| Lead paragraph | Playfair Display | Regular 400 | 24px | 18px | 1.5 | `#1D1D1B` | Intro paragraphs at top of sections |
| Body | Lexend Light 300 | — | 16px | 15px | 1.6 | `#1D1D1B` | All body copy |
| Body — secondary | Lexend Light 300 | — | 15px | 14px | 1.6 | `#4A3625` | Descriptions, captions, inside cards |
| Meta / caption | Lexend Light 300 | — | 12px | 12px | 1.5 | `#9F8A73` | Origen / certification meta strips |
| Nav | Lexend Light 300 | — | 14px | 16px | 1.4 | `#1D1D1B` | Header nav, sidebar nav |
| Button | Lexend Regular 400 | — | 14px | 14px | 1 | `#FFFFFF` | CTAs |

**Hierarchy rules:**
- Headings always Playfair Display Regular. **No bold, no italic, no semibold** in headings except the closing-band pull quote, which is Playfair Display Italic 28px.
- Body always Lexend Light 300. The only other Lexend weight allowed is Regular 400, used exclusively for buttons.
- Letter-spacing: default 0 for headings; 0.06em uppercase eyebrows; 0.02em on nav.
- Line-length cap: 720px for body, 540px for lead paragraphs. Never let body run wider on desktop.
- Headings break naturally — no manual `<br>` line breaks except in the home hero where the single line is intentional.
- All-caps reserved for the eyebrow/kicker style and the "DEL CAMPO" division name. Everything else is sentence case. The current site's all-caps section labels are abandoned.
- No drop caps. No text shadows. No outlines.

---

## Color Application — Locked

The brand has six colors. They each have one job. No improvising.

**`#FFFFFF` — pure white. The page.** 80%+ of every layout. Backgrounds of every section by default. Card backgrounds. Sidebar backgrounds (technically `#FAF8F5` for subtle separation, see below).

**`#1D1D1B` — near-black. Text and the logo wordmark.** This is where 95% of typography lives. All H1-H4. All body text. Logo wordmark. Header nav links. No gray text — `#1D1D1B` is the one true text color.

**`#4A3625` — dark brown. Secondary text only.** Product descriptions inside cards and division-page rows. Card descriptors. Anywhere copy needs to recede slightly behind a primary heading. Never used for headings, never used as a fill, never used as a border.

**`#9F8A73` — warm tan. The connective tissue.** This is the brand's warmth. Used for: eyebrow labels above sections, meta/caption text (Origen, Presentación), `>` breadcrumb separators, the hairline border at the bottom of the sticky header (`#EDEAE3`, a 10% tint), the sidebar active-state background tint (`#FAF8F5`, an 8% tint), and the utility-bar background (`#FAF8F5`). **Never used as a body-text color.** Never used as a section background fill at full strength — only as the 8-10% tints noted above. This is what gives Interloom warmth without going beige-heavy like Globe Natural.

**`#2E7B37` — forest green. The action color.** This is the only fill green on the web. Used for: the primary CTA button background, hover state on sidebar nav, the active-page underline in the header, the small `→` arrow on division cards, link color in body copy (only on links, not on every brown number/date). Never used as a section background, never used in headings, never as a large block. Appears on the home page in exactly two places: the hero CTA and the active-state underline. On division pages: the sidebar active state, the CTA at the end of the product list, and inline link color. **The forest green is a punctuation mark, not a paragraph.**

**`#009E3C` and `#C9CC3D` — bright green and yellow-green.** These two colors live in the logo gradient and **nowhere else on the website.** No buttons, no underlines, no fills, no icons. They exist inside the logo SVG and are not part of the web palette beyond that. This is per the brand manual rule about using bright green "in smallest proportion" — we go further and reserve it entirely to the mark itself, because once it's loose on the page it will fight `#2E7B37`.

**Backgrounds and tints (the only secondary surfaces):**
- `#FAF8F5` — utility bar background, sidebar active-state, certifications band background. Reads as "white with warmth."
- `#EDEAE3` — hairline borders (header bottom, product-row dividers, sidebar borders). Reads as "subtle separation."
- These are the only two non-pure-white surfaces allowed. No gray. No beige. No paper textures.

**Forbidden combinations:**
- Forest green text on warm tan background (low contrast, muddy).
- White text on warm tan background (fails AA).
- Logo on dark green or saturated green fields (per brand manual).
- Any gradient in UI surfaces (the logo gradient is the only gradient on the site).

---

## Footer Structure — Locked

Five-column grid on desktop, three rows. Generous — 96px top padding, 48px bottom, 80px outer side padding. Background `#FAF8F5` (warm white tint), top border 1px `#EDEAE3`. No dark footer. The brand rule about logo-on-light backgrounds means the footer can't go dark.

**Row 1 — main columns (desktop: 5 columns; tablet: 2; mobile: stacked):**

| Column 1 (1.5 width) | Column 2 | Column 3 | Column 4 | Column 5 |
|---|---|---|---|---|
| **Brand block** | **Divisiones** | **Empresa** | **Contacto** | **Certificaciones** |
| Horizontal logo, 48px tall | DEL CAMPO | Nosotros | Av. Jorge Basadre 310, Of. 504 | 6 cert logos in 2×3 grid (USDA Organic, EU Bio, BRC Food, Kiwa, Kosher, SMETA), 40px tall each, grayscale at 60% opacity |
| One-line descriptor: "+30 años de agro peruano con trazabilidad real." in Lexend Light 14px `#4A3625` | Ingredientes | Sostenibilidad | San Isidro, Lima – Perú | |
| Facebook + Instagram + LinkedIn icons (24px, `#1D1D1B`, 16px gap, hover `#2E7B37`) | Secos | Clientes | (511) 311-1730 | |
| | Frescos | Contacto | contacto@interloom.com.pe | |
| | Greenclover | | WhatsApp Business (DEL CAMPO) | |

Column headings use the eyebrow style (Playfair Display 16px `#9F8A73` uppercase letter-spacing 0.06em). Column links use Lexend Light 14px `#1D1D1B` with 12px vertical rhythm, hover `#2E7B37`.

**Row 2 — divider:** 1px hairline `#EDEAE3`, 48px above and below.

**Row 3 — legal strip:** Single horizontal line, Lexend Light 12px `#9F8A73`. Left side: `© 2026 Grupo Interloom. Todos los derechos reservados.` Right side: `Aviso legal · Política de privacidad · Cookies`. Mobile stacks them.

**No footer hero, no newsletter signup, no "back to top" floating button, no language toggle in the footer (it's in the header).** The footer is dense with information but quiet visually — five columns of links and one warm logo block. This is intentional contrast with the editorial body of the site.

**Mobile footer:** columns collapse to single-column accordions, except the brand block which stays open at the top and the legal strip which stays inline at the bottom. Tap to expand each section.

---

## Build Order — What to Touch First on Staging

1. **Verify staging is up** (Mazor) and run a fresh Duplicator Pro backup.
2. **Configure Bridge header** in Qode Options — Header Type 1, sticky, white background, import the new horizontal logo. Set up the utility bar (email + phone, off-white background).
3. **Set Elementor Global Colors** — six tokens: `#1D1D1B`, `#4A3625`, `#9F8A73`, `#2E7B37`, `#FAF8F5`, `#EDEAE3`. Plus pure white. Name them clearly: text-primary, text-secondary, accent-warm, accent-green, surface-warm, hairline.
4. **Set Elementor Global Fonts** — the type tokens above. Load Playfair Display (regular, italic) and Lexend (light, regular) from Google Fonts. Recoleta is logo-only, never as a global font.
5. **Build the global header in Elementor Theme Builder** using the layout above — utility bar, sticky main header, mobile drawer.
6. **Build the global footer** using the layout above.
7. **Build the home page** in this order: hero → certifications strip → divisions section → about teaser → contact CTA → footer (already global).
8. **Build the division template once** (using Elementor's Theme Builder for a custom WooCommerce category template) and apply it to all five divisions.
9. **Build Nosotros, Sostenibilidad, Clientes, Contacto** using the same type and color system.

---

## What This Direction Explicitly Rules Out

So tomorrow's build doesn't drift:

- No sliders. No LayerSlider, no Slider Revolution, no Elementor carousel on the hero.
- No dark sections. The site is white-dominant; dark color blocks belong to Peruvian Nature, not Interloom.
- No drop shadows on cards. Float on white. Hairlines and tints only.
- No icon library beyond a small custom set of 5 division icons in `#2E7B37` line style. No Font Awesome dump.
- No emojis in copy. No quotes in heavy stylized speech-bubble graphics.
- No hand-drawn flourishes (Globe Natural's underlines). The serif type carries the personality.
- No all-caps section labels (current site pattern). Eyebrows yes, all-caps body no.
- No "We are passionate about quality" hero copy. The headline must reference what Interloom actually does — agro peruano, trazabilidad, 30 años, divisions.
- No Recoleta in body or UI text — it's licensed for the logo only.

---

## One-line Summary

**A white-dominant, serif-led editorial site with a sticky thin header, two hero options (full-bleed photo vs editorial split — to be validated with client), five image-led division cards on the home, an LDC-style sidebar product page that scales across all five divisions, forest green used only as punctuation, warm tan used only as connective tissue, and a quiet five-column footer that stays on a warm-white surface — built in Elementor Pro on Bridge.**

That's the brief. Build from it.
