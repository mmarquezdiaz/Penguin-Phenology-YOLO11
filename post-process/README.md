## 🔍 Post-procesamiento

El post-procesamiento se realizó en **dos etapas**:

### 1. **Validación cruzada** (con imágenes de evaluación)
✍️ ~1.700 imágenes etiquetadas manualmente vs. etiquetado de 9 modelos personalizados YOLO11

Métricas: R^2
<img src="https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/7cdbc353adf460a62ce491daa3ecc6f8a36983b6/post-process/rl_padult.png" width="400">

### 2. **Evaluación** (Dataset completo)

```bash
-  📸~89000 imágenes de cámaras trampa (8 cámaras)
-  Modelos Train13 (polluelos) + Train15 (adultos)
-  Resultados: Series temporales interanuales
**🧪 Resultado**: [Zenodo](https://zenodo.org/records/20184303?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjdmMWVhNzQ4LTE0NzctNGU2NS1iMjA5LWRhZmU2ZTY5NGJhMSIsImRhdGEiOnt9LCJyYW5kb20iOiJiYjY0MWExYTVjMTAxZjA1MDAyMzVhMGE2YWViZTk2MiJ9.mgWf0jtg0wnq9UID8P9e9CRHT9S5WqMLgTHu0_VYden4A95kiTZ9rYozYtCyvb8iDlZlq5fb1Btfa1muwRjv5g)
```

**🧪 Notebook de post-procesamiento**: [post_process.ipynb](notebooks/post_process.ipynb)




