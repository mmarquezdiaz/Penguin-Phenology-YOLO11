## 🔍 Post-procesamiento

El post-procesamiento se realizó en **dos etapas**:

### 1. **Validación cruzada** (con imágenes de evaluación)
✍️ 1.700 imágenes etiquetadas manualmente

Comparación vs. etiquetado de 9 modelos personalizados YOLO11

Métricas: mAP@0.5, Precision, Recall

### 2. **Evaluación** (Dataset completo)
```bash
-  📸84.000 imágenes de cámaras trampa (8 cámaras)
-  Modelos Train13 (polluelos) + Train15 (adultos)
-  Resultados: Series temporales interanuales
```

**🧪 Notebook de post-procesamiento**: [post_process.ipynb](notebooks/post_process.ipynb)




