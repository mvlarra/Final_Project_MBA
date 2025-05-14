# Este será el archivo principal de navegación de tu app Streamlit. 
# Render lo usará como punto de inicio.
# ¿Qué debe contener ese archivo?
    # Como ya trabajaste todos los pasos dentro del notebook market_basket_analysis_VL.ipynb, 
    # lo ideal es que vayamos trasladando las partes clave al archivo .py, empezando 
    # por la sección Summary Report que querés mostrar primero.

# Puedo ayudarte a construirlo, sección por sección, con:
    # Encabezado
    # Sidebar (si querés navegación)
    # Visualización del Summary Report (top support, bundles, heatmap, etc.)
    # Visualización en modo Streamlit compatible con Render



# Tu archivo app.py ahora tiene:
#     Una barra lateral de navegación con 4 secciones
#     Visualización del Summary Report completo
#     Soporte para Render.com
#     Carga de datasets externos desde data/processed/
# 📌 Recordá crear o guardar estos archivos si aún no existen:
#     summary_rules.csv
#     bundle_products.csv
#     tabular_bundle.csv


import os
port = os.environ.get("PORT", 8501)
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import ast  # Para convertir el string a lista real si es necesario
import plotly.graph_objects as go
from charts.HeatmapXTab import HeatmapCrosstab



# ◯ Configuración general
st.set_page_config(page_title="Resumen MBA", layout="wide")


# ◯ Mostrar imagen en el sidebar
logo = Image.open("app/images/Img_0.png")
st.sidebar.image(logo, use_container_width=True)


# ◯ Texto centrado debajo de la imagen
st.sidebar.markdown(
    """
    <div style="
        text-align: center;
        font-size: 30px;
        font-family:  'Poppins', 'Quicksand', sans-serif;
        font-weight: 600;
        margin-top: 10px;
    ">
        🛍️ Reporte MBA
    </div>

    <hr style="margin-top: 10px; margin-bottom: 20px; border: none; border-top: 1px solid #88888833;" />
    """,
    unsafe_allow_html=True
)



# ◯ Sidebar de navegación
section = st.sidebar.radio("Navegación", [
    "🏠 Inicio",
    "Top 5 por Soporte",
    "Bundles de Productos",
    "Bundle Destacado",
    "Heatmap del Bundle",
    "📌 Heatmap de Producto"
])




# ◯ Cargar datasets procesados (ajustar path si es necesario)
@st.cache_data
def load_data():
    rules = pd.read_csv("data/processed/summary_rules.csv")
    df_bundle_products = pd.read_csv("data/processed/bundle_products.csv")
    tabular = pd.read_csv("data/processed/tabular_bundle.csv", index_col=0)
    return rules, df_bundle_products, tabular

rules, df_bundle_products, tabular = load_data()

# ◯ Sección: Inicio
if section == "🏠 Inicio":
    st.title("📊 Reporte de Reglas de Asociación")
    st.markdown(
        """
        Esta app interactiva permite analizar reglas de asociación entre productos a partir de transacciones reales. 
        Utiliza técnicas de Market Basket Analysis para encontrar combinaciones frecuentes y bundles relevantes. 
        
        Con esta herramienta podés:
        - Descubrir productos que suelen comprarse juntos.
        - Explorar agrupamientos naturales (bundles).
        - Identificar oportunidades para ventas cruzadas o promociones.

        Usá el menú lateral para navegar por los distintos análisis disponibles.
        """
    )


# ◯ Sección: Top 5 Reglas por Soporte
elif section == "Top 5 por Soporte":
    st.markdown("## 📈 Top 5 Reglas por Soporte")
    st.markdown("Estas son las 5 reglas más comunes, ordenadas por soporte. El soporte representa la proporción de transacciones donde aparece ese conjunto de productos.")

    # ◯ Nota explicativa con ejemplo concreto, estilo más sutil
    st.markdown(
        """
        <small><i>Ejemplo:</i> Si los productos <b>Taza</b> y <b>Plato</b> aparecen juntos en 50 de 1000 tickets, su soporte es 0.05 (es decir, el 5% de las transacciones).</small>
        """,
        unsafe_allow_html=True
    )

    top_support = rules.sort_values("support", ascending=False).iloc[::2].head(5).reset_index(drop=True)
    st.dataframe(top_support, use_container_width=True)





