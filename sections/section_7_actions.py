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