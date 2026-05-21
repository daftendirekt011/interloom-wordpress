# Opus Prompt 5 — Del Campo · Version B (5 conceptos de diseño)
> Copiá todo lo que está debajo de la línea horizontal en una conversación nueva de Claude Opus (Cowork mode).
> Tenés acceso a la carpeta del workspace de interloom.

---

Sos un diseñador web senior y desarrollador front-end. Estás trabajando en el rediseño de **Grupo Interloom** para WordPress + Bridge Theme + Elementor Pro.

El objetivo de esta sesión es **diseñar 5 conceptos distintos para la sección "Del Campo"** que aparece en el home. Cada concepto es un bloque HTML+CSS autocontenido que reemplaza la sección `.dc-featured` actual en `home-version-a.html`. Los 5 conceptos van en un único archivo HTML de comparación.

---

## PASO 1 — Leer estos archivos antes de empezar

1. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\home-version-a.html`
   - Tomá los tokens de diseño de `:root` (fuentes, colores, variables)
   - Encontrá el bloque `<!-- DEL CAMPO — marca propia -->` para ver qué reemplazás
   - Notá la estructura del nav, footer y secciones adyacentes para que el contexto visual sea correcto

2. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\del-campo.html`
   - Ver el azul de marca: la sección `.dc-hero` usa `#1B3D87` (o similar) como color principal
   - Tomá nota del tono, branding y CTAs que ya se usan en la página de la marca

---

## PASO 2 — Contexto del proyecto

### Del Campo — marca propia de Interloom
- Marca de alimentos para el mercado local peruano ("Lo natural a tu mesa")
- **3 productos solamente:**
  - `assets/delcampo_hero.jpg` → Arroces
  - `assets/delcampo_aceite.jpg` → Aceites
  - `assets/delcampo_manteca.jpg` → Manteca vegetal
- **Las imágenes son posters verticales** (más altas que anchas, aprox. 2:3). Cada una ya contiene: logotipo Del Campo, nombre del producto, slogan y packaging fotografiado. Son hojas vendedoras / packaging shots, NO thumbnails de producto.
- Color de marca: azul profundo (~`#1B3D87`) con blanco y dorado/amarillo como acentos
- CTAs: WhatsApp (pedidos) + "Conocer la marca" (link a del-campo.html)

### Sección actual que se reemplaza
```html
<a class="dc-featured" href="del-campo.html">
  <div class="dc-photo"></div>   <!-- background-image: url('assets/division-delcampo.jpg') -->
  <div class="dc-content">
    <div class="eyebrow">MARCA PROPIA · MERCADO LOCAL</div>
    <h3>Del Campo</h3>
    <p class="tagline">Lo natural a tu mesa</p>
    <p class="desc">Arroces, aceites y manteca vegetal para el hogar peruano...</p>
    <div class="dc-actions">
      [btn-wa] Hacer un pedido
      [btn-outline-sm] Conocer la marca →
    </div>
  </div>
</a>
```

### Tokens de diseño del sitio
```css
--text-primary:    #1D1D1B;
--text-secondary:  #4A3625;
--accent-warm:     #9F8A73;
--accent-green:    #2E7B37;
--surface-warm:    #FAF8F5;
--hairline:        #EDEAE3;
--dc-blue:         #1B3D87;   /* azul marca Del Campo */

/* Tipografías */
font-family: 'Playfair Display', serif;   /* headings, taglines */
font-family: 'Lexend', sans-serif;         /* body, eyebrows, botones */
```

### Restricciones WordPress/Bridge/Elementor
- **Animaciones CSS permitidas:** `transition`, `@keyframes`, `animation`, `transform`, `opacity`. Elementor las replica con "Motion Effects > Entrance Animation" y "Scrolling Effects (Parallax)". Bridge las replica con clases `.appear_from_bottom` etc.
- **NO usar:** GSAP, ScrollMagic, Intersection Observer custom, librerías JS de animación. Solo CSS puro.
- **Hover effects:** siempre OK, son CSS `:hover` + `transition`.
- **Stagger de animaciones:** usar `animation-delay` en incrementos (0ms, 150ms, 300ms). Elementor lo soporta con "Entrance Animation > Delay".
- **Slider Revolution** está disponible en Bridge, pero para este ejercicio no lo usemos — el bloque debe ser estático o animado con CSS puro.
- **Las imágenes poster son `<img>`**, no `background-image`, para que Elementor pueda administrarlas fácilmente como widgets de Image.

