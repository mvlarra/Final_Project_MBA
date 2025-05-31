# ◯ SECTION 8 – GLOSARIO DE MÉTRICAS
# Objetivo:
#   Proporcionar definiciones claras y fórmulas clave de las métricas utilizadas en el análisis de reglas de asociación.
# Contenido:
#   - Definiciones de Support, Confidence, Lift, Leverage y Conviction
#   - Ejemplos de fórmulas aplicadas
#   - Explicaciones orientadas a usuarios de negocio no técnicos

import streamlit as st



# ◯ Sección 8: GOLOSARIO DE METRICAS
# -----------------------------------------------------------------------------------------------------------------

def show_section_8_glosario():  # Función que muestra la sección de glosario de métricas, proporcionando definiciones y fórmulas clave utilizadas en el análisis de reglas de asociación.

    st.subheader("📏 Glosario de Métricas")

    st.markdown("""
    **:orange[Support]**  
    The proportion of transactions that contain a specific itemset. High support values indicate that the itemset is frequently purchased together.

    - *Item Support:*  
    `Support(A) = Transactions containing A / Total number of transactions`

    - *Co-occurrence Support:*  
    `Support(A ∪ B) = Transactions containing both A and B / Total number of transactions`


    **:orange[Confidence]**    
    The conditional probability that a transaction containing item A will also contain item B.

    - `Confidence(A → B) = Support(A ∪ B) / Support(A) × 100%`  
    - `Confidence(B → A) = Support(A ∪ B) / Support(B) × 100%`


    **:orange[Lift]**  
    Indicates how much more likely item B is purchased when item A is purchased, compared to when item B is purchased independently.

    - `Lift(A → B) = Support(A ∪ B) / (Support(A) × Support(B))`


    **:orange[Leverage]**  
    Measures how much more often A and B occur together than expected if they were independent.

    - `Leverage(A → B) = Support(A ∪ B) − (Support(A) × Support(B))`


    **:orange[Conviction]**  
    Indicates the strength of implication in the rule. High values (>1) suggest stronger dependency.

    - `Conviction(A → B) = (1 − Support(B)) / (1 − Confidence(A → B))`  
    - `Conviction(B → A) = (1 − Support(A)) / (1 − Confidence(B → A))`
    """)