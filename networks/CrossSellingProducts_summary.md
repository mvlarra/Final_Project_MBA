
# Explicación de Clase — `CrossSellingProducts`

Esta clase permite identificar oportunidades de **venta cruzada (cross-selling)** basadas en reglas de asociación. Se filtran, reordenan y enriquecen las reglas para encontrar relaciones sólidas y simétricas entre productos.

---

## 📦 Clase: `CrossSellingProducts`

| Elemento                  | Descripción                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------|
| `rules`                   | DataFrame con reglas de asociación.                                                         |
| `col_source`              | Columna de productos origen (`antecedents`).                                                |
| `col_target`              | Columna de productos destino (`consequents`).                                               |
| `RulesGraphManager`       | Clase para generar el grafo de relaciones (nodos y aristas) entre productos.                |

---

## 🔧 Método: `get_cross_selling_products(...)`

Devuelve un DataFrame filtrado y enriquecido con reglas ideales para sugerencias de **productos complementarios**. Aplica condiciones lógicas para encontrar relaciones equilibradas y significativas.

| Paso | Acción | Propósito |
|------|--------|-----------|
| 1 | Filtra por `support >= min_support` | Asegura que la regla tenga base estadística. |
| 2 | Filtra por `confidence >= min_confidence` | Descarta asociaciones débiles. |
| 3 | Calcula `support_ratio_diff` como: <br>max(antecedent support, consequent support) / min(...) | Mide desbalance entre productos. |
| 4 | Filtra por `support_ratio_diff < max_support_ratio_diff` | Se enfoca en productos con soporte similar. |
| 5 | Ordena por `confidence DESC` y `support_ratio_diff ASC` | Prioriza reglas confiables y balanceadas. |
| 6 | Calcula `consequent confidence` y `consequent support` desde la regla inversa (si existe) | Evalúa reciprocidad. |
| 7 | Renombra `confidence → antecedent confidence` y calcula `confidence_mean` como el promedio entre ambas direcciones. | Establece un score de simetría. |
| 8 | Filtra por `confidence_mean >= min_confidence` | Refuerza la consistencia bidireccional. |
| 9 | Devuelve columnas clave ordenadas por `confidence_mean` y `support`. | Devuelve resultados finales limpios y ordenados. |

**Columnas finales del DataFrame:**

- `antecedents`, `consequents`
- `antecedent support`, `consequent support`
- `antecedent confidence`, `consequent confidence`
- `support`, `support_ratio_diff`, `confidence_mean`

---

## 🧠 Método: `get_graph_features(...)`

| Acción | Descripción |
|--------|-------------|
| Instancia `RulesGraphManager` con las reglas filtradas. | Crea el grafo dirigido de relaciones. |
| Extrae `df_nodes` y `df_edges`. | Devuelve perfiles de productos y reglas para visualización o análisis. |

---

## ✅ Usos y Recomendaciones de Negocio

- Usar `confidence_mean` alto para identificar productos que **se refuerzan mutuamente**.
- Detectar pares equilibrados (`support_ratio_diff` ≈ 1) para **bundles simétricos**.
- Visualizar los resultados en red para encontrar **hubs de cross-selling**.
