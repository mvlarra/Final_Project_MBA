# 🛒 Market Basket Analysis — Streamlit App for Retail

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![mlxtend](https://img.shields.io/badge/Apriori-mlxtend-orange)
![Retail](https://img.shields.io/badge/Retail-Analytics-teal)
![Status](https://img.shields.io/badge/Deployed-Render-green)

---

<p align="center">
  <a href="https://market-basket-analysis-xb0x.onrender.com" target="_blank">
    <img src="https://raw.githubusercontent.com/mvlarra/Final_Project_MBA/main/app/images/Img_0.png" alt="Preview" width="200">
  </a>
</p>

<p align="center">
  🔗 <strong><a href="https://market-basket-analysis-xb0x.onrender.com" target="_blank">Abrir la app interactiva en vivo →</a></strong>
</p>

---

**Repositorio del proyecto final** del bootcamp de *Data Science & Machine Learning* de 4Geeks Academy.  
Esta app interactiva permite analizar transacciones reales de retail para generar recomendaciones personalizadas, descubrir patrones frecuentes y proponer acciones comerciales accionables.

---

Desarrollado por: **Valentina Larrañaga**\
App interactiva: [🔗 Ver app en vivo](https://market-basket-analysis-xb0x.onrender.com/)\
Repositorio GitHub: [📁 Ir al repositorio](https://github.com/mvlarra/Final_Project_MBA)

---

## 📘 Resumen del Proyecto

Este proyecto aplica técnicas de Market Basket Analysis para detectar patrones de compra frecuentes y proponer estrategias comerciales accionables en el contexto de retail.

---

## 🎯 Objetivo del proyecto

- Detectar asociaciones entre productos frecuentemente comprados juntos.
- Diseñar recomendaciones personalizadas.
- Proponer acciones comerciales para aumentar el ticket promedio.

---

## 🔎 Metodología aplicada

- Dataset real de transacciones online (UK, 2010–2011)
- Algoritmo: **Apriori** (`mlxtend`)
- Generación de matriz binaria `Factura x Producto`
- Filtros aplicados: soporte ≥ 1%, confianza ≥ 20%, lift ≥ 2

---

## 📊 Exploraciones y Reglas

- Visualización de productos más vendidos, transacciones por mes, ejemplo real de canasta.
- Reglas de asociación exploradas en red, tabla y heatmap.
- Reglas clave: confianza > 70%, lift > 20.

---

### 🖼️ Capturas de la App

#### 🏠 Acerca del Proyecto
>![Acerca del Proyecto](docs/img/1_home.png)


#### 📊 Exploración de Datos
>![Exploración de Datos](docs/img/2_exploracion.png)

#### 🔗 Reglas de Asociación

##### 🗺️ Red de productos
>![Red de Productos](docs/img/3_Red_de_Productos.png)

##### 📋 Tabla de reglas generadas
>![Tabla de Reglas](docs/img/3_Tabla_de_Reglas.png)

##### 🏆 Top 5 reglas por score
>![Top 5 Reglas](docs/img/3_Top5_by_Score.png)

##### ♨️ Heatmap de asociación
>![Heatmap](docs/img/3_Headmap.png)

#### 🛍 Recomendaciones Personalizadas
>![Recomendaciones](docs/img/4_recomendaciones.png)

#### 📌 Heatmap por Producto

##### 🎯 Relación con otros productos
>![Heatmap Co-ocurrencia](docs/img/5_Headmap_Co-ocurrencia.png)

##### 📍 Sugerencia de ubicación o agrupación
>![Sugerencia Ubicación](docs/img/5_Headmap_Co-ocurrencia_2.png)


#### 💼 Acciones Estratégicas


##### 🧩 Sugerencias agrupadas por tipo
>![Acciones sugeridas](docs/img/6_acciones_sugeridas.png)

##### 🧾 Acciones seleccionadas y plan descargable
>![Acciones seleccionadas](docs/img/6_acciones_seleccionadas.png)



#### 📋 Conclusiones y Resultados
>![Conclusiones](docs/img/7_conclusiones.png)



---

## 🛍️ Recomendaciones y Acciones Estratégicas

- Recomendaciones personalizadas por producto
- Heatmap para analizar asociaciones por soporte, confianza o lift
- Sugerencias de bundles, promociones cruzadas, rediseño de layout y acciones operativas

---

## 📋 Conclusiones y aprendizajes

Este proyecto permitió aplicar técnicas de análisis de canasta de productos con un enfoque práctico y orientado al negocio.

Se logró:
- Detectar reglas de asociación con alta confianza (hasta 76%) y lift mayor a 20
- Generar bundles reales y recomendaciones personalizadas con base estadística
- Transformar hallazgos en acciones estratégicas agrupadas, priorizables y exportables
- Desarrollar una app interactiva, clara y profesional, pensada para tomadores de decisión

💡 Todo esto sobre un dataset real del sector retail y utilizando herramientas 100% open source.

---

## 🛠️ Instrucciones Técnicas

### 📁 Estructura del Proyecto

```bash
Final_Project_MBA/
│
├── app.py                    # Archivo principal para ejecutar la app Streamlit
├── requirements.txt          # Librerías necesarias
├── devcontainer.json         # Configuración para GitHub Codespaces / Docker
├── /data/processed/          # CSVs con reglas y bundles procesados
├── /sections/                # Código modular por sección (about, metodología, reglas, etc.)
├── /charts/                  # Gráficos reutilizables (heatmap, redes, etc.)
├── /utils/                   # Funciones auxiliares (loaders, visual helpers)
└── /docs/img/                # Carpeta para capturas
```

### ⚙️ Requisitos del sistema

- Python 3.11+
- Docker (opcional, recomendado)
- GitHub Codespaces (opcional)
- Navegador web moderno

### 📦 Instalación local

```bash
# 1. Clonar el repositorio
git clone https://github.com/mvlarra/Final_Project_MBA.git
cd Final_Project_MBA

# 2. Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la app
streamlit run app.py
```

### 🚀 Despliegue

La app está desplegada en [Render](https://market-basket-analysis-xb0x.onrender.com/) y puede visualizarse sin instalar nada.

### 🧪 Datos utilizados

- Dataset original: **Online Retail Dataset (UCI)**
- Procesado a formato `Factura x Producto`
- Archivos clave:
  - `summary_rules.csv`
  - `bundle_products.csv`
  - `tabular_bundle.csv`

### 🧰 Librerías clave

- `mlxtend`: reglas de asociación (Apriori)
- `pandas`, `numpy`: manipulación de datos
- `plotly`, `networkx`, `matplotlib`: visualizaciones
- `streamlit`: app interactiva

### 📌 Notas para desarrollo

- `app.py` es el punto de entrada de la app (usado por Render)
- Podés modificar secciones editando `/sections/*.py`
- Los datos están en `/data/processed/`

---

## 👤 Autor y Créditos

Desarrollado por [Valentina Larrañaga](https://www.linkedin.com/in/valentinalarranaga)  
Bootcamp de Data Science & Machine Learning — 4Geeks Academy

