## 🔍 Post-procesamiento

El post-procesamiento se realizó en **dos etapas**:

### 1. **Validación cruzada** (con imágenes de evaluación)
✍️ ~1.700 imágenes etiquetadas manualmente vs. etiquetado de 9 modelos personalizados YOLO11

Métricas: R^2
![Regresion lineal]([https://github.com/mmarquezdiaz/Penguin-Phenology-YOLO11/blob/7cdbc353adf460a62ce491daa3ecc6f8a36983b6/post-process/rl_padult.png])

### 2. **Evaluación** (Dataset completo)
```bash
-  📸~89000 imágenes de cámaras trampa (8 cámaras)
-  Modelos Train13 (polluelos) + Train15 (adultos)
-  Resultados: Series temporales interanuales

```

**🧪 Notebook de post-procesamiento**: [post_process.ipynb](notebooks/post_process.ipynb)




