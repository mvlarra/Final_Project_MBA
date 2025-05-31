# ◯ Sección 2: RESUMEN DEL PROYECTO
# ............................................................................................
# Objetivo:
#   Presentar un resumen ejecutivo del análisis realizado, destacando el propósito del proyecto, el origen de los datos,
#   la metodología aplicada y los principales hallazgos obtenidos.
# Contenido:
#   - Objetivo del análisis y foco comercial
#   - Fuente y características del dataset utilizado
#   - Metodología empleada (Apriori, métricas de asociación)
#   - Hallazgos destacados y ejemplos de reglas obtenidas
#   - Recomendaciones accionables para el negocio
#   - Tecnologías y herramientas utilizadas en el desarrollo

import streamlit as st

# 2. ◯ Sección: RESUMEN DEL PROYECTO
# ............................................................................................

def show_section_2_summary():   # Función para mostrar la sección 2: Resumen del Proyecto
    
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