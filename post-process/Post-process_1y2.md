## 🔍 Post-procesamiento

El post-procesamiento se realizó en **cuatro etapas**:

### 1. **Evaluación independiente de modelos** (con imágenes de evaluación)
✍️ ~1.700 imágenes etiquetadas manualmente vs. etiquetado de 9 modelos personalizados YOLO11
Cálculo de la distancia Eucliana al punto de rendimiento ideal, con un 100 % de detecciones correctas y un 0 % de detecciones incorrectas 
```python
from ultralytics import YOLO

model = YOLO(r"...\runs\detect\train2\weights\best.pt")
metrics = model.val(data=r"...pinguino.yaml", classes=[0, 1])
```

### 2. **Evaluación** (Dataset completo)
-  📸~89000 imágenes de cámaras trampa (8 cámaras)
-  Modelo Train15 (adultos y pollos)
-  Resultados: Series temporales interanuales por cámara (cada cámara )

**Custom model**:[Train15](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/bd8fdf9775103b587a5b68880ba5a12c125f693d/custom%20model/train15.zip)

![Campo de vision de cámaras trampa de pingüino barbijo](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/f848d78099f10a0b0bf65847598bd172120e3fd1/post-process/Captura%20de%20pantalla%202026-05-29%20120004.png)
Campo de visión cámaras sobre colonias de Pingüino Barbijo a) HP01 en Punta Armonía, b) HP02 en Punta Armonía, c) Kop01 en Isla Kopaitic, d) Kop02 en isla kopaitic
![Campo de visión de cámaras trampa de Pingüino papúa](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/9d8e660f7447c44dd000f0f21d212486b8f64f52/post-process/Captura%20de%20pantalla%202026-05-29%20120119.png)
Campo de visión cámaras sobre colonias de pingüino P. papua a)HP03 en Punta Armonía, b) Kop03 en Isla Kopaitic, c) HP04 en Punta Armonía, d) HP05 en Punta Armonía

**Resultado**: [Series temporales interanuales](https://doi.org/10.5281/zenodo.20184303)







