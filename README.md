
# Proyecto Final  
## **Market Basket Analysis** for an Online Retail Business

📅 Abril 2025

Este proyecto analiza las compras realizadas en una tienda online durante un año para descubrir patrones sobre qué productos suelen comprarse juntos. Estos patrones permiten a la empresa entender mejor los hábitos de sus clientes y tomar decisiones inteligentes como:

- **Sugerencias automáticas:** Recomendar tazas de té cuando el cliente agrega una tetera.
- **Promociones combinadas:** Ofrecer descuentos por comprar productos relacionados (ej. papel de regalo + tarjetas).
- **Organización de la tienda online:** Ubicar productos que se venden juntos uno al lado del otro.
- **Campañas de email personalizadas:** Ofrecer artículos relacionados con compras anteriores.
- **Optimización de inventario:** Prever combinaciones de productos que se venden juntos.

---

## 🛒 App Interactiva – Market Basket Analysis

Esta aplicación permite analizar patrones de compra conjunta utilizando reglas de asociación (Apriori) con visualización interpretada y recomendaciones accionables.

### 🚀 ¿Qué puedes hacer?

- Explorar un dataset de transacciones preprocesado
- Ver productos que suelen comprarse juntos (Apriori)
- Analizar reglas de asociación con métricas clave
- Obtener recomendaciones por producto con interpretación automática

---

## 🧭 Navegación de la App

| Sección                    | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Introducción              | Explicación del propósito del análisis de cestas de mercado                 |
| Dataset                   | Vista previa del dataset binarizado (1 si un producto fue comprado)         |
| Conjuntos Frecuentes      | Resultados del algoritmo Apriori (productos frecuentes juntos)              |
| Reglas de Asociación      | Reglas generadas con soporte, confianza y lift                              |
| Recomendaciones           | Interpretación textual por producto seleccionado con acción sugerida       |

---

### 📸 Ejemplo de salida en "Recomendaciones"

```markdown
### 1. Regla: `roses regency teacup and saucer → green regency teacup and saucer`

- **Soporte**: 3.1%
- **Confianza**: 71.0%
- **Lift**: 17.72

✅ **Esta es una regla muy útil**

**📌 Acción recomendada:**  
*Product bundling* → Ofrecer ambos productos como un set o pack.
```

---

### 📦 Requisitos

- Python 3.8+
- Streamlit
- pandas, mlxtend, pickle

Instalar con:

```bash
pip install -r app/requirements.txt
```

---

### ▶️ Ejecutar la app localmente

```bash
cd app
streamlit run market_basket_nav_app.py
```

---

### 🌐 Despliegue automático (Render)

Este proyecto está preparado para Render.com. Al hacer push a GitHub, se redeploya automáticamente con:

```bash
streamlit run app/market_basket_nav_app.py --server.port=$PORT --server.address=0.0.0.0
```