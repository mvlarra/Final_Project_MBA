# 🛠️ Instrucciones Técnicas — Market Basket Analysis

Este archivo detalla cómo ejecutar, entender y modificar esta app de análisis de canasta de productos construida en Python y Streamlit.

---

## 📁 Estructura del Proyecto

```bash
Final_Project_MBA/
│
├── app.py                     # Archivo principal para ejecutar la app Streamlit
├── requirements.txt          # Librerías necesarias
├── devcontainer.json         # Configuración para GitHub Codespaces / Docker
├── /data/processed/          # CSVs con reglas y bundles procesados
├── /sections/                # Código modular por sección (about, metodología, reglas, etc.)
├── /charts/                  # Gráficos reutilizables (heatmap, redes, etc.)
├── /utils/                   # Funciones auxiliares (loaders, visual helpers)
├── /docs/ENTREGA_FINAL.md    # Entrega final del proyecto con capturas y resumen
└── /docs/img/                # Imágenes utilizadas en el markdown de entrega
```

---

## ⚙️ Requisitos del sistema

- Python 3.11+
- Docker (opcional, recomendado)
- GitHub Codespaces (opcional)
- Navegador web moderno

---

## 📦 Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/mvlarra/Final_Project_MBA.git
cd Final_Project_MBA
```

### 2. Crear entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la app

```bash
streamlit run app.py
```

---

## 🚀 Despliegue

Esta app ya se encuentra desplegada en [Render](https://market-basket-analysis-xb0x.onrender.com/).\
No requiere instalación para visualizar su funcionamiento.

---

## 🧪 Datos utilizados

Dataset original: **Online Retail Dataset (UCI)**\
Transformado a formato `Factura x Producto`, binarizado para aplicar el algoritmo Apriori.

Archivos intermedios:

- `summary_rules.csv`: reglas generadas y filtradas
- `bundle_products.csv`: agrupamientos descubiertos tipo bundle
- `tabular_bundle.csv`: matriz tabular de productos

---

## 🧰 Librerías clave

- `mlxtend`: algoritmo Apriori
- `pandas`, `numpy`: manipulación de datos
- `plotly`, `networkx`, `matplotlib`: visualizaciones
- `streamlit`: interfaz interactiva web

---

## 📌 Notas adicionales

- El archivo `app.py` está diseñado para Streamlit y es compatible con despliegue automático en Render.
- Para modificar o agregar nuevas secciones, editá los archivos en `/sections/` y sumalos a `app.py`.
- La app carga los datos desde `/data/processed/`. Asegurate de mantener esos archivos actualizados si regenerás reglas.

---

## 👤 Autor

Desarrollado por [Valentina Larrañaga](https://www.linkedin.com/in/valentinalarra/) como proyecto final del Bootcamp de Data Science & Machine Learning en 4Geeks Academy.

