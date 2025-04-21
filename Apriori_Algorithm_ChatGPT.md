¡Claro! Vamos a desglosarlo paso a paso de manera sencilla.

---

## 🧠 ¿Qué es el algoritmo Apriori?

**Apriori** es un algoritmo de *Aprendizaje No Supervisado* que se usa en **Reglas de Asociación**, dentro del campo de **Minería de Datos**.

Se utiliza para **descubrir relaciones frecuentes** entre conjuntos de ítems en bases de datos transaccionales, como por ejemplo:

📦 Qué productos suelen comprarse juntos en un supermercado.  
Ej: Si un cliente compra **pan**, probablemente también compre **manteca**.

---

## 📚 Grupo de algoritmos

**Categoría**: *Aprendizaje No Supervisado*  
**Subcategoría**: *Reglas de Asociación* (Association Rule Learning)

---

## 🧾 ¿Dónde se aplica?

- Retail / supermercados → productos que se compran juntos
- E-commerce → recomendaciones de productos
- Bancos → detección de combinaciones de servicios usados por clientes
- Salud → relaciones entre síntomas y enfermedades

---

## ⚙️ ¿Cómo funciona?

El algoritmo trabaja en tres pasos:

### ◯ Paso 1: Encontrar *ítems frecuentes*
Busca conjuntos de ítems (llamados *itemsets*) que ocurren juntos más veces que un umbral mínimo definido por el usuario (soporte mínimo).

Ejemplo:
```
Transacción 1: leche, pan, manteca  
Transacción 2: leche, pan  
Transacción 3: pan, manteca  
```
Si el soporte mínimo es 50%, el conjunto `["pan"]` es frecuente, aparece en 3 de 3 transacciones.

---

### ◯ Paso 2: Generar reglas de asociación
A partir de los ítems frecuentes, genera reglas del tipo:

```
{leche, pan} => {manteca}
```

Que se interpreta como:
> "Si alguien compra leche y pan, probablemente también compre manteca."

---

### ◯ Paso 3: Evaluar las reglas
Cada regla se evalúa con 3 métricas:

- **Soporte (support)**: frecuencia de la combinación en todas las transacciones  
  `Soporte({A,B}) = ocurrencias de A y B juntos / total transacciones`

- **Confianza (confidence)**: probabilidad de que B ocurra dado que ocurrió A  
  `Confianza(A => B) = Soporte({A,B}) / Soporte({A})`

- **Elevación (lift)**: mide si la aparición de B está realmente relacionada con A  
  `Lift(A => B) = Confianza(A => B) / Soporte(B)`

  Si:
  - **Lift > 1**: A y B están positivamente relacionados
  - **Lift = 1**: A y B son independientes
  - **Lift < 1**: A y B tienen relación negativa

---

## 🧪 Ejemplo práctico simple

Supongamos estas transacciones:

| ID | Ítems                           |
|----|---------------------------------|
| 1  | leche, pan, manteca            |
| 2  | leche, pan                     |
| 3  | pan, manteca                   |
| 4  | leche, manteca                 |
| 5  | leche, pan, manteca            |

### Resultado:
- Soporte de `pan` = 4/5 = 0.8
- Soporte de `{pan, manteca}` = 3/5 = 0.6
- Confianza de `{pan} => {manteca}` = 0.6 / 0.8 = 0.75
- Soporte de `manteca` = 4/5 = 0.8
- Lift = 0.75 / 0.8 = 0.9375 → ligeramente menos probable de lo esperado

---

## 📦 Implementación en Python

```python
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Transacciones
dataset = [['leche', 'pan', 'manteca'],
           ['leche', 'pan'],
           ['pan', 'manteca'],
           ['leche', 'manteca'],
           ['leche', 'pan', 'manteca']]

# Codificar transacciones
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apriori
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print(rules)
```

---


### 📋 Tabla resumen: Parámetros clave del algoritmo Apriori (`mlxtend`)

| Etapa              | Función                  | Parámetro        | Tipo       | Descripción                                                                 |
|--------------------|--------------------------|------------------|------------|-----------------------------------------------------------------------------|
| Itemsets frecuentes | `apriori()`              | `min_support`    | `float`    | Soporte mínimo requerido para considerar un conjunto de ítems como frecuente |
|                    |                          | `use_colnames`   | `bool`     | Si es `True`, muestra los nombres de los ítems en lugar de índices          |
|                    |                          | `max_len`        | `int`      | Longitud máxima del itemset (opcional)                                      |
|                    |                          | `verbose`        | `int`      | Muestra logs si se activa (opcional)                                        |
| Reglas de asociación | `association_rules()`   | `metric`         | `str`      | Métrica para evaluar las reglas: `"support"`, `"confidence"`, `"lift"`, etc. |
|                    |                          | `min_threshold`  | `float`    | Valor mínimo requerido para la métrica elegida                              |

### 🧠 Métricas más comunes usadas en `association_rules()`

| Métrica       | ¿Qué mide?                                                                 |
|---------------|------------------------------------------------------------------------------|
| `support`     | Frecuencia conjunta del antecedente y consecuente                           |
| `confidence`  | Probabilidad de que ocurra el consecuente dado el antecedente               |
| `lift`        | Relación entre A y B: si es > 1 hay asociación positiva, si < 1 es débil    |
| `leverage`    | Diferencia entre el soporte real y el esperado si fueran independientes     |
| `conviction`  | Medida alternativa a la confianza, más sensible a desequilibrios            |


### 🚀 Recomendación práctica de valores

| Caso de uso                     | `min_support` | `metric`      | `min_threshold` |
|----------------------------------|---------------|----------------|------------------|
| Reglas comunes                   | 0.3 – 0.5     | `"confidence"` | 0.6 – 0.8        |
| Reglas fuertes (pero raras)      | 0.1 – 0.2     | `"lift"`       | > 1.0            |
| Exploración general              | 0.01          | `"support"`    | 0.01             |


---


Ejemplo:

    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

Esto filtra solo reglas con lift > 1, es decir, que impliquen una relación positiva.