---

## PASO 3 — Los 5 conceptos

Creá 5 bloques HTML+CSS, cada uno completamente autocontenido (su CSS va en un `<style>` con clases prefijadas para no colisionar). Cada concepto debe:
- Funcionar visualmente como si estuviera incrustado en el home entre el nav y la sección de divisiones B2B
- Usar los 3 posters verticales reales (`delcampo_hero.jpg`, `delcampo_aceite.jpg`, `delcampo_manteca.jpg`)
- Respetar el sistema de diseño del sitio (fuentes, colores base)
- Incluir los dos CTAs (WhatsApp verde y "Conocer la marca" ghost/outline)
- Indicar en un comentario HTML qué widget de Elementor / sección de Bridge se usaría para construirlo

---

### Concepto 1 — ESTÁTICO: "Galería de marca"
**Idea:** Sección full-width con fondo azul del campo. El nombre "Del Campo" en Playfair grande centrado en la parte superior. Debajo, los 3 posters en fila horizontal con el mismo ancho, con un gap generoso entre ellos. Un texto corto de marca y los CTAs debajo de los posters, centrados.

Tono: Premium, limpio, como una marca de retail boutique. Los posters respiran en el azul.

- Fondo: `#1B3D87`
- Texto sobre azul: blanco
- Posters: con leve `border-radius` y `box-shadow` suave para que floten
- Ancho máximo: 1200px centrado

---

### Concepto 2 — ESTÁTICO: "Split editorial asimétrico"
**Idea:** Layout de dos columnas desiguales (55% / 45%). Columna izquierda: fondo azul, texto de marca grande (Playfair), eyebrow, tagline, CTAs y los 3 posters en escala pequeña apilados diagonalmente (como un abanico o stack). Columna derecha: el poster de Arroces a pantalla completa (full-height de la columna), sin padding.

Tono: Editorial de revista de alimentos, contraste fuerte entre azul y la foto real.

- La columna derecha es el poster más icónico (Arroces) a tamaño grande
- Los otros dos posters en la columna izquierda como acento visual (pequeños, superpuestos con `z-index` y leve rotación de ±3-5deg CSS)
- Sin animación, pero los posters pequeños tienen `box-shadow` para profundidad

---

### Concepto 3 — ANIMADO: "Entrance con stagger"
**Idea:** Sección con fondo blanco (o `var(--surface-warm)`). Franja azul arriba a modo de header de sección (aprox 120px de alto) con el texto "Del Campo · Marca propia" en blanco. Los 3 posters debajo, con la mitad superior "entrando" dentro del área de la franja azul (overflow visible, efecto de "romper el marco").

**Animación:** Al cargar (o al entrar en viewport), los 3 posters hacen `fadeInUp` con stagger: poster 1 a los 0ms, poster 2 a los 150ms, poster 3 a los 300ms. CSS `@keyframes fadeInUp` desde `translateY(40px) opacity(0)` a `translateY(0) opacity(1)`.

En Elementor: sección header azul + inner section de 3 columnas con widget Image en cada una + "Entrance Animation: Fade In Up" + delays 0 / 150 / 300ms.

```css
@keyframes dc3-fadeInUp {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}
.dc3-poster { animation: dc3-fadeInUp 0.65s ease forwards; }
.dc3-poster:nth-child(1) { animation-delay: 0ms; }
.dc3-poster:nth-child(2) { animation-delay: 150ms; }
.dc3-poster:nth-child(3) { animation-delay: 300ms; }
```

---

### Concepto 4 — ANIMADO: "Hover expand con reveal de info"
**Idea:** Los 3 posters se muestran en fila, cada uno ocupando aprox. 28% del ancho de la sección (con fondo azul general). En estado normal, el poster ocupa toda la tarjeta. Al hacer hover, la tarjeta crece (`flex-grow` o `width` transition) al 44% del ancho, las otras dos se comprimen al 18%, y aparece un overlay en la parte inferior de la tarjeta expandida con el nombre del producto y un CTA.

