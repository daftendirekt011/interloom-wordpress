# Opus Prompt — Catálogo de Fotos
> Copiá todo lo que está debajo de la línea horizontal en una conversación nueva de Claude Opus (Cowork mode).
> Tenés acceso a la carpeta del workspace de interloom.

---

Sos un director de arte y editor de fotografía trabajando en el rediseño web de **Grupo Interloom**, una empresa peruana de agrotrading.

---

## Contexto del sitio — leé esto antes de empezar

El sitio tiene estas secciones y necesidades fotográficas específicas:

### Páginas y qué foto necesita cada una

| Página | Sección | Qué tipo de foto funciona |
|--------|---------|--------------------------|
| **Home** | Hero principal (banner full-bleed, texto abajo a la izquierda) | Foto horizontal impactante, campo o planta, colores cálidos/naturales, sin personas en primer plano |
| **Home** | 5 cards de divisiones (formato 4:5 — más alta que ancha) | Una foto representativa por división, buen contraste, funciona recortada verticalmente |
| **Home** | About teaser (foto editorial al lado del texto) | Operaciones, planta, personas trabajando — cálida, auténtica |
| **División de Secos** | Hero | Planta agrícola o granos andinos, horizontal, impactante |
| **División de Secos** | Fichas de producto | Quinua, chía, kiwicha, maíz — sobre fondo neutro/blanco, limpio |
| **División de Frescos** | Hero | Campo de kion o cúrcuma, o planta Satipo |
| **División de Frescos** | Fichas de producto | Kion, cúrcuma, palta, cacao — sobre fondo neutro |
| **DEL CAMPO** | Hero | Packaging de arroz/aceite/manteca, o mercado local |
| **DEL CAMPO** | Productos | Fotos de packaging DEL CAMPO — arroz, aceite, manteca |
| **División de Ingredientes** | Hero | Almacén, planta, o producto (azúcar, almidón) |
| **Greenclover** | Hero | Puede ser la misma planta/campo — se enfoca en EE.UU. pero el producto es el mismo |
| **Nosotros** | Hero | Campo, equipo, o planta — con identidad humana/auténtica |
| **Nosotros** | Foto editorial | Personas del equipo, operaciones, planta — cálida, profesional |
| **Sostenibilidad** | Ilustración | Certificaciones, campo, prácticas sostenibles |
| **Clientes** | Ferias / eventos | Fotos de stands en ferias internacionales (Biofach, Anuga, etc.) |

