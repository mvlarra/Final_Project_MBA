
###################################################################################################################################################
# OLD
###################################################################################################################################################
# Sidebar para navegación

st.sidebar.title("🧭 Navegación")
section = st.sidebar.radio("Ir a la sección:", (
    "1. 📘 Acerca del Proyecto",
    "2. 📋 Resumen del Proyecto",
    "3. 🧪 Metodología del Análisis",
    "4. 📊 Exploración de Datos",
    "5. 🔎 Explorar Reglas de Asociación",
    "6. 🛒 Recomendaciones y Estrategias por Producto",
    "7. 💼 Acciones estratégicas para tu negocio",   
    "8. 📏 Glosario de Métricas", 
    "OLD 1. 🏠 Inicio",
    "OLD 9. 📎 Créditos y recursos del proyecto",
    # "🧪 Methodology",
    # "📏 Key Metrics",
    # "🔁 Cross Selling Products",
    # "OLD 4.1 ⚙️ Reglas de Asociación",
    # "OLD 7. 🗺️ Visualización de Relaciones",
    # "OLD 5. 📦 Bundles de Productos",
    # "OLD 6. 🛍️ Recomendaciones para tu carrito",
    # "Heatmap del Bundle",
    # "📌 Heatmap de Producto"
))


# # 6. ◯ Sección: RECOMENDACIONES PERSONALIZADAS
# # ............................................................................................
# elif section.startswith("OLD 6."):
#     st.title("🛍️ Recomendaciones para tu carrito")
#     st.markdown("""
#     Seleccioná un producto para obtener recomendaciones basadas en patrones de compra frecuentes.  
#     Estas sugerencias ayudan a aumentar el ticket promedio mediante **ventas cruzadas inteligentes**.

#     Las recomendaciones se basan en reglas del tipo:  
#     *"Los clientes que compraron X, también compraron Y"*
#     """)

#     # Asegurar que las columnas 'antecedents' y 'consequents' sean listas
#     rules['antecedents'] = rules['antecedents'].apply(lambda x: [x] if isinstance(x, str) else x)
#     rules['consequents'] = rules['consequents'].apply(lambda x: [x] if isinstance(x, str) else x)

#     # Crear lista única de productos disponibles como 'antecedents'
#     productos_disponibles = sorted(set([item for sublist in rules['antecedents'] for item in sublist]))

#     # Selector de producto base
#     producto_seleccionado = st.selectbox("🛍️ Elegí un producto:", productos_disponibles)

#     # Filtrar reglas con ese producto como antecedente
#     reglas_filtradas = rules[rules['antecedents'].apply(lambda x: producto_seleccionado in x)]

#     if not reglas_filtradas.empty:
#         st.success(f"Se encontraron {len(reglas_filtradas)} recomendaciones para el producto '{producto_seleccionado}'.")

#         # Ordenar por confianza
#         reglas_ordenadas = reglas_filtradas.sort_values(by='confidence', ascending=False)

#         # Preparar recomendaciones para mostrar
#         recomendaciones = reglas_ordenadas[['consequents', 'support', 'confidence', 'lift']].copy()
#         recomendaciones['consequents'] = recomendaciones['consequents'].apply(lambda x: ', '.join(x))

#         st.dataframe(recomendaciones.rename(columns={
#             'consequents': '🛒 Producto Recomendado',
#             'support': 'Soporte',
#             'confidence': 'Confianza',
#             'lift': 'Relevancia (Lift)'
#         }), use_container_width=True)

#         # Interpretación automática de la mejor sugerencia
#         mejor = reglas_ordenadas.iloc[0]
#         producto_recomendado = ', '.join(mejor['consequents'])

#         st.markdown("---")
#         st.markdown(f"""
#         **Producto seleccionado:** `{producto_seleccionado}`  
#         **Producto recomendado:** `{producto_recomendado}`

#         **Confianza:** `{mejor['confidence']:.2f}`  
#         🛈 *Esto significa que en el **{mejor['confidence']*100:.0f}%** de las veces que alguien compró **{producto_seleccionado}**, también compró **{producto_recomendado}**.*

#         **Relevancia (lift):** `{mejor['lift']:.2f}`  
#         🛈 *Un valor mayor a 1 indica que la compra conjunta entre estos productos es más frecuente de lo esperado.  
#         Cuanto más alto, más fuerte es la relación entre ambos productos.*
#         """)
#         st.markdown("---")