**Animación:** Todo CSS con `transition: all 0.4s ease`. El overlay usa `max-height: 0 → 80px` con `overflow: hidden` y `transition`.

En Elementor: requiere CSS personalizado en el widget (Elementor Pro permite CSS custom por widget). Se documenta qué CSS agregar y dónde.

```css
.dc4-container { display: flex; gap: 12px; }
.dc4-card { 
  flex: 1;
  transition: flex 0.4s ease; 
  overflow: hidden;
  position: relative;
}
.dc4-card:hover { flex: 2.2; }
.dc4-overlay {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: rgba(27, 61, 135, 0.92);
  max-height: 0; overflow: hidden;
  transition: max-height 0.35s ease;
  padding: 0 16px;
}
.dc4-card:hover .dc4-overlay { max-height: 80px; padding: 16px; }
```

---

### Concepto 5 — SUPER CREATIVO: "Mural de marca"
**Idea:** Sección full-width, sin max-width contenedor. Fondo azul profundo a pantalla completa. Los 3 posters se colocan en ángulos diferentes: el central vertical y centrado (el más grande, ~50% de la altura de la sección), el de la izquierda rotado ~-8deg saliendo parcialmente desde el borde izquierdo, el de la derecha rotado ~+6deg saliendo parcialmente desde el borde derecho. Sobre el fondo azul, el texto "DEL CAMPO" en Playfair enorme (aprox. 100-120px) en blanco muy tenue (opacity 0.08) como marca de agua detrás de los posters.

El nombre real, tagline y CTAs van en el centro debajo del poster central, en blanco sólido.

Tono: Bold, joven, como campaña de publicidad de producto masivo. Muy visual.

- CSS `transform: rotate(-8deg)` y `translate` para posicionar los posters laterales
- `overflow: hidden` en el contenedor para que los posters cortados no rompan el layout
- El texto de fondo usa `font-size: clamp(80px, 10vw, 140px)` con `opacity: 0.07`
- Sin animación (el diseño es suficientemente llamativo), pero los posters tienen `transition: transform 0.3s ease` y en hover vuelven a 0deg (se "enderezan")

---

## PASO 4 — Archivo de salida

Creá **un único archivo HTML** llamado:
```
C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\delcampo-v2-concepts.html
```

Estructura del archivo:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- mismo head que home-version-a.html: fonts, charset, viewport -->
  <style>
    /* Reset y variables compartidas (copiadas de home-version-a.html) */
    /* Luego el CSS de cada concepto con clases prefijadas dc1-, dc2-, etc. */
  </style>
</head>
<body>

<!-- NAVEGACIÓN: copiar el nav exacto de home-version-a.html para contexto visual -->

<!-- ============================================================
     CONCEPTO 1 — "Galería de marca"
     ============================================================ -->
<section class="dc-concept dc-concept--1">
  <div class="concept-label">Concepto 1 · Galería de marca · Estático</div>
  <!-- ... HTML del concepto ... -->
</section>

<!-- ... repetir para conceptos 2-6 ... -->

