# Pre-procesamiento

Este repositorio contiene el proceso secuencial previo a la obtención de los modelos personalizados con los que se pueden reproducir los resultados presentados en el artículo: Automated estimation of interannual variation in penguin colony phenologies Antarctic Peninsula using a deep learning-based YOLO11 model customized for camera trap imagery.

### Creación de un dataset de imágenes y anotaciones
Con la herramienta "labelimg" se realizó el etiquetado de imágenes en formato YOLO.
Las etiquetas de interés son pingüino adulto y pollo, sin embargo, en varias de las imágenes para etiquetar aparecian, personas, mamíferos como lobos y focas y otras aves como petreles. Por lo tanto, fue necesario definir las clases person, mammal and bird (además de penguin_adult y penguin_chick).

![Etiquetado labelImg](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/af76677bebd9db3c85ff9e9189864f85455c709c/pre-process/Captura%20de%20pantalla%202026-05-07%20111003.png)

### Ambiente de trabajo
Una vez instalado python se procedió a instalar Jupyter notebooks en la consola del cmd, debido a que permite el análisis interactivo y seleccion de ambiente de trabajo.

En cmd de windows se ejecutaron los siguientes comandos para crear e iniciar ambientede trabajo

```bash
>py -m venv penguin_env ## se crea ambiente de trabajo específico para visión artificial
>penguin_env\Scripts\activate ### Activa ambiente para instalar paquetes, luego de esto en la linea de comandos aparecerá (penguin_env)
>py -m pip install ultralytics ## Instalar utralytics en ambiente para poder usar YOLO
>py -m install ipykernel
>python -m ipykernel install --user --name penguin_env --display-name "penguin_env" ##configura ambiente virtual
>deactivate 
>py -m jupyter lab ### abre jupyter para comenzar a trabajar en el script.
```
### Etiquetado semisupervisado (opcional)
Con las primeras 1000 etiquetas se realizó el primer entrenamiento del modelo, la finalidad de este modelo era realizar un etiquetado semisupervisado de imágenes para que entren al entrenamiento final del modelo. Este proceso fue iterativo y requiere que el modelo haga detecciones automáticas pero luego ser revisadas manualmente, como trabajo sola este paso me ahorro muchísimo tiempo pero es opcional.

Entrenamiento modelo personalizado
```python
from ultralytics import YOLO
model = YOLO("yolo11n.pt")
results = model.train(data="...pinguino.yaml", epochs=150, imgsz=640, batch=-1)
```

Utilización de modelo personalizado para realizar detecciones sobre imágenes y generar archivo .txt de etiquetado.
```python
from ultralytics import YOLO ##carfar herramientas
import glob
import cv2
import os
import numpy as np
import pandas as pd

model = YOLO(".../train/weights/best.pt") #cargar modelo

image_dir = r"...\img" ##Directorio  de imágenes
image_paths = glob.glob(os.path.join(image_dir, "*.JPG")) # Obtener una lista de todos los archivos JPG

output_dir = r"...\output_dir" # 3. Directorios para guardar los resultados 
os.makedirs(output_dir, exist_ok=True)  # Crear el directorio si no existe
label_dir = r"...\label_dir"
os.makedirs(label_dir, exist_ok=True)  # Crear el directorio si no existe

data = []

for image_path in image_paths:
    img = cv2.imread(image_path) # Leer imagen
    if img is None:
        print(f"Error al cargar: {image_path}")
        continue
    
    height, width = img.shape[:2]  # Alto y ancho de la imagen# Obtener dimensiones
    
    results = model(img) # Detección
    
    # Preparar archivo de etiquetado
    file_name = os.path.basename(image_path)
    file_name_without_extension = os.path.splitext(file_name)[0]
    txt_path = os.path.join(label_dir, f"{file_name_without_extension}.txt")
    
    # Abrir archivo una sola vez por imagen
    with open(txt_path, 'w') as f:  # 'w' para sobrescribir en cada imagen
        counts = {}
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Obtener valores absolutos
                x1_abs, y1_abs, x2_abs, y2_abs = box.xyxy[0].tolist()
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                
                # Convertir a formato YOLO (coordenadas normalizadas)
                x_center = (x1_abs + x2_abs) / 2 / width
                y_center = (y1_abs + y2_abs) / 2 / height
                w = (x2_abs - x1_abs) / width
                h = (y2_abs - y1_abs) / height
                
                # Escribir en formato YOLO: class_id x_center y_center width height
                f.write(f"{class_name} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")
                
                counts[class_name] = counts.get(class_name, 0) + 1

        data.append({"image": file_name, **counts})

    # Visualización y guardado 
    annotated_frame = results[0].plot()
    cv2.imwrite(os.path.join(output_dir, f"{file_name_without_extension}_det.jpg"), annotated_frame)

print("Proceso completado.")
```

