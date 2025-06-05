# ◯ SECCIÓN 9 – CONCLUSIONES Y APRENDIZAJES DEL PROYECTO
# ............................................................................................
# Objetivo:
#   Presentar una síntesis técnica del proyecto realizada desde una perspectiva analítica,
#   incluyendo el objetivo general, decisiones metodológicas, habilidades aplicadas, resultados
#   obtenidos, recomendaciones estratégicas y oportunidades de mejora.
#
# Contenido:
#   - Objetivo general del proyecto
#   - Metodología aplicada y enfoque analítico
#   - Habilidades puestas en práctica durante el desarrollo
#   - Principales resultados y hallazgos
#   - Recomendaciones accionables para el negocio
#   - Reflexión sobre mejoras futuras y escalabilidad

import streamlit as st

def show_section_9_summary():


    st.subheader("📌 Objetivo General")
    st.markdown("""
    Este proyecto tiene como propósito aplicar el análisis de canasta de productos en un entorno de retail, utilizando reglas de asociación para identificar patrones de compra y generar recomendaciones estratégicas.
    """)

    st.markdown("---")

    st.subheader("🔍 Enfoque Analítico y Metodología")
    st.markdown("""
    - Transformación de datos reales de transacciones a formato canasta.  
    - Aplicación del algoritmo **Apriori** con la librería `mlxtend`.  
    - Evaluación de las reglas utilizando métricas clave:  
      `support`, `confidence` y `lift`.
    - Priorización de reglas interpretables y de alto valor accionable para el negocio.
    """)

    st.markdown("---")

    st.subheader("🧠 Habilidades Aplicadas")
    st.markdown("""
    - Preprocesamiento y limpieza de datos reales.  
    - Minería de reglas de asociación y evaluación estadística.  
    - Visualización interactiva de resultados y patrones.  
    - Desarrollo de una app funcional con navegación, interpretación automática y recomendaciones accionables.
    """)

    st.markdown("---")

    st.subheader("📈 Resultados Destacados")
    st.markdown("""
    - Identificación de reglas con **confianza superior al 70%** y **lift mayor a 20**.  
    - Detección de patrones frecuentes entre variantes de productos (ej: juegos de té).  
    - Generación de recomendaciones automáticas basadas en combinaciones reales de productos.
    """)

    st.markdown("---")

    st.markdown("""
    <div style='font-size:10px'>
    
    #### 📋 Metricas y Recomendaciones")
      
    | Categoría de Acción                  | Métrica aplicada                          | 📊 Qué nos dice la métrica (visión analítica)                                                                 | 🚀 Acción recomendada (aplicación práctica)                                       |
    |--------------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
    | ✔️ Bundles inteligentes              | Lift > 3                                  | Productos que se compran juntos con una relación 3× más fuerte que el azar.                                   | Ofrecer bundles de productos frecuentemente comprados juntos.                   |
    | ✔️ Promociones cruzadas              | Confidence > 0.70                         | Alta probabilidad (más del 70%) de que los productos se compren en la misma transacción.                      | Diseñar campañas promocionales con descuentos por compra combinada.             |
    | ✔️ Recomendaciones personalizadas    | Confidence > 0.60 y Support > 5%          | Asociación frecuente y con probabilidad razonable de que los productos aparezcan juntos.                      | Incorporar recomendaciones personalizadas en el carrito o página de producto.   |
    | ✔️ Optimización de inventario        | Top productos como antecedente en reglas  | Algunos productos suelen impulsar la compra de otros; son disparadores clave.                                 | Optimizar layout en tienda física o e-commerce, y ajustar niveles de stock.     |
    | ✔️ Campañas Puntuales                | Top 5 productos más frecuentes en reglas  | Productos más influyentes en la red de asociaciones, ideales para captar atención.                            | Usarlos como foco en campañas, promociones destacadas o visual merchandising.   |
    | ✔️ Acciones operativas y formativas  | Basado en reglas conectadas               | Algunos productos o patrones tienen alta conexión; clave para decisiones internas o formación.                | Capacitar al equipo de ventas y generar reportes de seguimiento periódicos.     |

    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.subheader("🛠️ Posibles Mejoras Futuras")
    st.markdown("""
    - Incorporar segmentación de clientes para recomendaciones más personalizadas.  
    - Aplicar algoritmos más eficientes como **FP-Growth** para escalabilidad.  
    - Implementar reducción de reglas mediante clustering o filtrado inteligente.  
    - Evaluar la efectividad de las recomendaciones en otros escenarios reales.
    """)

    st.markdown("---")

    st.success("Este proyecto integró herramientas y técnicas clave de ciencia de datos, con foco en generar valor de negocio a través del análisis de transacciones. Refleja tanto el conocimiento adquirido como una base sólida para iteraciones futuras más avanzadas.")
