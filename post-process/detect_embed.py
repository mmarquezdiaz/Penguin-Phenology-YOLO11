from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path
import pandas as pd
from PIL import Image


MODEL_PATH = (
    "/home/bioinfo/Magdalena_data/"
    "detecciones_mari/modelos/train15/weights/best.pt"
)

VAL_DIR = Path(
    "/home/bioinfo/Magdalena_data/"
    "rootia/img/ECA59/arm/CamChinstrapPeak"
)

OUTPUT_CSV = (
    "/home/bioinfo/Magdalena_data/RF/embed_results/"
    "embeddings_class_id_E59chinpeak.csv"
)

EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp"}

detector = YOLO(MODEL_PATH)
embedding_model = YOLO(MODEL_PATH)


def extract_embedding(crop):
    crop = cv2.resize(crop, (128, 128))
    emb = embedding_model.embed(source=crop, verbose=False)[0]

    return emb.detach().cpu().numpy().ravel().astype(np.float32)


results_table = []

for img_path in sorted(VAL_DIR.rglob("*")):
    if (
        not img_path.is_file()
        or img_path.suffix.lower() not in EXTENSIONS
    ):
        continue

    fecha = np.nan

    try:
        with Image.open(img_path) as im:
            exif_data = im.getexif()
            if exif_data:
                fecha = exif_data.get(306, np.nan)

    except Exception as exc:
        print(f"No se pudo leer EXIF de {img_path.name}: {exc}")

    img = cv2.imread(str(img_path))

    if img is None:
        print(f"No se pudo leer la imagen: {img_path.name}")
        continue

    alto, ancho = img.shape[:2]

    result = detector.predict(
    source=img,
    verbose=False
    )[0]

    if not hasattr(result, "boxes"):
        raise TypeError(
            f"Resultado inesperado para {img_path.name}: {type(result)}; "
            f"shape={getattr(result, 'shape', None)}"
        )

    if result.boxes is None or len(result.boxes) == 0:
        continue

    boxes = result.boxes.xyxy.cpu().numpy()
    confs = result.boxes.conf.cpu().numpy()
    classes = result.boxes.cls.cpu().numpy().astype(int)

    print(
        f"{img_path.name}: "
        f"detecciones={len(result.boxes)}"
    )

    for box, conf, class_id in zip(boxes, confs, classes):
        x1, y1, x2, y2 = box

        x1 = max(0, min(int(round(x1)), ancho - 1))
        y1 = max(0, min(int(round(y1)), alto - 1))
        x2 = max(0, min(int(round(x2)), ancho))
        y2 = max(0, min(int(round(y2)), alto))

        if x2 <= x1 or y2 <= y1:
            continue

        crop = img[y1:y2, x1:x2]

        if crop.size == 0:
            continue

        feat = extract_embedding(crop)

        if feat.size != 256:
            raise ValueError(
                f"Embedding de {img_path.name} tiene "
                f"{feat.size} dimensiones; se esperaban 256."
            )

        result_dict = {
            "foto": img_path.name,
            "ruta": str(img_path),
            "fecha": fecha,
            "class_id": int(class_id),
            "confidence": float(conf),
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "width": x2 - x1,
            "height": y2 - y1,
        }

        result_dict.update(
            {
                f"f_{j}": float(feat[j])
                for j in range(256)
            }
        )

        results_table.append(result_dict)


df_results = pd.DataFrame(results_table)

print(f"Total detecciones: {len(df_results)}")

if df_results.empty:
    print("No se encontraron detecciones.")
else:
    print(
        f"Columnas: {df_results.columns.tolist()[:10]}..."
        f" ({len(df_results.columns)} columnas)"
    )
    print("\nPrimeras 5 filas:")
    print(df_results.head())

    print("\nÚltimas 5 filas:")
    print(df_results.tail())

    df_results.to_csv(OUTPUT_CSV, index=False)

    print(f"\nArchivo guardado en: {OUTPUT_CSV}")
    print("\nDistribución de class_id:")
    print(df_results["class_id"].value_counts().sort_index())
