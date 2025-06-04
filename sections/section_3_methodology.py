# ◯ SECTION 3 – METODOLOGÍA
# Objetivo:
#   Describir el origen del dataset, el enfoque metodológico y los parámetros utilizados para generar las reglas de asociación.
# Contenido:
#   - Fuente del dataset y contexto comercial
#   - Algoritmo utilizado (Apriori)
#   - Biblioteca empleada (mlxtend)
#   - Parámetros clave del modelo: combinación máxima y soporte mínimo

import streamlit as st
from utils.visual_helpers import mostrar_matriz_binaria




# ◯ Sección 3: METODOLOGIA DE ANALISIS
# -----------------------------------------------------------------------------------------------------------------

def show_section_3_methodology(matriz_binaria):  # Funcion que muestra la sección de metodología del análisis, describiendo el origen del dataset, el enfoque metodológico y los parámetros utilizados.
    st.title("🧪 Metodología")

    st.markdown("""
    Este proyecto aplica **Market Basket Analysis** utilizando datos reales del dataset **Online Retail II**, que contiene más de **500.000 transacciones** de una tienda online del Reino Unido.
    """)
    
    # Formato de Tabs
    st.markdown("""
    <style>
    /* Espaciado entre tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
    }

    /* Tabs base (no seleccionadas) */
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f0f0;
        padding: 10px 20px;
        border-radius: 8px 8px 0 0;
        border: 1px solid #ccc;
        color: #333;
        font-weight: 600;
        font-size: 14px;
    }

    /* Tab activa */
    .stTabs [aria-selected="true"] {
        background-color: #ffdb99;
        color: black;
        font-weight: 800 !important;
        font-size: 18px !important;
        border-bottom: none;
        box-shadow: 0px 4px 6px rgba(60, 60, 60, 0.6); /* ← Sombra gris oscura */
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Tabs principales
    tab1, tab2, tab3, tab4 = st.tabs([
        "🟠 Limpieza y Preparación de Datos",
        "🟠 Modelo Aplicado",
        "🟠 Parámetros y Filtrado de Reglas",
        "🟠 Visualización y Resultados"
    ])
    
    with tab1:
      st.markdown("""
        🔍 Para asegurar la calidad del análisis, se realizaron los siguientes pasos de depuración:

        ✅ **Filtrado de transacciones**  
        - Se consideraron solo ventas realizadas a clientes del Reino Unido, por consistencia geográfica.  
        - Se eliminaron devoluciones (códigos de factura con `'C'`) y filas con `Quantity <= 0` o `UnitPrice <= 0`.  
        - Se excluyeron productos sin descripción o con códigos genéricos irrelevantes.  

        ✅ **Tratamiento de valores nulos**  
        - Se eliminaron filas con `CustomerID` faltante.  

        ✅ **Estandarización de texto**  
        - Se unificaron descripciones a minúsculas y se corrigieron errores comunes para mejorar la agrupación de productos.  

        ✅ **Generación de matriz binaria**  
        - Para poder aplicar el algorithmo fue necesario crear una matriz de **Factura x Producto**
        - Luego del procesamiento, su estructura es la siguiente:  
            * cada Fila es una Transacción  
            * cada Columna un Producto.  
            * El valor `1` indica que ese producto `fue comprado` en esa transacción.  
    
        Veamos mas abajo, las primeras filas de la matriz binaria centrada en los **{top_n} productos más frecuentes**.  
        """)
      mostrar_matriz_binaria(matriz_binaria, top_n=10)  # Mostrar un fragmento de la matriz binaria filtrada

    with tab2:
        st.markdown("""
        ---
        ## Modelo Aplicado

        Para detectar productos que se compran juntos frecuentemente se aplicó el algoritmo **Apriori**, implementado con la librería `mlxtend`, una biblioteca confiable de Python especializada en extensiones de aprendizaje automático.

        🧪 **Algoritmo seleccionado: Apriori**  
        - **Justificación:** fácil interpretación, buen desempeño en datasets pequeños y medianos, ideal para análisis exploratorio.  
        - Altamente efectivo para identificar *frequent itemsets* (conjuntos de ítems frecuentes) y derivar reglas de asociación, basándose en métricas predefinidas como el **support** y la **confidence**.

        ---

        ### ⚙️ Parámetros utilizados en Apriori

        | Parámetro                     | Descripción                                              | Valor         | ¿Esto asegura que...?                                                                 |
        |------------------------------|----------------------------------------------------------|---------------|----------------------------------------------------------------------------------------|
        | Maximum Combination Length   | Longitud máxima de combinación de ítems                  | 2             | Solo se consideren pares de productos, facilitando interpretaciones y decisiones.     |
        | Minimum Co-Occurrence Support| Umbral mínimo de soporte de coocurrencia                 | 0.005 (0.5%)  | Se filtren combinaciones raras, enfocándose en asociaciones realmente frecuentes.     |
        | Support                      | Frecuencia relativa de un itemset                        | ≥ 0.01        | Las reglas identificadas aparezcan en al menos el 1% de todas las transacciones.      |
        | Confidence                   | Probabilidad de co-ocurrencia dado un antecedente        | ≥ 0.2         | Las reglas sugeridas tengan una probabilidad razonable de repetirse en nuevas ventas. |
        | Lift                         | Intensidad de la relación entre dos productos            | ≥ 2           | Las asociaciones detectadas sean más fuertes que las esperadas por azar.             |

        ---

      """)

    with tab3:
      st.markdown(""" 
      ## Parametros y Filtrado de Reglas

      * Se eliminaron reglas duplicadas o reflejadas (A→B y B→A).  
      * Se priorizaron reglas con:   
        - Productos de alta frecuencia de compra   
        - Interpretación clara para el negocio  
      * Se destacaron combinaciones con potencial de **cross-selling** o **agrupamiento físico** en tienda.
      """)

    with tab4:
      st.markdown("""  
      ## Visualización y Exploración

      Las reglas y resultados se presentan mediante:

      - 📊 Tablas ordenadas por métricas clave  
      - 🧠 Interpretaciones automáticas
      - 🔗 Redes de co-ocurrencia  
      - 🧯 Heatmap cruzado entre productos  

      > Todo se organiza en una interfaz amigable para el análisis por parte del usuario final.
    """)