#     else:
#         st.warning("No se encontraron recomendaciones para este producto. Probá con otro.")





# # 7. ◯ Sección: VISUALIZACIÓN DE RELACIONES
# # ............................................................................................
# elif section.startswith("OLD 7."):
#     st.title("🗺️ Red de Relaciones entre Productos")
#     st.markdown("""
#     Esta visualización muestra cómo se conectan los productos entre sí a partir de reglas de asociación. 
#     Cada nodo representa un producto, y los enlaces indican que se suelen comprar juntos. 
#     El grosor del enlace refleja la **fuerza de la relación** según la métrica seleccionada.
#     """)

#     # ◯ Elegir métrica para evaluar relaciones
#     metrica = st.selectbox("🔍 Elegí la métrica de relación:", ["lift", "confidence", "support"])

#     # ◯ Filtro por valor mínimo
#     valor_minimo = st.slider(f"🔧 Filtrar relaciones con {metrica} mayor a:", min_value=0.0, max_value=5.0, value=1.2, step=0.1)

#     # ◯ Filtrar reglas por métrica seleccionada
#     reglas_filtradas = rules[rules[metrica] >= valor_minimo]

#     # ◯ Mostrar solo las N relaciones más fuertes
#     top_n = st.slider("🔢 ¿Cuántas relaciones querés visualizar?", min_value=10, max_value=100, value=50, step=5)
#     reglas_top = reglas_filtradas.nlargest(top_n, metrica)

#     if reglas_top.empty:
#         st.warning("⚠️ No hay relaciones que cumplan con estos filtros.")
#     else:
#         # ◯ Crear grafo dirigido
#         G = nx.DiGraph()

#         for _, row in reglas_top.iterrows():
#             origen = row['antecedents'][0] if isinstance(row['antecedents'], list) else row['antecedents']
#             destino = row['consequents'][0] if isinstance(row['consequents'], list) else row['consequents']
#             peso = row[metrica]

#             G.add_node(origen)
#             G.add_node(destino)
#             G.add_edge(origen, destino, weight=peso)

#         pos = nx.spring_layout(G, k=0.5, iterations=50)

#         edge_x, edge_y = [], []
#         for edge in G.edges():
#             x0, y0 = pos[edge[0]]
#             x1, y1 = pos[edge[1]]
#             edge_x.extend([x0, x1, None])
#             edge_y.extend([y0, y1, None])

#         edge_trace = go.Scatter(
#             x=edge_x, y=edge_y,
#             line=dict(width=1.5, color='gray'),
#             hoverinfo='none',
#             mode='lines'
#         )

#         node_x, node_y, texts = [], [], []
#         for node in G.nodes():
#             x, y = pos[node]
#             node_x.append(x)
#             node_y.append(y)
#             texts.append(node)

#         node_trace = go.Scatter(
#             x=node_x, y=node_y,
#             mode='markers+text',
#             text=texts,
#             textposition='top center',
#             hoverinfo='text',
#             marker=dict(
#                 showscale=False,
#                 color='darkorange',
#                 size=10,
#                 line_width=2
#             )
#         )

#         fig = go.Figure(data=[edge_trace, node_trace],
#                         layout=go.Layout(
#                             title=f'Red de relaciones entre productos (basado en {metrica})',
#                             titlefont_size=16,
#                             showlegend=False,
#                             hovermode='closest',
#                             margin=dict(b=20, l=5, r=5, t=40),
#                             xaxis=dict(showgrid=False, zeroline=False),
#                             yaxis=dict(showgrid=False, zeroline=False)
#                         ))

#         st.plotly_chart(fig, use_container_width=True)
        
    
#         # Interpretación automática
#         productos_unicos = set()
#         for _, row in reglas_top.iterrows():
#             productos_unicos.update(row['antecedents'])
#             productos_unicos.update(row['consequents'])

#         st.markdown("### 🧾 Resumen de la visualización")
#         st.markdown(f"""
#         - 🔗 Se muestran **{len(reglas_top)} relaciones** entre productos.
#         - 🛍️ Hay **{len(productos_unicos)} productos únicos** conectados.
#         - 📏 La métrica seleccionada es **{metrica}**, con un valor mínimo de `{valor_minimo}`.
#         - 📊 Promedio de {metrica}: `{reglas_top[metrica].mean():.2f}`
#         """)
    
    




