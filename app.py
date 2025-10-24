import json, base64, os

with open("hasil.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

os.makedirs("images", exist_ok=True)
count = 0
for cell in nb["cells"]:
    if "outputs" in cell:
        for out in cell["outputs"]:
            if "data" in out and "image/png" in out["data"]:
                imgdata = base64.b64decode(out["data"]["image/png"])
                with open(f"images/img_{count}.png", "wb") as f:
                    f.write(imgdata)
                count += 1

print(f"Disimpan {count} gambar di folder images/")