### Estética del sitio (diseño aprobado por el cliente)
- Estilo: minimalista, limpio, moderno — "cool con identidad de campo"
- Paleta: blanco dominante, crema (#FAF8F5), marrón oscuro, verde bosque (#2E7B37)
- Las fotos tienen que respirar — NO fotos oscuras, saturadas o muy cargadas
- Funciona mejor: luz natural, colores cálidos/terrosos, composición limpia
- No funciona: fondos muy oscuros, colores muy saturados, fotos de stock genéricas

### Divisiones del grupo
- **DEL CAMPO** — Marca propia, mercado local peruano. Arroz importado, aceites, manteca. Fotos de packaging y mercado.
- **División de Ingredientes** — B2B local. Azúcar, almidón de papa, glutamato. Fotos de producto/planta.
- **División de Secos** — Exportación. Quinua, chía, kiwicha, maíz, legumbres. Planta propia en Callao.
- **División de Frescos** — Exportación. Kion (jengibre), cúrcuma, palta, cacao. Planta propia en Satipo, Junín.
- **Greenclover Naturals LLC** — Subsidiaria en EE.UU. Comercialización y pallet sales con trazabilidad.

---

## Tu tarea

Revisar todas las fotos disponibles y crear un catálogo completo que le permita a la diseñadora web saber exactamente qué tiene, qué calidad tiene, y para qué sirve cada foto en el sitio.

El catálogo se guarda en:
`C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\PHOTO_CATALOG.md`

---

## Carpetas a revisar (en este orden de prioridad)

### PRIORIDAD 1 — Fotos propias del cliente (OneDrive)
Estas son las más importantes — fotos originales de alta calidad del cliente.

```
C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\OneDrive_1_5-13-2026\
```

Subcarpetas:
- `Kion\` — 25 fotos de kion/jengibre (campo, producto, proceso)
- `Granos\` — 16 fotos de granos andinos (quinua, etc.)
- `FOTOS PRODUCTOS\` — 11 fotos de productos
- `Fotos Planta, Ferias y demas\Fotos Planta Agricola\` — 32 fotos de planta
- `Fotos Planta, Ferias y demas\Certificaciones\` — 9 logos/imágenes de certificaciones
- `Ferias\` — 36 fotos de ferias y eventos
- `Mercado Local\Hojas Vendedoras\` — 16 imágenes (hojas de venta, packaging)
- `Mercado Local\Fotos Campo\` — ~9 fotos de campo/mercado

### PRIORIDAD 1B — Fotos nuevas de campo (mayo 2026) ⭐ MUY IMPORTANTES
Estas son las fotos más recientes del cliente — tomadas esta semana directamente en campo. Priorizalas.

```
C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\OneDrive_campo_mayo2026\Campo_jpg\
```

56 fotos JPG (convertidas de HEIC/iPhone). Fechas del archivo: 18 de mayo 2026. Son fotos de campo tomadas con iPhone — pueden ser muy buenas para heroes y editoriales. Revisalas con especial atención.

### PRIORIDAD 2 — WordPress Media Library (fotos del sitio actual)
Fotos del sitio viejo. Las más recientes primero.

```
C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\media_library_export-interloom-2026_05_13_22_49_06\
```

**Orden: 2025 → 2024 → 2023 → 2022.**

---

## Cómo revisar cada foto

1. **Obtener la fecha del archivo:** Antes de procesar cada carpeta, corrés un comando bash para listar los archivos con sus fechas de modificación:
   ```bash
   ls -la --time-style=+"%Y-%m-%d" "RUTA_CARPETA/"
   ```
   Guardás esas fechas para incluirlas en la tabla.

2. **Ver la imagen:** Usá el `Read` tool en cada archivo de imagen. Podés ver las imágenes directamente — describí lo que ves.

---

## Formato de la tabla

Cada fila de la tabla tiene estas columnas:

| # | Archivo | Fecha | Descripción | Calidad | Orientación | Categoría | Uso web sugerido | Nombre sugerido |
|---|---------|-------|-------------|---------|-------------|-----------|-----------------|-----------------|

### Calidad técnica (1–5)
- **1** — Borrosa, oscura, fuera de foco, inutilizable
- **2** — Problemas técnicos importantes, uso muy limitado
- **3** — Aceptable, se puede usar con reservas
- **4** — Buena calidad, lista para usar
- **5** — Profesional, impactante, top pick

### Categorías
`hero` · `editorial` · `producto` · `certificacion` · `feria_evento` · `campo` · `packaging` · `descarte`

### Usos web sugeridos
`hero_home` · `hero_secos` · `hero_frescos` · `hero_delcampo` · `hero_ingredientes` · `hero_greenclover` · `hero_nosotros` · `card_division` · `producto_secos` · `producto_frescos` · `producto_delcampo` · `producto_ingredientes` · `editorial_nosotros` · `feria_clientes` · `sostenibilidad` · `certificacion` · `skip`

### Nombre sugerido
En snake_case, descriptivo, con número si hay varios similares.
Ejemplos: `kion_campo_aereo_01.jpg`, `quinua_producto_blanco_02.jpg`, `planta_operarios_01.jpg`

---

## Formato del catálogo completo

```markdown
# Catálogo de Fotos — Interloom
Generado: [fecha]
Total revisadas: X fotos

---

## PRIORIDAD 1 — OneDrive (fotos del cliente)

### Kion (25 fotos)

| # | Archivo | Fecha | Descripción | Calidad | Orientación | Categoría | Uso web sugerido | Nombre sugerido |
|---|---------|-------|-------------|---------|-------------|-----------|-----------------|-----------------|
| 1 | IMG_4521.jpg | 2025-03-14 | Campo de kion, vista aérea con dron, luz de tarde | 5 | Horizontal | hero | hero_frescos, hero_home | kion_campo_aereo_01.jpg |
...

### Granos (16 fotos)
...

[continuar con cada subcarpeta]

---

## PRIORIDAD 2 — WordPress Media Library

### 2025 (15 archivos)
...

### 2024 (5 archivos)
...

[etc.]

---

## RESUMEN — Top picks por sección

Al final, después de revisar todo, completá este resumen:

| Sección del sitio | Foto(s) recomendada(s) | Razón breve |
|-------------------|----------------------|-------------|
| Hero Home | ... | ... |
| Card — DEL CAMPO | ... | ... |
| Card — Ingredientes | ... | ... |
| Card — Secos | ... | ... |
| Card — Frescos | ... | ... |
| Card — Greenclover | ... | ... |
| Hero División de Secos | ... | ... |
| Hero División de Frescos | ... | ... |
| Hero DEL CAMPO | ... | ... |
| Hero Ingredientes | ... | ... |
| Hero Greenclover | ... | ... |
| Hero Nosotros | ... | ... |
| Editorial Nosotros | ... | ... |
| Productos Secos (quinua, chía...) | ... | ... |
| Productos Frescos (kion, cúrcuma...) | ... | ... |
| Productos DEL CAMPO (packaging) | ... | ... |
| Ferias / Clientes | ... | ... |
| Sostenibilidad | ... | ... |
```

---

## Instrucciones de ejecución

1. Creá el archivo `PHOTO_CATALOG.md` al inicio con el encabezado
2. Procesá carpeta por carpeta — **guardá cada tabla apenas la terminás** (para no perder progreso)
3. Si una foto es claramente un duplicado, indicalo: "Similar a [nombre]"
4. Al final, completá la sección "Top picks"
5. No revisés `web_ready\` — esas ya están seleccionadas y en uso

Empezá listando los archivos de `OneDrive_1_5-13-2026\Kion\` con bash para obtener las fechas, luego revisá cada imagen con el Read tool.