# # ◯ Sección: Cross Selling Products
# # -----------------------------------------------------------------------------------------------------------------

# elif section == "🔁 Cross Selling Products":
#     st.markdown("## 🔁 Cross Selling Products")
#     st.markdown("""
#     **Top 5 Cross-Selling Products**

#     Cross-selling involves identifying products frequently purchased together, gauged by high **:orange[support]** reflecting their `co-occurrence` in transactions.   
#     The concept considers not only the `frequency of joint purchases` but also the `strength of these associations` measured by **:orange[confidence]**.

#     Focusing on product combinations with both `high support and confidence` helps pinpoint reliably associated items, enabling businesses to strategically promote or bundle products for an `enhanced customer shopping` experience.

#     The table below shows the **:orange[top 5 cross-selling-product pairs]**, sorted by their `average confidence and support`.
#     """)




# ◯ Sección: Bundle Destacado

#  codigo original
#  elif section == "Bundle Destacado":
#     st.subheader("🔹 Bundle: Pomo de Cajón Cerámico de Rayas Rojas")
#     PRODUCTS_CATEGORY = "POMO DE CAJÓN CERÁMICO DE RAYAS ROJAS"
#     related_products = df_bundle_products[df_bundle_products["category"].str.contains(PRODUCTS_CATEGORY)]["nodes"].values
#     if len(related_products) > 0:
#         st.markdown("**Productos agrupados:**")
#         st.write(list(related_products[0]))
#     else:
#         st.warning("No se encontraron productos relacionados.")





# # ◯ Sección: Heatmap del Bundle
# elif section == "Heatmap del Bundle":
#     st.markdown("## 🔥 Heatmap del Bundle Seleccionado")
#     st.markdown(
#         "Este mapa muestra la frecuencia con la que los productos del bundle se compran juntos. "
#         "Cuanto más intenso el color, mayor el soporte conjunto entre esos productos."
#     )

#     import plotly.graph_objects as go
#     import numpy as np

#     z = tabular.values
#     x_labels = tabular.columns.tolist()
#     y_labels = tabular.index.tolist()
#     text_labels = np.round(z, 3)

#     fig = go.Figure(data=go.Heatmap(
#         z=z,
#         x=x_labels,
#         y=y_labels,
#         colorscale='Reds',
#         hoverongaps=False,
#         text=text_labels,
#         texttemplate="%{text}",
#         hovertemplate="Producto A: %{y}<br>Producto B: %{x}<br>Soporte: %{z}<extra></extra>"
#     ))

#     fig.update_layout(
#         title="Heatmap de soporte entre productos del bundle",
#         title_x=0.5,
#         height=900,
#         xaxis_tickangle=-45,
#         xaxis=dict(tickfont=dict(size=10), automargin=True),
#         yaxis=dict(tickfont=dict(size=10), automargin=True),
#         margin=dict(l=200, r=50, t=50, b=200),
#         plot_bgcolor='#0e1117',
#         paper_bgcolor='#0e1117',
#         font=dict(color="#f0f0f0")
#     )

#     st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})






# # 4.1 ◯ Sección: REGLAS DE ASOCIACIÓN
# # -----------------------------------------------------------------------------------------------------------------
# elif section.startswith("OLD 4.1"):
    
#     st.markdown("---")
#     st.title("⚙️ Reglas de Asociación")
#     st.markdown("En esta sección verás las principales reglas encontradas con el algoritmo Apriori")

#     st.subheader("📈 Top 5 Regles by Soporte")
#     st.markdown("Estas son las 5 reglas más comunes, ordenadas por soporte. El soporte representa la proporción de transacciones donde aparece ese conjunto de productos.")

#     # ◯ Nota explicativa con ejemplo concreto, estilo más sutil
#     st.markdown(
#         """
#         <small><i>Ejemplo:</i> Si los productos <b>Taza</b> y <b>Plato</b> aparecen juntos en 50 de 1000 tickets, su soporte es 0.05 (es decir, el 5% de las transacciones).</small>
#         """,
#         unsafe_allow_html=True
#     )

#     top_support = rules.sort_values("support", ascending=False).iloc[::2].head(5).reset_index(drop=True)
#     st.dataframe(top_support, use_container_width=True)


#     st.markdown("---")
#     st.subheader("🏆 Top 5 Association Rules by Score")

#     st.markdown("""
#     While evaluating association rules, we utilize key metrics such as **:orange[support]**, **:orange[confidence]**, and **:orange[lift]** to discern their significance.

