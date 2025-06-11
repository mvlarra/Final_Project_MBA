# 🛒 Market Basket Analysis

### Proyecto final — Bootcamp Data Science & Machine Learning (4Geeks Academy)

Desarrollado por: **Valentina Larrañaga**  
App interactiva: [🔗 Ver app en vivo](https://market-basket-analysis-xb0x.onrender.com/)  
Repositorio GitHub: [📁 Ir al repositorio](https://github.com/mvlarra/Final_Project_MBA)

---

## 🎯 Objetivo del proyecto

Aplicar técnicas de Market Basket Analysis (análisis de canasta de productos) para detectar patrones de compra frecuentes, generar recomendaciones accionables y proponer estrategias comerciales que aumenten el ticket promedio y la rentabilidad.

---

## 🔎 Metodología aplicada

- Dataset real de transacciones online (UK, 2010–2011)
- Algoritmo: **Apriori** (librería `mlxtend`)
- Generación de matriz binaria `transacción × producto`
- Filtros: soporte ≥ 1%, confianza ≥ 20%, lift ≥ 2
- Evaluación de reglas mediante métricas: support, confidence, lift, leverage, conviction

---

## 📊 Exploración de Datos

Se realiza una visualización inicial del dataset, destacando:

- Top 10 productos más vendidos
- Ejemplo real de una transacción (canasta)
- Distribución mensual de compras

![Exploración de Datos](docs/img/exploracion.png)

---

## 🔗 Reglas de Asociación

Reglas generadas con Apriori que revelan relaciones frecuentes entre productos.  
Se pueden explorar en tabla, grafo de red o heatmap cruzado.

![Reglas](docs/img/reglas.png)

---

## 🛍️ Recomendaciones por Producto

Exploración interactiva para cada producto:

- Productos recomendados según reglas frecuentes
- Relevancia medida por lift y confianza
- Ejemplo de recomendaciones tipo “quienes compraron esto, también compraron...”

![Recomendaciones](docs/img/recomendaciones.png)

---

## 📌 Heatmap de Producto

Visualización que muestra, para un producto base, la intensidad de asociación con otros productos según soporte, confianza o lift.

![Heatmap](docs/img/heatmap.png)

---

## 💼 Acciones Estratégicas para el Negocio

A partir de las reglas descubiertas se sugieren acciones como:

- Creación de bundles
- Promociones cruzadas
- Recomendaciones personalizadas
- Optimización de layout en tienda o web
- Capacitación del equipo de ventas

![Acciones](docs/img/acciones.png)

---

## 📋 Conclusiones y aprendizajes

- Se detectaron reglas con confianza > 70% y lift > 20
- Se identificaron combinaciones clave para ventas cruzadas
- Se propusieron acciones estratégicas segmentadas por tipo de métrica
- Se desarrolló una app interactiva reutilizable para gerentes de negocio

![Conclusiones](docs/img/conclusiones.png)

---

## 🧰 Tecnologías utilizadas

- Python (Pandas, NumPy, Scikit-learn, mlxtend)
- Visualización: Plotly, Matplotlib, Seaborn
- App: Streamlit
- Entorno: Docker + Codespaces (devcontainer.json)
- Despliegue: Render

---

## 🌐 Enlaces relevantes

- [🔗 App en vivo en Render](https://market-basket-analysis-xb0x.onrender.com/)
- [📁 Repositorio GitHub](https://github.com/mvlarra/Final_Project_MBA)

---

© 2025 — Valentina Larrañaga

