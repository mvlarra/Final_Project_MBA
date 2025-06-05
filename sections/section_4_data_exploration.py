# ◯ SECTION 4 – EXPLORACIÓN DE DATOS
# Objetivo:
#   Realizar una primera aproximación visual al dataset para comprender su estructura y contenido.
# Contenido:
#   - Vista general del dataset original
#   - Productos más vendidos
#   - Ejemplo real de una transacción
#   - Distribución mensual de transacciones

import streamlit as st

# ◯ Sección 4: EXPLORACIÓN DE DATOS
# ............................................................................................



from utils.visual_helpers import (
    mostrar_top_10_productos,
    mostrar_transacciones_por_mes,
    mostrar_ejemplo_canasta
)

def show_section_4(dataset_sample, Top_10_Mas_Vendidos, example_basket, monthly_transactions):
    """
    Muestra la sección de exploración de datos con visualizaciones y ejemplos.
    
    :param dataset_sample: DataFrame con una muestra del dataset original.
    :param Top_10_Mas_Vendidos: DataFrame con el top 10 de productos más vendidos.
    :param example_basket: DataFrame con un ejemplo de canasta de compra.
    :param monthly_transactions: DataFrame con transacciones por mes.
    """
  # ◯ Tabs antes del título 
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
   
    
    tab1, tab2, tab3, tab4 = st.tabs([
    "🟠 Vista general del dataset", 
    "🟠 Productos más vendidos", 
    "🟠 Ejemplo de una transacción", 
    "🟠 Distribución mensual"
    ])
    
    
    # Tabs principales 
  

    
    with tab1:          # ◯ Mostrar dataset general
        st.markdown("---")
        st.subheader("`🧾 Vista general del dataset`")
        st.markdown("""
        Incluye transacciones realizadas en una Tienda Online entre 2009 y 2011.
        """)
        st.dataframe(dataset_sample)

    with tab2:          # ◯ Mostrar top 10 productos más vendidos
        mostrar_top_10_productos(Top_10_Mas_Vendidos)
        
    with tab3:          # ◯ Mostrar ejemplo de canasta de compra    
        mostrar_ejemplo_canasta(example_basket)      
        # footer:
        st.markdown(f"""
        {"<div style='font-size:12px;color:gray;margin-top:10px;'>ℹ️ Esta sección muestra datos crudos no transformados con nombres de productos traducidos para facilitar su interpretación.</div>"}
        """, unsafe_allow_html=True)
        
    with tab4:          # ◯ Mostrar transacciones por mes   
        mostrar_transacciones_por_mes(monthly_transactions)