# Bridge Theme — Capabilities Reference
> Researched May 10, 2026 from bridge.qodeinteractive.com/documentation
> Purpose: validate DESIGN_DIRECTION.md against what Bridge can actually build

---

## Header Types (8 available)

| Type | Behavior | Notes |
|------|----------|-------|
| **Regular** | Scrolls out of view | Not suitable — no sticky |
| **Fixed** | Always visible, pinned to top | ✅ Simplest for our design |
| **Fixed Minimal** | Fixed, centered logo, fullscreen menu icon | Too minimal |
| **Fixed Advanced** | Fixed; logo visible on scroll, menu hidden until hover | Complex UX |
| **Fixed Header Top** | Only top utility bar is fixed | Not what we need |
| **Sticky** | Disappears on scroll down, reappears on scroll up | ✅ More modern feel |
| **Sticky Expanded** | Logo above menu initially, horizontal when sticky | Option |
| **Sticky Divided** | Logo centered, menus left and right | Interesting but complex |

**Recommendation for Interloom:** Use **Fixed** — utility bar + main nav always visible, never disappears. Simplest to configure, easiest for client to manage, no scroll surprise behavior. If more modern feel is wanted, use **Sticky**.

---

## Header Top Area (Utility Bar)

✅ **Built-in natively.** Enable at: Qode Options → Header → Header Top → Show Header Top Area.

- Two widget areas: **Header Top Left** and **Header Top Right**
- Add any widget — text widget for email/phone, social icons widget, language switcher
- Styling: background color, text color, height all configurable
- ⚠️ **Disabled on mobile/tablet portrait** by default — needs custom CSS if you want it visible on mobile

**For Interloom:** Put `contacto@interloom.com.pe` in left widget area, `(511) 311-1730` + social icons in right widget area. Background `#FAF8F5`, text `#1D1D1B` Lexend Light 12px (via custom CSS since widget areas use the theme default).

---

## Mega Menu

❌ **NOT built-in natively.** Bridge only supports standard WordPress menus up to 3 levels deep. No multi-column dropdowns, no widget content inside dropdowns, no icon support in nav items.

**Options:**
1. **Simplify to standard dropdown** — 5 stacked items under "Divisiones ▾" — cleanest, no plugin needed, client can manage
2. **Max Mega Menu plugin** (free) — adds multi-column dropdown capability, works with Bridge, requires extra plugin to manage
3. **Custom CSS** — fake a mega menu with CSS on the standard dropdown — not maintainable by client

**Decision for Interloom:** Use **option 1 — simplified standard dropdown**. The 5-column icon mega menu from DESIGN_DIRECTION.md is NOT buildable without a plugin. Standard dropdown is cleaner, faster, and easier for the client to manage long-term.

### Revised Divisiones dropdown
- White background panel, 1px `#EDEAE3` border at bottom of each item
- 5 items stacked vertically: **DEL CAMPO · División de Ingredientes · División de Secos · División de Frescos · Greenclover Naturals**
- Lexend Light 14px `#1D1D1B`, 16px vertical padding per item
- Hover: text shifts to `#2E7B37`
- Active page: text `#2E7B37`, optional left border in `#2E7B37`
- Panel width: 280px, left-aligned below the "Divisiones" nav item

This is actually cleaner than a 5-column mega menu — faster to load, no JS complexity, easier to read.

---

## Typography Control

✅ Available at: Qode Options → Fonts → Header & Menu

- Separate font settings for: 1st level nav, 2nd level nav, 3rd level nav
- Control: font family, size, weight, letter-spacing, color
- Set these to Lexend Light 14px `#1D1D1B` letter-spacing 0.02em for nav items
- ⚠️ Bridge typography settings can conflict with Elementor Global Fonts on page content — set Bridge fonts for header/menu only, let Elementor Global Fonts handle page content

---

## Logo

✅ Supports 7 logo image variants: Normal, Light skin, Dark skin, Sticky, Fixed Advanced, Mobile, Side Menu Area Bottom. Set horizontal logo PNG at 40px height for the header. Bridge auto-handles retina (2x).

---

## Footer

✅ Fully configurable via Qode Options → Footer. Supports widget areas, multi-column layouts, custom background color. Build the 5-column footer layout here using WordPress widgets for each column.

---

## What This Means for the Build

| Feature | Bridge can do it? | How |
|---------|------------------|-----|
| Fixed/sticky header | ✅ | Qode Options → Header Type |
| Utility bar above nav | ✅ | Header Top Area widget zones |
| Sticky white header with border | ✅ | Fixed type + color settings |
| New logo (gradient clover + Recoleta) | ✅ | Upload to Qode Options → Logo |
| 5-column Divisiones mega menu | ❌ | Replace with standard dropdown |
| Standard Divisiones dropdown (5 items) | ✅ | WordPress Menus + Bridge styling |
| Language toggle ES/EN | ✅ | TranslatePress widget in header top right |
| Nav typography (Lexend Light) | ✅ | Qode Options → Fonts → Header |
| Multi-column footer | ✅ | Qode Options → Footer + widgets |
| Mobile hamburger menu | ✅ | Bridge handles automatically |
| Page content (Elementor) | ✅ | All page content via Elementor Pro |
| WooCommerce templates | ✅ | Elementor Theme Builder (already set up) |
