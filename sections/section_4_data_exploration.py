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

    st.title("📊 Exploración de Datos")

    st.markdown("""
    `Fuente de datos:`  
    Dataset Online Retail II de la UCI Machine Learning Repository.
    """)
    # ◯ Mostrar dataset general
    st.markdown("---")
    st.subheader("`🧾 Vista general del dataset`")
    st.markdown("""
    Incluye transacciones realizadas en una Tienda Online entre 2009 y 2011.
    """)
    st.dataframe(dataset_sample)

    mostrar_top_10_productos(Top_10_Mas_Vendidos)
    mostrar_ejemplo_canasta(example_basket)
    mostrar_transacciones_por_mes(monthly_transactions)