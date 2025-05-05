
import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from joblib import load

# Configuración inicial
st.set_page_config(page_title="Market Basket Analysis", page_icon="🛒", layout="wide")

# Sidebar de navegación
page = st.sidebar.radio("Navegación", [
    "Introducción", 
    "Dataset", 
    "Frecuencias (Apriori)", 
    "Reglas de Asociación", 
    "Recomendaciones"
])

# Cargar datos preprocesados
try:
    basket = load("basket.joblib")
except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'basket.joblib'. Asegúrate de cargarlo en el entorno de ejecución.")
    st.stop()

# Página: Introducción
if page == "Introducción":
    st.title("🛒 Análisis de Market Basket")
    st.markdown("""
    Esta aplicación analiza datos transaccionales de una tienda online para descubrir patrones de compra conjunta entre productos.

    **¿Para qué sirve esto?**
    - Identificar productos que suelen comprarse juntos
    - Crear promociones cruzadas más efectivas
    - Reorganizar productos en la tienda online
    - Generar recomendaciones inteligentes para clientes

    Utilizamos el algoritmo **Apriori** para detectar conjuntos de productos frecuentes y reglas de asociación.
    """)

# Página: Dataset
elif page == "Dataset":
    st.title("📦 Datos Preprocesados")
    st.markdown("Vista previa de los datos transformados a formato de cesta binaria (1 = comprado, 0 = no comprado):")
    st.dataframe(basket.head())

# Página: Frecuencias (Apriori)
elif page == "Frecuencias (Apriori)":
    st.title("📊 Conjuntos Frecuentes")
    min_support = st.sidebar.slider("Soporte mínimo", 0.001, 0.1, 0.03, 0.001)
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    frequent_itemsets["length"] = frequent_itemsets["itemsets"].apply(lambda x: len(x))
    st.markdown("Conjuntos de productos que aparecen juntos con frecuencia:")
    st.dataframe(frequent_itemsets.sort_values(by="support", ascending=False))

# Página: Reglas de Asociación
elif page == "Reglas de Asociación":
    st.title("🔗 Reglas de Asociación")
    metric = st.sidebar.selectbox("Métrica", ["lift", "confidence", "support"])
    min_threshold = st.sidebar.slider("Umbral mínimo", 0.1, 2.0, 0.5, 0.1)
    frequent_itemsets = apriori(basket, min_support=0.03, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
    st.markdown("Reglas extraídas usando el algoritmo Apriori:")
    st.dataframe(rules[["antecedents", "consequents", "support", "confidence", "lift"]])

# Página: Recomendaciones
elif page == "Recomendaciones":
    st.title("🎯 Explorador de Recomendaciones")
    frequent_itemsets = apriori(basket, min_support=0.03, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)

    all_items = sorted(basket.columns)
    selected_item = st.selectbox("Selecciona un producto:", all_items)

    filtered_rules = rules[rules["antecedents"].apply(lambda x: selected_item in x)]
    if not filtered_rules.empty:
        st.success(f"Recomendaciones para clientes que compran '{selected_item}':")
        st.dataframe(filtered_rules[["antecedents", "consequents", "support", "confidence", "lift"]])
    else:
        st.warning("No se encontraron reglas con ese producto como antecedente.")
