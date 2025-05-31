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