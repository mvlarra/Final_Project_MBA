
import os
port = os.environ.get("PORT", 8501)

import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import pickle

# Configuración inicial
st.set_page_config(page_title="Market Basket Analysis", page_icon="🛒", layout="wide")

# Sidebar de navegación
page = st.sidebar.radio("Navegación", [
    "Introducción", 
    "Dataset", 
    "Conjuntos Frecuentes", 
    "Reglas de Asociación", 
    "Recomendaciones Interactivas",
    "Recomendaciones Destacadas",
    "Métricas", 
    "Referencias"
])

# Cargar datos preprocesados
try:
    with open("app/models/basket.pkl", "rb") as f:
        basket = pickle.load(f)
except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'basket.pkl'. Asegúrate de cargarlo en el entorno de ejecución.")
    st.stop()

# Página: Introducción
if page == "Introducción":
    st.title("🛒 Análisis de Combinaciones de Productos Frecuentes")
    st.markdown("""
    Esta aplicación explora combinaciones de productos frecuentes (productos que se venden en conjunto) en una tienda online usando reglas de asociación.

    Se utiliza el algoritmo Apriori para descubrir patrones valiosos, generar recomendaciones y apoyar decisiones comerciales basadas en datos.
    """)

# Página: Dataset
elif page == "Dataset":
    st.title("📦 Datos Preprocesados")
    st.dataframe(basket.head())

# Página: Conjuntos Frecuentes
elif page == "Conjuntos Frecuentes":
    st.title("📊 Conjuntos Frecuentes (Apriori)")
    min_support = st.sidebar.slider("Soporte mínimo", 0.001, 0.1, 0.03, 0.001)
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    frequent_itemsets["length"] = frequent_itemsets["itemsets"].apply(lambda x: len(x))
    st.dataframe(frequent_itemsets.sort_values(by="support", ascending=False))

