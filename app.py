import json, base64, os, zipfile
from google.colab import files

with open("/content/predict_student_with_XAI.ipynb", "r", encoding="utf-8") as f:
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

zip_filename = "images.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files_in_dir in os.walk("images"):
        for file in files_in_dir:
            zipf.write(os.path.join(root, file), arcname=file)

print(f"File zip selesai dibuat: {zip_filename}")
