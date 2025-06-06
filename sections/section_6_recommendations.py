# ◯ SECTION 6 – RECOMENDACIONES Y ESTRATEGIAS POR PRODUCTO
# Objetivo:
#   Ofrecer recomendaciones y estrategias accionables basadas en productos reales.
# Contenido:
#   - Reglas destacadas por soporte y score
#   - Bundles de productos descubiertos
#   - Recomendaciones personalizadas por producto
#   - Heatmap cruzado por producto
#   - Identificación de oportunidades de cross-selling

import streamlit as st
import streamlit as st
from charts.HeatmapXTab import HeatmapCrosstab
import plotly.graph_objects as go


# ◯ Seccion 6: RECOMENDACIONES Y ESTRATEGIAS POR PRODUCTO
# ............................................................................................

def show_section_6_recommendations(rules, df_bundle_products, Top_5_Rules_by_Score):
    """
    Muestra la sección de recomendaciones y estrategias por producto, basada en reglas de asociación.
    Permite al usuario explorar reglas destacadas, bundles sugeridos y recomendaciones personalizadas.
    :param rules: DataFrame con las reglas de asociación generadas.
    :param df_bundle_products: DataFrame con los bundles de productos descubiertos.
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
    
    
    tabs = st.tabs([
        "🟠 Bundles sugeridos", 
        "🟠 Recomendaciones personalizadas",
        "🟠 Heatmap de Producto",
        "🟠 Cross Selling Products"
    ])


  
    with tabs[0]:        # ◯ Bundles sugeridos (desde OLD 5)
        
        st.subheader("🎁 Bundles recomendados")
        st.markdown("""
        Cada *bundle* agrupa productos que suelen comprarse juntos de forma consistente.  
        A continuación se listan los grupos descubiertos, ordenados por su soporte promedio.
        """)
        total_bundles = df_bundle_products['category'].nunique()
        st.markdown(f"🔍 Se identificaron **{total_bundles} bundles** de productos.")

        summary_bundles = df_bundle_products.groupby("category").agg(
            products=('nodes', 'unique'),
            support_mean=('support', 'mean'),
            n=('nodes', 'size')
        ).sort_values("support_mean", ascending=False).reset_index().rename(columns={"category": "bundle_name"})

        summary_bundles["products"] = summary_bundles["products"].apply(lambda x: "  •  ".join(x))

        styled_df = summary_bundles.style.set_table_styles([
            {'selector': 'td', 'props': [('font-size', '13px'), ('line-height', '1.6')]},
            {'selector': 'th', 'props': [('font-size', '13px'), ('font-weight', 'normal'), ('text-align', 'left')]}
        ]).set_properties(**{'white-space': 'pre-wrap'})

        st.markdown(styled_df.to_html(), unsafe_allow_html=True)

        st.markdown(
            """
            <small><b>ℹ️ Referencia de columnas:</b></small>
            <small>
            <ul>
                <li><b>bundle_name</b>: Nombre representativo del grupo de productos relacionados, probablemente el producto central o más distintivo del bundle.
                    <br><i>Ejemplo:</i> <code>POMO DE CAJÓN CERÁMICO DE RAYAS ROJAS</code> es un bundle que agrupa varios pomos similares.</li>
                <li><b>products</b>: Lista de productos que componen el bundle.</li>
                <li><b>support_mean</b>: Promedio de soporte de los productos del grupo.</li>
                <li><b>n</b>: Cantidad total de productos dentro del bundle.</li>
            </ul>
            </small>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.subheader("🎯 Bundle Destacado")
        st.markdown(
            "Explorá en detalle los productos que forman parte de un bundle específico. "
            "Seleccioná uno del menú desplegable para ver su composición."
        )

        bundles_disponibles = df_bundle_products["category"].sort_values().unique()
        st.markdown("""
        Explorá en detalle los productos que forman parte de un bundle específico.  
        Seleccioná uno del menú desplegable para ver su composición.
        """)
        selected_bundle = st.selectbox("📦 Seleccioná un bundle:", bundles_disponibles)

        rows = df_bundle_products[df_bundle_products["category"] == selected_bundle]

        if len(rows) > 0:
            productos = []

            for fila in rows["nodes"]:
                if isinstance(fila, list):
                    productos.extend(fila)
                elif isinstance(fila, str):
                    productos.append(fila)

            productos_unicos = list(set(productos))

            if productos_unicos:
                st.markdown("**Productos agrupados en este bundle:**")

            df_bundle = rows.explode("nodes")
            df_bundle = df_bundle[["nodes", "support"]].dropna()
            df_bundle = df_bundle.groupby("nodes").mean().sort_values("support", ascending=False)

            if not df_bundle.empty:
                df_bundle["support_pct"] = df_bundle["support"] * 100

                fig = go.Figure(go.Bar(
                    x=df_bundle["support_pct"],
                    y=df_bundle.index,
                    orientation='h',
                    marker=dict(color='#d26a00'),
                    hovertemplate='%{y}<br>Soporte: %{x:.2f} %<extra></extra>',
                    text=[f"<b>{s:.2f}%</b>" for s in df_bundle["support_pct"]],
                    textposition='auto',
                    textfont=dict(color="#ffffff", size=16),
                    insidetextanchor='end',
                    showlegend=False
                ))

                fig.update_layout(
                    title="Frecuencia (soporte) de los productos en este bundle",
                    title_x=0.5,
                    xaxis_title=None,
                    xaxis=dict(showticklabels=False, showgrid=False),
                    yaxis=dict(title="", autorange="reversed"),
                    plot_bgcolor='#0e1117',
                    paper_bgcolor='#0e1117',
                    font=dict(color="#f0f0f0", size=14),
                    margin=dict(l=200, r=40, t=50, b=40),
                    height=60 * len(df_bundle) + 80
                )

                st.plotly_chart(fig, use_container_width=True, config=dict(displayModeBar=False))
            else:
                st.info("Este bundle no contiene productos.")
        else:
            st.warning("No se encontraron datos para el bundle seleccionado.")


    # ◯ Recomendaciones personalizadas (desde OLD 6)
    with tabs[1]:
        st.subheader("🛍️ Recomendaciones para tu carrito")
        
        st.markdown("""
        Seleccioná un producto para obtener recomendaciones basadas en patrones de compra frecuentes.  
        Luego veremos la lista de productos recomendados en base a los productos ya presentes en el carrito.  
        Como estrategia comercial, podrian mostrarse como recomendaciones dinámicas en el checkout, ayudando a aumentar el ticket promedio mediante **ventas cruzadas inteligentes**. 
        
        Las recomendaciones se basan en reglas del tipo:  
        *"Los clientes que compraron X, también compraron Y"*
        """)
        

  
        
        rules['antecedents'] = rules['antecedents'].apply(lambda x: [x] if isinstance(x, str) else x)
        rules['consequents'] = rules['consequents'].apply(lambda x: [x] if isinstance(x, str) else x)

        productos_disponibles = sorted(set([item for sublist in rules['antecedents'] for item in sublist]))
        producto_seleccionado = st.selectbox("🛍️ Elegí un producto:", productos_disponibles)

        reglas_filtradas = rules[rules['antecedents'].apply(lambda x: producto_seleccionado in x)]

        if not reglas_filtradas.empty:
            st.success(f"Se encontraron {len(reglas_filtradas)} recomendaciones para el producto '{producto_seleccionado}'.")
            reglas_ordenadas = reglas_filtradas.sort_values(by='confidence', ascending=False)

            recomendaciones = reglas_ordenadas[['consequents', 'support', 'confidence', 'lift']].copy()
            recomendaciones['consequents'] = recomendaciones['consequents'].apply(lambda x: ', '.join(x))

            st.dataframe(recomendaciones.rename(columns={
                'consequents': '🛒 Producto Recomendado',
                'support': 'Soporte',
                'confidence': 'Confianza',
                'lift': 'Relevancia (Lift)'
            }), use_container_width=True)

            mejor = reglas_ordenadas.iloc[0]
            producto_recomendado = ', '.join(mejor['consequents'])

            st.markdown("---")
            st.markdown(f"""
            **Producto seleccionado:** `{producto_seleccionado}`  
            **Producto recomendado:** `{producto_recomendado}`

            **Confianza:** `{mejor['confidence']:.2f}`  
            🛈 *Esto significa que en el **{mejor['confidence']*100:.0f}%** de las veces que alguien compró **{producto_seleccionado}**, también compró **{producto_recomendado}**.*

            **Relevancia (lift):** `{mejor['lift']:.2f}`  
            🛈 *Un valor mayor a 1 indica que la compra conjunta entre estos productos es más frecuente de lo esperado.*
            """)
            st.markdown("---")
        else:
            st.warning("No se encontraron recomendaciones para este producto. Probá con otro.")
    
        # footer:
        st.markdown(f"""
        {"<div style='font-size:12px;color:gray;margin-top:10px;'>ℹ️ Utiliza reglas de asociación inversas aplicadas sobre los ítems seleccionados. Se aplican filtros por confianza y lift.</div>"}
        """, unsafe_allow_html=True)
        
             
            
    # ◯ Heatmap por producto (movido desde sección separada)
    with tabs[2]:
        st.subheader == "📌 Heatmap de Producto"
        
        st.markdown("## 📌 Heatmap de Co-ocurrencia por Producto")
        st.markdown(
            "Este gráfico muestra cómo se relaciona un producto específico con otros, "
            "según la métrica seleccionada."
        )

        from charts.HeatmapXTab import HeatmapCrosstab

        # ◯ Crear instancia del generador de heatmaps
        heat = HeatmapCrosstab(rules)

        # ◯ Obtener productos únicos desde reglas
        productos_disponibles = sorted(set(rules['antecedents'].explode()) | set(rules['consequents'].explode()))
        producto_base = st.selectbox("🧲 Seleccioná un producto base:", productos_disponibles)

        # ◯ Selección de métrica
        metrica = st.selectbox("📏 Seleccioná la métrica:", ["support", "lift", "confidence"])

        # ◯ Explicación contextual de la métrica seleccionada
        explicaciones = {
            "support": "🔥 <b>Support (Soporte)</b>: muestra qué tan seguido se venden juntos los productos.<br>"
                    "👉 Útil para detectar <b>productos que siempre aparecen en conjunto</b>.",

            "confidence": "🔥 <b>Confidence (Confianza)</b>: indica qué tan probable es que se compre el segundo producto "
                        "cuando ya se compró el primero.<br>"
                        "👉 Útil para sugerencias de <b>“quienes compraron esto, también compraron…”</b>",

            "lift": "🔥 <b>Lift</b>: mide si dos productos se potencian cuando se venden juntos, más allá de lo esperable.<br>"
                    "👉 Útil para identificar <b>combinaciones fuertes o ideales para promociones cruzadas</b>."
        }

        st.markdown(
            f"""
            <div style='
                font-size: 14px;
                margin-bottom: 20px;
                background-color: #f1f1f105;
                padding: 10px 15px;
                border-left: 4px solid #ff6d00;
                border-radius: 5px;
                color: #ddd;
                line-height: 1.5;
            '>
            {explicaciones[metrica]}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ◯ Filtrar reglas donde el producto seleccionado es el antecedente
        recomendaciones = rules[rules['antecedents'].apply(lambda x: producto_base in x)]

        # ◯ Ordenar por la métrica elegida
        recomendaciones = recomendaciones.sort_values(metrica, ascending=False)

        # ◯ Mostrar los 5 recomendados más fuertes
        top_recomendados = recomendaciones['consequents'].explode().value_counts().head(5).index.tolist()

        st.markdown("### 🔗 Recomendaciones basadas en asociación")
        st.write("Los siguientes productos aparecen frecuentemente junto a", f"**{producto_base}**:")

        # ◯ Crear tabla cruzada manualmente desde reglas
        df = rules.copy()
        df = df.explode("antecedents")
        df = df.explode("consequents")
        df = df[df["antecedents"] == producto_base]

        crosstab = df.pivot_table(
            index="antecedents",
            columns="consequents",
            values=metrica,
            aggfunc="mean",
            fill_value=0
        ).iloc[:, :10]  # Mostrará hasta 10 productos relacionados como máximo

        # ◯ Graficar heatmap
        fig = heat.plot_heatmap(crosstab)

        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

        st.markdown(
        f"""
        <div style='
            margin-top: 25px;
            padding: 15px;
            background-color: #1e1e1e;
            border-left: 4px solid #ff6d00;
            border-radius: 5px;
            font-size: 15px;
            line-height: 1.6;
            color: #ddd;
        '>
            <b>¿Cómo interpretar este heatmap?</b><br>
            El gráfico muestra la intensidad de relación entre <b>{producto_base}</b> y otros productos.<br>
            Cuanto más oscuro el recuadro, mayor es la <b>{metrica}</b> observada entre ambos ítems.<br>
            Esto puede ayudarte a identificar productos que suelen comprarse juntos o que podrían recomendarse juntos en la tienda o sitio web.
        </div>
        """,
        unsafe_allow_html=True
        )

        # ◯ Mostrar ubicación sugerida si el producto base está en un bundle conocido
        ubicacion = df_bundle_products[df_bundle_products['nodes'] == producto_base]

        if not ubicacion.empty:
            categoria = ubicacion['category'].iloc[0]

            # ◯ Buscar todos los productos en ese mismo bundle
            otros = df_bundle_products[df_bundle_products['category'] == categoria]

            # ◯ Excluir el producto actual
            productos_relacionados = otros[otros['nodes'] != producto_base]['nodes'].tolist()

            # ◯ Mostrar bloque de sugerencia

            # ◯ Calcular productos sugeridos ordenados por métrica
            df_metric = df.groupby("consequents")[metrica].mean().sort_values(ascending=False)
            df_metric = df_metric[df_metric.index != producto_base]

            # ◯ Armar la lista en HTML
            items_html = "".join([
                f"<div style='margin-bottom:6px; color: #ddd; font-size:15px;'>"
                f"<span style='color: #ffaa00; font-weight: bold;'>✔️</span> {prod}</div>"
                for prod in df_metric.index.tolist()
            ])

            # ◯ Cuadro de sugerencia completo con lista integrada
            st.markdown(
                f"""
                <div style='
                    margin-top: 20px;
                    padding: 15px;
                    background-color: #1e1e1e;
                    border-left: 4px solid #ff6d00;
                    border-radius: 5px;
                    font-size: 15px;
                    line-height: 1.6;
                    color: #ddd;
                '>
                    <div style='font-size:21px; font-weight:bold; color:#fff; margin-bottom:10px;'>
                    🟡 Sugerencia de Ubicación / Agrupación
                    </div>
                    Este producto forma parte del bundle: <b>📦 {categoria}</b>.<br>
                    Podría colocarse cerca de productos similares para mejorar la visibilidad o fomentar compras combinadas.
                    <br><br>
                    <b>Productos sugeridos para agrupar (ordenados por <code>{metrica}</code>):</b>
                    {items_html}
                    </div>
                """,
                unsafe_allow_html=True
            )


    # ◯ Sección Cross Selling Products
    # -----------------------------------------------------------------------------------------------------------------
    with tabs[3]:
            st.markdown("## 🔁 Cross Selling Products")
            st.markdown("""
            **Top 5 Cross-Selling Products**

            Cross-selling involves identifying products frequently purchased together, gauged by high **:orange[support]** reflecting their `co-occurrence` in transactions.   
            The concept considers not only the `frequency of joint purchases` but also the `strength of these associations` measured by **:orange[confidence]**.

            Focusing on product combinations with both `high support and confidence` helps pinpoint reliably associated items, enabling businesses to strategically promote or bundle products for an `enhanced customer shopping` experience.

            The table below shows the **:orange[top 5 cross-selling-product pairs]**, sorted by their `average confidence and support`.
            """)