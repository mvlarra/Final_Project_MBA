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

def show_section_3_methodology():  # Funcion que muestra la sección de metodología del análisis, describiendo el origen del dataset, el enfoque metodológico y los parámetros utilizados.
    st.title("🧪 Metodología")

    tab2, tab3 =  st.tabs([
        "🧪 Versión enriquecida (detallada)",
        "📄 Versión técnica (para README)",
    ])

    with tab2:
        st.markdown("""
        ## 🧪 Metodología Detallada

        Este proyecto aplica **Market Basket Analysis** (Análisis de Canasta de Compras) utilizando datos reales del dataset **Online Retail II**, que contiene más de **500.000 transacciones** de una tienda online del Reino Unido.

        ---

        ### 📁 1. Limpieza y Preparación de Datos

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
        - Se creó una matriz **Factura x Producto** con valores `1` si un producto fue comprado en esa transacción.

        ---

        ### 📈 2. Algoritmo de Reglas de Asociación

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
        | Confidence                   | Probabilidad de co-ocurrencia dado un antecedente       | ≥ 0.2         | Las reglas sugeridas tengan una probabilidad razonable de repetirse en nuevas ventas. |
        | Lift                         | Intensidad de la relación entre dos productos            | ≥ 2           | Las asociaciones detectadas sean más fuertes que las esperadas por azar.             |

        📌 También se calculó **Conviction**, aunque no se priorizó en la visualización.

        ---

        ### 🧹 3. Filtrado de Reglas

        🔁 Se eliminaron reglas duplicadas o reflejadas (A→B y B→A).  
        📊 Se priorizaron reglas con:   
            - Productos de alta frecuencia de compra   
            - Interpretación clara para el negocio  
        🧺 Se destacaron combinaciones con potencial de **cross-selling** o **agrupamiento físico** en tienda.

        ---

        ### 📈 4. Visualización y Exploración

        Las reglas y resultados se presentan mediante:

        - 📊 Tablas ordenadas por métricas clave  
        - 🧠 Interpretaciones automáticas por producto  
        - 🔗 Redes de co-ocurrencia  
        - 🧯 Heatmap cruzado entre productos  

        > Todo se organiza en una interfaz amigable para el análisis por parte del usuario final.
        """)

    with tab3:
        st.markdown("""
        ## 🧪 Methodology (README Style)

        This project applies Market Basket Analysis using real-world transaction data from the [Online Retail II dataset](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci), which contains over 500,000 purchases from a UK-based e-commerce wholesaler.

        ### 1. Data Cleaning & Preparation

        - Filtered only **transactions from the United Kingdom**.
        - Removed:
          - Cancellations (InvoiceNo starting with 'C')
          - Negative quantities or unit prices
          - Rows with missing `CustomerID` or empty `Description`
        - Standardized product descriptions (lowercase, trimming, typo cleaning)
        - Built a **binary basket matrix** (`Invoice x Product`) for algorithm input

        ### 2. Algorithm & Implementation

        - Used **Apriori algorithm** (`mlxtend` library)
        - Parameters:
          - `min_support`: 0.01
          - `min_confidence`: 0.2
          - `lift threshold`: 2.0
        - All itemsets and rules were filtered based on their business value and clarity.

        ### 3. Metrics Used

        | Metric      | Meaning                                                |
        |-------------|--------------------------------------------------------|
        | `Support`   | Frequency of co-occurrence in the dataset              |
        | `Confidence`| Likelihood of product B being purchased given A        |
        | `Lift`      | Strength of association compared to random occurrence |

        Other metrics (e.g., `Conviction`, `Leverage`) were computed but not prioritized in the main interface.

        ### 4. Business Logic

        Rules were filtered and ranked by:
        - Relevance to high-frequency products
        - Interpretability and usefulness for **cross-selling**
        - Elimination of mirrored or redundant rules

        ### 5. Visualization Strategy

        The app presents insights via:
        - Rule tables with interactive filtering
        - Association graphs (network of co-occurrences)
        - Cross-product heatmaps
        - Contextual recommendations based on real baskets
        """)