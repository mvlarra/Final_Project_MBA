
# Explicación de Clase — `ProductNetwork`

Esta clase implementa una red de productos basada en reglas de asociación. Utiliza búsqueda en amplitud (BFS) para explorar relaciones desde productos iniciales y construir subredes basadas en métricas como `support`, `confidence` o `lift`.

---

## 📦 Clase: `ProductNetwork`

| Elemento                  | Descripción                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------|
| `rules`                   | DataFrame con reglas de asociación.                                                         |
| `col_source`              | Columna que representa el producto origen (`antecedents`).                                  |
| `col_target`              | Columna que representa el producto destino (`consequents`).                                 |
| `RulesGraphManager`       | Clase para construir grafos con nodos y aristas a partir de reglas.                         |

---

## 🔍 Método: `get_bfs_rules(...)`

Realiza una búsqueda en amplitud desde uno o varios productos para construir una red de productos relacionada.

| Parámetro         | Descripción |
|-------------------|-------------|
| `products`        | Lista de productos raíz para iniciar la búsqueda. |
| `metric`          | Métrica a usar para priorizar relaciones (`support`, `confidence`, etc). |
| `threshold`       | Valor mínimo de la métrica para considerar la relación. |
| `max_depth`       | Profundidad máxima del grafo a explorar. |
| `top_n`           | Número máximo de relaciones por producto. |

✅ Devuelve:
- `df_bfs`: nodos alcanzados, profundidad, y padres.
- `rules_bfs`: subconjunto de reglas entre esos nodos.

---

## 🎯 Método: `get_graph_features(...)`

Construye un grafo con nodos y enlaces desde los resultados de `get_bfs_rules`.

- Mapea los productos alcanzados (`df_bfs`) con las reglas aplicables (`rules_bfs`).
- Asigna una `rank` a los enlaces que conectan cada par (padre → hijo).
- Permite filtrar solo las reglas estrictas del recorrido si `strict_rules=True`.

---

## 🔁 Método Estático: `bfs(...)`

Versión simplificada de la búsqueda en amplitud. Devuelve una lista de nodos con su nivel de profundidad y su padre directo.

---

## 🚀 Método Estático: `bfs_complete(...)`

Extiende la búsqueda BFS incluyendo:

| Columna Resultante        | Significado |
|----------------------------|-------------|
| `rank`                    | Orden de aparición en la red. |
| `depth`                   | Nivel de profundidad del nodo. |
| `nodes`, `parent`, `root` | Nodo actual, su padre y el nodo raíz. |
| `edges_<metric>`          | Valor de la métrica entre padre e hijo. |
| `edges_route_<metric>`    | Valores acumulados a lo largo del camino. |
| `rank_edges`              | Orden relativo dentro del nivel. |
| `route`                   | Camino completo desde el nodo raíz. |

---

## ✅ Recomendaciones de Negocio

- Usar `bfs_complete` para explorar rutas de influencia de productos líderes.
- Visualizar redes para detectar productos puente, hubs o rutas de compra.
- Aplicar filtros por `confidence` o `lift` para asegurar relevancia comercial.
