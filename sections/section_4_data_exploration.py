# ◯ SECTION 4 – EXPLORACIÓN DE DATOS
# Objetivo:
#   Realizar una primera aproximación visual al dataset para comprender su estructura y contenido.
# Contenido:
#   - Vista general del dataset original
#   - Productos más vendidos
#   - Ejemplo real de una transacción
#   - Distribución mensual de transacciones

import streamlit as st
from utils.footer import footer_reglas_asociacion, footer_red_productos, footer_heatmap, footer_recomendaciones_carrito, footer_canasta_real

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

    st.title("📊 Exploración de Datos")
    
    st.markdown("""
    Esta sección permite realizar una primera aproximación visual al dataset para comprender su estructura y contenido.
    El objetivo es familiarizarse con los datos antes de aplicar técnicas de análisis más avanzadas.
    Luego procederemos a trabajar en la limipieza y el procesamiento de los datos. 
    Pasos Claves para asegurar un análisis efectivo y sin ruidos. 
    """)
    
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
   
    
    tab1, tab2, tab3, tab4 = st.tabs([
    "🟠 Vista general del dataset", 
    "🟠 Productos más vendidos", 
    "🟠 Ejemplo de una transacción", 
    "🟠 Distribución mensual"
    ])

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
        footer_canasta_real()        
    
    with tab4:          # ◯ Mostrar transacciones por mes   
        mostrar_transacciones_por_mes(monthly_transactions)