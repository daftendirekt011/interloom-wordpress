# Opus Prompt 3 — DEL CAMPO Architecture Change
> Copiá todo lo que está debajo de la línea horizontal en una conversación nueva de Claude Opus (Cowork mode).
> Tenés acceso a la carpeta del workspace de interloom. Leé los archivos listados antes de empezar.

---

Sos un diseñador web senior y desarrollador front-end trabajando en el rediseño de **Grupo Interloom**. Ya existe un mockup aprobado por el cliente. El cliente pidió un cambio de arquitectura específico que tenés que implementar.

---

## PASO 1 — Leer estos archivos primero

1. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\home-version-a.html` — home aprobada, base de todo
2. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\division-secos.html` — template de página de división vigente
3. `C:\Users\DCPor\OneDrive\Documentos\interloom\01_brief\CLIENT_BRIEF.md` — info de la empresa y divisiones
4. `C:\Users\DCPor\OneDrive\Documentos\interloom\05_inspiration\DESIGN_DIRECTION.md` — decisiones de diseño bloqueadas
5. `C:\Users\DCPor\OneDrive\Documentos\interloom\07_wordpress\BRIDGE_CAPABILITIES.md` — qué puede hacer Bridge/Elementor (crítico)

No empieces a construir hasta leer los cinco.

---

## PASO 2 — El cambio que pidió el cliente

### Contexto de DEL CAMPO

DEL CAMPO es una división diferente a las otras cuatro (Ingredientes, Secos, Frescos, Greenclover). Es una **marca de consumo masivo** para el mercado peruano local, con su propia identidad visual: logo en azul y amarillo, tagline "Lo natural a tu mesa". Tiene productos de consumo masivo: arroz, aceites, manteca vegetal.

Su público en el sitio web son **compradores mayoristas y distribuidores** (bodegones, minimarkets) que quieren conocer la marca o hacer pedidos por WhatsApp. No es B2B internacional como las otras cuatro.

### El cambio pedido

**Sacar DEL CAMPO del dropdown de Divisiones y darle su propio ítem en el nav principal**, al mismo nivel que "Divisiones".

**Nav actual:**
```
[LOGO]   Nosotros  |  Divisiones ▾  |  Sostenibilidad  |  Clientes  |  Contacto    ES | EN
```
**Dropdown actual de Divisiones (5 ítems):**
```
DEL CAMPO · División de Ingredientes · División de Secos · División de Frescos · Greenclover Naturals LLC
```

**Nav nuevo:**
```
[LOGO]   Nosotros  |  Del Campo  |  Divisiones ▾  |  Sostenibilidad  |  Clientes  |  Contacto    ES | EN
```
**Dropdown nuevo de Divisiones (4 ítems):**
```
División de Ingredientes · División de Secos · División de Frescos · Greenclover Naturals LLC
```

---

## PASO 3 — Qué tenés que construir

### Archivo 1: `home-grid-options.html`
Una página de comparación que muestre **3 opciones de diseño** para la sección "Nuestras Divisiones" del home. El objetivo es que la diseñadora web pueda ver las tres opciones juntas y decidir cuál usar.

El problema a resolver: DEL CAMPO ya no está en el dropdown de Divisiones, pero el home tiene un grid de 5 cards de divisiones. ¿Qué hacemos con ese grid?

Las tres opciones tienen que ser distintas, funcionales, y **todas buildables en Elementor Pro**. No usés componentes que requieran JS complejo o plugins adicionales.

Para cada opción mostrá:
- La sección completa con estilos reales (no placeholders vacíos)
- Un badge/etiqueta que diga "Opción A", "Opción B", "Opción C"
- Debajo de cada opción, una nota breve (2-3 líneas) explicando la decisión de diseño y por qué funciona

**Ideas de partida para las opciones** (podés modificarlas o proponer algo mejor):

