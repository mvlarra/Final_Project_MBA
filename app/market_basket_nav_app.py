
import os
port = os.environ.get("PORT", 8501)

import streamlit as st
import pandas as pd

# Configuración inicial
st.set_page_config(page_title="Recomendaciones MBA", page_icon="🛍️", layout="wide")

# Sidebar de navegación
page = st.sidebar.radio("Navegación", [
    "Introducción", 
    "Recomendaciones Fijas"
])

# Página: Introducción
if page == "Introducción":
    st.title("🛍️ Reglas de Asociación Más Relevantes")
    st.markdown("""
    Esta sección presenta las reglas más útiles obtenidas del análisis de Market Basket realizado previamente.

    Se muestran reglas con alta confianza y/o lift, acompañadas de una interpretación automática y sugerencias de acción comercial.
    """)

# Página: Recomendaciones Fijas
elif page == "Recomendaciones Fijas":
    st.title("🎯 Recomendaciones Destacadas (desde archivo)")

    try:
        path = "app/models/association_rules_final.csv"
        rules = pd.read_csv(path)
    except FileNotFoundError:
        st.error("❌ No se encontró 'association_rules_final.csv' en app/models.")
        st.stop()

    def interpretar_regla(row, idx):
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
        st.markdown(interpretar_regla(row, i))
