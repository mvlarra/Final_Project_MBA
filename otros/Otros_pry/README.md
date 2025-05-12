
# 🛍️ Proyecto Final: Análisis de Cestas de Mercado (Market Basket Analysis)

**Abril 2025**

Este proyecto aborda el análisis de combinaciones de productos frecuentes (productos que se venden en conjunto) utilizando datos de transacciones históricas de una tienda online. Su objetivo es descubrir combinaciones frecuentes de productos adquiridos por los clientes, con el fin de generar recomendaciones comerciales inteligentes, optimizar promociones y mejorar la disposición de productos tanto online como en tienda física.

---

## 🎯 Objetivo del Proyecto

A través del análisis de reglas de asociación (Market Basket Analysis), buscamos responder:

> ¿Qué productos se compran frecuentemente juntos?

Esto permite tomar decisiones basadas en datos, tales como:

- **Sugerencias automáticas:** Ej. si un cliente añade una tetera, sugerir tazas de té.
- **Promociones combinadas:** Descuentos para ítems como papel de regalo y tarjetas.
- **Organización de la tienda:** Agrupar combinaciones de productos frecuentes.
- **Email marketing personalizado:** Recomendar productos complementarios según historial.
- **Optimización de inventario:** Preparar stock para productos que se venden en conjunto.

---

## 💻 Aplicación Interactiva: Market Basket App

Se desarrolló una aplicación con Streamlit para explorar los resultados del análisis de reglas de asociación usando el algoritmo **Apriori**. La app incluye visualizaciones interpretadas y recomendaciones accionables listas para ejecutar.

### 🧭 Funcionalidades principales

| Sección                    | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **Introducción**          | Contexto y propósito del análisis                                           |
| **Dataset**               | Vista previa del dataset binarizado por transacción/producto               |
| **Conjuntos Frecuentes**  | Productos que suelen aparecer juntos con frecuencia (Apriori)              |
| **Reglas de Asociación**  | Relaciones descubiertas entre productos con soporte, confianza y lift       |
| **Recomendaciones**       | Interpretación narrativa y acción sugerida basada en reglas destacadas     |

---

## 🔍 Ejemplo de salida interpretada

```markdown
### 1. Regla: `roses regency teacup and saucer → green regency teacup and saucer`

- **Soporte**: 3.1%
- **Confianza**: 71.0%
- **Lift**: 17.72

✅ Esta es una regla muy útil.

📌 Acción recomendada:  
*Product bundling* – ofrecer ambos productos como un set de colección.
```

---

## ⚙️ Requisitos del Proyecto

- Python 3.8 o superior
- Dependencias principales:
  - Streamlit
  - pandas
  - mlxtend
  - pickle (o joblib)

Instalación recomendada:

```bash
pip install -r app/requirements.txt
```

---

## ▶️ Instrucciones para uso local

```bash
cd app
streamlit run market_basket_nav_app.py
```

Asegúrate de tener cargado el archivo `basket.pkl` en `app/models/`.

---

## ☁️ Despliegue en Render.com

Este proyecto está preparado para desplegarse automáticamente usando GitHub + Render.

### Comando de ejecución en entorno Render:

```bash
streamlit run app/market_basket_nav_app.py --server.port=$PORT --server.address=0.0.0.0
```

Cualquier `push` al repositorio activa un redeploy automático en Render.com.

---

## 📂 Estructura del Proyecto

```
Final_Project_MBA/
├── app/
│   ├── models/
│   │   ├── basket.pkl
│   │   └── association_rules_final.csv
│   ├── market_basket_nav_app.py
│   └── requirements.txt
├── data/
│   └── raw/
│       └── data.csv
├── notebooks/
│   └── Final_Project_Market_Basket_Analysis_VL.ipynb
└── README.md
```


---


## 📐 Métricas de Evaluación de Reglas de Asociación

Las reglas de asociación permiten descubrir combinaciones de productos frecuentes (productos que se venden en conjunto). Estas reglas se generan a partir de conjuntos frecuentes mediante el algoritmo Apriori.

Cada regla tiene **un antecedente (producto A)** y **un consecuente (producto B)**, y se evalúa con tres métricas principales:

---

### 🔹 Soporte (Support)

Indica la **frecuencia con la que ambos productos (A y B) aparecen juntos** en todas las transacciones.

\[
\text{Soporte}(A \rightarrow B) = \frac{\text{# transacciones con A y B}}{\text{total de transacciones}}
\]

🔍 **Interpretación:**  
Un soporte de 0.031 significa que el 3.1% de todas las transacciones contienen esa combinación de productos.

---

### 🔹 Confianza (Confidence)

Es la **probabilidad de que un cliente compre B dado que ya compró A**.

\[
\text{Confianza}(A \rightarrow B) = \frac{\text{# transacciones con A y B}}{\text{# transacciones con A}}
\]

🔍 **Interpretación:**  
Una confianza de 0.70 implica que el 70% de quienes compraron A también compraron B.

---

### 🔹 Elevación (Lift)

Mide la **fuerza de la relación** entre A y B. Compara la confianza con la frecuencia independiente de B.  

\[
\text{Lift}(A \rightarrow B) = \frac{\text{Confianza}(A \rightarrow B)}{\text{Soporte}(B)}
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

---


---


## 📚 Fuentes y Referencias

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
   [Ver dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
