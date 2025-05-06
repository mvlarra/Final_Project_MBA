
import os
port = os.environ.get("PORT", 8501)

import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import pickle
from PIL import Image


# Configuración inicial
st.set_page_config(page_title="Market Basket Analysis", page_icon="🛒", layout="wide")
logo = Image.open("app/images/IMG.png") # Imagen en el sidebar
st.sidebar.image(logo,  use_container_width=True)
st.sidebar.markdown("### Retail Market Basket Analysis", unsafe_allow_html=True)


# Sidebar de navegación
page = st.sidebar.radio("Navegación", [
    "Introducción", 
    "📘 ¿Qué es Market Basket Analysis?",
    "🎯 Objetivo del MBA",
    "🔗 Reglas de Asociación",
    "⚙️ Algoritmo Apriori",
    "✅ Ventajas del MBA",
    "🛍️ Perspectiva del Cliente",
    "📦 El Dataset",
    "📊 Reglas en acción",
    "✔️ Introducción",
    "✔️ Goals",
    "✔️ Methodology",
    "✔️ Key Metrics",
    "✔️ Top 5 Association Rules",
    "✔️ Top 5 Cross-Selling Products",
    "✔️ Recommendations",
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
    st.title("🛒 Market Basket Analysis")
    st.markdown("""
    **Introduccion**
    Atualmente, el **Machine Learning** está ayudando a la industria del retail de muchas formas. Desde predecir el rendimiento de las ventas hasta identificar patrones de compra de los clientes, existen múltiples aplicaciones del aprendizaje automático en este sector.
    Una de las más destacadas es el **Market Basket Analysis** (Análisis de Canasta de Compras), una técnica que analiza el comportamiento de compra histórico para descubrir **qué productos suelen adquirirse juntos con frecuencia**.
    Esto permite a los negocios:
        - Ofrecer recomendaciones personalizadas
        - Diseñar promociones combinadas efectivas
        - Optimizar la organización del catálogo online o físico

    A través de esta app interactiva, exploraremos estas combinaciones frecuentes utilizando el algoritmo **Apriori**, generaremos reglas de asociación interpretables y propondremos acciones prácticas basadas en los resultados.
    """)

# Pagina: Que es el Market Basket Analysis?
elif page == "📘 ¿Qué es Market Basket Analysis?":
    st.title("📘 ¿Qué es Market Basket Analysis?")
    st.image("app/images/Img1.png", width=200)
    st.markdown("""
    Cuando vamos al supermercado o compramos en línea, solemos adquirir todos los artículos que necesitamos en una sola compra.  
    Podemos definir una canasta de compras como un conjunto de artículos que una persona agrupa y compra en una sola transacción.

    Este proceso permite identificar los hábitos de compra del cliente al encontrar asociaciones entre productos colocados juntos en su “canasta”.  
    Esto ayuda a los minoristas a diseñar mejores estrategias de marketing.

    Ejemplo: si un cliente compra leche, ¿qué tan probable es que también compre pan? Esta información ayuda a hacer promociones más efectivas y organizar mejor los productos.
        """)


elif page == "🎯 Objetivo del MBA":
    st.title("🎯 Objetivo del Market Basket Analysis")
    st.markdown("""
    **Venta cruzada (Cross Selling):** Recomendar productos relacionados para que el cliente gaste más.

    **Ubicación de productos (Product Placement):** Agrupar productos complementarios juntos en la góndola, como leche seguida de manteca y harina.  
    Esto sigue un planograma, que es un modelo para maximizar ventas con la ubicación física de productos.
    """)


elif page == "🔗 Reglas de Asociación":
    st.title("🔗 ¿Qué son las Reglas de Asociación?")
    st.markdown("""
    Las reglas de asociación identifican patrones frecuentes en transacciones, usando métricas como soporte, confianza y lift.

#### Ejemplo:
- 100 clientes
- 10 compraron leche, 8 manteca, 6 ambos

- Soporte = 6/100 = 0.06  
- Confianza = 0.06 / 0.08 = 0.75  
- Lift = 0.75 / 0.10 = 7.5
    """)


elif page == "⚙️ Algoritmo Apriori":
    st.title("⚙️ Algoritmo Apriori")
    st.markdown("""
    El algoritmo Apriori identifica combinaciones frecuentes de productos usando soporte y confianza.

    - Lift = 1 → sin relación  
    - Lift > 1 → correlación positiva  
    - Lift < 1 → correlación negativa

    ❗ Limitación: requiere muchas pasadas por la base de datos, lo que puede ser costoso en tiempo.
    """)


elif page == "✅ Ventajas del MBA":
    st.title("✅ Ventajas del Market Basket Analysis")
    st.markdown("""
    1. Aumenta la interacción del cliente  
    2. Mejora ventas y ROI  
    3. Optimiza campañas de marketing  
    4. Mejora la experiencia del cliente  
    5. Ayuda a entender al cliente  
    6. Identifica patrones de compra
    """)


elif page == "🛍️ Perspectiva del Cliente":
    st.title("🛍️ ¿Cómo se ve desde la perspectiva del cliente?")
    st.image("app/images/Img3.png", width=300)
    st.markdown("""
    Ejemplo: Amazon muestra productos frecuentemente comprados juntos.  
    Esto simula la experiencia de un supermercado virtual, recomendando artículos relevantes y aumentando la satisfacción.
    """)


elif page == "📦 El Dataset":
    st.title("📦 El Dataset")
    st.markdown("""
    Se usó un dataset con 7501 transacciones y 120 productos.  
    - Producto más comprado: agua mineral  
    - Menos comprado: espárrago

    [Ver dataset](https://github.com/Debasishsaha123/MARKET-BASKET-ANALYSIS/blob/main/Market_Basket_Optimisation%20(1).csv)

    ```python
    all_items = data.melt()["value"].dropna().sort_values()
    print(f"There were {all_items.nunique()} different products:\n", all_items.unique())
    ```
    """)


elif page == "📊 Reglas en acción":
    st.title("📊 Aplicación de Reglas")
    st.markdown("""
    Se usó Apriori con `min_support = 0.1`.  
    Se filtraron reglas con `lift >= 1.2`.

    Ejemplo fuerte:  
    - Antecedente: herb & pepper  
    - Consecuente: ground beef  
    - Lift ≈ 2.5  
    - Conviction > 1

    También se encontró alta relación entre ground beef y spaghetti, vino tinto y aceite de oliva.
    """)





if page == "✔️ Introducción":
    st.title("✔️ Introducción")
    st.markdown("""
Market Basket Analysis is a data mining technique employed to discover relationships and patterns within large datasets, particularly in the context of market analysis. By identifying frequently co-occurring items in transactions, businesses can gain valuable insights into customer behavior, optimize product placement, and enhance overall marketing strategies.
    """)

elif page == "✔️ Goals":
    st.title("✔️ Goals")
    st.markdown("""
**Association Rule Discovery:**  
Identify associations and correlations among products or items in a dataset. Discover rules that indicate the likelihood of certain items being bought together.

**Cross-Selling Opportunities:**  
Uncover opportunities for cross-selling by understanding which products are frequently purchased together.

**Promotion Planning:**  
Optimize promotional campaigns by identifying items that are frequently bought together. Design effective promotions and discounts to incentivize the purchase of complementary products.

**Optimizing Product Layout:**  
Arrange products in-store or online in a way that encourages the purchase of related items, creating a more convenient and satisfying shopping experience.
    """)

elif page == "✔️ Methodology":
    st.title("✔️ Methodology")
    st.markdown("""
**Data Source:**  
The data is sourced from **Online Retail II**, which encompasses transactions from a UK-based online retailer (Dec 1, 2009 – Dec 9, 2011), specializing in giftware.

**Algorithm Used:**  
We utilize the **Apriori algorithm** from the `mlxtend` library to extract frequent itemsets and association rules using support and confidence thresholds.

**Parameters:**
- **Maximum Combination Length:** 2 items (focus on pairs)
- **Minimum Co-Occurrence Support Threshold:** 0.5%
    """)

elif page == "✔️ Key Metrics":
    st.title("✔️ Key Metrics")
    st.markdown("""
### Support  
The proportion of transactions that contain a specific itemset.  
- Item Support = Transactions with A / Total transactions  
- Co-occurrence Support = Transactions with A and B / Total transactions

### Confidence  
The conditional probability that a transaction containing item A also contains item B.  
- Confidence(A→B) = Support(A∪B) / Support(A) × 100%  
- Confidence(B→A) = Support(A∪B) / Support(B) × 100%

### Lift  
Measures how much more likely B is bought with A compared to random chance.  
- Lift(A→B) = Support(A∪B) / (Support(A) × Support(B))

### Leverage  
Difference between observed and expected frequency of A and B together.  
- Leverage(A→B) = Support(A∪B) − (Support(A) × Support(B))

### Conviction  
Indicates the likelihood the rule is incorrect.  
- Conviction(A→B) = (1−Support(B)) / (1−Confidence(A→B))  
- Conviction(B→A) = (1−Support(A)) / (1−Confidence(B→A))
    """)

elif page == "✔️ Top 5 Association Rules":
    st.title("✔️ Top 5 Association Rules")
    try:
        df = pd.read_csv("app/models/association_rules_final.csv")
        top5 = df.sort_values(by=["lift", "confidence", "support"], ascending=False).head(5)
        st.markdown("""
        While evaluating association rules, we utilize key metrics such as support, confidence, and lift to discern their significance. Each rule is independently ranked based on these metrics, and a mean rank is computed across all three rankings. This mean rank serves as a composite score, capturing the overall performance of each rule across the different metrics.
        The table below shows the top 5 association rules based on the composite score.
        """)
        st.dataframe(top5)
    except Exception as e:
        st.error(f"Error loading rules: {e}")

elif page == "✔️ Top 5 Cross-Selling Products":
    st.title("✔️ Top 5 Cross-Selling Products")
    try:
        df = pd.read_csv("app/models/association_rules_final.csv")
        df["score"] = df["confidence"] + df["support"].str.replace("%", "").astype(float)
        top5 = df.sort_values(by="score", ascending=False).head(5)
        st.markdown("""
        Cross-selling involves identifying products frequently purchased together, gauged by high support reflecting their co-occurrence in transactions. The concept considers not only the frequency of joint purchases but also the strength of these associations measured by confidence.
        
        Focusing on product combinations with both high support and confidence helps pinpoint reliably associated items, enabling businesses to strategically promote or bundle products for an enhanced customer shopping experience.

        The table below shows the top 5 cross-selling-product sorted by their mean confidence and support:                
        """)
        st.dataframe(top5[["antecedents", "consequents", "support", "confidence", "lift"]])
    except Exception as e:
        st.error(f"Error loading rules: {e}")

elif page == "✔️ Recommendations":
    st.title("✔️ Recommendations")
    st.markdown("""
    Pairs of items highly recommended for bundling or being displayed together based on strong association rules.
    """)
    try:
        df = pd.read_csv("app/models/association_rules_final.csv")
        for i, row in df.iterrows():
            st.markdown(f"#### 🔗 {i+1}. `{row['antecedents']} → {row['consequents']}`")
            st.markdown(f"\- **Support:** {row['support']}")
            st.markdown(f"\- **Confidence:** {round(float(row['confidence']) * 100, 2)}%")
            st.markdown(f"\- **Lift:** {round(float(row['lift']), 2)}")
    except Exception as e:
        st.error(f"Error displaying recommendations: {e}")


elif page == "Referencias":
    st.title("📚 Fuentes y Referencias")
    st.markdown("""## 📚 Fuentes y Referencias

    Este proyecto se apoyó en literatura académica y artículos especializados para fundamentar el uso de Market Basket Analysis y el algoritmo Apriori.

    Artículos y publicaciones:

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
    [Ver dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
    """)