# Penguin-Phenology-YOLO11

En este repositorio se encuentra el proceso secuencial para la obtención de los modelos personalizados con los que se pueden reproducir los resultados presentados en el artículo *[Automated estimation of interannual variation in penguin colony phenologies Antarctic Peninsula using a deep learning-based YOLO11 model customized for camera trap imagery](link_al_articulo)*.

**Objetivo**: Estimar la variación interanual de pingüinos (adultos y polluelos) desde el campo de visión de 8 cámaras trampa a través de un sistema de visión artificial, para ello se personalizó el modelo YOLO11 [![YOLO11](https://img.shields.io/badge/Modelo-YOLO11-blue)](https://github.com/ultralytics/ultralytics)

## Modelos personalizados utilizados
Se utilizaron 1717 imágenes de cámaras trampa seleccionadas al azar para realizar un etiquetado manual y evaluar el desempeño de los 9 modelos personalizados entrenados y elegir los más adecuados para la evaluación sobre el set completo de imágenes.

## Pipeline técnico

### 1. **Pre-procesamiento** (Local)
Windows 11 Pro

Intel i5, 8 GB RAM

text

### 2. **Entrenamiento** (NLHPC - Guacolda)
Cluster: NVIDIA V100 (1 nodo, 9 CPU)

Data augmentation personalizado

text

### 3. **Evaluación** (84.000 imágenes - Servidor INACH)
```bash
Hardware:
-  GPU: MGA G200e 64 bits
-  CPU: 2x Intel XEON 4114 (20 cores, 40 threads)
-  RAM: 240 GB DDR4 2666 MHz
-  Storage: 4 TB RAID 5 (SAS 12 Gbps)
-  OS: Ubuntu 20.04
```

**Salida**: DataFrame con fecha + conteo (adultos/polluelos) por imagen.


## 📊 Resultados

.

---

**🧪 Reproducir análisis**: [Jupyter Notebook](notebooks/phenology_analysis.ipynb)  
**📈 Modelos personalizados**: [Carpeta custom model](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/300c26b9a41ce238336b60105ad9e4e20471aa1e/custom%20model/custom%20models.zip)  
**🔬 Paper**: [Enlace al artículo](link_al_paper.pdf)