#     Each rule is independently ranked based on these metrics, and a **mean rank** is computed across all three rankings.

#     This mean rank serves as a **composite score**, capturing the overall performance of each rule across the different metrics.  

#     The table below shows the **top 5 association rules** based on the composite score.
#     """)
#     # Mostrar la tabla

#     st.dataframe(Top_5_Rules_by_Score, use_container_width=True)

#     st.markdown("### ✅ Recomendaciones basadas en las reglas")

#     st.markdown("""
#     1. **Si alguien compra “TAZA DE TÉ Y PLATILLO VERDE REGENCY”, recomendale también “TAZA DE TÉ Y PLATILLO ROSES REGENCY”.**  
#     Alta confianza (76%) y fuerte lift (22× más probable que al azar).

#     2. **Si alguien compra “TAZA DE TÉ Y PLATILLO ROSES REGENCY”, recomendale también “TAZA DE TÉ Y PLATILLO VERDE REGENCY”.**  
#     Alta probabilidad y relación recíproca con la anterior.

#     3. **Quien compra la versión rosa, tiene alta chance (83%) de interesarse también en la verde.**  
#     Ideal para bundles visualmente combinados.

#     4. **Si compran la verde, podrías ofrecer también la rosa, aunque con menor confianza (63%).**  
#     Útil como recomendación cruzada secundaria.

#     5. **Compradores de la versión rosa también suelen elegir la versión ROSES.**  
#     Oportunidad para agruparlas como “línea de colección” o sugerirlas juntas en promociones.
#     """)    




        
        
        
# # 5. ◯ Sección: BUNDLES DE PRODUCTOS
# # ............................................................................................
# elif section.startswith("OLD 5."):
#     st.title("📦 Bundles de Productos")
#     st.markdown("""
#         Cada *bundle* agrupa productos que suelen comprarse juntos de forma consistente.  
#         A continuación se listan los grupos descubiertos, ordenados por su soporte promedio.
#     """)

#     # ◯ Mostrar cantidad total de bundles encontrados
#     total_bundles = df_bundle_products['category'].nunique()
#     st.markdown(f"🔍 Se identificaron **{total_bundles} bundles** de productos.")

#     # ◯ Agrupar datos y renombrar columna
#     summary_bundles = df_bundle_products.groupby("category").agg(
#         products=('nodes', 'unique'),
#         support_mean=('support', 'mean'),
#         n=('nodes', 'size')
#     ).sort_values("support_mean", ascending=False).reset_index().rename(columns={"category": "bundle_name"})

#     # ◯ Formatear lista de productos como texto separado por punto medio " • "
#     summary_bundles["products"] = summary_bundles["products"].apply(lambda x: "  •  ".join(x))

#     # ◯ Estilizar tabla
#     styled_df = summary_bundles.style.set_table_styles([
#         {'selector': 'td', 'props': [('font-size', '13px'), ('line-height', '1.6')]},
#         {'selector': 'th', 'props': [('font-size', '13px'), ('font-weight', 'normal'), ('text-align', 'left')]}
#     ]).set_properties(**{'white-space': 'pre-wrap'})

#     st.markdown(styled_df.to_html(), unsafe_allow_html=True)

#     # ◯ Referencias de columnas con ejemplo y separador actualizado
#     st.markdown(
#         """
#         <small><b>ℹ️ Referencia de columnas:</b></small>
#         <small>
#         <ul>
#             <li><b>bundle_name</b>: Nombre representativo del grupo de productos relacionados, probablemente el producto central o más distintivo del bundle.
#                 <br><i>Ejemplo:</i> <code>POMO DE CAJÓN CERÁMICO DE RAYAS ROJAS</code> es un bundle que agrupa varios pomos similares.</li>
#             <li><b>products</b>: Lista de productos que componen el bundle.</li>
#             <li><b>support_mean</b>: Promedio de soporte de los productos del grupo.</li>
#             <li><b>n</b>: Cantidad total de productos dentro del bundle.</li>
#         </ul>
#         </small>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown("---")
#     st.subheader("🎯 Bundle Destacado")
#     st.markdown(
#         "Explorá en detalle los productos que forman parte de un bundle específico. "
#         "Seleccioná uno del menú desplegable para ver su composición."
#     )

#     # Selección de bundle
#     bundles_disponibles = df_bundle_products["category"].sort_values().unique()
#     selected_bundle = st.selectbox("📦 Seleccioná un bundle:", bundles_disponibles)

