
### 3. **Diferenciar especies de pingüinos** (subset imágenes evaluación)
-  📸 Detección de embeddings de 800 imágenes etiquetadas (subset de imágenes de cámaras HP02 y KOP03 cámaras)
-  Machine Learning: Ginni index dentro de Random forest para diferenciar pingüino Gentoo de Chinstrap.
-  Resultado: Embeddings predictores más importantes para distinguir Gentoo de Chinstrap.

***Extracción de embeddings desde imágenes etiquetadas***
```python
# Configuración
# -----------------------------
images_dir = Path(r"C:\Users\...\images")
labels_dir = Path(r"C:\Users\...\label")

# Modelo YOLO personalizado
yolo_model_path = r"C:\Users\...\Train15\best.pt"  
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

            boxes.append({"class_id": int(cls), "bbox": (x1, y1, x2, y2)})
    return boxes

def extract_embedding_from_crop(crop, model):
    crop_resized = cv2.resize(crop, (128, 128))
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

        row = {"image": img_path.name,"class_id": class_id}
        for i, v in enumerate(emb):
            row[f"f_{i}"] = float(v)
        rows.append(row)

df = pd.DataFrame(rows)
```
***Random forest-Ginni index***
```python
# ── CARGAR ─────────────────────────────────────────────────────────────────────
df = df[df["class_id"].isin([0, 2])].copy() ###0: chinstrap, 2:Gentoo
emb_cols = [c for c in df.columns if c.startswith('f_') and c[2:].isdigit()]
X = df[emb_cols].values
y = df['class_id'].values.astype(int)

print(f"✓ Matriz: {len(df):,} filas | {len(emb_cols)} bandas")
print(f"  Papua: {(y==2).sum():,} | Chinstrap: {(y==0).sum():,}\n")

# ── ENTRENAR ────────────────────────────────────────────────────────────────────
rf = RandomForestClassifier(n_estimators=400, class_weight='balanced', max_features= 0.5, min_samples_leaf= 5, min_samples_split= 20, random_state=42, n_jobs=-1)
rf.fit(X, y)

cv   = StratifiedKFold(n_splits=3, shuffle=True, random_state=SEED)
aucs = cross_val_score(rf, X, y, cv=cv, scoring='roc_auc', n_jobs=-1)

# ── IMPORTANCIA ─────────────────────────────────────────────────────────────────
imp = pd.DataFrame({'embedding': emb_cols, 'importance': rf.feature_importances_}) \
        .sort_values('importance', ascending=False).reset_index(drop=True)
imp['rank']           = range(1, len(imp)+1)
imp['importance_pct'] = 100 * imp['importance'] / imp['importance'].sum()
imp['cumulative_pct'] = imp['importance_pct'].cumsum()
```

### 4. **Patrón interanual por especie en Punta Armonía** (imágenes de HP01 y HP02)
-  📸Detección de embeddings sobre 9976 imágenes de cámaras HP01 y HP02 no etiquetadas. [script](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/0f6944134f016d88647309cbc17e9d2468d6ba4d/post-process/detect_embed.py)
-  Suma TOP3 embeddings para diferenciar pingüino Gentoo de Chinstrap
-  Resultado: Serie temporal interanual diferenciada por especie

