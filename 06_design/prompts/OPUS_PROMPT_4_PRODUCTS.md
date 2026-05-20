# Opus Prompt 4 — Fotos de productos + hero Contacto
> Copiá todo lo que está debajo de la línea horizontal en una conversación nueva de Claude Opus (Cowork mode).
> Tenés acceso a la carpeta del workspace de interloom.

---

Sos un diseñador web senior y desarrollador front-end trabajando en el rediseño de **Grupo Interloom**. El mockup está casi listo para entregar como high-fidelity en GitHub Pages. Esta sesión tiene un objetivo concreto: **inyectar las fotos de producto reales en todas las páginas de división** y **mejorar el hero de Contacto**.

---

## PASO 1 — Leer estos archivos antes de empezar

1. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\division-secos.html`
2. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\division-frescos.html`
3. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\division-ingredientes.html`
4. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\del-campo.html`
5. `C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\contacto.html`

Identificá en cada archivo:
- Cómo están estructuradas las fichas de producto (clases CSS, HTML de cada card)
- Qué imágenes ya tienen (`assets/prod_*.jpg`) y cuáles tienen placeholders o están vacías
- Dónde va el hero de Contacto

---

## PASO 2 — Procesar y copiar las imágenes

Todas las imágenes fuente están en:
```
C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\media_library_export-interloom-2026_05_13_22_49_06\
```

Las imágenes destino van en:
```
C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\assets\
```

### Procesamiento estándar para fotos de producto

Usá Python + Pillow. Para **todas** las fotos de producto:
- Recortar al cuadrado centrado (crop al centro)
- Redimensionar a **400×400 px**
- Guardar como JPEG quality=82, optimize=True
- Nombre: `prod_NOMBRE.jpg` (ver tabla de mapeo abajo)

**REGLA CRÍTICA: No pisar imágenes existentes.** Antes de procesar cada imagen, verificá si el archivo destino ya existe en `assets/`. Si existe, saltear y pasar al siguiente. Solo procesá las que NO existen todavía.

```python
from PIL import Image, ImageOps
import os

def process_product(src_path, dst_path, max_size=400):
    # Guard: no pisar existentes
    if os.path.exists(dst_path):
        print(f"  SKIP (ya existe): {os.path.basename(dst_path)}")
        return
    img = Image.open(src_path)
    img = ImageOps.exif_transpose(img)
    w, h = img.size
    # Crop cuadrado centrado
    s = min(w, h)
    left = (w - s) // 2
    top = (h - s) // 2
    img = img.crop((left, top, left + s, top + s))
    # IMPORTANTE: no upscalar — si la imagen ya es pequeña, mantener su tamaño
    final_size = min(s, max_size)
    img = img.resize((final_size, final_size), Image.LANCZOS)
    img.convert("RGB").save(dst_path, "JPEG", quality=75, optimize=True)
```

**Nota crítica sobre tamaño:** Las imágenes del media library ya vienen en 300×300. No las subas a 400 — se pixelarían. Quedan en 300×300 máximo. El target de peso por imagen de producto es **<50KB**.

---

## PASO 3 — Mapa completo de imágenes por división

### División de Secos

Productos actuales en el sitio (según interloom.com.pe/exportacion/):