</body>
</html>
```

Cada concepto va separado por una barra visual con el nombre y tipo (Estático / Animado / Creativo / Inspirado en la identidad de marca). NO incluir footer para que el archivo sea liviano.

---

### Concepto 6 — IDENTIDAD DE MARCA: "Según el Manual de Ana Marina"

**Contexto:** El manual de marca de Interloom (2026) fue diseñado por Ana Marina (diseñadora de identidad del proyecto). Su filosofía establece: **mínimo 80% de fondo blanco**, colores como acento (nunca como fondo dominante), tipografía Recoleta Regular como display principal.

**Antes de diseñar este concepto, leer:**
```
C:\Users\DCPor\Downloads\drive-download-20260506T200737Z-3-001\Manual_marca.pdf
```

**Nota sobre tipografía:** NO usar Recoleta en este concepto. Recoleta es exclusiva del logotipo — no se usa en texto web. El nombre "Del Campo" va en Playfair Display como el resto del sitio.

**Paleta del manual de Anita:**
```css
--verde-principal: #009E3C;
--verde-oscuro:    #2E7B37;
--negro:           #1D1D1B;
--tierra:          #4A3625;
--calido:          #9F8A73;
--amarillo-lima:   #C9CC3D;
```

**Idea:** Sección con fondo blanco puro. Arriba, una línea finísima (`1px solid #009E3C`) separa la sección del contenido anterior. El nombre "Del Campo" en Recoleta grande (~72px), color `#1D1D1B`, seguido del tagline en Playfair italic. A la derecha (o debajo, según el layout que mejor respire), los 3 posters en fila con una leve sombra muy sutil (`box-shadow: 0 2px 16px rgba(0,0,0,0.08)`). Los CTAs usan verde `#009E3C` (WhatsApp) y un outline verde para "Conocer la marca". Un pequeño detalle en amarillo-lima (`#C9CC3D`) como acento — puede ser una línea de 3px debajo del título o un punto decorativo.

Tono: Limpio, artesanal-premium, fiel a la identidad de marca. Sin azul. Sin fondos de color. Solo tipografía fuerte, espacio en blanco y los posters como protagonistas.

En Elementor: sección blanca, columna de texto (Heading widget con Recoleta via font upload en Bridge, Text widget para tagline), columna de imágenes (3 Image widgets en inner section). La línea verde superior puede ser el border-top de la sección en Elementor > Style > Border.

**Nota importante:** Este concepto representa la visión de la diseñadora de identidad (Ana Marina). Ofrece una alternativa radicalmente distinta a los conceptos 1-5 — no usa el azul Del Campo como protagonista, sino que respeta el sistema de marca corporativo de Interloom. Es valiosa para que el cliente decida si quiere que Del Campo "rompa" visualmente del sistema o quede integrada.

---

### Concepto 7 — ANIMADO INTERACTIVO: "Inversión de marca"

**Idea:** La sección arranca en blanco. En el centro, el logo/isologotipo de Del Campo en su versión normal (colores). Los 3 posters están dispuestos debajo o a los costados, en escala. Al hacer **hover sobre la sección completa** (o click en mobile), todo el fondo hace una transición suave a azul `#1B3D87`, el logo pasa a su versión negativa (blanco), los textos cambian a blanco, y los posters ganan un leve `brightness(1.1)` para resaltar sobre el azul. Al salir del hover, vuelve todo a blanco.

El efecto es como "entrar al mundo de la marca" — la sección te recibe en blanco (neutro) y al interactuar se "viste" de Del Campo.

```css
.dc7-section {
  background: #ffffff;
  transition: background 0.55s ease;
  cursor: default;
}
.dc7-section:hover {
  background: #1B3D87;
}
.dc7-title {
  color: #1D1D1B;
  transition: color 0.55s ease;
}
.dc7-section:hover .dc7-title { color: #ffffff; }

.dc7-logo-normal  { opacity: 1;  transition: opacity 0.55s ease; }
.dc7-logo-negativo{ opacity: 0;  transition: opacity 0.55s ease; position: absolute; top: 0; left: 0; }
.dc7-section:hover .dc7-logo-normal  { opacity: 0; }
.dc7-section:hover .dc7-logo-negativo{ opacity: 1; }
```

Para mobile (sin hover): agregar un pequeño botón o usar click con JS mínimo:
```js
document.querySelector('.dc7-section').addEventListener('click', function() {
  this.classList.toggle('dc7-active');
});
```
Y las reglas `:hover` se duplican para `.dc7-active`.

**Logo a usar:** `assets/logo.png` como versión normal. Para la versión negativa (blanco), Opus puede aplicar `filter: brightness(0) invert(1)` en CSS — no hace falta un archivo separado.

En Elementor: se implementa con CSS Custom en la sección + hover state en Elementor Pro (Background Color hover). Para el toggle en mobile, un snippet en el Custom CSS del theme o en un widget HTML.

---

### Concepto 8 — ANIMADO INTERACTIVO: "Tipografía que respira"

