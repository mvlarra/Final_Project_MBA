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
import plotly.graph_objects as go
import numpy as np

# ◯ Configuración general
st.set_page_config(page_title="Resumen MBA", layout="wide")
st.title("📊 Reporte de Reglas de Asociación")

# ◯ Sidebar de navegación
section = st.sidebar.radio("Navegación", [
    "Top 5 por Soporte",
    "Bundles de Productos",
    "Bundle Destacado",
    "Heatmap del Bundle"
])

# ◯ Cargar datasets procesados (ajustar path si es necesario)
@st.cache_data
def load_data():
    rules = pd.read_csv("data/processed/summary_rules.csv")
    df_bundle_products = pd.read_csv("data/processed/bundle_products.csv")
    tabular = pd.read_csv("data/processed/tabular_bundle.csv", index_col=0)
    return rules, df_bundle_products, tabular

rules, df_bundle_products, tabular = load_data()

# ◯ Sección: Top 5 Reglas por Soporte
if section == "Top 5 por Soporte":
    st.subheader("🔹 Top 5 Reglas por Soporte")
    top_support = rules.sort_values("support", ascending=False).iloc[::2].head(5).reset_index(drop=True)
    st.dataframe(top_support)

# ◯ Sección: Bundles de Productos
elif section == "Bundles de Productos":
    st.subheader("🔹 Bundles de Productos (Modularidad)")
    summary_bundles = df_bundle_products.groupby("category").agg(
        products=('nodes', 'unique'),
        support_mean=('support', 'mean'),
        n=('nodes', 'size')
    ).sort_values("support_mean", ascending=False)
    st.dataframe(summary_bundles)

# ◯ Sección: Bundle Destacado
elif section == "Bundle Destacado":
    st.subheader("🔹 Bundle: Pomo de Cajón Cerámico de Rayas Rojas")
    PRODUCTS_CATEGORY = "POMO DE CAJÓN CERÁMICO DE RAYAS ROJAS"
    related_products = df_bundle_products[df_bundle_products["category"].str.contains(PRODUCTS_CATEGORY)]["nodes"].values
    if len(related_products) > 0:
        st.markdown("**Productos agrupados:**")
        st.write(list(related_products[0]))
    else:
        st.warning("No se encontraron productos relacionados.")

# ◯ Sección: Heatmap del Bundle
elif section == "Heatmap del Bundle":
    st.subheader("🔹 Heatmap entre Productos del Bundle")
    # Limitar a 5 productos
    tabular_5 = tabular.iloc[:5, :5]
    z = tabular_5.values
    x_labels = tabular_5.columns.tolist()
    y_labels = tabular_5.index.tolist()
    text_labels = np.where(np.isnan(z), "", np.round(z, 3))

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
        height=700,
        title="Heatmap de soporte entre productos del bundle (Top 5)",
        xaxis_tickangle=-45,
        xaxis=dict(tickfont=dict(size=10), automargin=True),
        yaxis=dict(tickfont=dict(size=10), automargin=True),
        margin=dict(l=200, r=50, t=50, b=200)
    )

    st.plotly_chart(fig, use_container_width=True)
