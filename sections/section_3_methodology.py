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
      
      
      .stTabs [data-baseweb="tab-list"] {
      overflow-x: auto !important;      /* permite scroll horizontal */
      white-space: nowrap;              /* evita que se bajen de línea */
      display: flex;                    /* asegura que se alineen horizontalmente */
      flex-wrap: nowrap;                /* evita que se acomoden en más de una línea */
      scrollbar-width: thin;            /* (opcional) scroll más fino en Firefox */
      }

      
      /* Scrollbar para navegadores WebKit (Chrome, Edge, Safari) */
      .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
          height: 6px;                      /* altura de la barra de scroll */
      }
      .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar-thumb {
          background-color: #aaa;           /* color del "pulgar" del scroll */
          border-radius: 4px;               /* bordes redondeados para estética */
      }
      
      .stTabs [data-baseweb="tab"] {
          background-color: #f0f0f0;
          padding: 8px 16px;
          border-radius: 8px 8px 0 0;
          font-weight: bold;
          color: #333333;
          border: 1px solid #ccc;
      }
      .stTabs [aria-selected="true"] {
          background-color: #ffdb99;
          box-shadow: 0px 4px 6px rgba(60, 60, 60, 0.6);
          color: black;
          font-weight: 800 !important;
          font-size: 16px !important;
          border-bottom: none;
      }
      </style>
      """, unsafe_allow_html=True)
    
    # Tabs principales
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🟠 Limpieza y Preparación de Datos",
        "🟠 Modelo Aplicado",
        "🟠 Parámetros y Filtrado de Reglas",
        "🟠 Visualización y Resultados",
        "🟠 Glosario de Métricas"
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
      
      
    with tab5:    # SECTION 8 – GLOSARIO DE MÉTRICAS
                  # Objetivo:
                  #   Proporcionar definiciones claras y fórmulas clave de las métricas utilizadas en el análisis de reglas de asociación.
                  # Contenido:
                  #   - Definiciones de Support, Confidence, Lift, Leverage y Conviction
                  #   - Ejemplos de fórmulas aplicadas
                  #   - Explicaciones orientadas a usuarios de negocio no técnicos
           
      st.subheader("📏 Glosario de Métricas")

      st.markdown("""
      **:orange[Support]**  
      The proportion of transactions that contain a specific itemset. High support values indicate that the itemset is frequently purchased together.

      - *Item Support:*  
      `Support(A) = Transactions containing A / Total number of transactions`

      - *Co-occurrence Support:*  
      `Support(A ∪ B) = Transactions containing both A and B / Total number of transactions`


      **:orange[Confidence]**    
      The conditional probability that a transaction containing item A will also contain item B.

      - `Confidence(A → B) = Support(A ∪ B) / Support(A) × 100%`  
      - `Confidence(B → A) = Support(A ∪ B) / Support(B) × 100%`


      **:orange[Lift]**  
      Indicates how much more likely item B is purchased when item A is purchased, compared to when item B is purchased independently.

      - `Lift(A → B) = Support(A ∪ B) / (Support(A) × Support(B))`


      **:orange[Leverage]**  
      Measures how much more often A and B occur together than expected if they were independent.

      - `Leverage(A → B) = Support(A ∪ B) − (Support(A) × Support(B))`


      **:orange[Conviction]**  
      Indicates the strength of implication in the rule. High values (>1) suggest stronger dependency.

      - `Conviction(A → B) = (1 − Support(B)) / (1 − Confidence(A → B))`  
      - `Conviction(B → A) = (1 − Support(A)) / (1 − Confidence(B → A))`
      """)
      