**Idea:** El concepto más minimalista de todos. Sección mayormente tipográfica, sin imágenes protagonistas — solo texto en grande y los 3 posters como fondo o acento muy sutil.

**Estado normal (blanco):** Fondo blanco. "Del Campo" en Playfair Display muy grande (clamp 64-96px), color `#1D1D1B`. Debajo, el tagline "Lo natural a tu mesa" en Playfair italic. Más abajo, los 3 nombres de producto ("Arroces · Aceites · Manteca") en Lexend espaciado. Los 3 posters aparecen muy pequeños y en baja opacidad (20%) a modo de textura/referencia visual, posicionados detrás del texto.

**Estado hover/activo (azul):** Todo el fondo transiciona a `#1B3D87`. El texto grande pasa a blanco. Los posters detrás suben a opacidad 60% — ahora se ven bien sobre el azul. El tagline cambia a un dorado suave (`#C9CC3D`, del manual de marca) para dar contraste. Los CTAs emergen desde abajo con `translateY` (estaban ocultos en estado normal).

La idea es que en reposo la sección es casi invisible (blanco sobre blanco del sitio), y al hacer hover "explota" de identidad de marca.

```css
.dc8-section {
  background: #ffffff;
  transition: background 0.6s ease;
  position: relative;
  overflow: hidden;
  padding: 80px var(--gutter-desktop);
  min-height: 480px;
}
.dc8-section.dc8-active,
.dc8-section:hover { background: #1B3D87; }

.dc8-big-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(64px, 8vw, 96px);
  color: #1D1D1B;
  transition: color 0.6s ease;
}
.dc8-section:hover .dc8-big-title,
.dc8-section.dc8-active .dc8-big-title { color: #ffffff; }

.dc8-tagline {
  font-style: italic;
  color: #9F8A73;
  transition: color 0.6s ease;
}
.dc8-section:hover .dc8-tagline,
.dc8-section.dc8-active .dc8-tagline { color: #C9CC3D; }

/* Posters de fondo */
.dc8-poster-bg {
  position: absolute;
  opacity: 0.12;
  transition: opacity 0.6s ease;
  pointer-events: none;
}
.dc8-section:hover .dc8-poster-bg,
.dc8-section.dc8-active .dc8-poster-bg { opacity: 0.55; }

/* CTAs ocultos, emergen al hover */
.dc8-ctas {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.4s ease 0.2s, transform 0.4s ease 0.2s;
}
.dc8-section:hover .dc8-ctas,
.dc8-section.dc8-active .dc8-ctas {
  opacity: 1;
  transform: translateY(0);
}
```

Toggle para click en mobile (mismo patrón que Concepto 7):
```js
document.querySelector('.dc8-section').addEventListener('click', function() {
  this.classList.toggle('dc8-active');
});
```

En Elementor: la transición de fondo se maneja con "Background Color" + hover en la sección. Los posters de fondo son Image widgets con opacidad reducida y position absolute via CSS custom. Los CTAs con Entrance Animation "Fade In Up". Para el toggle de click, un snippet custom de 3 líneas en el footer del theme.

---

## PASO 5 — Verificación final

Al terminar:
1. Abrí el archivo en el browser (o verificá que no haya errores de sintaxis obvios)
2. Confirmá que los 3 paths de imágenes sean correctos (`assets/delcampo_hero.jpg`, `assets/delcampo_aceite.jpg`, `assets/delcampo_manteca.jpg`)
3. Verificá que ningún concepto use librerías JS externas (solo CSS)
4. Para el Concepto 6: confirmá que no se usa Recoleta — solo Playfair Display y Lexend como el resto del sitio
5. Reportá si alguna imagen no existe en `assets/` y necesita procesarse

---

## Notas

- La sección de comparación es para que el cliente elija un concepto, NO para producción directa
- Una vez elegido el concepto, se portará a `home-version-a.html` en la rama `delcampo-prominent` del repo
- El cliente valora: azul de marca Del Campo, posters verticales bien exhibidos, CTAs claros, modernidad
- Las animaciones deben ser sutiles y no distraer del producto — Bridge/Elementor las hace al scrollear, no en loop

Empezá leyendo los dos HTMLs del Paso 1.