#     # Filtrar y obtener productos del bundle
#     rows = df_bundle_products[df_bundle_products["category"] == selected_bundle]

#     if len(rows) > 0:
#         productos = []

#         for fila in rows["nodes"]:
#             if isinstance(fila, list):
#                 productos.extend(fila)
#             elif isinstance(fila, str):
#                 productos.append(fila)

#         productos_unicos = list(set(productos))

#         if productos_unicos:
#             st.markdown("**Productos agrupados en este bundle:**")

#         # Crear y ordenar df_bundle
#         df_bundle = rows.explode("nodes")
#         df_bundle = df_bundle[["nodes", "support"]].dropna()
#         df_bundle = df_bundle.groupby("nodes").mean().sort_values("support", ascending=False)

#         if not df_bundle.empty:
#             df_bundle["support_pct"] = df_bundle["support"] * 100

#             fig = go.Figure(go.Bar(
#                 x=df_bundle["support_pct"],
#                 y=df_bundle.index,
#                 orientation='h',
#                 marker=dict(color='#d26a00'),
#                 hovertemplate='%{y}<br>Soporte: %{x:.2f} %<extra></extra>',
#                 text=[f"<b>{s:.2f}%</b>" for s in df_bundle["support_pct"]],
#                 textposition='auto',
#                 textfont=dict(color="#ffffff", size=16),  # más grande
#                 insidetextanchor='end',
#                 showlegend=False
#             ))

#             fig.update_layout(
#                 title="Frecuencia (soporte) de los productos en este bundle",
#                 title_x=0.5,
#                 xaxis_title=None,
#                 xaxis=dict(showticklabels=False, showgrid=False),
#                 yaxis=dict(title="", autorange="reversed"),
#                 plot_bgcolor='#0e1117',
#                 paper_bgcolor='#0e1117',
#                 font=dict(color="#f0f0f0", size=14),
#                 margin=dict(l=200, r=40, t=50, b=40),
#                 height=60 * len(df_bundle) + 80
#             )

#             st.plotly_chart(fig, use_container_width=True, config=dict(displayModeBar=False))
#         else:
#             st.info("Este bundle no contiene productos.")
#     else:
#         st.warning("No se encontraron datos para el bundle seleccionado.")


# # ◯ Sección: HEATMAP old "📌 Heatmap de Producto"
# # -------------------------------------------------------------------------------------------------------------

# elif section == "📌 Heatmap de Producto":
#     st.markdown("## 📌 Heatmap de Co-ocurrencia por Producto")
#     st.markdown(
#         "Este gráfico muestra cómo se relaciona un producto específico con otros, "
#         "según la métrica seleccionada."
#     )

#     from charts.HeatmapXTab import HeatmapCrosstab

#     # ◯ Crear instancia del generador de heatmaps
#     heat = HeatmapCrosstab(rules)

#     # ◯ Obtener productos únicos desde reglas
#     productos_disponibles = sorted(set(rules['antecedents'].explode()) | set(rules['consequents'].explode()))
#     producto_base = st.selectbox("🧲 Seleccioná un producto base:", productos_disponibles)

#     # ◯ Selección de métrica
#     metrica = st.selectbox("📏 Seleccioná la métrica:", ["support", "lift", "confidence"])

#     # ◯ Explicación contextual de la métrica seleccionada
#     explicaciones = {
#         "support": "🔥 <b>Support (Soporte)</b>: muestra qué tan seguido se venden juntos los productos.<br>"
#                 "👉 Útil para detectar <b>productos que siempre aparecen en conjunto</b>.",

#         "confidence": "🔥 <b>Confidence (Confianza)</b>: indica qué tan probable es que se compre el segundo producto "
#                     "cuando ya se compró el primero.<br>"
#                     "👉 Útil para sugerencias de <b>“quienes compraron esto, también compraron…”</b>",

#         "lift": "🔥 <b>Lift</b>: mide si dos productos se potencian cuando se venden juntos, más allá de lo esperable.<br>"
#                 "👉 Útil para identificar <b>combinaciones fuertes o ideales para promociones cruzadas</b>."
#     }