| Producto | Archivo fuente (en media_library) | Destino en assets/ |
|----------|----------------------------------|-------------------|
| Quinua Blanca | `2023/07/quinua-blanca-300x300.jpg` | `prod_quinua_blanca.jpg` ← ya existe, verificar |
| Quinua Roja | `2023/09/quinua-roja-300x300.jpg` | `prod_quinua_roja.jpg` |
| Quinua Negra | `2023/09/quinua-negra-300x300.jpg` | `prod_quinua_negra.jpg` |
| Quinua Tricolor | `2023/09/quinua-tricolor-300x300.jpg` | `prod_quinua_tricolor.jpg` |
| Chía | `2022/12/chia-300x300.jpg` | `prod_chia.jpg` ← ya existe, verificar |
| Kiwicha | buscar `kiwicha` en media_library (puede no existir) | `prod_kiwicha.jpg` |
| Pallares | `2023/09/pallar-mediano-300x300.jpg` | `prod_pallar.jpg` |
| Maíz Gigante Cusco | `2022/12/maiz-cuzco-300x300.jpg` | `prod_maiz_cusco.jpg` |
| Maíz Mote | `2023/07/maiz-mote-1-300x300.jpg` | `prod_maiz_mote.jpg` |
| Frijol Canario | `2022/12/frijol-canario-2-300x300.jpg` | `prod_frijol_canario.jpg` |
| Azúcar Rubia (export) | `2022/12/azucar-rubia-300x300.jpg` | `prod_azucar_rubia.jpg` |
| Harina de Quinua | `2023/07/harina-de-quinoa-300x300.jpg` | `prod_harina_quinua.jpg` |
| Sésamo | `2023/07/sesamo-1-300x300.jpg` | `prod_sesamo.jpg` |

