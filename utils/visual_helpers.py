# tres funciones reutilizables para:

    # Mostrar el gráfico de top 10 productos más vendidos.

    # Visualizar transacciones por mes.

    # Presentar un ejemplo de canasta de compra.



import streamlit as st
import plotly.express as px

def mostrar_top_10_productos(Top_10_Mas_Vendidos):
    """
    Visualiza el Top 10 de productos más vendidos con gráfico de barras horizontal
    y una tabla expandible con el detalle de unidades vendidas.
    """
    st.markdown("---")
    st.subheader("`🏆 Top 10 productos más vendidos`")
    st.markdown("""
    Esta visualización muestra los 10 productos con mayor cantidad de unidades vendidas en el periodo analizado. 
    Puede ayudarte a identificar tus **productos estrella** o con mayor rotación.
    """)

    # Ordenar explícitamente de mayor a menor por cantidad
    Top_10_Mas_Vendidos_sorted = Top_10_Mas_Vendidos.sort_values('Unidades Vendidas', ascending=True)

    # Crear gráfico de barras horizontal
    fig = px.bar(
        Top_10_Mas_Vendidos_sorted,
        x='Unidades Vendidas',
        y='Producto',
        orientation='h',
        text='Unidades Vendidas',
        title=''
    )

    # Ajustar estilo del gráfico
    fig.update_traces(
        textposition='outside',
        marker_color='darkorange'
    )

    fig.update_layout(
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis_title='Unidades Vendidas',
        yaxis_title='Producto',
        yaxis=dict(tickfont=dict(size=11)),
        height=400
    )

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar tabla con cantidades en expander
    with st.expander("Ver detalle en tabla"):
        st.dataframe(Top_10_Mas_Vendidos, use_container_width=True)

def mostrar_transacciones_por_mes(df):
    """
    Visualiza la cantidad de transacciones por mes con un gráfico de barras.
    El DataFrame debe contener las columnas 'Invoice_Date' y 'Transaction_Count'.
    """
    st.markdown("---")
    st.subheader("📅 Transacciones por Mes")
    st.markdown("""
    Este gráfico muestra la cantidad de transacciones realizadas cada mes, 
    lo que permite identificar patrones estacionales y tendencias de compra.
    """)

    fig = px.bar(
        df,
        x='Invoice_Date',
        y='Transaction_Count',
        text='Transaction_Count',
        color_discrete_sequence=['darkorange']
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title='Mes',
        yaxis_title='Cantidad de Transacciones',
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Ver detalle en tabla"):
        st.dataframe(df, use_container_width=True)


def mostrar_ejemplo_canasta(df):
    """
    Muestra un ejemplo detallado de una canasta de compra.
    """
    st.markdown("---")
    st.subheader("🛒 Ejemplo de Canasta de Compra")
    st.markdown("""
    A continuación se presenta un ejemplo real de una canasta de compra, 
    detallando los productos adquiridos en una transacción específica.
    """)

    st.dataframe(df, use_container_width=True)
    
    
def mostrar_matriz_binaria(df_binaria, top_n=10):
    """
    Muestra un fragmento filtrado de la matriz binaria (Factura × Producto),
    destacando las columnas más relevantes (más compradas).
    """
    st.markdown("---")
    st.markdown("🧾 Ejemplo de Matriz Binaria")

    # Eliminar columnas no relevantes
    df_binaria = df_binaria.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], errors='ignore')

    # Obtener los productos más frecuentes
    top_columns = df_binaria.sum().sort_values(ascending=False).head(top_n).index

    # Filtrar filas que contengan al menos un '1' en esos productos
    df_filtrada = df_binaria[df_binaria[top_columns].sum(axis=1) > 0]

    # Mostrar las primeras filas filtradas
    st.dataframe(df_filtrada[top_columns].head(15), use_container_width=True)