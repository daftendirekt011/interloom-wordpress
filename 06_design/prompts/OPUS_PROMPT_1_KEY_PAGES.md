# Opus Prompt 1 — Key Template Pages
> Copiá todo lo que está debajo de la línea horizontal en una conversación nueva de Claude Opus (Cowork mode).
> Tenés acceso a la carpeta del workspace de interloom. Leé los archivos listados antes de empezar.

---

Sos un diseñador web senior y desarrollador front-end trabajando en el rediseño del sitio de **Grupo Interloom**, una empresa peruana de agrotrading.

## PASO 1 — Leer estos archivos primero (en este orden)

Usá el Read tool en cada uno antes de hacer cualquier otra cosa:

1. `C:\Users\DCPor\OneDrive\Documentos\interloom\SESSION_MAY7.md` — contexto de sesión, decisiones tomadas, el stack técnico
2. `C:\Users\DCPor\OneDrive\Documentos\interloom\05_inspiration\DESIGN_DIRECTION.md` — todas las decisiones de diseño bloqueadas: colores, tipografía, layouts, lo prohibido
3. `C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\BRAND_SUMMARY.md` — reglas del logo, paleta, principios de marca de Anita
4. `C:\Users\DCPor\OneDrive\Documentos\interloom\01_brief\CLIENT_BRIEF.md` — info de la empresa, divisiones, productos, equipo, datos de contacto
5. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\SITE_SKELETON.md` — índice completo de páginas, URLs, user flows, contenido por sección
6. `C:\Users\DCPor\OneDrive\Documentos\interloom\07_wordpress\BRIDGE_CAPABILITIES.md` — qué puede y no puede hacer Bridge (crítico — leer antes de diseñar)

No saltees ningún archivo. No empecés a construir hasta leer los seis.

---

## PASO 2 — Estado actual de los mockups (leer antes de construir)

Ya existen dos archivos en `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\`:

- **`home-version-a.html`** — ya existe, fue aprobada por el cliente y el PM. **NO la reescribas desde cero.** Leela, entendé su estructura CSS, tokens y componentes, y mejorala si hace falta (consistencia, secciones faltantes). Usá su sistema de diseño como base para todos los demás archivos.
- **`division-secos.html`** — ya existe como primer borrador. Revisala, mejorala con el contenido completo del SITE_SKELETON.md y asegurate que sea consistente con home-version-a.html.

Leé ambos archivos antes de escribir cualquier código nuevo.

---

## PASO 3 — Lo que estás construyendo

Cuatro archivos HTML pulidos, pixel-accurate, completamente self-contained. Se van a mostrar al cliente mañana y después se usan como referencia exacta para construir en WordPress (Bridge theme + Elementor Pro).

**Stack (de los archivos arriba):**
- Bridge controla: header y footer (via Qode Options)
- Elementor Pro controla: todo el contenido de las páginas — todas las secciones del medio
- El grid de 5 columnas de divisiones en home es contenido Elementor → completamente válido, sin problema
- El mega menu fue reemplazado por un dropdown estándar de 5 ítems → ya documentado en BRIDGE_CAPABILITIES.md
- Sin sliders, sin LayerSlider, sin secciones oscuras, sin texto en all-caps

**Archivos a guardar en `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\`:**

1. `home-version-a.html` — Home page, Version A (hero full-bleed — BLOQUEADA por el cliente) — mejorar la existente
2. `division-secos.html` — División de Secos (template de página de división) — mejorar la existente
3. `nosotros.html` — Página Nosotros / About — crear nueva
4. `contacto.html` — Página Contacto — crear nueva

---

## PASO 4 — Logo real (usar este, no inventar SVG)

El logo real del cliente ya está en el workspace:
- **Header/footer:** `C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\logos\logo_horizontal_transparent.png`
- **Ícono solo:** `C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\logos\logo_isologo_transparent.png`

Para incrustarlo en HTML sin depender de rutas relativas: convertí el PNG a base64 con Python y usalo como `<img src="data:image/png;base64,...">`. Esto hace el archivo completamente self-contained.

Comando Python para convertir:
```python
import base64
with open(r"C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\logos\logo_horizontal_transparent.png", "rb") as f:
    print(base64.b64encode(f.read()).decode())
