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
     
  # ◯ Tabs antes del título     
       
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
    tab1, tab2, tab3 = st.tabs([
        "🟠 Modelo Aplicado",
        "🟠 Preprocesamiento de Datos",
        "🟠 Glosario de Métricas"
    ])


    with tab1:
      st.markdown("""
        ---
        ## **Algoritmo Apriori** 
        
        ### ¿Qué es Apriori?
        Apriori es un algoritmo de `Minería de Datos` utilizado para descubrir `Reglas de Asociación` en grandes conjuntos de datos.  
        Se basa en el principio de que si un conjunto de productos es frecuente, entonces todos sus subconjuntos también deben serlo.  
        Esto permite identificar combinaciones de productos que se compran juntos con frecuencia, lo que es especialmente útil en el sector retail.

                     
        ### ¿Por qué Apriori?
        - **Eficiencia:** diseñado para trabajar con grandes conjuntos de datos, identificando patrones de compra comunes.
        - **Interpretabilidad:** genera reglas de asociación fáciles de entender, lo que permite a los analistas y gerentes tomar decisiones informadas.
        - **Flexibilidad:** permite ajustar parámetros como soporte y confianza para adaptarse a diferentes necesidades comerciales.

   
        ### Contexto Comercial  
        En el contexto del retail, Apriori se utiliza para analizar transacciones de ventas y descubrir patrones de compra.  
        Por ejemplo, puede identificar que los clientes que compran pan también tienden a comprar manteca, lo que sugiere una asociación entre estos productos.   
        Esta información puede ser utilizada para mejorar la disposición de los productos en tienda, ofrecer promociones cruzadas o personalizar las recomendaciones de productos a los clientes.
       
         
        ### ¿Cómo se implementa?
        El algoritmo Apriori se implementa en Python utilizando la librería `mlxtend`, que proporciona una interfaz sencilla para aplicar el algoritmo a conjuntos de datos de transacciones.   
        A continuación, se describen los pasos clave del proceso:
        1. **Carga de datos:** se cargan las transacciones de ventas en un formato adecuado para el análisis.
        2. **Preprocesamiento:** se transforma el conjunto de datos en una `matriz binaria` donde cada fila representa una transacción y cada columna un producto, con valores de 1 o 0 indicando si el producto fue comprado o no.
        3. **Aplicación del algoritmo:** se aplica el algoritmo Apriori para identificar combinaciones frecuentes de productos, utilizando los parámetros definidos.
        4. **Generación de reglas de asociación:** a partir de las combinaciones frecuentes, se generan reglas de asociación que indican la probabilidad de que un producto sea comprado dado otro producto.        
        5. **Evaluación de reglas:** se evalúan las reglas generadas utilizando métricas como soporte, confianza y lift para identificar las más relevantes y útiles para el negocio.
        
        
        ### Parámetros del Algoritmo
        - **Maximum Combination Length:** define la longitud máxima de las combinaciones de productos a considerar. 
            👉🏻 En nuestro caso fijaremos este parametro en 2, con el fin de considerar unicamente pares de productos, para facilitar la interpretaciones y la toma de decisiones.
        - **Minimum Co-Occurrence Support:** establece un umbral mínimo de soporte para filtrar combinaciones raras, asegurando que solo se consideren asociaciones significativas.       
            👉🏻 En nuestro caso lo definimos en 0.005 para enfocarnos en asociaciones realmente frecuentes, descartando asociaciones raras.
        - **Support:** mide la frecuencia relativa de un conjunto de productos en las transacciones, ayudando a identificar asociaciones comunes
            👉🏻 En nuestro caso es definido en ≥ 0.01, asegurando que las reglas identificadas aparezcan en al menos el 1% de todas las transacciones, garantizando relevancia.
        - **Confidence:** indica la probabilidad de que un producto sea comprado dado otro producto, lo que ayuda a evaluar la fuerza de la asociación.
            👉🏻 En nuestro caso lo fijamos en ≥ 0.2, asegurando que las reglas sugeridas tengan una probabilidad razonable de repetirse en nuevas ventas.
        - **Lift:** mide la intensidad de la relación entre dos productos, comparando la probabilidad de que se compren juntos con la probabilidad de que se compren independientemente.
            👉🏻 En nuestro caso lo fijamos en ≥ 2, asegurando que las asociaciones detectadas sean más fuertes que las esperadas por azar, lo que indica una relación significativa entre los productos.
        - **Leverage:** mide la diferencia entre la probabilidad de que dos productos se compren juntos y la probabilidad de que se compren independientemente, ayudando a identificar asociaciones significativas.    
     
             
        ### Ejemplo de Regla de Asociación
        A continuación, se muestra un ejemplo de una regla de asociación generada por el algoritmo Apriori:
        - **Regla:** Si un cliente compra `Pan`, entonces es probable que también compre `Manteca`.
        - **Soporte:** 0.05 (5% de las transacciones contienen ambos productos)
        - **Confianza:** 0.8 (80% de las transacciones que contienen Pan también contienen Manteca)
        - **Lift:** 2.5 (la probabilidad de comprar Manteca es 2.5 veces mayor cuando se compra Pan)
        - **Interpretación:** Esta regla sugiere que los clientes que compran Pan tienen una alta probabilidad de comprar Manteca, lo que puede ser utilizado para mejorar la disposición de los productos en tienda o para ofrecer promociones cruzadas.

      
          
        ### Resultados esperados
        - **Identificación de patrones de compra:** se espera descubrir combinaciones de productos que los clientes compran juntos con frecuencia, lo que permite a la empresa optimizar su estrategia de ventas.
        - **Mejora de la experiencia del cliente:** al entender qué productos se compran juntos, la empresa puede ofrecer recomendaciones personalizadas y mejorar la disposición de los productos en tienda.
        - **Oportunidades de ventas cruzadas:** se espera identificar oportunidades para aumentar las ventas mediante la promoción de `Productos Complementarios`, lo que puede mejorar la rentabilidad y la satisfacción del cliente.

            
        ### Conclusión
        El algoritmo Apriori es una herramienta poderosa para descubrir patrones de compra en retail, permitiendo a las empresas identificar oportunidades de ventas cruzadas y mejorar la experiencia del cliente.  
        Su capacidad para generar reglas de asociación claras y significativas lo convierte en una opción ideal para el análisis de datos de ventas.

        ---

      """)

      st.markdown(""" 
        ### Reglas Seleccionadas
        
        Las reglas de asociación se filtraron y priorizaron de la siguiente manera:
        * Se eliminaron reglas duplicadas o reflejadas (A→B y B→A).  
        * Se priorizaron reglas con:   
          - Productos de alta frecuencia de compra   
          - Interpretación clara para el negocio  
        * Se destacaron combinaciones con potencial de **cross-selling** o **agrupamiento físico** en tienda.
      """)

    
    with tab2:
      st.markdown("---")    
      st.markdown("""
        ## Procesamiento de los Datos
        Para asegurar la calidad del análisis, se realizaron los siguientes pasos de depuración:

        ### Filtrado de transacciones:
          - Se consideraron solo ventas realizadas a clientes del Reino Unido, por consistencia geográfica.  
          - Se eliminaron devoluciones (códigos de factura con `'C'`) y filas con `Quantity <= 0` o `UnitPrice <= 0`.  
          - Se excluyeron productos sin descripción o con códigos genéricos irrelevantes.  

        ### Tratamiento de valores nulos:
          - Se eliminaron filas con `CustomerID` faltante.  

        ### Estandarización de texto:
          - Se unificaron descripciones a minúsculas y se corrigieron errores comunes para mejorar la agrupación de productos.  

        ### Generación de matriz binaria:
          - Para poder aplicar el algorithmo fue necesario crear una matriz de `Factura x Producto`.
          - Luego del procesamiento, la estructura de la matriz es la siguiente:  
              * cada Fila representa una Transacción  
              * cada Columna representa Producto.  
              * El valor `1` indica que ese producto `fue comprado` en esa transacción.  
    
        Veamos mas abajo, la matriz binaria enfocandonos, por ejemplo, en los 10 productos más frecuentes  
        """)
      mostrar_matriz_binaria(matriz_binaria, top_n=10)  # Mostrar un fragmento de la matriz binaria filtrada




    with tab3:    # SECTION 8 – GLOSARIO DE MÉTRICAS
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
      
      
