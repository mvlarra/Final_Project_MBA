
import streamlit as st

def show_footer_interpretation(titulo, que_ves, que_significa, que_hacer, nota_profesor=None):
    """
    Muestra un bloque de interpretación para el gerente + nota técnica para el profesor.

    Parámetros:
    - titulo (str): Título general de la interpretación.
    - que_ves (str): Descripción de la visualización.
    - que_significa (str): Interpretación para el negocio.
    - que_hacer (str): Acción sugerida para el negocio.
    - nota_profesor (str, opcional): Nota técnica visible solo como aclaración en letra más chica.
    """
    st.markdown(f"""
    ---
    ### 🧠 {titulo}

    📊 **¿Qué estás viendo?**  
    {que_ves}

    💡 **¿Qué significa?**  
    {que_significa}

    🛍️ **¿Qué deberías hacer?**  
    {que_hacer}

    {"<div style='font-size:12px;color:gray;margin-top:10px;'>ℹ️ " + nota_profesor + "</div>" if nota_profesor else ""}
    """, unsafe_allow_html=True)


# ◯ Ejemplo de uso para sección: Reglas de Asociación
def footer_reglas_asociacion():
    show_footer_interpretation(
        titulo="Relaciones frecuentes entre productos",
        que_ves="Una tabla con reglas de asociación ordenadas por lift.",
        que_significa="Estas reglas revelan qué productos tienden a comprarse juntos de forma significativa.",
        que_hacer="Agrupar físicamente estos productos o sugerir promociones conjuntas.",
        nota_profesor="Esta sección utiliza el algoritmo Apriori (mlxtend) con soporte ≥ 0.01, confianza ≥ 0.2 y lift ≥ 2. Las reglas fueron filtradas y ordenadas por lift."
    )

# ◯ Ejemplo de uso para sección: Red de Productos
def footer_red_productos():
    show_footer_interpretation(
        titulo="Red de productos relacionados",
        que_ves="Un grafo que muestra productos conectados por reglas de asociación.",
        que_significa="Los nodos conectados tienen alta probabilidad de co-ocurrencia en una misma compra.",
        que_hacer="Usar esta información para decidir layout de góndolas o agrupación temática online.",
        nota_profesor="Visualización construida con NetworkX y Plotly. Las aristas representan reglas con lift > 2."
    )

# ◯ Ejemplo de uso para sección: Heatmap de Producto
def footer_heatmap():
    show_footer_interpretation(
        titulo="Interacciones cruzadas entre productos",
        que_ves="Un heatmap donde se observa qué productos aparecen juntos con mayor frecuencia.",
        que_significa="Las combinaciones con colores más intensos indican alta co-ocurrencia.",
        que_hacer="Colocar estos productos en promociones combinadas o bundles.",
        nota_profesor="Generado con seaborn. Matriz calculada a partir de la co-ocurrencia de productos binarizados."
    )

# ◯ Ejemplo para Recomendaciones para tu carrito
def footer_recomendaciones_carrito():
    show_footer_interpretation(
        titulo="Sugerencias personalizadas basadas en reglas de asociación",
        que_ves="Una lista de productos recomendados en base a los productos ya presentes en el carrito.",
        que_significa="Se identifican productos con alta probabilidad de ser comprados juntos según las reglas obtenidas.",
        que_hacer="Mostrar estos productos como recomendaciones dinámicas en el checkout o sugerencias contextuales.",
        nota_profesor="Utiliza reglas de asociación inversas aplicadas sobre los ítems seleccionados. Se aplican filtros por confianza y lift."
    )

# ◯ Ejemplo para sección: Canasta Real
def footer_canasta_real():
    show_footer_interpretation(
        titulo="Ejemplo real de una transacción",
        que_ves="Una tabla que muestra todos los productos comprados en una transacción real del dataset.",
        que_significa="Permite ver un patrón real de comportamiento de compra y su potencial para generar reglas.",
        que_hacer="Usar esta transacción como caso base para simular bundles o recomendaciones de productos relacionados.",
        nota_profesor="Esta sección muestra datos crudos no transformados con nombres de productos traducidos para facilitar su interpretación."
    )
