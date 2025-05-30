# ◯ SECCIÓN 2 – EXPLORACIÓN DE DATOS
# Objetivo:
#   Presentar una visión general del comportamiento de las transacciones y los productos más vendidos.
# Contenido:
#   - Distribución de transacciones por mes
#   - Productos más vendidos
#   - Canasta de compra real (ejemplo individual)

import streamlit as st

# 2. ◯ Sección: RESUMEN DEL PROYECTO
# ............................................................................................

st.title("🛒 Market Basket Analysis")
st.subheader("Resumen Final del Proyecto")

st.markdown("""
**📌 Objetivo**  
Identificar productos que suelen comprarse juntos en transacciones de retail, para descubrir patrones útiles en estrategias de venta cruzada, bundles, optimización de layout y recomendaciones personalizadas.

---

**📂 Dataset**  
- **Fuente:** Online Retail II — UCI Machine Learning Repository  
- **Período:** Diciembre 2009 a Diciembre 2011  
- **Alcance:** Transacciones de clientes del Reino Unido  
- **Preprocesamiento:** Filtrado de ventas válidas, eliminación de cancelaciones y valores nulos

---

**⚙️ Metodología**  
- Transformación de los datos a formato canasta (ítems × transacciones)  
- Aplicación del algoritmo **`Apriori`** con la librería `mlxtend`  
- Evaluación de reglas utilizando las siguientes métricas:  
    - **`Support:`** Frecuencia del conjunto  
    - **`Confidence:`** Probabilidad de ocurrencia conjunta  
    - **`Lift:`** Fuerza de la asociación

---

**🏆 Principales Hallazgos**  
- Se detectaron asociaciones sólidas entre variantes de productos (ej. distintos colores de juegos de té)  
- Las reglas más destacadas obtuvieron altos valores en todas las métricas:  
    - Confianza por encima del 70%  
    - Lift superior a 20  
- Estas reglas son altamente accionables para estrategias de marketing y experiencia de usuario

---

**✅ Recomendaciones de Negocio**  
- Implementar **`sugerencias automáticas de productos`** en el carrito de compras  
- Ofrecer **`bundles`** basados en productos frecuentemente comprados juntos  
- Optimizar la **`disposición de productos`** en tienda física u online  
- Lanzar **`campañas segmentadas`** basadas en afinidades entre productos

---

**🔧 Herramientas y Tecnologías**  
+ Python · pandas · mlxtend · Streamlit  
+ Visualización con plotly y matplotlib  
+ Diseño modular con navegación lateral e insights interpretables

---

Esta app fue desarrollada como el **proyecto final del Bootcamp de Data Science**, demostrando habilidades de punta a punta: desde la preparación de datos y detección de patrones, hasta la generación de insights de negocio y desarrollo de una aplicación funcional.
""")