# ◯ Sección: Bundles de Productos
elif section == "Bundles de Productos":
    st.markdown("## 📦 Bundles de Productos")
    st.markdown(
        "Cada *bundle* agrupa productos que suelen comprarse juntos de forma consistente. "
        "A continuación se listan los grupos descubiertos, ordenados por su soporte promedio."
    )

    # ◯ Mostrar cantidad total de bundles encontrados
    total_bundles = df_bundle_products['category'].nunique()
    st.markdown(f"🔍 Se identificaron **{total_bundles} bundles** de productos.")

    # ◯ Agrupar datos y renombrar columna
    summary_bundles = df_bundle_products.groupby("category").agg(
        products=('nodes', 'unique'),
        support_mean=('support', 'mean'),
        n=('nodes', 'size')
    ).sort_values("support_mean", ascending=False).reset_index().rename(columns={"category": "bundle_name"})

    # ◯ Formatear lista de productos como texto separado por punto medio " • "
    summary_bundles["products"] = summary_bundles["products"].apply(lambda x: "  •  ".join(x))

    # ◯ Estilizar tabla
    styled_df = summary_bundles.style.set_table_styles([
        {'selector': 'td', 'props': [('font-size', '13px'), ('line-height', '1.6')]},
        {'selector': 'th', 'props': [('font-size', '13px'), ('font-weight', 'normal'), ('text-align', 'left')]}
    ]).set_properties(**{'white-space': 'pre-wrap'})

    st.markdown(styled_df.to_html(), unsafe_allow_html=True)

    # ◯ Referencias de columnas con ejemplo y separador actualizado
    st.markdown(
        """
        <small><b>ℹ️ Referencia de columnas:</b></small>
        <small>
        <ul>
            <li><b>bundle_name</b>: Nombre representativo del grupo de productos relacionados, probablemente el producto central o más distintivo del bundle.
                <br><i>Ejemplo:</i> <code>POMO DE CAJÓN CERÁMICO DE RAYAS ROJAS</code> es un bundle que agrupa varios pomos similares.</li>
            <li><b>products</b>: Lista de productos que componen el bundle.</li>
            <li><b>support_mean</b>: Promedio de soporte de los productos del grupo.</li>
            <li><b>n</b>: Cantidad total de productos dentro del bundle.</li>
        </ul>
        </small>
        """,
        unsafe_allow_html=True
    )




# ◯ Sección: Bundle Destacado

#  codigo original
#  elif section == "Bundle Destacado":
#     st.subheader("🔹 Bundle: Pomo de Cajón Cerámico de Rayas Rojas")
#     PRODUCTS_CATEGORY = "POMO DE CAJÓN CERÁMICO DE RAYAS ROJAS"
#     related_products = df_bundle_products[df_bundle_products["category"].str.contains(PRODUCTS_CATEGORY)]["nodes"].values
#     if len(related_products) > 0:
#         st.markdown("**Productos agrupados:**")
#         st.write(list(related_products[0]))
#     else:
#         st.warning("No se encontraron productos relacionados.")




elif section == "Bundle Destacado":
    st.markdown("## 🎯 Bundle Destacado")
    st.markdown(
        "Explorá en detalle los productos que forman parte de un bundle específico. "
        "Seleccioná uno del menú desplegable para ver su composición."
    )

    # Selección de bundle
    bundles_disponibles = df_bundle_products["category"].sort_values().unique()
    selected_bundle = st.selectbox("📦 Seleccioná un bundle:", bundles_disponibles)

    # Filtrar y obtener productos del bundle
    rows = df_bundle_products[df_bundle_products["category"] == selected_bundle]

    if len(rows) > 0:
        productos = []

        for fila in rows["nodes"]:
            if isinstance(fila, list):
                productos.extend(fila)
            elif isinstance(fila, str):
                productos.append(fila)

        productos_unicos = list(set(productos))

        if productos_unicos:
            st.markdown("**Productos agrupados en este bundle:**")

        # Crear y ordenar df_bundle
        df_bundle = rows.explode("nodes")
        df_bundle = df_bundle[["nodes", "support"]].dropna()
        df_bundle = df_bundle.groupby("nodes").mean().sort_values("support", ascending=False)

        if not df_bundle.empty:
            df_bundle["support_pct"] = df_bundle["support"] * 100

            fig = go.Figure(go.Bar(
                x=df_bundle["support_pct"],
                y=df_bundle.index,
                orientation='h',
                marker=dict(color='#d26a00'),
                hovertemplate='%{y}<br>Soporte: %{x:.2f} %<extra></extra>',
                text=[f"<b>{s:.2f}%</b>" for s in df_bundle["support_pct"]],
                textposition='auto',
                textfont=dict(color="#ffffff", size=16),  # más grande
                insidetextanchor='end',
                showlegend=False
            ))

            fig.update_layout(
                title="Frecuencia (soporte) de los productos en este bundle",
                title_x=0.5,
                xaxis_title=None,
                xaxis=dict(showticklabels=False, showgrid=False),
                yaxis=dict(title="", autorange="reversed"),
                plot_bgcolor='#0e1117',
                paper_bgcolor='#0e1117',
                font=dict(color="#f0f0f0", size=14),
                margin=dict(l=200, r=40, t=50, b=40),
                height=60 * len(df_bundle) + 80
            )

            st.plotly_chart(fig, use_container_width=True, config=dict(displayModeBar=False))
        else:
            st.info("Este bundle no contiene productos.")
    else:
        st.warning("No se encontraron datos para el bundle seleccionado.")