- **Opción A — Featured band:** DEL CAMPO aparece en una banda propia full-width antes del grid de 4 divisiones. El grid queda con Ingredientes, Secos, Frescos, Greenclover.
- **Opción B — Grid asimétrico:** Layout de 2 columnas — DEL CAMPO ocupa la columna izquierda grande (2 unidades de ancho), las 4 divisiones en columna derecha en grid 2×2.
- **Opción C — Grid de 5 con diferenciación visual:** Se mantienen las 5 cards pero DEL CAMPO tiene tratamiento visual distinto — fondo levemente azulado, badge "Marca Propia", quizás tamaño diferente.

Si se te ocurre una opción mejor que alguna de estas, implementala y explicá por qué.

Usá el mismo sistema de diseño (CSS custom properties, tipografías, colores) que está en `home-version-a.html`. El resto de la página (hero, about teaser, stats, etc.) no hace falta incluirlo — solo la sección del grid con el contexto mínimo necesario.

### Archivo 2: `del-campo.html`
La página standalone de DEL CAMPO. Esta página debe sentirse **distinta al template de división estándar** — más comercial, más cálida, más "marca de consumo" — pero sin romper la coherencia del sitio Interloom.

**Stack:** Bridge header/footer (igual que todas las páginas). Todo el contenido del medio = Elementor Pro.

**Elementos de diseño a decidir (usá tu criterio):**
- ¿Introducís el azul de DEL CAMPO (#003399 o similar) como color de acento en esta página? Si sí, ¿dónde y cómo lo dosificás para que no choque con la paleta Interloom?
- ¿El hero muestra packaging o campo? ¿Qué composición elegís?
- ¿Cómo presentás los productos? (no es el mismo formato que Secos con sidebar técnico)

**Estructura mínima de la página:**
1. Header (igual a todas las páginas, con nuevo nav: Del Campo en el nav principal)
2. Hero — foto + H1 "Del Campo" con tagline "Lo natural a tu mesa"
3. Intro — quiénes son, qué hacen (2-3 párrafos cortos)
4. Productos — catálogo visual: Arroces, Aceites, Manteca Vegetal. Las fotos de packaging están en:
   ```
   C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\assets\
   ```
   Hay: `division-delcampo.jpg`, y en el brief se mencionan los productos. Usá los assets disponibles con rutas relativas `assets/nombre.jpg`.
5. CTA — WhatsApp Business prominente (fondo `#25D366`, no es negociable)
6. Footer (igual a todas las páginas)

**Nota sobre el logo de DEL CAMPO:** El logo tiene azul y amarillo intensos, muy distinto a Interloom. No hagas que compitan. Podés usar el logo de DEL CAMPO en la página (como imagen, no recreado en SVG) pero controlá dónde lo ponés.

### Archivo 3: Actualizar el nav en los mockups existentes

Después de crear los dos archivos nuevos, actualizá el nav en:
- `home-version-a.html`
- `division-secos.html`
- `nosotros.html` (si existe)
- `contacto.html` (si existe)

El cambio en cada uno es solo el bloque de navegación: agregar "Del Campo" como ítem propio y dejarlo en el dropdown como solo 4 divisiones.

---

## PASO 4 — Sistema de diseño (no cambiar)

```css
--text-primary:    #1D1D1B;
--text-secondary:  #4A3625;
--accent-warm:     #9F8A73;
--accent-green:    #2E7B37;
--surface-warm:    #FAF8F5;
--hairline:        #EDEAE3;
--white:           #FFFFFF;
```

Fuentes: Playfair Display (títulos) + Lexend (body/UI). Solo Google Fonts.

El verde `#2E7B37` es puntuación de Interloom: CTAs, hovers, activos. DEL CAMPO puede tener su propio color de acento en su página, pero sin mezclar en el nav ni el footer general.

---

## PASO 5 — Guardar en

```
C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\
```

Orden de construcción:
1. `home-grid-options.html` (las 3 opciones de grid)
2. `del-campo.html` (página standalone)
3. Actualizar nav en archivos existentes

Confirmá cada archivo guardado antes de continuar con el siguiente.

Empezá leyendo los cinco archivos del Paso 1.