**Nota sobre kiwicha:** Si no hay foto en media_library, buscar en:
`C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\OneDrive_1_5-13-2026\Granos\`
Si tampoco hay, omitir ese producto de la ficha o dejar placeholder `[Foto pendiente]`.

---

### División de Frescos

| Producto | Archivo fuente | Destino en assets/ |
|----------|---------------|-------------------|
| Kion / Jengibre Fresco | `2022/12/jenjibre-organico-300x300.jpg` | `prod_kion.jpg` ← ya existe, verificar |
| Cúrcuma Fresca | `2022/12/curcuma-300x300.jpg` | `prod_curcuma.jpg` ← ya existe, verificar |
| Jengibre Deshidratado | `2023/07/jengibre-deshidratado-300x300.jpg` | `prod_kion_deshidratado.jpg` |
| Cúrcuma en Polvo | `2023/07/curcuma-en-polvo-1-300x300.jpg` | `prod_curcuma_polvo.jpg` |
| Palta Fresca | `2023/07/palta-1-300x300.jpg` | `prod_palta.jpg` |
| Cacao en Grano | `2022/12/cacao-en-grano-1-300x300.jpg` | `prod_cacao_grano.jpg` |
| Cacao en Polvo | `2022/12/cacao-en-polvo-300x300.jpg` | `prod_cacao_polvo.jpg` |

---

### División de Ingredientes

| Producto | Archivo fuente | Destino en assets/ |
|----------|---------------|-------------------|
| Azúcar Blanca | `2023/07/azucar-blanca-1-300x300.jpg` | `prod_azucar_blanca.jpg` |
| Azúcar Rubia | `2022/12/azucar-rubia-300x300.jpg` | `prod_azucar_rubia.jpg` |
| Almidón de Papa | buscar `almidon` en media_library | `prod_almidon.jpg` |
| Glutamato | buscar `glutamato` en media_library | `prod_glutamato.jpg` |

Si no hay foto de almidón o glutamato, buscá algo representativo en `FOTOS PRODUCTOS/` de OneDrive. Si no hay nada, dejá el card sin foto pero con el nombre del producto y una nota `[Foto pendiente]`.

---

### Del Campo (del-campo.html)

Ya tiene: `delcampo_hero.jpg` (Arroces), `delcampo_aceite.jpg` (Aceites), `delcampo_manteca.jpg` (Manteca).

**Agregar si la página no lo tiene:**
- Azúcar Rubia Del Campo: usar la hoja vendedora `Azucar Embolsado.jpg` de:
  `C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\OneDrive_1_5-13-2026\Mercado Local\Hojas Vendedoras\`
  Recortarla en la zona del packaging (parte superior de la hoja) → `prod_azucar_delcampo.jpg`

Solo agregá este producto si en el HTML de del-campo.html ya hay una sección para "Azúcar" o un slot disponible. Si no hay espacio, no lo agregues.

---

## PASO 4 — Inyectar las imágenes en los HTMLs

Para cada división, encontrá las fichas de producto en el HTML y:

1. Si la ficha ya tiene una imagen con la ruta correcta → verificar que el archivo exista en assets/, si no procesarlo
2. Si la ficha tiene un placeholder de texto como `[Foto pendiente]` o un div vacío → reemplazarlo con `<img src="assets/NOMBRE.jpg" alt="Producto">`
3. Si la ficha no existe para un producto del sitio actual → **agregar** la ficha al HTML siguiendo el mismo patrón de las fichas existentes

El patrón de ficha de producto varía por página. Leé el HTML de cada una primero y replicá la estructura exacta.

**Importante:** no cambies el diseño ni el CSS — solo inyectá las imágenes en las estructuras que ya existen.

---

## PASO 5 — Hero de Contacto

### El problema
El hero actual de `contacto.html` usa `nosotros_planta.jpg` (foto de planta de procesamiento). El cliente pidió algo más relevante para una página de contacto — idealmente una imagen que transmita "disponibles para atenderte".

### La solución
Usá esta foto de feria que ya está en la media library:
```
C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\OneDrive_1_5-13-2026\Fotos Planta, Ferias y demas\Ferias\
```
Buscá la foto que el catálogo (`PHOTO_CATALOG.md`) llama `IMG_8449` (stand con badge "FINALISTA Mejor Stand EXPOALIMENTARIA") o `IMG_8446` (stand amplio de Interloom en feria). Son las únicas fotos de feria disponibles.

Procesamiento:
- Recortar 16:9 centrado
- Resize a 1920×1080
- Quality=78
- Guardar como `assets/hero_contacto.jpg`
- Reemplazar en contacto.html: `url('assets/nosotros_planta.jpg')` → `url('assets/hero_contacto.jpg')`

Si ninguna de esas fotos funciona bien en 16:9, usá como alternativa la foto de la planta con operarios del catálogo:
`Fotos Planta, Ferias y demas/Fotos Planta Agricola/` — elegir la más profesional (calidad 4 o 5).

---

## PASO 6 — Orden de ejecución

1. Procesar todas las imágenes de producto → assets/ (usar bash para listar primero qué ya existe)
2. Inyectar en division-secos.html
3. Inyectar en division-frescos.html
4. Inyectar en division-ingredientes.html
5. Verificar del-campo.html (confirmar que las 3 imágenes existentes están bien)
6. Procesar y aplicar hero de contacto
7. Verificar: hacer un listado final de `assets/` y confirmar que no hay paths rotos en ningún HTML

---

## PASO 7 — Verificación final

Al terminar, correr este check:

```python
import re, os

html_dir = "C:/Users/DCPor/OneDrive/Documentos/interloom/06_design/mockups"
assets_dir = os.path.join(html_dir, "assets")
existing = set(os.listdir(assets_dir))

for fname in os.listdir(html_dir):
    if not fname.endswith('.html'):
        continue
    content = open(os.path.join(html_dir, fname)).read()
    refs = re.findall(r"assets/([^'\")\s]+)", content)
    for ref in refs:
        if ref not in existing:
            print(f"BROKEN: {fname} → assets/{ref}")
```

Reportá cualquier imagen rota y arreglala antes de cerrar.

---

## Notas

- No uses imágenes de shutterstock que están en la carpeta — tienen marca de agua y requieren licencia
- Si una imagen de la media_library no existe con ese nombre exacto, buscar variantes (`-300x300`, sin sufijo, `.jpeg` vs `.jpg`)
- No cambies el diseño, tipografías ni colores — solo fotos
- Guardá cada archivo HTML apenas terminés de inyectar esa división

Empezá leyendo los 5 HTML del Paso 1.
