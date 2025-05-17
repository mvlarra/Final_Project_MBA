# ✅ Antes del Deploy a Render.com

Guía de verificacion para asegurar compatibilidad de la app Streamlit en Render.com.

---

## 📅 Revisión hasta el Paso 41

### ✅ Todo lo que **es compatible** con Render.com

| Elemento                              | ¿Funciona en Render? | Comentario breve                                             |
| ------------------------------------- | -------------------- | ------------------------------------------------------------ |
| `ProductNetwork`, `RulesGraphManager` | ✅ Sí                 | Son clases propias de Python, sin dependencias problemáticas |
| `pandas`, `numpy`, `plotly.express`   | ✅ Sí                 | Común en data apps                                           |
| `mlxtend`, `networkx`, `copy`, `json` | ✅ Sí                 | Todo funciona bien                                           |
| `streamlit-echarts` (`st_echarts`)    | ✅ Sí                 | Recomendado para visualización de grafos                     |

---

### ⚠️ Elementos que **no funcionan** o requieren atención

| Elemento                         | ¿Funciona en Render? | Detalles & Recomendación                                    |
| -------------------------------- | -------------------- | ----------------------------------------------------------- |
| `JupyterEcharts(...)`            | ❌ No                 | Solo funciona en notebooks (Jupyter/Colab)                  |
| `JupyterEcharts.show(...)`       | ❌ No                 | Usar `st_echarts()` en su lugar                             |
| Markdown con `![img](...)`       | ⚠️ Depende           | Streamlit no renderiza markdown con rutas locales de imagen |
| Imágenes estáticas en `/images/` | ⚠️ Depende           | Asegurar que se muestren con `st.image()`                   |

---

## 🔧 Recomendaciones prácticas

1. 🔄 Reemplazá todos los `JupyterEcharts(...)` por `st_echarts(...)`

2. 🖼️ Mostrá imágenes así en Streamlit:

   ```python
   st.image("app/images/product_network.png", caption="Red de productos por profundidad")
   ```

3. 🗃️ Organizá tus archivos:

   * Código en `/app/`
   * Datos en `/data/`
   * Imágenes en `/app/images/`

4. 🔢 Verificá `requirements.txt`:

   ```text
   streamlit
   streamlit-echarts
   mlxtend
   pandas
   numpy
   plotly
   networkx
   ```

---

## ✅ Validaciones post-deploy

Verificá lo siguiente después de hacer deploy en Render:

* 🔗 La app carga correctamente en la URL de Render
* 🚫 No hay errores en la consola de logs (Render → Logs)
* 🖼️ Las imágenes se visualizan con `st.image()`
* 📊 Los gráficos de red generados con `st_echarts()` se muestran bien e interactúan sin errores
* ⏱️ La carga general no demora más de 10–15 segundos en iniciar (puede depender del plan)
* 📤 Los archivos que se suben (si hay inputs) no exceden el límite de tamaño
* 🔁 Navegar entre secciones del sidebar funciona sin resets inesperados

---
Usalo como checklist final antes de hacer el deploy en Render.com ✈️


### 📌 Nota técnica: Uso opcional de Kaleido para exportar imágenes estáticas con Plotly

Kaleido es una herramienta gratuita y open source que permite exportar gráficos de Plotly como imágenes estáticas (PNG, PDF, SVG, EPS).

#### ✅ ¿Por qué usarlo?

* Ideal para generar gráficos listos para informes, presentaciones o para mostrar en Streamlit con `st.image()`

#### 📦 Instalación

```bash
pip install kaleido
```

Agregá esta línea en tu `requirements.txt`:

```
kaleido>=0.2.1
```

#### 🧲 Verificación opcional en el entorno

```python
try:
    import kaleido
    print("✅ Kaleido está instalado y listo para exportar imágenes.")
except ImportError:
    print("⚠️ Kaleido no está instalado. Ejecutá: pip install kaleido")
```

---

### 📌 Nota técnica: Uso opcional de `streamlit-echarts` para visualización interactiva

Permite mostrar gráficos tipo red (como grafos de productos) en una app de Streamlit, usando la librería ECharts.

#### 📦 Instalación

```bash
pip install streamlit-echarts
```

Agregá esta línea en `requirements.txt`:

```
streamlit-echarts>=0.4.0
```

#### 🧲 Ejemplo de uso

```python
from streamlit_echarts import st_echarts

st.subheader("🔗 Red de productos relacionados")
st_echarts(option_dict, height="600px")
```

---

### 📌 Nota técnica: Uso opcional de Matplotlib para gráficos rápidos

Aunque Plotly es interactivo, Matplotlib es útil para visualizaciones simples o exportables en entornos sin navegador.

#### 📦 Instalación

```bash
pip install matplotlib
```

Agregá esta línea en `requirements.txt`:

```
matplotlib>=3.7.1
```

#### 🧲 Ejemplo de uso

```python
import matplotlib.pyplot as plt

plt.hist(df['support'])
plt.title("Distribución del soporte")
plt.show()
```

---

### 📌 Nota técnica: Despliegue de tu app Streamlit en Render.com

Render.com es ideal para desplegar dashboards interactivos construidos con Streamlit.

#### ✅ Requisitos:

* Archivo principal: `/app/market_basket_nav_app.py`
* Dependencias: `requirements.txt`
* Comando de inicio:

```
streamlit run app/market_basket_nav_app.py
```

#### 📁 Organización sugerida del proyecto:

```
/app/               → app Streamlit  
/app/images/        → imágenes estáticas  
/app/models/        → archivos auxiliares  
/data/processed/    → datasets traducidos  
requirements.txt    → dependencias
```

#### ⚠️ Consideraciones para el Free Tier:

* Tiempo de inactividad por falta de tráfico
* Límite de tamaño de archivos estáticos (≈100 MB)
* Mejor subir imágenes ya generadas que depender de exportación en tiempo real

#### 🔍 Debugging:

Accedé a la pestaña “Logs” en tu servicio Render para ver errores o trazas de ejecución.

📖 Más info: [https://render.com/docs/deploy-streamlit](https://render.com/docs/deploy-streamlit)