# ◯ Sección: Heatmap del Bundle
elif section == "Heatmap del Bundle":
    st.markdown("## 🔥 Heatmap del Bundle Seleccionado")
    st.markdown(
        "Este mapa muestra la frecuencia con la que los productos del bundle se compran juntos. "
        "Cuanto más intenso el color, mayor el soporte conjunto entre esos productos."
    )

    import plotly.graph_objects as go
    import numpy as np

    z = tabular.values
    x_labels = tabular.columns.tolist()
    y_labels = tabular.index.tolist()
    text_labels = np.round(z, 3)

    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=x_labels,
        y=y_labels,
        colorscale='Reds',
        hoverongaps=False,
        text=text_labels,
        texttemplate="%{text}",
        hovertemplate="Producto A: %{y}<br>Producto B: %{x}<br>Soporte: %{z}<extra></extra>"
    ))

    fig.update_layout(
        title="Heatmap de soporte entre productos del bundle",
        title_x=0.5,
        height=900,
        xaxis_tickangle=-45,
        xaxis=dict(tickfont=dict(size=10), automargin=True),
        yaxis=dict(tickfont=dict(size=10), automargin=True),
        margin=dict(l=200, r=50, t=50, b=200),
        plot_bgcolor='#0e1117',
        paper_bgcolor='#0e1117',
        font=dict(color="#f0f0f0")
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})




# ◯ Sección: HEATMAP
# -------------------------------------------------------------------------------------------------------------

