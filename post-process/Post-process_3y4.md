
### 3. **Diferenciar especies de pingüinos** (subset imágenes evaluación)
```bash
-  📸800 imágenes (subset de imágenes de cámaras HP02 y KOP03 cámaras)
-  Machine Learning: Ginni index dentro de Random forest para diferenciar pingüino Gentoo de Chinstrap.
-  Resultado: Embeddings predictores más importantes para distinguir Gentoo de Chinstrap.
```
Extracción de embeddings desde imágenes etiquetadas
```python
# -----------------------------
# Configuración
# -----------------------------
images_dir = Path(r"C:\Users\...\images")
labels_dir = Path(r"C:\Users\...\label")

# Modelo YOLO entrenado o base
yolo_model_path = r"C:\Users\...\Train15\best.pt"   # cambia por tu modelo
model = YOLO(yolo_model_path)

# -----------------------------
# Utilidades
# -----------------------------
def read_yolo_labels(label_file, img_w, img_h):
    boxes = []
    if not label_file.exists():
        return boxes

    with open(label_file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            cls, xc, yc, w, h = map(float, parts)

            x1 = int((xc - w / 2) * img_w)
            y1 = int((yc - h / 2) * img_h)
            x2 = int((xc + w / 2) * img_w)
            y2 = int((yc + h / 2) * img_h)

            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(img_w, x2)
            y2 = min(img_h, y2)

            boxes.append({
                "class_id": int(cls),
                "bbox": (x1, y1, x2, y2)
            })
    return boxes

def extract_embedding_from_crop(crop, model):
    crop_resized = cv2.resize(crop, (128, 128))

    # YOLO11 usa embed
    emb = model.embed(crop_resized)[0]

    return emb

# -----------------------------
# Construcción del dataset
# -----------------------------
rows = []

image_files = sorted([p for p in images_dir.iterdir() if p.suffix.lower() in [".jpg", ".jpeg", ".png"]])

for img_path in image_files:
    label_path = labels_dir / f"{img_path.stem}.txt"

    img = cv2.imread(str(img_path))
    if img is None:
        continue

    h, w = img.shape[:2]
    anns = read_yolo_labels(label_path, w, h)

    for ann in anns:
        class_id = ann["class_id"]
        x1, y1, x2, y2 = ann["bbox"]

        crop = img[y1:y2, x1:x2]
        if crop.size == 0:
            continue

        emb = extract_embedding_from_crop(crop, model)

        row = {
            "image": img_path.name,
            "class_id": class_id
        }
        for i, v in enumerate(emb):
            row[f"f_{i}"] = float(v)

        rows.append(row)

df = pd.DataFrame(rows)
df.to_csv(r"C:\Users\...\train_embeddings.csv", index=False)
```

### 4. **Patrón interanual por especie en Punta Armonía** (imágenes de HP01 y HP02)
```bash
-  📸9976 imágenes de cámaras HP01 y HP02
-  Random forest para diferenciar pingüino Gentoo de Chinstrap
-  Resultado: Serie temporal interanual diferenciada por especie
```
