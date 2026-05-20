## 🔍 Post-procesamiento

El post-procesamiento se realizó en **dos etapas**:

### 1. **Validación cruzada** (con imágenes de evaluación)
✍️ ~1.700 imágenes etiquetadas manualmente vs. etiquetado de 9 modelos personalizados YOLO11

<img src="https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/0eb83567e21afc50c22d6b163ac56aa46cbc3be0/post-process/counts.png" width="600">


### 2. **Evaluación** (Dataset completo)

```bash
-  📸~89000 imágenes de cámaras trampa (8 cámaras)
-  Modelo Train15 (adultos y pollos)
-  Resultados: Series temporales interanuales
```
**🧪 Resultado**: [Zenodo](https://zenodo.org/records/20184303?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMWVhNzQ4LTE0NzctNGU2NS1iMjA5LWRhZmU2ZTY5NGJhMSIsImRhdGEiOnt9LCJyYW5kb20iOiJiYjY0MWExYTVjMTAxZjA1MDAyMzVhMGE2YWViZTk2MiJ9.mgWf0jtg0wnq9UID8P9e9CRHT9S5WqMLgTHu0_VYden4A95kiTZ9rYozYtCyvb8iDlZlq5fb1Btfa1muwRjv5g)

**🧪 Notebook de post-procesamiento**: [post_process.ipynb](notebooks/post_process.ipynb)




