# ◯ SECCIÓN 1 – ACERCA DEL PROYECTO
# Objetivo:
#   Presentar el propósito general del proyecto, su contexto, el objetivo del análisis y los créditos.
# Contenido:
#   - Objetivo del análisis
#   - Tecnologías utilizadas
#   - Recursos y vínculos
#   - Contacto profesional

import streamlit as st


# 1. ◯ New Sección: ACERCAS DEL PROYECTO (Unificar Sección 1 (Resumen) y Sección 9 (Créditos))
# ............................................................................................
def show_section_1_about():
    # .........................................................................
    # Función para mostrar la sección 1: Acerca del Proyecto
    # Contenido: Objetivo, tecnologías utilizadas, recursos, contacto
    # .........................................................................
    
    st.markdown("# 📘 Acerca del Proyecto:   Market Basket Analysis")

    st.markdown("""
    Este proyecto fue desarrollado como parte del **Bootcamp de Data Science & Machine Learning en 4Geeks Academy**, por **Valentina Larrañaga**.
    Busca transformar datos transaccionales en estrategias accionables para retail, aplicando Market Basket Analysis con reglas de asociación.
    """)
    
    st.markdown("---")
    st.markdown("### 🔎 Enfoque del análisis")
    st.markdown("""
    El recorrido de la app está organizado de forma progresiva: Va desde la exploración de los datos hasta las recomendaciones estratégicas.
    ```
    📦 Datos de Transacciones → 📊Exploracion de los Datos → 🔎 Reglas de Asociación → 🧠 Recomendaciones Personalizadas → 💼 Acciones Estratégicas
    ```
    """)
           
    st.markdown("---")
    st.markdown("### 🎯 Objetivos Especificos")
    st.markdown("""
    Identificar patrones de compra frecuentes y generar recomendaciones accionables para mejorar la estrategia comercial.

    **`1. Descubrimiento de Reglas de Asociación`**  
    Identificar asociaciones y correlaciones entre productos o artículos en un conjunto de datos. Descubrir reglas que indiquen la probabilidad de que ciertos artículos se compren juntos.

    **`2. Oportunidades de Venta Cruzada`**  
    Detectar oportunidades de venta cruzada comprendiendo qué productos se compran frecuentemente en conjunto.

    **`3. Planificación de Promociones`**  
    Optimizar campañas promocionales identificando artículos que suelen comprarse juntos. Diseñar promociones y descuentos efectivos para incentivar la compra de productos complementarios.

    **`4. Ubicación Estratégica de Productos`**  
    Organizar los productos en la tienda física o en línea de forma que se fomente la compra de artículos relacionados, creando una experiencia de compra más conveniente y satisfactoria.
    """)

    st.markdown("---")
    st.markdown("### 🚀 Tecnologías utilizadas")
    st.markdown("""
    - Python · pandas · numpy  
    - mlxtend (reglas de asociación)  
    - plotly · matplotlib  
    - Streamlit  
    - GitHub Codespaces
    - **Render (despliegue en la nube)**
    """)
    
    st.markdown("---")
    st.markdown("### 🌐 Recursos")
    st.markdown("""
    - Código fuente: [GitHub del proyecto](https://github.com/mvlarra/Final_Project_MBA)  
    - Dataset: Online Retail Dataset (UCI / Kaggle)  
    - App en vivo: (📎 https://market-basket-analysis-xb0x.onrender.com/)
    """)

    st.markdown("---")
    st.markdown("### 📫 Contacto")
    st.markdown("""
    - [LinkedIn](https://www.linkedin.com/in/valentinalarra)  
    - [GitHub](https://github.com/mvlarra)
    """)