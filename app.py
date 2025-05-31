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
import ast  # Para convertir el string a lista real si es necesario
from utils.loader import load_data  
from utils.visual_helpers import ( 
    mostrar_top_10_productos,
    mostrar_transacciones_por_mes,
    mostrar_ejemplo_canasta
)
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import streamlit as st
from PIL import Image
from charts.HeatmapXTab import HeatmapCrosstab, draw_heatmap
from charts.GraphNetwork import draw_graph
from utils.show_explanation import show_explanation


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

# # ◯ Texto centrado debajo de la imagen
# st.sidebar.markdown(
#     """
#     <div style="
#         text-align: center;
#         font-size: 30px;
#         font-family:  'Poppins', 'Quicksand', sans-serif;
#         font-weight: 600;
#         margin-top: 10px;
#     ">
#         🛍️ MBA
#     </div>

#     <hr style="margin-top: 10px; margin-bottom: 20px; border: none; border-top: 1px solid #88888833;" />
#     """,
#     unsafe_allow_html=True
# )

# ◯ Cargar datasets procesados (desde utils/loader.py)

dataset_sample, Top_10_Mas_Vendidos, example_basket, monthly_transactions, rules, df_bundle_products, tabular, Top_5_Rules_by_Score = load_data()

# ◯ Sidebar para navegación
# ............................................................................................

st.sidebar.title("🧭 Navegación")
section = st.sidebar.radio("Ir a la sección:", (
    "1. 📘 Acerca del Proyecto",
    "2. 📋 Resumen del Proyecto",
    "3. 🧪 Metodología del Análisis",
    "4. 📊 Exploración de Datos",
    "5. 🔎 Explorar Reglas de Asociación",
    "6. 🛒 Recomendaciones y Estrategias por Producto",
    "7. 💼 Acciones estratégicas para tu negocio",   
    "8. 📏 Glosario de Métricas", 
    "OLD 1. 🏠 Inicio",
    "OLD 9. 📎 Créditos y recursos del proyecto",
    # "🧪 Methodology",
    # "📏 Key Metrics",
    # "🔁 Cross Selling Products",
    # "OLD 4.1 ⚙️ Reglas de Asociación",
    # "OLD 7. 🗺️ Visualización de Relaciones",
    # "OLD 5. 📦 Bundles de Productos",
    # "OLD 6. 🛍️ Recomendaciones para tu carrito",
    # "Heatmap del Bundle",
    # "📌 Heatmap de Producto"
))



# 1. ◯ New Sección: ACERCAS DEL PROYECTO (Unificar Sección 1 (Resumen) y Sección 9 (Créditos))
# ............................................................................................
# Objetivo:
#   Presentar el propósito general del proyecto, su contexto, el objetivo del análisis y los créditos.
# Contenido:
#   - Objetivo del análisis
#   - Tecnologías utilizadas
#   - Recursos y vínculos
#   - Contacto profesional

if section.startswith("1."):
    import sections.section_1_about


# 2. ◯ Sección: RESUMEN DEL PROYECTO
# ............................................................................................
# Objetivo:
#   Presentar una visión general del comportamiento de las transacciones y los productos más vendidos.
# Contenido:
#   - Distribución de transacciones por mes
#   - Productos más vendidos
#   - Canasta de compra real (ejemplo individual)

elif section.startswith("2."):
    import sections.section_2_summary
    

# ◯ Sección 3: METODOLOGIA DE ANALISIS
# -----------------------------------------------------------------------------------------------------------------
# Objetivo:
#   Describir el origen del dataset, el enfoque metodológico y los parámetros utilizados para generar las reglas de asociación.
# Contenido:
#   - Fuente del dataset y contexto comercial
#   - Algoritmo utilizado (Apriori)
#   - Biblioteca empleada (mlxtend)
#   - Parámetros clave del modelo: combinación máxima y soporte mínimo

elif section.startswith("3."):
    import sections.section_3_methodology




# ◯ Sección 4: EXPLORACIÓN DE DATOS
# ............................................................................................
# Objetivo:
#   Realizar una primera aproximación visual al dataset para comprender su estructura y contenido.
# Contenido:
#   - Vista general del dataset original
#   - Productos más vendidos
#   - Ejemplo real de una transacción
#   - Distribución mensual de transacciones

elif section.startswith("4."):
    import sections.section_4_data_exploration
    
    
    
# ◯ Seccion 5: EXPLORAR REGLAS DE ASOCIACIÓN (unificada)
# ............................................................................................
# Objetivo:
#   Permitir al usuario explorar de manera interactiva las reglas de asociación generadas mediante Apriori.
# Contenido:
#   - Reglas destacadas con mayor score
#   - Red de relaciones entre productos
#   - Heatmap cruzado entre productos
#   - Tabla completa de todas las reglas generadas

elif section.startswith("5. 🔎"):
    import sections.section_5_rules



# ◯ Seccion 6: RECOMENDACIONES Y ESTRATEGIAS POR PRODUCTO
# ............................................................................................
# Objetivo:
#   Ofrecer recomendaciones y estrategias accionables basadas en productos reales.
# Contenido:
#   - Reglas destacadas por soporte y score
#   - Bundles de productos descubiertos
#   - Recomendaciones personalizadas por producto
#   - Heatmap cruzado por producto
#   - Identificación de oportunidades de cross-selling

elif section.startswith("6. 🛒"):
    import sections.section_6_recommendations

# 7. ◯ Sección: ACCIONES ESTRATÉGICAS PARA TU NEGOCIO
# ............................................................................................
# Objetivo:
#   Traducir hallazgos analíticos en acciones prácticas que generen impacto comercial.
# Contenido:
#   - Sugerencias accionables como bundles, descuentos o reubicaciones
#   - Asociación entre reglas y productos clave
#   - Priorización personalizada de acciones por parte del usuario
#   - Exportación de las acciones seleccionadas

elif section.startswith("7."):
    import sections.section_7_actions



# ◯ Sección 8: GOLOSARIO DE METRICAS
# -----------------------------------------------------------------------------------------------------------------
# Objetivo:
#   Proporcionar definiciones claras y fórmulas clave de las métricas utilizadas en el análisis de reglas de asociación.
# Contenido:
#   - Definiciones de Support, Confidence, Lift, Leverage y Conviction
#   - Ejemplos de fórmulas aplicadas
#   - Explicaciones orientadas a usuarios de negocio no técnicos

elif section == "8. 📏 Glosario de Métricas":
   import sections.section_8_glosario