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


#    ------------------------------------------------------------------------------------------
# 🟠 IMPORTs:
#    ------------------------------------------------------------------------------------------

import os
port = os.environ.get("PORT", 8501)
import ast  # Para convertir el string a lista real si es necesario
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import streamlit as st
from PIL import Image
from charts.HeatmapXTab import HeatmapCrosstab, draw_heatmap
from charts.GraphNetwork import draw_graph

# ◯ Importar Utilities
from utils.loader import load_data  


# ◯ Funciones por sección:
from sections.section_1_about import show_section_1_about
from sections.section_3_methodology import show_section_3_methodology
from sections.section_4_data_exploration import show_section_4
from sections.section_5_rules import show_section_5_rules
from sections.section_6_recommendations import show_section_6_recommendations
from sections.section_7_actions import show_section_7_actions
from sections.section_9_summary import show_section_9_summary   


#    ------------------------------------------------------------------------------------------
# 🟠 PAGE SETTINGs:
#    ------------------------------------------------------------------------------------------
    
# ◯ Configuración de página
st.set_page_config(page_title="Market Basket Analysis", layout="wide")

# Ajustar el tamaño de letra base en toda la app
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 10px !important;
        font-family:Lato !important;
    }
    </style>
""", unsafe_allow_html=True)

#    ------------------------------------------------------------------------------------------
# 🟠 DATA LOAD:
#    ------------------------------------------------------------------------------------------

# Cargar datasets procesados (desde utils/loader.py)

dataset_sample, Top_10_Mas_Vendidos, example_basket, monthly_transactions, matriz_binaria, rules, df_bundle_products, tabular, Top_5_Rules_by_Score = load_data()


#    ------------------------------------------------------------------------------------------
# 🟠 SIDEBAR:
#    ------------------------------------------------------------------------------------------

# Sidebar para navegación

# ◯ TÍTULO en la barra lateral
st.sidebar.markdown(
    "<h1 style='text-align: center; font-family:Open Sans; font-size: 22px;'>🛒 Market Basket Analysis</h1>",
    unsafe_allow_html=True
)

# ◯ Mostrar imagen en el sidebar
logo = Image.open("app/images/Img_0.png")
st.sidebar.image(logo, use_container_width=True)

st.sidebar.title("Navegación")
section = st.sidebar.radio("Ir a la sección:", (
    "1. ✔️ Acerca del Proyecto",
    "4. ✔️ Exploración de Datos",
    "3. ✔️ Metodología del Análisis",
    "5. ✔️ Reglas de Asociación",
    "6. ✔️ Recomendaciones por Producto",
    "7. ✔️ Estratégicas de negocio",   
    "9. ✔️ Conclusiones"
))

#    ------------------------------------------------------------------------------------------
# 🟠 PAGES:
#    ------------------------------------------------------------------------------------------


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
    show_section_1_about()



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
    show_section_3_methodology(matriz_binaria)


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
    show_section_4(dataset_sample, Top_10_Mas_Vendidos, example_basket, monthly_transactions)

    
# ◯ Seccion 5: EXPLORAR REGLAS DE ASOCIACIÓN (unificada)
# ............................................................................................
# Objetivo:
#   Permitir al usuario explorar de manera interactiva las reglas de asociación generadas mediante Apriori.
# Contenido:
#   - Reglas destacadas con mayor score
#   - Red de relaciones entre productos
#   - Heatmap cruzado entre productos
#   - Tabla completa de todas las reglas generadas

elif section.startswith("5."):
    show_section_5_rules(rules, tabular, Top_5_Rules_by_Score)



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

elif section.startswith("6."):
    show_section_6_recommendations(rules, df_bundle_products, Top_5_Rules_by_Score)
    
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
    show_section_7_actions(rules, Top_10_Mas_Vendidos)

# 9. ◯ Sección: RESUMEN DEL PROYECTO
# ............................................................................................
# Objetivo:
#   Presentar un resumen ejecutivo del análisis realizado, destacando el propósito del proyecto, el origen de los datos,
#   la metodología aplicada y los principales hallazgos obtenidos.
# Contenido:
#   - Objetivo del análisis y foco comercial
#   - Fuente y características del dataset utilizado
#   - Metodología empleada (Apriori, métricas de asociación)
#   - Hallazgos destacados y ejemplos de reglas obtenidas
#   - Recomendaciones accionables para el negocio
#   - Tecnologías y herramientas utilizadas en el desarrollo

elif section.startswith("9."):
    show_section_9_summary()