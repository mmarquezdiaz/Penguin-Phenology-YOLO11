## 🔍 Post-procesamiento

El post-procesamiento se realizó en **dos etapas**:

### 1. **Validación cruzada** (con imágenes de evaluación)
✍️ ~1.700 imágenes etiquetadas manualmente vs. etiquetado de 9 modelos personalizados YOLO11

Métricas: R^2
![Regresion lineal](https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/af76677bebd9db3c85ff9e9189864f85455c709c/pre-process/Captura%20de%20pantalla%202026-05-07%20111003.png)

### 2. **Evaluación** (Dataset completo)
```bash
-  📸~89000 imágenes de cámaras trampa (8 cámaras)
-  Modelos Train13 (polluelos) + Train15 (adultos)
-  Resultados: Series temporales interanuales

```

**🧪 Notebook de post-procesamiento**: [post_process.ipynb](notebooks/post_process.ipynb)




