# ◯ SECTION 7 – ACCIONES ESTRATÉGICAS PARA TU NEGOCIO
# Objetivo:
#   Traducir hallazgos analíticos en acciones prácticas que generen impacto comercial.
# Contenido:
#   - Sugerencias accionables como bundles, descuentos o reubicaciones
#   - Asociación entre reglas y productos clave
#   - Priorización personalizada de acciones por parte del usuario
#   - Exportación de las acciones seleccionadas

import streamlit as st
import pandas as pd


# 7. ◯ Sección: ACCIONES ESTRATÉGICAS PARA TU NEGOCIO
# ............................................................................................

def show_section_7_actions(rules, Top_10_Mas_Vendidos):
    """
    Muestra la sección de acciones estratégicas basadas en las reglas de asociación generadas.
    Permite al usuario seleccionar acciones sugeridas para mejorar la estrategia comercial.
    :param rules: DataFrame con las reglas de asociación generadas.
    :param Top_10_Mas_Vendidos: DataFrame con el top 10 de productos más vendidos.
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
        "🟠 Old", 
        "🟠 New",
 
    ])

  
    with tabs[0]:    
        st.title("💼 Acciones estratégicas para tu negocio")

        st.markdown("""
        Basado en los patrones encontrados en los datos, estas son **acciones sugeridas** orientadas a generar impacto real en las ventas.  
        Cada acción está relacionada con productos clave del análisis y podés marcar su prioridad de implementación.

        ✅ El objetivo es **convertir los hallazgos en oportunidades de mejora**, aplicando estrategias como bundles, descuentos o reubicación de productos para **incrementar los ingresos, optimizar la rotación, potenciar la estrategia comercial y mejorar la experiencia de compra**.
        """)

        # ◯ Asegurar que antecedents y consequents estén en formato lista
        rules['antecedents'] = rules['antecedents'].apply(lambda x: [x] if isinstance(x, str) else x)
        rules['consequents'] = rules['consequents'].apply(lambda x: [x] if isinstance(x, str) else x)

        # ◯ Construir DataFrame con acciones, productos y lógica
        acciones = [
            {
                "Acción": "📦 Crear bundles con productos frecuentemente comprados juntos",
                "Productos sugeridos": "<br>• " + "<br>• ".join(
                    [f"{', '.join(r['antecedents'])} + {', '.join(r['consequents'])}" 
                        for _, r in rules.sort_values(by='lift', ascending=False).head(3).iterrows()]
                ),
                "Lógica utilizada": "Top 3 reglas con mayor lift"
            },
            {
                "Acción": "🛒 Ofrecer descuentos por comprar productos complementarios",
                "Productos sugeridos": "<br>• " + "<br>• ".join(
                    [f"{', '.join(r['antecedents'])} → {', '.join(r['consequents'])}"
                        for _, r in rules[rules['confidence'] > 0.7].head(3).iterrows()]
                ),
                "Lógica utilizada": "Reglas con confidence > 0.7"
            },
            {
                "Acción": "🏷️ Rediseñar la disposición de los productos en tienda o web",
                "Productos sugeridos": "<br>• " + "<br>• ".join(
                    rules['antecedents'].explode().value_counts().head(3).index.tolist()
                ),
                "Lógica utilizada": "Productos que aparecen con más frecuencia como antecedente"
            },
            {
                "Acción": "📈 Monitorear la rotación de los productos más vendidos",
                "Productos sugeridos": "<br>• " + "<br>• ".join(
                    Top_10_Mas_Vendidos['Producto'].head(3).tolist()
                ),
                "Lógica utilizada": "Top 10 productos más vendidos"
            },
            {
                "Acción": "🎯 Usar recomendaciones en tiempo real en el checkout",
                "Productos sugeridos": "<br>• " + "<br>• ".join(
                    [f"{', '.join(r['antecedents'])} → {', '.join(r['consequents'])}"
                        for _, r in rules[(rules['confidence'] > 0.6) & (rules['support'] > 0.05)].head(3).iterrows()]
                ),
                "Lógica utilizada": "Reglas con confidence > 0.6 y support > 0.05"
            },
            {
                "Acción": "🔍 Identificar productos con baja venta pero alta conexión (lift)",
                "Productos sugeridos": "<br>• " + "<br>• ".join(
                    [f"{', '.join(r['antecedents'])} → {', '.join(r['consequents'])}"
                        for _, r in rules[(rules['support'] < 0.05) & (rules['lift'] > 3)].head(3).iterrows()]
                ),
                "Lógica utilizada": "Reglas con support bajo y lift alto"
            },
            {
                "Acción": "📊 Generar reportes periódicos para seguir tendencias de compra",
                "Productos sugeridos": "-",
                "Lógica utilizada": "No aplica: acción operativa"
            },
            {
                "Acción": "💬 Capacitar al equipo de ventas en productos más conectados",
                "Productos sugeridos": "<br>• " + "<br>• ".join(
                    rules['antecedents'].explode().value_counts().head(3).index.tolist()
                ),
                "Lógica utilizada": "Productos que más veces aparecen en reglas"
            }
        ]

        df_acciones = pd.DataFrame(acciones)

        # ◯ Capturar interacción del usuario
        resultados_finales = []
        for i, fila in df_acciones.iterrows():
            st.markdown("---")  # Separador visual simple

            col1, col2 = st.columns([0.75, 0.25])
            with col1:
                check = st.checkbox(fila["Acción"], key=f"check_{i}")
            with col2:
                prioridad = st.selectbox("Prioridad", ["Alta", "Media", "Baja"], key=f"prio_{i}")

            st.markdown(f"""
            <div style='font-size: 0.85em; color: gray; line-height: 1.3;'>
                <b>Productos sugeridos:</b><br>{fila['Productos sugeridos']}<br>
                <b>Lógica:</b> {fila['Lógica utilizada']}
            </div>
            """, unsafe_allow_html=True)

            resultados_finales.append({
                "Acción": fila["Acción"],
                "Prioridad": prioridad,
                "Marcado": check,
                "Productos sugeridos": fila["Productos sugeridos"].replace("<br>• ", " - ").replace("<br>", " "),
                "Lógica utilizada": fila["Lógica utilizada"]
            })

        # ◯ Mostrar resumen de acciones marcadas
        st.markdown("### 🧾 Acciones seleccionadas")
        resumen_df = pd.DataFrame(resultados_finales)
        seleccionadas = resumen_df[resumen_df["Marcado"] == True]

        if not seleccionadas.empty:
            st.dataframe(seleccionadas.drop(columns=["Marcado"]), use_container_width=True)

            # ◯ Botón para exportar CSV
            csv = seleccionadas.drop(columns=["Marcado"]).to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Descargar recomendaciones seleccionadas", data=csv,
                                file_name="acciones_recomendadas.csv", mime="text/csv")
        else:
            st.info("Seleccioná al menos una acción para ver el resumen o exportarlo.")
            
    with tabs[1]:
            # ◯ Sección 5: ACCIONES ESTRATÉGICAS PARA TU NEGOCIO
            # -----------------------------------------------------------------------------------------------------------------
            # Objetivo:
            #   Presentar ideas prácticas y personalizadas que surgen del análisis de reglas de asociación.
            #   Enfocarse en mejorar la rentabilidad, retención de clientes y experiencia de compra.

        st.markdown("## 💼 Acciones estratégicas para tu negocio")
        
        st.markdown("---")
        st.markdown("### 🎯 Objetivo de esta sección")
        st.markdown("""
        En base al análisis de reglas de asociación y comportamiento de compra de tus clientes,
        te presentamos un conjunto de acciones que podés implementar en tu estrategia comercial.
        """)

        # ◯ Acciones por categoría
        st.markdown("### 🧩 Acciones recomendadas")
        
        acciones = {
            "🛍️ Bundles inteligentes": [
                "Agrupar productos con alta confianza (ej: 80%) y lift elevado para maximizar ventas conjuntas.",
                "Ejemplo: Ofrecé la taza verde Regency junto con la rosa, dado que se compran juntas frecuentemente."
            ],
            "🎁 Promociones cruzadas": [
                "Aplicar descuentos o puntos extra cuando se agregan productos relacionados al carrito.",
                "Ejemplo: Si se compra un set de platos florales, sugerí vasos del mismo estilo con 10% OFF."
            ],
            "🧠 Recomendaciones personalizadas": [
                "Usar las reglas con mayor lift para sugerencias dinámicas en el sitio o post-compra.",
                "Ejemplo: Recomendá un artículo complementario apenas se visualiza uno clave."
            ],
            "📦 Optimización de inventario": [
                "Identificar productos que se venden solo en conjunto y evitar sobrestock de los que no rotan solos.",
                "Ejemplo: Un adorno que siempre se compra junto a una vela podría necesitar menos stock individual."
            ],
            "📊 Decisiones basadas en datos": [
                "Priorizá productos con alta frecuencia en reglas como foco de campañas y displays en tienda.",
                "Ejemplo: Los 5 productos más frecuentes como antecedente pueden ser destacados en la home."
            ]
        }

        for categoria, ideas in acciones.items():
            st.markdown(f"#### {categoria}")
            for idea in ideas:
                st.markdown(f"- {idea}")
            st.markdown("")

        # ◯ Llamado a la acción
        st.markdown("---")
        st.markdown("### ✅ ¿Qué podés hacer hoy?")
        st.markdown("""
        - Elegí **2 o 3 acciones** y probalas durante una semana.
        - Medí resultados: ¿aumentaron las ventas de ciertos productos? ¿se agregaron más ítems al carrito?
        - Ajustá tus estrategias y repetí con nuevos productos clave.
        """)   
        
