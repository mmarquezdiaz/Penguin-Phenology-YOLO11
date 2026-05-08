# Workflow-NLHPC
Luego del pre-procesamiento y con el set de datos de entrenamiento y validación (imágenes y etiquetados) se puede proceder a entrenar un modelo personalizado (o varios).
El sistema operativo del supercomputador es LINUX, por lo tanto, para usarlo debí pasar algunas horas aprendiendo UBUNTU y realizando los cursos para uso de la infraestructura. Este notebook es básico y muestra los simples pasos a través de los cuales se puede ejecutar una tarea en el NLHPC. 

En este trabajo con el mismo set de datos de entrenamiento y validación se realizaron varios entrenamientos con diferentes aumentos de datos, para ello se utilizaron herramientas computacionales dependientes del Laboratorio Nacional de Computación de Alto Rendimiento (NLHPC), de esta forma cada entrenamiento tardaba un poco más de una hora.

Una vez que se tiene cuenta y clave de acceso al supercomputador se pueden copiar los datos (imágenes, etiquetas y scripts) en la carpeta/ambiente de trabajo, yo lo hice a través de FileZilla.

Luego a través de la consola de Windows powershell, se creó un acceso remoto al servidor, allí se creo un entorno virtual de python para más tarde enviar las tareas, con la siguiente linea de comando:
```bash
sbatch main_script.sh
```
Luego de esto en la consola aparecerá un número que es el del turno de la tarea, el tiempo que tarde la fila de espera dependerá de la cantidad y recursos de las tareasde los demás usuarios.

El contenido de 'main_script.sh' es:
```bash
#!/usr/bin/sh
echo "INICIO main_job"

# Submit the download job
tarea1=$(sbatch YOLO_train1.job | awk '{print $4}')
echo "Tarea $tarea1 encolada"

# Submit the process job, dependent on the download job
tarea2=$(sbatch --dependency=afterok:$tarea1 YOLO_train2.job | awk '{print $4}')
echo "Tarea $tarea2 encolada"
.
.#Se encolaron tantas tareas como entrenamientos se realizaron
.
echo

echo "FIN main_job"
```

YOLO_train.job contiene la información de cluster, partición, nodo, cpu, modulo y comando:
```bash
#!/bin/bash
#---------------Script SBATCH - NLHPC ----------------
#SBATCH -J YOLO_train1
#SBATCH -p v100
#SBATCH --gres=gpu:1
#SBATCH -n 1
#SBATCH -c 9
#SBATCH --mem=15000
#SBATCH --mail-user= 
#SBATCH --mail-type=ALL
#SBATCH -o trans_img_%j.err.out

# ----------------Modulos----------------------------
ml purge
ml Python

#Activamos entorno CONDA
eval "$(conda shell.bash hook)"
conda activate Yolo_env

# ----------------Comando--------------------------
python3 YOLO_p1.py
```

Finalmente YOLO_p1.py contiene el código en python que indica los argumentos de entrenamiento. 
```python
from ultralytics import YOLO

random_seed= 2 #define seed para repoducibilidad

model = YOLO("yolo11n.pt")    

results = model.train(data=".../pinguino.yaml",epochs=400,imgsz=640, 
batch=0.8, seed=random_seed, hsv_h=0.02,hsv_s=0.8,hsv_v=0.4, scale=0.6, fliplr=0.5, mosaic=0.8,
mixup=0.2,copy_paste=0.1, copy_paste_mode='flip',auto_augment='randaugment',device=0)
```

Realicé tantos archivos '.job' y '.py' como entrenamientos diferentes se realizaron. 

Los resultados los copié en mi computador de escritorio a través filezilla para post-procesamiento.

Los modelos utilizados para evaluar las fotografías fueron:
| Modelo  | Clase objetivo     |      |
|---------|--------------------|-------------|
| Train15 | Pingüinos **adultos** |  |
| Train13 | Pingüinos **polluelos** |  |

[Carpeta custom model](data/processed/)  




