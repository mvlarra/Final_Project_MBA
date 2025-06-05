# ◯ SECTION 5 – EXPLORAR REGLAS DE ASOCIACIÓN
# Objetivo:
#   Permitir al usuario explorar de manera interactiva las reglas de asociación generadas mediante Apriori.
# Contenido:
#   - Reglas destacadas con mayor score
#   - Red de relaciones entre productos
#   - Heatmap cruzado entre productos
#   - Tabla completa de todas las reglas generadas

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import networkx as nx
from charts.HeatmapXTab import draw_heatmap



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

    st.markdown("""
    <style>
        
    .stTabs [data-baseweb="tab-list"] {
    overflow-x: auto !important;      /* permite scroll horizontal */
    white-space: nowrap;              /* evita que se bajen de línea */
    display: flex;                    /* asegura que se alineen horizontalmente */
    flex-wrap: nowrap;                /* evita que se acomoden en más de una línea */
    scrollbar-width: thin;            /* (opcional) scroll más fino en Firefox */
    }

    
    /* Scrollbar para navegadores WebKit (Chrome, Edge, Safari) */
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
        height: 6px;                      /* altura de la barra de scroll */
    }
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar-thumb {
        background-color: #aaa;           /* color del "pulgar" del scroll */
        border-radius: 4px;               /* bordes redondeados para estética */
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f0f0;
        padding: 8px 16px;
        border-radius: 8px 8px 0 0;
        font-weight: bold;
        color: #333333;
        border: 1px solid #ccc;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffdb99;
        box-shadow: 0px 4px 6px rgba(60, 60, 60, 0.6);
        color: black;
        font-weight: 800 !important;
        font-size: 16px !important;
        border-bottom: none;
    }
    </style>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "🟠 Reglas Encontradas",
        "🟠 Reglas Destacadas",
        "🟠 Red de productos",
        "🟠 Heatmap cruzado",
     ])
    


    with tab1:
        try:
            # ◯ Leer archivo con resumen de reglas
            rules_df = pd.read_csv("data/processed/summary_rules.csv")
            total_rules = len(rules_df)

            # ◯ Limpieza de strings de conjuntos
            rules_df["antecedents"] = rules_df["antecedents"].str.replace(r"[{}']", "", regex=True)
            rules_df["consequents"] = rules_df["consequents"].str.replace(r"[{}']", "", regex=True)

            # ◯ Copia del DataFrame para aplicar filtros luego
            filtered_df = rules_df.copy()

            # ◯ Título y total de reglas encontradas
            st.markdown("---")            
            st.markdown(
                f"<div style='font-size:20px;'>🔵 Total de Reglas Encontradas: <b>{total_rules:,}</b></div>",
                unsafe_allow_html=True
            )
            st.markdown("---")  
            
            # ◯ Criterios del modelo en Expander
            with st.expander("ℹ️ Ver criterios de generación del modelo"):
                st.markdown("""
                **Criterios utilizados con el algoritmo Apriori:**

                - `Soporte ≥ 0.01`: aparecen en ≥1% de las transacciones.
                - `Confianza ≥ 0.20`: precisión mínima del 20%.
                - `Lift ≥ 2`: 2 veces más probable que lo esperado por azar.

                Estos valores garantizan que las reglas mostradas tengan relevancia estadística y utilidad comercial.
                """)

            # ◯ Descripción para el usuario
            st.markdown("""
            Explorá las reglas de asociación generadas.  
            Podés usar los filtros para encontrar relaciones específicas entre productos.

            - **Antecedente:** lo que se compra primero  
            - **Consecuente:** lo que suele comprarse después

            Si no seleccionás filtros, se muestran todas las reglas encontradas.
            """)

            st.markdown("---")
            st.markdown("### 🔵 Filtros por Producto")

            # ◯ Opciones únicas
            antecedent_options = sorted(rules_df["antecedents"].unique())
            consequent_options = sorted(rules_df["consequents"].unique())

            # ◯ Selección de filtros
            col1, col2 = st.columns(2)
            with col1:
                selected_antecedents = st.multiselect("🔽 Antecedente", antecedent_options)
            with col2:
                selected_consequents = st.multiselect("🔽 Consecuente", consequent_options)

            # ◯ Aplicar filtros si corresponde
            filtered_df = rules_df.copy()
            if selected_antecedents:
                filtered_df = filtered_df[filtered_df["antecedents"].isin(selected_antecedents)]
            if selected_consequents:
                filtered_df = filtered_df[filtered_df["consequents"].isin(selected_consequents)]

            # ◯ Mostrar resumen de cantidad de reglas filtradas
            st.markdown(
                f"<div style='font-size:18px;'>➡️ Mostrando <b>{len(filtered_df):,}</b> reglas filtradas de un total de <b>{total_rules:,}</b></div>",
                unsafe_allow_html=True
            )

            st.markdown("---")

            # ◯ Mostrar tabla con columnas relevantes
            cols_to_show = ['antecedents', 'consequents', 'support', 'confidence', 'lift']
            st.dataframe(filtered_df[cols_to_show].reset_index(drop=True))

        except FileNotFoundError:
            st.warning("⚠️ No se encontró el archivo `summary_rules.csv`. Verificá que esté en la carpeta `data/processed`.")


    with tab2: # ◯ Reglas relevantes (desde OLD 4 - solo las destacadas)
        
        st.markdown("En esta sección verás las principales reglas encontradas con el algoritmo Apriori")

        st.markdown("---")
        st.subheader("📈 Top 5 Reglas por Soporte")
        st.markdown("Estas son las 5 reglas más comunes, ordenadas por soporte. El soporte representa la proporción de transacciones donde aparece ese conjunto de productos.")

        # ◯ Nota explicativa con ejemplo concreto, estilo más sutil
        st.markdown(
            """
            <small><i>Ejemplo:</i> Si los productos <b>Taza</b> y <b>Plato</b> aparecen juntos en 50 de 1000 tickets, su soporte es 0.05 (es decir, el 5% de las transacciones).</small>
            """,
            unsafe_allow_html=True
        )

        top_support = rules.sort_values("support", ascending=False).iloc[::2].head(5).reset_index(drop=True)
        st.dataframe(top_support, use_container_width=True)


        st.markdown("---")
        st.subheader("🏆 Top 5 de las Reglas de Asociación (por Score)")

        st.markdown("""
        Al evaluar las reglas de asociación, utilizamos métricas clave como **:orange[support]**, **:orange[confidence]** y **:orange[lift]** para determinar su relevancia.

        Cada regla se clasifica de forma independiente según estas métricas, y luego se calcula un **ranking promedio** entre las tres posiciones.

        Este ranking promedio actúa como un **puntaje compuesto**, que refleja el rendimiento general de cada regla a través de las distintas métricas.

        La siguiente tabla muestra las **5 reglas de asociación principales** basadas en este puntaje compuesto.
        """)
        
        # Mostrar la tabla

        st.dataframe(Top_5_Rules_by_Score, use_container_width=True)
        
        st.markdown("---")
   
        st.markdown("""
        <span style='font-size: 0.85rem; color: gray;'>
        
        #### ✅ Ejemplos de recomendaciones basadas en estas reglas
        
        1. **Si alguien compra “TAZA DE TÉ Y PLATILLO VERDE REGENCY”, recomendale también “TAZA DE TÉ Y PLATILLO ROSES REGENCY”.**  
        Alta confianza (76%) y fuerte lift (22× más probable que al azar).

        2. **Si alguien compra “TAZA DE TÉ Y PLATILLO ROSES REGENCY”, recomendale también “TAZA DE TÉ Y PLATILLO VERDE REGENCY”.**  
        Alta probabilidad y relación recíproca con la anterior.

        3. **Quien compra la versión rosa, tiene alta chance (83%) de interesarse también en la verde.**  
        Ideal para bundles visualmente combinados.

        4. **Si compran la verde, podrías ofrecer también la rosa, aunque con menor confianza (63%).**  
        Útil como recomendación cruzada secundaria.

        5. **Compradores de la versión rosa también suelen elegir la versión ROSES.**  
        Oportunidad para agrupar productos similares en promociones.

        </span>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.subheader("🗺️ Red de Relaciones entre Productos")
        st.markdown("""
        🧠 <b>¿Qué estás viendo?</b><br>
        Esta visualización muestra cómo se conectan los productos entre sí a partir de reglas de asociación.<br>
        Cada nodo representa un producto, y los enlaces indican que se suelen comprar juntos.<br>
        El grosor del enlace refleja la **fuerza de la relación** según la métrica seleccionada.
        """, unsafe_allow_html=True)
      
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
        
        # Footer:
        st.markdown(f"""
        {"<div style='font-size:12px;color:gray;margin-top:10px;'>ℹ️ Visualización construida con NetworkX y Plotly. Las aristas representan reglas con lift > 2.</div>"}
        """, unsafe_allow_html=True)    

   
    with tab4:
            st.subheader("📊 Heatmap cruzado entre productos")
            st.markdown("""
            🧠 <b>¿Qué estás viendo?</b><br>
            Esta vista muestra la intensidad de co-ocurrencia entre productos en una matriz de calor.</b>.<br>
            Permite identificar fácilmente combinaciones frecuentes que podrían ser aprovechadas para promociones o bundles.<br>
            Las filas corresponden a productos base, y las columnas a productos recomendados.<br>
            El color representa qué tan fuerte es la relación entre ellos.
            """, unsafe_allow_html=True)                   
            
            # ◯ Transformación previa al heatmap
            tabular_heatmap = tabular.set_index("antecedents")

            # ◯ Generar visualización
            fig_heatmap = draw_heatmap(tabular_heatmap)
            st.plotly_chart(fig_heatmap, use_container_width=True)
            
            # footter:
            st.markdown(f"""
            {"<div style='font-size:12px;color:gray;margin-top:10px;'>ℹ️ Generado con seaborn. Matriz calculada a partir de la co-ocurrencia de productos binarizados.</div>"}
            """, unsafe_allow_html=True)
