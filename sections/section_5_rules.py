# ◯ SECTION 5 – EXPLORAR REGLAS DE ASOCIACIÓN
# Objetivo:
#   Permitir al usuario explorar de manera interactiva las reglas de asociación generadas mediante Apriori.
# Contenido:
#   - Reglas destacadas con mayor score
#   - Red de relaciones entre productos
#   - Heatmap cruzado entre productos
#   - Tabla completa de todas las reglas generadas

import streamlit as st
import plotly.graph_objects as go
import networkx as nx
from charts.HeatmapXTab import draw_heatmap
from utils.show_explanation import show_explanation


# ◯ Seccion 5: EXPLORAR REGLAS DE ASOCIACIÓN (unificada)
# ............................................................................................

def show_section_5_rules(rules, tabular, Top_5_Rules_by_Score):
    """
    Muestra la sección de exploración de reglas de asociación generadas mediante Apriori.           
    Permite al usuario interactuar con diferentes visualizaciones y métricas para entender las relaciones entre productos.
    :param rules: DataFrame con las reglas de asociación generadas.
    :param tabular: DataFrame con las reglas en formato tabular.
    :param Top_5_Rules_by_Score: DataFrame con las 5 reglas destacadas por score.
    """

    st.title("🔎 Explorar Reglas de Asociación")

    st.markdown("""
    Elegí una forma de visualizar las reglas de asociación generadas a partir de las canastas de productos.  
    Podés alternar entre diferentes perspectivas para entender mejor los patrones de compra.
    """)

    opcion_vista = st.radio(
        "Elegí cómo querés explorar las reglas:",
        ["📌 Reglas destacadas", "🗺️ Red de productos", "📊 Heatmap cruzado", "📋 Tabla completa"],
        horizontal=True
    )

    # Mostrar explicación específica
    show_explanation(opcion_vista)

    if opcion_vista == "📌 Reglas destacadas":
        st.subheader("📌 Reglas con mayor score (lift + soporte + confianza)")
        st.dataframe(Top_5_Rules_by_Score, use_container_width=True)

    elif opcion_vista == "🗺️ Red de productos":
        st.subheader("🗺️ Red de Relaciones entre Productos")
        st.markdown("""
        Esta visualización muestra cómo se conectan los productos entre sí a partir de reglas de asociación. 
        Cada nodo representa un producto, y los enlaces indican que se suelen comprar juntos. 
        El grosor del enlace refleja la **fuerza de la relación** según la métrica seleccionada.
        """)

        # ◯ Elegir métrica para evaluar relaciones
        metrica = st.selectbox("🔍 Elegí la métrica de relación:", ["lift", "confidence", "support"])

        # ◯ Filtro por valor mínimo
        valor_minimo = st.slider(f"🔧 Filtrar relaciones con {metrica} mayor a:", min_value=0.0, max_value=5.0, value=1.2, step=0.1)

        # ◯ Filtrar reglas por métrica seleccionada
        reglas_filtradas = rules[rules[metrica] >= valor_minimo]

        # ◯ Mostrar solo las N relaciones más fuertes
        top_n = st.slider("🔢 ¿Cuántas relaciones querés visualizar?", min_value=10, max_value=100, value=50, step=5)
        reglas_top = reglas_filtradas.nlargest(top_n, metrica)

        if reglas_top.empty:
            st.warning("⚠️ No hay relaciones que cumplan con estos filtros.")
        else:
            # ◯ Crear grafo dirigido
            G = nx.DiGraph()

            for _, row in reglas_top.iterrows():
                origen = row['antecedents'][0] if isinstance(row['antecedents'], list) else row['antecedents']
                destino = row['consequents'][0] if isinstance(row['consequents'], list) else row['consequents']
                peso = row[metrica]
                G.add_node(origen)
                G.add_node(destino)
                G.add_edge(origen, destino, weight=peso)

            pos = nx.spring_layout(G, k=0.5, iterations=50)

            edge_x, edge_y = [], []
            for edge in G.edges():
                x0, y0 = pos[edge[0]]
                x1, y1 = pos[edge[1]]
                edge_x.extend([x0, x1, None])
                edge_y.extend([y0, y1, None])

            edge_trace = go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=1.5, color='gray'),
                hoverinfo='none',
                mode='lines'
            )

            node_x, node_y, texts = [], [], []
            for node in G.nodes():
                x, y = pos[node]
                node_x.append(x)
                node_y.append(y)
                texts.append(node)

            node_trace = go.Scatter(
                x=node_x, y=node_y,
                mode='markers+text',
                text=texts,
                textposition='top center',
                hoverinfo='text',
                marker=dict(
                    showscale=False,
                    color='darkorange',
                    size=10,
                    line_width=2
                )
            )

            fig = go.Figure(data=[edge_trace, node_trace],
                            layout=go.Layout(
                                title=f'Red de relaciones entre productos (basado en {metrica})',
                                titlefont_size=16,
                                showlegend=False,
                                hovermode='closest',
                                margin=dict(b=20, l=5, r=5, t=40),
                                xaxis=dict(showgrid=False, zeroline=False),
                                yaxis=dict(showgrid=False, zeroline=False)
                            ))

            st.plotly_chart(fig, use_container_width=True)

            # Interpretación automática
            productos_unicos = set()
            for _, row in reglas_top.iterrows():
                productos_unicos.update(row['antecedents'])
                productos_unicos.update(row['consequents'])

            st.markdown("### 🧾 Resumen de la visualización")
            st.markdown(f"""
            - 🔗 Se muestran **{len(reglas_top)} relaciones** entre productos.
            - 🛍️ Hay **{len(productos_unicos)} productos únicos** conectados.
            - 📏 La métrica seleccionada es **{metrica}**, con un valor mínimo de `{valor_minimo}`.
            - 📊 Promedio de {metrica}: `{reglas_top[metrica].mean():.2f}`
            """)

    elif opcion_vista == "📊 Heatmap cruzado":
        st.subheader("📊 Heatmap cruzado entre productos")
        from charts.HeatmapXTab import draw_heatmap
        # ◯ Transformación previa al heatmap
        tabular_heatmap = tabular.set_index("antecedents")

        # ◯ Generar visualización
        fig_heatmap = draw_heatmap(tabular_heatmap)
        st.plotly_chart(fig_heatmap, use_container_width=True)

    elif opcion_vista == "📋 Tabla completa":
        st.subheader("📋 Todas las reglas generadas")
        st.dataframe(rules, use_container_width=True)