#     st.markdown(
#         f"""
#         <div style='
#             font-size: 14px;
#             margin-bottom: 20px;
#             background-color: #f1f1f105;
#             padding: 10px 15px;
#             border-left: 4px solid #ff6d00;
#             border-radius: 5px;
#             color: #ddd;
#             line-height: 1.5;
#         '>
#         {explicaciones[metrica]}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     # ◯ Filtrar reglas donde el producto seleccionado es el antecedente
#     recomendaciones = rules[rules['antecedents'].apply(lambda x: producto_base in x)]

#     # ◯ Ordenar por la métrica elegida
#     recomendaciones = recomendaciones.sort_values(metrica, ascending=False)

#     # ◯ Mostrar los 5 recomendados más fuertes
#     top_recomendados = recomendaciones['consequents'].explode().value_counts().head(5).index.tolist()

#     st.markdown("### 🔗 Recomendaciones basadas en asociación")
#     st.write("Los siguientes productos aparecen frecuentemente junto a", f"**{producto_base}**:")

#     # ◯ Crear tabla cruzada manualmente desde reglas
#     df = rules.copy()
#     df = df.explode("antecedents")
#     df = df.explode("consequents")
#     df = df[df["antecedents"] == producto_base]

#     crosstab = df.pivot_table(
#         index="antecedents",
#         columns="consequents",
#         values=metrica,
#         aggfunc="mean",
#         fill_value=0
#     ).iloc[:, :10]  # Mostrará hasta 10 productos relacionados como máximo

#     # ◯ Graficar heatmap
#     fig = heat.plot_heatmap(crosstab)

#     st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

#     st.markdown(
#     f"""
#     <div style='
#         margin-top: 25px;
#         padding: 15px;
#         background-color: #1e1e1e;
#         border-left: 4px solid #ff6d00;
#         border-radius: 5px;
#         font-size: 15px;
#         line-height: 1.6;
#         color: #ddd;
#     '>
#         <b>¿Cómo interpretar este heatmap?</b><br>
#         El gráfico muestra la intensidad de relación entre <b>{producto_base}</b> y otros productos.<br>
#         Cuanto más oscuro el recuadro, mayor es la <b>{metrica}</b> observada entre ambos ítems.<br>
#         Esto puede ayudarte a identificar productos que suelen comprarse juntos o que podrían recomendarse juntos en la tienda o sitio web.
#     </div>
#     """,
#     unsafe_allow_html=True
#     )

#     # ◯ Mostrar ubicación sugerida si el producto base está en un bundle conocido
#     ubicacion = df_bundle_products[df_bundle_products['nodes'] == producto_base]

#     if not ubicacion.empty:
#         categoria = ubicacion['category'].iloc[0]

#         # ◯ Buscar todos los productos en ese mismo bundle
#         otros = df_bundle_products[df_bundle_products['category'] == categoria]

#         # ◯ Excluir el producto actual
#         productos_relacionados = otros[otros['nodes'] != producto_base]['nodes'].tolist()

#         # ◯ Mostrar bloque de sugerencia

#         # ◯ Calcular productos sugeridos ordenados por métrica
#         df_metric = df.groupby("consequents")[metrica].mean().sort_values(ascending=False)
#         df_metric = df_metric[df_metric.index != producto_base]

#         # ◯ Armar la lista en HTML
#         items_html = "".join([
#             f"<div style='margin-bottom:6px; color: #ddd; font-size:15px;'>"
#             f"<span style='color: #ffaa00; font-weight: bold;'>✔️</span> {prod}</div>"
#             for prod in df_metric.index.tolist()
#         ])

#         # ◯ Cuadro de sugerencia completo con lista integrada
#         st.markdown(
#             f"""
#             <div style='
#                 margin-top: 20px;
#                 padding: 15px;
#                 background-color: #1e1e1e;
#                 border-left: 4px solid #ff6d00;
#                 border-radius: 5px;
#                 font-size: 15px;
#                 line-height: 1.6;
#                 color: #ddd;
#             '>
#                 <div style='font-size:21px; font-weight:bold; color:#fff; margin-bottom:10px;'>
#                 🟡 Sugerencia de Ubicación / Agrupación
#                 </div>
#                 Este producto forma parte del bundle: <b>📦 {categoria}</b>.<br>
#                 Podría colocarse cerca de productos similares para mejorar la visibilidad o fomentar compras combinadas.
#                 <br><br>
#                 <b>Productos sugeridos para agrupar (ordenados por <code>{metrica}</code>):</b>
#                 {items_html}
#                 </div>
#             """,
#             unsafe_allow_html=True
#         )