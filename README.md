# Penguin-Phenology-YOLO11 🐧❄️

En este repositorio se encuentra el proceso secuencial para la obtención de los modelos personalizados con los que se pueden reproducir los resultados presentados en el artículo *[Automated monitoring of Antarctic penguin colonies phenology using a customized YOLO11 model and camera trap imagery](link_al_articulo)*.

**Objetivo**: Estimar la variación interanual de pingüinos (adultos y polluelos) desde el campo de visión de 8 cámaras trampa a través de un sistema de visión artificial, para ello se personalizó el modelo YOLO11 [![YOLO11](https://img.shields.io/badge/Modelo-YOLO11-blue)](https://github.com/ultralytics/ultralytics)

## Modelos personalizados utilizados
Se utilizaron 1744 imágenes de cámaras trampa seleccionadas al azar para realizar un etiquetado manual y evaluar el desempeño de 9 modelos personalizados, con el fin de elegir los más adecuados para la evaluación sobre el set completo de imágenes.

## Pipeline técnico

### 1. **Pre-procesamiento y Post-Procesamiento** (Local)
Windows 11 Pro

Intel i5, 8 GB RAM

**Salida**: Set de datos etiquetados/ Gráficos 

### 2. **Entrenamiento** (NLHPC - Guacolda)
Cluster: NVIDIA V100 (1 nodo, 9 CPU)

Data augmentation personalizado

**Salida**: 9 modelos personalizados para recuento de pingüinos.

**📈 Modelo personalizado seleccionado**:[Train15](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/7d4ab53e12f910e97e9432e90f04a0db458b4e83/custom%20model/train15.zip)  

### 3. **Evaluación** (90744 imágenes) y **extracción de embeddings** (10776 imágenes)
####Servidor INACH
Hardware:
-  GPU: MGA G200e 64 bits
-  CPU: 2x Intel XEON 4114 (20 cores, 40 threads)
-  RAM: 240 GB DDR4 2666 MHz
-  Storage: 4 TB RAID 5 (SAS 12 Gbps)
-  OS: Ubuntu 20.04

**Salida**: DataFrame con fecha + conteo (adultos/polluelos) por imagen y dataframe con embeddings extraídos para cada detección

## 📊 Resultados 🐧❄️
Transformacion de imágenes de cámara trampa en series de tiempo interpretables que revelaron diferencias fenológicas entre colonias y especies de Pygocelis.🐧

**🧪 Resultado**: [Automated Penguin Counting: Antarctic Peninsula (2022–2026)](https://doi.org/10.5281/zenodo.20184303) 

**🔬 Paper**: in progress
---
## 📊 Flujo de trabajo (inglés) 🐧❄️
```bash
       WORKFLOW
==========================

                              ┌─────────────────────────────────────┐
                              │     YOLO11 CUSTOM MODEL DATASET     │
                              │                                     │
                              │  636 images                         │
                              │                                     │
                              │  Training:                           │
                              │    ├── 5,040 adult penguin labels   │
                              │    └── 1,600 chick labels           │
                              │                                     │
                              │  Validation:                        │
                              │    ├──   573 adult penguin labels   │
                              │    └──   250 chick labels           │
                              └──────────────────┬──────────────────┘
                                                 │
                                                 ▼
                              ┌─────────────────────────────────────┐
                              │      CUSTOMIZED YOLO11 MODEL        │
                              │                                     │
                              │      Training + Validation          │
                              └──────────────────┬──────────────────┘
                                                 │
                                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         INDEPENDENT MODEL EVALUATION                                 │
│                                                                                     │
│  1,744 randomly selected images from camera traps:                                  │
│                                                                                     │
│      HP01 ── HP02 ── Kop01 ── Kop02 ── Kop03                                      │
│                                                                                     │
│  ≈10% of all images captured by these cameras through March 2025                   │
│                                                                                     │
│  Ground-truth annotations:                                                         │
│      ├── 44,976 adult penguin annotations                                           │
│      └──  3,020 chick annotations                                                   │
│                                                                                     │
│                         ↓                                                           │
│                  YOLO11 PERFORMANCE                                                 │
│                    EVALUATION                                                        │
└──────────────────────────────────────────┬──────────────────────────────────────────┘
                                           │
                                           │
                    ┌──────────────────────┴──────────────────────┐
                    │                                             │
                    ▼                                             ▼
┌─────────────────────────────────────┐       ┌──────────────────────────────────────┐
│       RANDOM FOREST DATASET          │       │     FULL CAMERA-TRAP DATASET        │
│                                     │       │                                      │
│  800 images                         │       │  ≈89,000 images                      │
│                                     │       │                                      │
│  HP02 ── Kop03                      │       │  HP01 ── HP02 ── HP03 ── HP04        │
│                                     │       │  HP05 ── Kop01 ── Kop02 ── Kop03     │
│  Same images used in the            │       │                                      │
│  independent YOLO11 evaluation     │       │  Time period:                         │
│                                     │       │    HP01–HP05 → through 2026          │
│  YOLO11 image embeddings            │       │    Kop01–Kop03 → through 2025        │
└──────────────────┬──────────────────┘       │                                      │
                   │                          │              ↓                       │
                   ▼                          │       YOLO11 AUTOMATIC                 │
┌─────────────────────────────────────┐       │          DETECTION                   │
│       RANDOM FOREST MODEL           │       │                                      │
│                                     │       │       Phenology / attendance         │
│  Species classification:            │       │          data extraction              │
│                                     │       └──────────────────────────────────────┘
│    Gentoo vs. Chinstrap             │
│                                     │
│  Input: YOLO11 image embeddings     │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│      RANDOM FOREST EVALUATION       │
│                                     │
│  9,976 camera-trap images           │
│                                     │
│  HP01 ── HP02                        │
│                                     │
│  → Species classification           │
│  → Performance evaluation           │
└─────────────────────────────────────┘
```


