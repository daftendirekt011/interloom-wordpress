import re, os

html_dir = "C:/Users/DCPor/OneDrive/Documentos/interloom/06_design/mockups"
assets_dir = os.path.join(html_dir, "assets")
existing = set(os.listdir(assets_dir))
broken = []

for fname in sorted(os.listdir(html_dir)):
    if not fname.endswith(".html"):
        continue
    content = open(os.path.join(html_dir, fname), encoding="utf-8").read()
    refs = re.findall(r"assets/([^'\"\)\s]+)", content)
    for ref in refs:
        if ref not in existing:
            broken.append(f"BROKEN: {fname} -> assets/{ref}")

if broken:
    for b in broken:
        print(b)
else:
    print("All asset references OK - no broken links found.")

print(f"Files checked: {len([f for f in os.listdir(html_dir) if f.endswith('.html')])}")
print(f"Assets available: {len(existing)}")