elif section == "📌 Heatmap de Producto":
    st.markdown("## 📌 Heatmap de Co-ocurrencia por Producto")
    st.markdown(
        "Este gráfico muestra cómo se relaciona un producto específico con otros, "
        "según la métrica seleccionada."
    )

    from charts.HeatmapXTab import HeatmapCrosstab

    # ◯ Crear instancia del generador de heatmaps
    heat = HeatmapCrosstab(rules)

    # ◯ Obtener productos únicos desde reglas
    productos_disponibles = sorted(set(rules['antecedents'].explode()) | set(rules['consequents'].explode()))
    producto_base = st.selectbox("🧲 Seleccioná un producto base:", productos_disponibles)

    # ◯ Selección de métrica
    metrica = st.selectbox("📏 Seleccioná la métrica:", ["support", "lift", "confidence"])

    # ◯ Explicación contextual de la métrica seleccionada
    explicaciones = {
        "support": "🔥 <b>Support (Soporte)</b>: muestra qué tan seguido se venden juntos los productos.<br>"
                "👉 Útil para detectar <b>productos que siempre aparecen en conjunto</b>.",

        "confidence": "🔥 <b>Confidence (Confianza)</b>: indica qué tan probable es que se compre el segundo producto "
                    "cuando ya se compró el primero.<br>"
                    "👉 Útil para sugerencias de <b>“quienes compraron esto, también compraron…”</b>",

        "lift": "🔥 <b>Lift</b>: mide si dos productos se potencian cuando se venden juntos, más allá de lo esperable.<br>"
                "👉 Útil para identificar <b>combinaciones fuertes o ideales para promociones cruzadas</b>."
    }

    st.markdown(
        f"""
        <div style='
            font-size: 14px;
            margin-bottom: 20px;
            background-color: #f1f1f105;
            padding: 10px 15px;
            border-left: 4px solid #ffaa00;
            border-radius: 5px;
            color: #ddd;
            line-height: 1.5;
        '>
        {explicaciones[metrica]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ◯ Filtrar reglas donde el producto seleccionado es el antecedente
    recomendaciones = rules[rules['antecedents'].apply(lambda x: producto_base in x)]

    # ◯ Ordenar por la métrica elegida
    recomendaciones = recomendaciones.sort_values(metrica, ascending=False)

    # ◯ Mostrar los 5 recomendados más fuertes
    top_recomendados = recomendaciones['consequents'].explode().value_counts().head(5).index.tolist()

    st.markdown("### 🔗 Recomendaciones basadas en asociación")
    st.write("Los siguientes productos aparecen frecuentemente junto a", f"**{producto_base}**:")

    # ◯ Crear tabla cruzada manualmente desde reglas
    df = rules.copy()
    df = df.explode("antecedents")
    df = df.explode("consequents")
    df = df[df["antecedents"] == producto_base]

    crosstab = df.pivot_table(
        index="antecedents",
        columns="consequents",
        values=metrica,
        aggfunc="mean",
        fill_value=0
    ).iloc[:, :10]  # Mostrará hasta 10 productos relacionados como máximo

    # ◯ Graficar heatmap
    fig = heat.plot_heatmap(crosstab)

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.markdown(
    f"""
    <div style='
        margin-top: 25px;
        padding: 15px;
        background-color: #1e1e1e;
        border-left: 4px solid #d26a00;
        border-radius: 5px;
        font-size: 15px;
        line-height: 1.6;
        color: #ddd;
    '>
        <b>¿Cómo interpretar este heatmap?</b><br>
        El gráfico muestra la intensidad de relación entre <b>{producto_base}</b> y otros productos.<br>
        Cuanto más oscuro el recuadro, mayor es la <b>{metrica}</b> observada entre ambos ítems.<br>
        Esto puede ayudarte a identificar productos que suelen comprarse juntos o que podrían recomendarse juntos en la tienda o sitio web.
    </div>
    """,
    unsafe_allow_html=True
    )

    # ◯ Mostrar ubicación sugerida si el producto base está en un bundle conocido
    ubicacion = df_bundle_products[df_bundle_products['nodes'] == producto_base]

    if not ubicacion.empty:
        categoria = ubicacion['category'].iloc[0]

        # ◯ Buscar todos los productos en ese mismo bundle
        otros = df_bundle_products[df_bundle_products['category'] == categoria]

        # ◯ Excluir el producto actual
        productos_relacionados = otros[otros['nodes'] != producto_base]['nodes'].tolist()

        # ◯ Mostrar bloque de sugerencia

        # ◯ Calcular productos sugeridos ordenados por métrica
        df_metric = df.groupby("consequents")[metrica].mean().sort_values(ascending=False)
        df_metric = df_metric[df_metric.index != producto_base]

        # ◯ Armar la lista en HTML
        items_html = "".join([
            f"<div style='margin-bottom:6px; color: #ddd; font-size:15px;'>"
            f"<span style='color: #ffaa00; font-weight: bold;'>✔️</span> {prod}</div>"
            for prod in df_metric.index.tolist()
        ])

        # ◯ Cuadro de sugerencia completo con lista integrada
        st.markdown(
            f"""
            <div style='
                margin-top: 20px;
                padding: 15px;
                background-color: #1e1e1e;
                border-left: 4px solid #4a90e2;
                border-radius: 5px;
                font-size: 15px;
                line-height: 1.6;
                color: #ddd;
            '>
                <div style='font-size:21px; font-weight:bold; color:#fff; margin-bottom:10px;'>
                🟡 Sugerencia de Ubicación / Agrupación
                </div>
                Este producto forma parte del bundle: <b>📦 {categoria}</b>.<br>
                Podría colocarse cerca de productos similares para mejorar la visibilidad o fomentar compras combinadas.
                <br><br>
                <b>Productos sugeridos para agrupar (ordenados por <code>{metrica}</code>):</b>
                {items_html}
                </div>
            """,
            unsafe_allow_html=True
        )



