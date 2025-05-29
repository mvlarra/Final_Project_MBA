import streamlit as st

def show_explanation(vista):
    if vista == "📌 Reglas destacadas":
        st.markdown("""
        🧠 <b>¿Qué estás viendo?</b><br>
        Esta sección muestra un <b>resumen de las reglas más relevantes</b> encontradas a partir de las canastas de productos.<br>
        Se ordenan por un <i>score compuesto</i> que combina métricas como soporte, confianza y lift para priorizar las reglas más útiles para el negocio.
        """, unsafe_allow_html=True)

    elif vista == "🕸️ Red de productos":
        st.markdown("""
        🧠 <b>¿Qué estás viendo?</b><br>
        Esta red representa <b>conexiones visuales entre productos</b> frecuentemente comprados juntos.<br>
        Cada nodo es un producto, y los enlaces muestran reglas de asociación. El grosor indica la fuerza del vínculo según la métrica seleccionada.
        """, unsafe_allow_html=True)

    elif vista == "📊 Heatmap cruzado":
        st.markdown("""
        🧠 <b>¿Qué estás viendo?</b><br>
        Este heatmap muestra la <b>intensidad de asociación entre productos</b>.<br>
        Las filas corresponden a productos base, y las columnas a productos recomendados. El color representa qué tan fuerte es la relación entre ellos.
        """, unsafe_allow_html=True)

    elif vista == "📋 Tabla completa":
        st.markdown("""
        🧠 <b>¿Qué estás viendo?</b><br>
        Esta tabla muestra <b>todas las reglas de asociación generadas</b> sin filtros.<br>
        Es ideal para análisis detallado, auditoría o exportación de reglas para otros fines.
        """, unsafe_allow_html=True)
