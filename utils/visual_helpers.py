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
    fig = px.bar(
        df,
        x='Invoice_Date',
        y='Transaction_Count',
        orientation='v',
        text='Transaction_Count'
    )
    fig.update_traces(
        textposition='outside',
        marker_color='darkorange',
        textfont_color='white'
    )
    fig.update_layout(
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis_title='Cantidad de Transacciones',
        yaxis_title='Mes',
        yaxis=dict(showgrid=False, tickfont=dict(size=11)),
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

def mostrar_ejemplo_canasta(df):
    st.write("Transacción N°:", df['Invoice'].iloc[0])
    st.dataframe(df[['Description', 'Quantity', 'InvoiceDate']], use_container_width=True)
