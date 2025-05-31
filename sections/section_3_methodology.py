# ◯ SECTION 3 – METODOLOGÍA
# Objetivo:
#   Describir el origen del dataset, el enfoque metodológico y los parámetros utilizados para generar las reglas de asociación.
# Contenido:
#   - Fuente del dataset y contexto comercial
#   - Algoritmo utilizado (Apriori)
#   - Biblioteca empleada (mlxtend)
#   - Parámetros clave del modelo: combinación máxima y soporte mínimo

import streamlit as st

# ◯ Sección 3: METODOLOGIA DE ANALISIS
# -----------------------------------------------------------------------------------------------------------------

st.title("🧪 Metodología del Análisis")

st.markdown("""
Los datos utilizados provienen del dataset 'Online Retail II'.

- Este conjunto de datos abarca todas las transacciones realizadas por un minorista en línea del Reino Unido (registrado y sin tienda física), desde el 1 de diciembre de 2009 hasta el 9 de diciembre de 2011.
- La empresa se especializa en la venta de artículos de regalo distintivos para diversas ocasiones.

Para llevar a cabo el análisis de Market Basket se utiliza:

- El `Apriori Algorithm`, altamente efectivo para identificar `frequent itemsets` (conjuntos de ítems frecuentes) y derivar reglas de asociación, basándose en métricas predefinidas como el support y la confidence.
- Para ejecutar el algoritmo Apriori, se emplea la `mlxtend library`, una biblioteca confiable de Python especializada en extensiones de aprendizaje automático.

Los siguientes parámetros fueron configurados para el algoritmo:

- **`Maximum Combination Length:`**  
Se establece una longitud máxima de combinación de 2 ítems. Esta decisión permite enfocarse en pares de productos, favoreciendo un análisis más específico de coocurrencias.

- **`Minimum Co-Occurrence Support Threshold:`**  
Se define un umbral mínimo de soporte de coocurrencia del 0.5%. Esto asegura que solo se consideren asociaciones con una presencia significativa en el dataset.
""")