```

---

## PASO 5 — Fotos reales (YA PROCESADAS — usar estas)

Las fotos están en `C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\web_ready\`.

Usá rutas relativas desde la carpeta `06_design/mockups/`. El path relativo correcto para todas las fotos es:

```
../../03_assets/images/web_ready/nombre_foto.jpg
```

Ejemplo: `<img src="../../03_assets/images/web_ready/hero_planta.jpg">`

Para los heroes que van como `background-image` en CSS:
```css
background-image: url('../../03_assets/images/web_ready/hero_planta.jpg');
background-size: cover;
background-position: center;
```

**No uses base64** — haría los HTML demasiado pesados.

**Mapa de fotos → secciones:**

| Sección | Archivo | Notas |
|---|---|---|
| **Hero HOME** | `hero_planta.jpg` | Foto planta profesional, horizontal 1920px |
| **Hero HOME alternativa** | `hero_kion_aerial.jpg` | Drone aéreo, impactante |
| **Hero DIVISIÓN DE SECOS** | `hero_planta_2.jpg` | Planta agrícola, vista diferente |
| **Hero NOSOTROS** | `hero_kion_field.jpg` | Campo kion/jengibre desde terreno |
| **Hero CONTACTO** | `nosotros_planta.jpg` | Editorial planta, más íntimo |
| **Sección About home (foto editorial)** | `nosotros_equipo.jpg` | Operaciones planta |
| **Closing band SECOS** | `hero_kion_work.jpg` | Operarios trabajando, cálido |
| **Prod: Quinua Blanca** | `prod_quinoa_blanca.jpg` | Sobre blanco, 600px |
| **Prod: Kion/Jengibre** | `prod_kion.jpg` | Sobre blanco, 600px |
| **Prod: Cúrcuma** | `prod_curcuma.jpg` | Sobre blanco, 600px |
| **Prod: Chía** | `prod_chia.jpg` | Sobre blanco, 600px |
| **Prod: Legumbre (Secos)** | `prod_lima_bean.jpg` | Sobre blanco, 600px |
| **DEL CAMPO — Arroz embolsado** | `delcampo_arroz.jpg` | Packaging real DEL CAMPO |
| **DEL CAMPO — Arroz Rico** | `delcampo_arroz_rico.jpg` | Packaging real |
| **DEL CAMPO — Manteca** | `delcampo_manteca.jpg` | Packaging real |
| **DEL CAMPO — Aceite** | `delcampo_aceite.jpg` | Packaging real |

Para las secciones donde no hay foto real todavía (cards de división en home, logos de certificaciones), usá placeholder CSS gradient con etiqueta clara.

---

## PASO 6 — Constraints de diseño no negociables

**Fuentes:** Playfair Display (títulos, 400 Regular + italic) + Lexend (body/UI, 300 Light + 400 Regular). Solo Google Fonts.

**Colores (6 tokens, usar CSS custom properties):**
```css
--text-primary:   #1D1D1B;
--text-secondary: #4A3625;
--accent-warm:    #9F8A73;
--accent-green:   #2E7B37;
--surface-warm:   #FAF8F5;
--hairline:       #EDEAE3;
```
Blanco puro `#FFFFFF` es la superficie por defecto. Verde (`#2E7B37`) es puntuación — solo CTAs, hovers, estados activos.

**Eyebrows/kickers:** Lexend Light 12px, `#9F8A73`, uppercase, letter-spacing 0.10em. (NO Playfair para eyebrows.)

**Números de estadísticas:** `#2E7B37` (verde) para los contadores grandes.

**Hero (home):** Version A bloqueada — foto full-bleed, máscara gradiente oscuro en tercio izquierdo, titular bottom-left. Sin slider.

**Cards de divisiones (home):** Grid 5 columnas Elementor — válido. Cada card: foto 4:5, nombre Playfair 20px, descriptor Lexend Light 13px `#4A3625`, flecha verde `→`. Hover: imagen escala 1.03, flecha se mueve 4px derecha.

**Template de división:** Layout LDC-style — breadcrumb, hero 60vh, banda intro (párrafo lead Playfair), sidebar sticky 280px (categorías + certs), filas de productos (imagen 280px + texto, divisores hairline), banda cierre full-bleed con pull quote Playfair Italic.

**Técnico:** Cada archivo completamente self-contained. CSS custom properties. HTML semántico. Responsive en 900px y 640px. Dropdown CSS en "Divisiones" (`:hover`). Scroll shadow en header via JS mínimo.

---

## PASO 7 — Orden de construcción

Un archivo a la vez. Para cada uno:
1. Anunciá el filename
2. Procesá cualquier imagen necesaria (base64 si corresponde)
3. Outputeá el archivo completo
4. Guardalo en la carpeta mockups

Orden: revisar `home-version-a.html` → mejorar y guardar → revisar `division-secos.html` → mejorar y guardar → crear `nosotros.html` → crear `contacto.html`

Todos los archivos comparten header y footer idénticos (solo cambia el estado activo del nav). Contenido real de CLIENT_BRIEF.md y SITE_SKELETON.md — nombres reales, productos reales, datos de contacto reales.

Empezá leyendo los seis archivos del Paso 1.
