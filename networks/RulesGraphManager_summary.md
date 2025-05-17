
# Explicación de Columnas — Market Basket Graph Analysis

Este documento resume el significado, uso, aplicación y recomendaciones de negocio para las columnas generadas por el análisis de red con `RulesGraphManager`.

---

## 🔵 df_nodes_profile — Productos como Nodos

| Columna         | Significado                                                  | Usado para                                         | Acciones donde se utiliza                          | Recomendaciones de Negocio                                       |
|------------------|---------------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| `nodes`          | Nombre del producto                                           | Identificación del nodo                            | Etiquetas de nodo, selección                       | Identificar productos clave para destacar en la tienda           |
| `adjacent_edges` | Total de conexiones (in + out)                               | Nivel de conectividad en la red                    | Ranking de hubs, tamaño de nodo                    | Promocionar productos con alto grado de conexión                 |
| `out_edges`      | Reglas donde es antecedente                                  | Detectar influencia como iniciador                 | Filtrar líderes de reglas                          | Usar como productos gancho o iniciales en bundles                |
| `in_edges`       | Reglas donde es consecuente                                  | Medir cuán recomendado es                          | Detectar productos destino                         | Posicionar cerca de productos iniciales o en upselling           |
| `mutual_edges`   | Relaciones recíprocas con otros nodos                        | Co-ocurrencia fuerte bidireccional                 | Detectar vínculos dobles                           | Vender como dúo, promociones combinadas                         |
| `support`        | Frecuencia del producto en transacciones                     | Medir popularidad                                  | Filtros de relevancia                              | Mantener stock alto, considerar para promociones masivas        |

---

## 🟠 df_edges_profile — Reglas como Enlaces

| Columna              | Significado                                             | Usado para                                          | Acciones donde se utiliza                            | Recomendaciones de Negocio                                               |
|------------------------|----------------------------------------------------------|------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------|
| `antecedents`          | Producto(s) origen de la regla                          | Patrón de inicio de compra                           | Mostrar en red, construir reglas                       | Evaluar qué productos disparan compras relacionadas                      |
| `consequents`          | Producto(s) sugerido como resultado                     | Destino de la asociación                             | Generación de recomendaciones                          | Mostrar junto a su antecedente o incluir en paquetes                     |
| `antecedent support`   | Frecuencia del antecedente                              | Base de la regla                                     | Filtrar reglas relevantes                              | Focalizar promociones en productos con base sólida                       |
| `consequent support`   | Frecuencia del consecuente                              | Atractivo individual                                 | Reglas con productos tendencia                         | Usar productos atractivos como anzuelo en promociones cruzadas           |
| `support`              | Frecuencia conjunta                                     | Co-ocurrencia real                                   | Ranking por fuerza                                     | Confirmar asociaciones fuertes para empaquetado                          |
| `confidence`           | Probabilidad de B dado A                                | Precisión de la regla                                | Filtros de confianza                                   | Reforzar visualmente la conexión entre productos en tienda o web         |
| `lift`                 | Valor predictivo frente al azar                         | Medir valor real                                     | Ordenar reglas, encontrar más impactantes              | Priorizar reglas con alto lift para campañas de recomendación            |
| `representativity`     | Relevancia o cobertura relativa                         | Generalización de la regla                           | Filtrar reglas más robustas                            | Aplicar promociones que impacten en mayor volumen de ventas              |
| `leverage`             | Diferencia frente a la independencia                    | Ganancia informativa                                 | Reglas con valor añadido                               | Detectar reglas que realmente cambian el comportamiento del cliente     |
| `conviction`           | Implicación lógica inversa                              | Certeza de la regla                                  | Análisis avanzado                                      | Usar en análisis de reglas sólidas a largo plazo                         |
| `zhangs_metric`        | Métrica sin sesgo por frecuencia                        | Evaluación justa                                     | Métricas alternativas                                  | Asegurar calidad de regla incluso en productos menos frecuentes          |
| `jaccard`              | Similaridad entre conjuntos                             | Co-ocurrencia relativa                               | Agrupamiento de productos                              | Sugerir productos similares o intercambiables                            |
| `certainty`            | Certeza de implicación                                  | Validez lógica                                       | Filtrado de reglas                                     | Detectar relaciones confiables para mejorar la experiencia del cliente   |
| `kulczynski`           | Promedio confianza A→B y B→A                            | Simetría en co-ocurrencia                            | Medición avanzada                                      | Sugerir relaciones estables o agrupamientos de productos                 |
| `edges`                | Texto representativo de la regla                        | Visualización de relaciones                          | Construcción de grafos                                 | Usar en dashboards, tooltips o presentaciones ejecutivas                |
