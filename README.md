# Penguin-Phenology-YOLO11
En este repositorio se encuentra el proceso secuencial para la obtención de los modelos personalizados con los que se pueden reproducir los resultados presentados en el artículo: Automated estimation of interannual variation in penguin colony phenologies Antarctic Peninsula using a deep learning-based YOLO11 model customized for camera trap imagery.

Este trabajo tuvo por objetivo estimar la variación interanual de pingüinos (adultos y polluelos) desde el campo de visión de 8 cámaras trampa a través de un sistema de visión artificial, para ello se personalizó el modelo YOLO11 y se realizó un recuento automatizado sobre cada imagen con el modelo obtenido desde el Train15 para pingüinos adultos y Train13 para pingüinos pollos.

El pre-procesamiento se realizó en un computador de escritorio Windows11pro, procesador i5 y 8 GB de RAM.

Los modelos personalizados se realizaron con diferente aumento de datos mediante acceso remoto al Laboratorio Nacional de Computación de Alto Rendimiento (NLHPC), cluster Guacolda, partición v100 (ya que cuenta con tarjeta NVIDIA), 1 nodo y 9 CPU.

Luego, el recuento automatizado sobre las 84000 imágenes de cámaras trampa almacenadas, se realizó con el servidor de INACH que cuenta con tarjeta gráfica MGA G200e de 64 bits, dos procesadores Intel XEON 4114 de 2,2 GHz, con 20 núcleos y 40 threads, 240 GB de memoria RAM DDR4 2666 MHz y dos discos duros tipo SAS de 2,5" con una tasa de transferencia de 12 Gbps. Cada disco es de 2 TB, montados en un arreglo RAID 5 y sistema operativo Ubuntu 20.04. De cada imagen se obtuvo la fecha y el recuento de pollos y adultos, estos datos se compilaron en un data frame.



