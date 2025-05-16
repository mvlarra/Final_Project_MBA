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



# ◯ Configuración de página
st.set_page_config(page_title="Market Basket Analysis", layout="wide")

# Ajustar el tamaño de letra base en toda la app
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 14px !important;
    }
    </style>
""", unsafe_allow_html=True)


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
    "📋 Resumen del Proyecto",
    "📌 Introduccion",
    "🎯 Goals",
    "🧪 Methodology",
    "📏 Key Metrics",
    "🏆 Top 5 Rules",
    "🔁 Cross Selling Products",
    "✅ Recommendations",
    "aca",
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
    Top_5_Rules_by_Score = pd.read_csv("data/processed/Top_5_Rules_by_Score.csv")
    return rules, df_bundle_products, tabular, Top_5_Rules_by_Score

rules, df_bundle_products, tabular, Top_5_Rules_by_Score = load_data()


# ◯ Sección: RESUMEN DEL PROYECTO
# -----------------------------------------------------------------------------------------------------------------
if section == "📋 Resumen del Proyecto":
    st.subheader("📋 Análisis de Canasta de Compras — Resumen Final del Proyecto")

    st.markdown("""
    **📌 Objetivo**  
    Identificar productos que suelen comprarse juntos en transacciones de retail, para descubrir patrones útiles en estrategias de venta cruzada, bundles, optimización de layout y recomendaciones personalizadas.

    ---

    **📂 Dataset**  
    - **Fuente:** Online Retail II — UCI Machine Learning Repository  
    - **Período:** Diciembre 2009 a Diciembre 2011  
    - **Alcance:** Transacciones de clientes del Reino Unido  
    - **Preprocesamiento:** Filtrado de ventas válidas, eliminación de cancelaciones y valores nulos

    ---

    **⚙️ Metodología**  
    - Transformación de los datos a formato canasta (ítems × transacciones)  
    - Aplicación del algoritmo **Apriori** con la librería `mlxtend`  
    - Evaluación de reglas utilizando las siguientes métricas:  
    - **Support:** Frecuencia del conjunto  
    - **Confidence:** Probabilidad de ocurrencia conjunta  
    - **Lift:** Fuerza de la asociación

    ---

    **🏆 Principales Hallazgos**  
    - Se detectaron asociaciones sólidas entre variantes de productos (ej. distintos colores de juegos de té)  
    - Las reglas más destacadas obtuvieron altos valores en todas las métricas:  
    - Confianza por encima del 70%  
    - Lift superior a 20  
    - Estas reglas son altamente accionables para estrategias de marketing y experiencia de usuario

    ---

    **✅ Recomendaciones de Negocio**  
    - Implementar **sugerencias automáticas de productos** en el carrito de compras  
    - Ofrecer **bundles** basados en productos frecuentemente comprados juntos  
    - Optimizar la disposición de productos en tienda física u online  
    - Lanzar **campañas segmentadas** basadas en afinidades entre productos

    ---

    **🔧 Herramientas y Tecnologías**  
    Python · pandas · mlxtend · Streamlit  
    + Visualización con plotly y matplotlib  
    + Diseño modular con navegación lateral e insights interpretables

    ---

    Esta app fue desarrollada como el **proyecto final del Bootcamp de Data Science**, demostrando habilidades de punta a punta: desde la preparación de datos y detección de patrones, hasta la generación de insights de negocio y desarrollo de una aplicación funcional.
    """)




# ◯ Sección: Introduccion
# -----------------------------------------------------------------------------------------------------------------
elif section == "📌 Introduccion":

    st.title("🛒 Market Basket Analysis")
    st.markdown("## Bienvenido/a al Análisis de Canasta de Compras para Retail")

    # Imagen de portada debajo
    st.image("app/images/Img3.png", width=500)  # Ajustás el tamaño según necesidad

     
    # ✏️ Introducción general
    st.markdown("""
    Market Basket Analysis (MBA) es una técnica de minería de datos que permite descubrir patrones de compra entre productos. 
    Analiza qué artículos suelen adquirirse juntos por los clientes durante una misma transacción.

    Este enfoque ayuda a:
    - ✅ Optimizar la disposición de productos en tienda
    - ✅ Diseñar promociones más efectivas
    - ✅ Aumentar las ventas mediante estrategias de **cross-selling**
    - ✅ Mejorar la experiencia del cliente
                
    En esta aplicación interactiva podrás:
    - Explorar reglas de asociación entre productos
    - Visualizar productos frecuentemente comprados juntos
    - Evaluar oportunidades de mejora en ventas y layout
    """)

    # Info del proyecto
    st.markdown("""
    **🗂️ Fuente de datos:**  
    Dataset *Online Retail II* de la UCI Machine Learning Repository.  
    Incluye transacciones realizadas por un minorista online entre 2009 y 2011.

    **📅 Período Analizado:**  
    Del 01/12/2009 al 09/12/2011

    **📍 Enfoque:**  
    Filtramos exclusivamente las compras realizadas por clientes en **Reino Unido**, para facilitar la visualización y generar recomendaciones más específicas.

    """)


# ◯ Sección: Goals
# -----------------------------------------------------------------------------------------------------------------

elif section == "🎯 Goals":
    st.subheader("🎯 Goals")

    st.markdown("""
    **`1. Association Rule Discovery`**  
    Identify associations and correlations among products or items in a dataset. Discover rules that indicate the likelihood of certain items being bought together.

    **`2. Cross-Selling Opportunities`**  
    Uncover opportunities for cross-selling by understanding which products are frequently purchased together.

    **`3. Promotion Planning`**  
    Optimize promotional campaigns by identifying items that are frequently bought together. Design effective promotions and discounts to incentivize the purchase of complementary products.

    **`4. Optimizing Product Layout`**  
    Arrange products in-store or online in a way that encourages the purchase of related items, creating a more convenient and satisfying shopping experience.
    """)

# ◯ Sección: Methodology
# -----------------------------------------------------------------------------------------------------------------

elif section == "🧪 Methodology":
    st.header("🧪 Methodology")
    st.markdown("""
    The data is sourced from 'Online Retail II'.

    - This dataset encompasses all transactions conducted by a UK-based and registered non-store online retailer from December 1, 2009, to December 9, 2011.
    - The company specializes in the sale of distinctive all-occasion giftware.

    For conducting market basket analysis we utilize:

    - The `Apriori Algorithm` proving highly effective in discerning `frequent itemsets` and deriving association rules, relying on predefined metrics like support and confidence.
    - To execute the Apriori algorithm, we utilize the `mlxtend library`, a reliable Python library for machine learning extensions.

    The following parameters are configured for the algorithm:

    - **`Maximum Combination Length:`**  
    We set the maximum combination length to 2 items. This choice is made to focus on pairs of items, allowing for a more targeted analysis of co-occurrences.
    - **`Minimum Co-Occurrence Support Threshold:`**  
    A minimum co-occurrence support threshold of 0.5% is established to filter out infrequent itemsets. This ensures that only associations with a significant presence in the dataset are considered.
    """)



# ◯ Sección: Key Metrics
# -----------------------------------------------------------------------------------------------------------------
elif section == "📏 Key Metrics":
    st.subheader("📏 Key Metrics")

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

# ◯ Sección: TOP 5 ASSOCIATION RULES by score
# -----------------------------------------------------------------------------------------------------------------
elif section == "🏆 Top 5 Rules":
    st.subheader("🏆 Top 5 Association Rules")

    st.markdown("""
    While evaluating association rules, we utilize key metrics such as **:orange[support]**, **:orange[confidence]**, and **:orange[lift]** to discern their significance.

    Each rule is independently ranked based on these metrics, and a **mean rank** is computed across all three rankings.

    This mean rank serves as a **composite score**, capturing the overall performance of each rule across the different metrics.  
    The table below shows the **top 5 association rules** based on the composite score.
    """)
    # Mostrar la tabla

    st.dataframe(Top_5_Rules_by_Score, use_container_width=True)

    st.markdown("### ✅ Recomendaciones basadas en las reglas")

    st.markdown("""
    1. **Si alguien compra “TAZA DE TÉ Y PLATILLO VERDE REGENCY”, recomendale también “TAZA DE TÉ Y PLATILLO ROSES REGENCY”.**  
    Alta confianza (76%) y fuerte lift (22× más probable que al azar).

    2. **Si alguien compra “TAZA DE TÉ Y PLATILLO ROSES REGENCY”, recomendale también “TAZA DE TÉ Y PLATILLO VERDE REGENCY”.**  
    Alta probabilidad y relación recíproca con la anterior.

    3. **Quien compra la versión rosa, tiene alta chance (83%) de interesarse también en la verde.**  
    Ideal para bundles visualmente combinados.

    4. **Si compran la verde, podrías ofrecer también la rosa, aunque con menor confianza (63%).**  
    Útil como recomendación cruzada secundaria.

    5. **Compradores de la versión rosa también suelen elegir la versión ROSES.**  
    Oportunidad para agruparlas como “línea de colección” o sugerirlas juntas en promociones.
    """)


# ◯ Sección: Cross Selling Products
# -----------------------------------------------------------------------------------------------------------------

elif section == "🔁 Cross Selling Products":
    st.markdown("## 🔁 Cross Selling Products")
    st.markdown("""
    **Top 5 Cross-Selling Products**

    Cross-selling involves identifying products frequently purchased together, gauged by high **:orange[support]** reflecting their `co-occurrence` in transactions.   
    The concept considers not only the `frequency of joint purchases` but also the `strength of these associations` measured by **:orange[confidence]**.

    Focusing on product combinations with both `high support and confidence` helps pinpoint reliably associated items, enabling businesses to strategically promote or bundle products for an `enhanced customer shopping` experience.

    The table below shows the **:orange[top 5 cross-selling-product pairs]**, sorted by their `average confidence and support`.
    """)


# ◯ Sección: Top 5 Reglas por Soporte
# -----------------------------------------------------------------------------------------------------------------
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
            border-left: 4px solid #ff6d00;
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
        border-left: 4px solid #ff6d00;
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
                border-left: 4px solid #ff6d00;
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