# Página: Reglas de Asociación
elif page == "Reglas de Asociación":
    st.title("🔗 Reglas de Asociación")
    metric = st.sidebar.selectbox("Métrica", ["lift", "confidence", "support"])
    min_threshold = st.sidebar.slider("Umbral mínimo", 0.1, 2.0, 0.5, 0.1)
    frequent_itemsets = apriori(basket, min_support=0.03, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
    st.dataframe(rules[["antecedents", "consequents", "support", "confidence", "lift"]])

# Página: Recomendaciones Interactivas
elif page == "Recomendaciones Interactivas":
    st.title("🎯 Recomendaciones Interactivas")
    frequent_itemsets = apriori(basket, min_support=0.03, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)

    all_items = sorted(basket.columns)
    selected_item = st.selectbox("Selecciona un producto:", all_items)

    filtered_rules = rules[rules["antecedents"].apply(lambda x: selected_item in x)]

    def interpretar_regla(row, idx):
        antecedents = ', '.join(row['antecedents'])
        consequents = ', '.join(row['consequents'])
        support_pct = round(row['support'] * 100, 2)
        confidence_pct = round(row['confidence'] * 100, 2)
        lift = round(row['lift'], 2)

        if lift > 10 and confidence_pct > 70:
            utilidad = "**Esta es una regla muy útil ✅**"
            accion = "*Product bundling*: Ofrecer ambos productos como un set o pack."
        elif lift > 5 and confidence_pct > 40:
            utilidad = "**Es útil 🟡**, con una asociación fuerte."
            accion = "*Item placement*: Ubicar los productos cerca o sugerir en conjunto."
        elif lift > 2:
            utilidad = "**Moderadamente útil 🟡**, con confianza baja pero conexión clara."
            accion = "*Checkout suggestion*: Ofrecer como sugerencia al final de la compra."
        else:
            utilidad = "**Asociación débil 🔍**"
            accion = "*No prioritaria*, puede usarse como dato de interés general."

        descripcion = f'''
### {idx+1}. Regla: `{antecedents} → {consequents}`

- **Soporte**: {support_pct}%
- **Confianza**: {confidence_pct}%
- **Lift**: {lift}

{utilidad}

**Acción recomendada:**  
{accion}
'''
        return descripcion

    if not filtered_rules.empty:
        for i, row in filtered_rules.reset_index().iterrows():
            st.markdown(interpretar_regla(row, i))
    else:
        st.warning("No se encontraron recomendaciones para el producto seleccionado.")

# Página: Recomendaciones Destacadas
elif page == "Recomendaciones Destacadas":
    st.title("🏆 Reglas Destacadas (preseleccionadas)")

    try:
        rules = pd.read_csv("app/models/association_rules_final.csv")
    except FileNotFoundError:
        st.error("❌ No se encontró 'association_rules_final.csv'.")
        st.stop()

    def interpretar_fija(row, idx):
        antecedents = row['antecedents']
        consequents = row['consequents']
        support_pct = row['support']
        confidence_pct = round(float(row['confidence']) * 100, 2)
        lift = round(float(row['lift']), 2)

        if lift > 10 and confidence_pct > 70:
            utilidad = "**Esta es una regla muy útil ✅**"
            accion = "*Product bundling*: Ofrecer ambos productos como un set o pack."
        elif lift > 5 and confidence_pct > 40:
            utilidad = "**Es útil 🟡**, con una asociación fuerte."
            accion = "*Item placement*: Ubicar los productos cerca o sugerir en conjunto."
        elif lift > 2:
            utilidad = "**Moderadamente útil 🟡**, con confianza baja pero conexión clara."
            accion = "*Checkout suggestion*: Ofrecer como sugerencia al final de la compra."
        else:
            utilidad = "**Asociación débil 🔍**"
            accion = "*No prioritaria*, puede usarse como dato de interés general."

        descripcion = f'''
### {idx+1}. Regla: `{antecedents} → {consequents}`

- **Soporte**: {support_pct}
- **Confianza**: {confidence_pct}%
- **Lift**: {lift}

{utilidad}

**Acción recomendada:**  
{accion}
'''
        return descripcion

    for i, row in rules.iterrows():
        st.markdown(interpretar_fija(row, i))

# Página: Métricas
elif page == "Métricas", 
    "Referencias":
    st.title("📐 Métricas de Evaluación de Reglas de Asociación")
    st.markdown("""## 📐 Métricas de Evaluación de Reglas de Asociación

Las reglas de asociación permiten descubrir combinaciones de productos frecuentes (productos que se venden en conjunto). Estas reglas se generan a partir de conjuntos frecuentes mediante el algoritmo Apriori.

Cada regla tiene **un antecedente (producto A)** y **un consecuente (producto B)**, y se evalúa con tres métricas principales:

---

### 🔹 Soporte (Support)

Indica la **frecuencia con la que ambos productos (A y B) aparecen juntos** en todas las transacciones.

\[
	ext{Soporte}(A 
ightarrow B) = rac{	ext{# transacciones con A y B}}{	ext{total de transacciones}}
\]

🔍 **Interpretación:**  
Un soporte de 0.031 significa que el 3.1% de todas las transacciones contienen esa combinación de productos.

---

### 🔹 Confianza (Confidence)

Es la **probabilidad de que un cliente compre B dado que ya compró A**.

\[
	ext{Confianza}(A 
ightarrow B) = rac{	ext{# transacciones con A y B}}{	ext{# transacciones con A}}
\]

🔍 **Interpretación:**  
Una confianza de 0.70 implica que el 70% de quienes compraron A también compraron B.

---

### 🔹 Elevación (Lift)

Mide la **fuerza de la relación** entre A y B. Compara la confianza con la frecuencia independiente de B.  

\[
	ext{Lift}(A 
ightarrow B) = rac{	ext{Confianza}(A 
ightarrow B)}{	ext{Soporte}(B)}
\]

🔍 **Interpretación:**
- **Lift > 1** → Asociación positiva (A y B ocurren más de lo esperado)
- **Lift = 1** → Independencia (A y B no tienen relación)
- **Lift < 1** → Asociación negativa (ocurren juntos menos de lo esperado)

---

### 📊 Ejemplo real del proyecto

- **Regla:** `roses regency teacup and saucer → green regency teacup and saucer`
- **Soporte:** 3.10%
- **Confianza:** 70.5%
- **Lift:** 17.72 ✅ Asociación extremadamente fuerte

📌 Esto sugiere que estos productos se venden muy bien juntos. Podrían ofrecerse como un **set de colección** o incluirse en una **promoción conjunta**.

---

### 🧠 ¿Qué significan en la práctica?

| Métrica      | ¿Qué mide?                                          | ¿Cómo usarla?                                  |
|--------------|-----------------------------------------------------|------------------------------------------------|
| Soporte      | Frecuencia conjunta de A y B                        | Eliminar reglas muy poco frecuentes            |
| Confianza    | Probabilidad condicional de B dado A                | Evaluar la confiabilidad de la recomendación   |
| Lift         | Intensidad real de la relación entre A y B          | Priorizar asociaciones fuertes (lift > 1.5~2+) |

Estas métricas permiten priorizar reglas útiles para promociones, organización de productos o motores de recomendación.

---""")


elif page == "Referencias":
    st.title("📚 Fuentes y Referencias")
    st.markdown("""## 📚 Fuentes y Referencias

Este proyecto se apoyó en literatura académica y artículos especializados para fundamentar el uso de Market Basket Analysis y el algoritmo Apriori.

### Artículos y publicaciones:

1. **Halim, Octavia, & Alianto** (2019)  
   *Designing Facility Layout of an Amusement Arcade using Market Basket Analysis*  
   Procedia Computer Science, Vol 161, pp. 623–629  
   [Ver artículo](https://www.sciencedirect.com/science/article/pii/S1877050919318769)

2. **Maitra, Sarit** (2019)  
   *Association Rule Mining using Market Basket Analysis*  
   [Artículo en Towards Data Science](https://towardsdatascience.com/market-basket-analysis-knowledge-discovery-in-database-simplistic-approach-dc41659e1558)

3. **Subramanian, Dhilip** (2019)  
   *Association Discovery — the Apriori Algorithm*  
   [Artículo en Medium](https://medium.com/towards-artificial-intelligence/association-discovery-the-apriori-algorithm-28c1e71e0f04)

4. **Chauhan, Nagesh Singh** (2019)  
   *Market Basket Analysis*  
   [Artículo en Towards Data Science](https://towardsdatascience.com/market-basket-analysis-978ac064d8c6)

5. **Li, Susan** (2017)  
   *A Gentle Introduction on Market Basket Analysis — Association Rules*  
   [Artículo en Towards Data Science](https://towardsdatascience.com/a-gentle-introduction-on-market-basket-analysis-association-rules-fa4b986a40ce)

6. **UCI Machine Learning Repository**  
   *Online Retail II Dataset*  
   [Ver dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)""")
