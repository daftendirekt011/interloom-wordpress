"""
Interloom — procesa imágenes de producto y hero de contacto.
Regla: no pisar archivos existentes.
"""
from PIL import Image, ImageOps
import os

BASE_ML = r"C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\media_library_export-interloom-2026_05_13_22_49_06"
BASE_OD = r"C:\Users\DCPor\OneDrive\Documentos\interloom\03_assets\images\OneDrive_1_5-13-2026"
DST     = r"C:\Users\DCPor\OneDrive\Documentos\interloom\06_design\mockups\assets"


def process_product(src_path, dst_name, max_size=300):
    dst_path = os.path.join(DST, dst_name)
    if os.path.exists(dst_path):
        print(f"  SKIP  (ya existe): {dst_name}")
        return
    if not os.path.exists(src_path):
        print(f"  ERROR (no existe): {src_path}")
        return
    img = Image.open(src_path)
    img = ImageOps.exif_transpose(img)
    w, h = img.size
    s = min(w, h)
    left = (w - s) // 2
    top  = (h - s) // 2
    img  = img.crop((left, top, left + s, top + s))
    final_size = min(s, max_size)
    img = img.resize((final_size, final_size), Image.LANCZOS)
    img.convert("RGB").save(dst_path, "JPEG", quality=75, optimize=True)
    sz = os.path.getsize(dst_path) // 1024
    print(f"  OK    {dst_name}  ({final_size}x{final_size}, {sz} KB)")


def process_hero(src_path, dst_name, tw=1920, th=1080):
    dst_path = os.path.join(DST, dst_name)
    if os.path.exists(dst_path):
        print(f"  SKIP  (ya existe): {dst_name}")
        return
    if not os.path.exists(src_path):
        print(f"  ERROR (no existe): {src_path}")
        return
    img = Image.open(src_path)
    img = ImageOps.exif_transpose(img)
    iw, ih = img.size
    target_ratio = tw / th
    src_ratio    = iw / ih
    if src_ratio > target_ratio:
        # más ancha — recortar lados
        new_w = int(ih * target_ratio)
        left  = (iw - new_w) // 2
        img   = img.crop((left, 0, left + new_w, ih))
    else:
        # más alta — recortar arriba/abajo (centrado)
        new_h = int(iw / target_ratio)
        top   = (ih - new_h) // 2
        img   = img.crop((0, top, iw, top + new_h))
    img = img.resize((tw, th), Image.LANCZOS)
    img.convert("RGB").save(dst_path, "JPEG", quality=78, optimize=True)
    sz = os.path.getsize(dst_path) // 1024
    print(f"  OK    {dst_name}  ({tw}x{th}, {sz} KB)")


print("=== SECOS ===")
process_product(os.path.join(BASE_ML, r"2023\09\quinua-roja.jpg"),      "prod_quinua_roja.jpg")
process_product(os.path.join(BASE_ML, r"2023\09\quinua-negra.jpg"),     "prod_quinua_negra.jpg")
process_product(os.path.join(BASE_ML, r"2023\09\quinua-tricolor.jpg"),  "prod_quinua_tricolor.jpg")
process_product(os.path.join(BASE_ML, r"2022\12\kiwicha-organica.jpg"), "prod_kiwicha.jpg")
process_product(os.path.join(BASE_ML, r"2023\09\pallar-mediano.jpg"),   "prod_pallar.jpg")
process_product(os.path.join(BASE_ML, r"2022\12\maiz-cuzco.jpg"),       "prod_maiz_cusco.jpg")
process_product(os.path.join(BASE_ML, r"2023\07\maiz-mote-1.jpg"),      "prod_maiz_mote.jpg")
process_product(os.path.join(BASE_ML, r"2022\12\frijol-canario-2.jpg"), "prod_frijol_canario.jpg")
process_product(os.path.join(BASE_ML, r"2022\12\azucar-rubia.jpg"),     "prod_azucar_rubia.jpg")
process_product(os.path.join(BASE_ML, r"2023\07\harina-de-quinua.jpg"), "prod_harina_quinua.jpg")
process_product(os.path.join(BASE_ML, r"2023\07\sesamo-1.jpg"),         "prod_sesamo.jpg")

print("=== FRESCOS ===")
process_product(os.path.join(BASE_ML, r"2023\07\jengibre-deshidratado.jpg"), "prod_kion_deshidratado.jpg")
process_product(os.path.join(BASE_ML, r"2023\07\curcuma-en-polvo-1.jpg"),    "prod_curcuma_polvo.jpg")
process_product(os.path.join(BASE_ML, r"2023\07\palta-1.jpg"),               "prod_palta.jpg")
process_product(os.path.join(BASE_ML, r"2022\12\cacao-en-grano-1.jpg"),      "prod_cacao_grano.jpg")
process_product(os.path.join(BASE_ML, r"2022\12\cacao-en-polvo.jpg"),        "prod_cacao_polvo.jpg")

print("=== INGREDIENTES ===")
process_product(os.path.join(BASE_ML, r"2023\07\azucar-blanca-1.jpg"),  "prod_azucar_blanca.jpg")
process_product(os.path.join(BASE_ML, r"2022\12\fecula-de-papa.jpg"),   "prod_almidon.jpg")

print("=== HERO CONTACTO ===")
process_hero(os.path.join(BASE_OD, r"Ferias\IMG_8449.JPG"), "hero_contacto.jpg")

print("\nDone.")
