
import pandas as pd

def get_top_cross_selling_rules(rules_df, top_n=5, sort_by="confidence_mean"):
    """
    Filtra las mejores reglas de cross-selling eliminando duplicados A→B y B→A.

    Parámetros:
    - rules_df: DataFrame resultado de get_cross_selling_products()
    - top_n: número de reglas a retornar
    - sort_by: columna de ordenamiento principal (por defecto: "confidence_mean")

    Retorna:
    - DataFrame con las top-N reglas no duplicadas (simétricamente)
    """
    # Crear clave simétrica para identificar duplicados tipo A→B y B→A
    rules_df = rules_df.copy()
    rules_df["pair_key"] = rules_df.apply(
        lambda x: tuple(sorted([x["antecedents"], x["consequents"]])), axis=1
    )

    # Eliminar duplicados simétricos
    rules_dedup = rules_df.drop_duplicates(subset="pair_key").drop(columns="pair_key")

    # Ordenar y devolver top-N
    return rules_dedup.sort_values(by=[sort_by, "support"], ascending=False).head(top_n).reset_index(drop=True)
