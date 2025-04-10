# Algoritmo Apriori Explicado

**User:** Valentina Larrañaga (mvlarra@gmail.com)  
**Created:** 4/10/2025 12:56  
**Updated:** 4/10/2025 12:57  
**Exported:** 4/10/2025 12:59  

## Prompt:
puedes explicarme brevemente y con ejemplos de que se trata este algoritmo de ML: Apriori Algorithm

## Response:
¡Claro! El algoritmo **Apriori** es un algoritmo clásico de **Machine Learning** usado principalmente en **minería de datos** para encontrar **reglas de asociación** entre elementos dentro de grandes conjuntos de datos.

* * *

### 🧠 ¿Qué hace el Algoritmo Apriori?

Busca **patrones frecuentes** y **reglas de asociación** en transacciones, como:

> “Los clientes que compran pan y manteca, también tienden a comprar leche”.

Se usa mucho en **análisis de canasta de mercado (market basket analysis)**.

* * *

### ⚙️ ¿Cómo funciona Apriori?

1.  **Encuentra ítems frecuentes** en un conjunto de transacciones (los que aparecen con una frecuencia mínima, llamada _soporte_).
    
2.  A partir de esos ítems frecuentes, genera **combinaciones (conjuntos de ítems)** que ocurren juntos.
    
3.  De esas combinaciones, crea **reglas de asociación** del tipo:
    
    > Si A y B ocurren, entonces C también (A, B → C)
    

* * *

### 📊 Ejemplo simple:

Supongamos que tenemos estas transacciones de supermercado:

| Transacción | Productos comprados |
| --- | --- |
| T1 | Pan, Leche |
| T2 | Pan, Pañales, Cerveza, Manteca |
| T3 | Leche, Pañales, Cerveza, Pan |
| T4 | Pan, Leche, Pañales, Cerveza |
| T5 | Leche, Pan, Cerveza |

#### Paso 1: Contamos qué productos son más frecuentes (soporte)

*   Pan: 5 veces
    
*   Leche: 4 veces
    
*   Pañales: 3 veces
    
*   Cerveza: 4 veces
    
*   Manteca: 1 vez
    

Supongamos que el soporte mínimo es 3, entonces eliminamos Manteca.

#### Paso 2: Generamos combinaciones frecuentes (como {Pan, Leche}, {Pan, Cerveza}, etc.)

#### Paso 3: Generamos reglas como:

*   **{Pañales, Cerveza} → Pan** con un cierto _confianza_ (probabilidad condicional de que si alguien compra Pañales y Cerveza, también compre Pan)
    

* * *

### 📌 Métricas clave del algoritmo:

*   **Soporte (support)**: Frecuencia con la que aparece un ítem o conjunto.
    
*   **Confianza (confidence)**: Cuán seguido ocurre la consecuencia si ocurre el antecedente.
    
*   **Lift**: Cuánto mejora la probabilidad de la consecuencia si se da el antecedente (comparado con que ocurran por separado).
    

* * *

¿Querés que te lo muestre con código en Python usando `mlxtend` o algún dataset real tipo supermercado?

## Prompt:
pero dentro de cual grupo de algorithmo de ML estaria ? Ejemplo:
Decission Tree
Random Forest

## Response:
¡Buena pregunta! El **Apriori Algorithm** **no** pertenece a los algoritmos clásicos de predicción como los que mencionás (**Decision Tree**, **Random Forest**, etc.), sino que cae en otra categoría dentro del aprendizaje automático.

* * *

### 📦 ¿A qué grupo pertenece Apriori?

**➡️ Apriori pertenece al grupo de: `Aprendizaje no supervisado (Unsupervised Learning)`**, más específicamente a la **minería de reglas de asociación** (_Association Rule Learning_).

* * *

### 🔍 Comparación con otros tipos de algoritmos:

| Tipo de algoritmo | Ejemplos | ¿Qué hace? |
| --- | --- | --- |
| **Supervisado** | Decision Tree, Random Forest, SVM | Predice una etiqueta u objetivo conocido |
| **No supervisado** | Apriori, K-Means, DBSCAN | Encuentra patrones o agrupaciones sin objetivo conocido |
| **Reforzamiento** | Q-Learning, Deep Q-Networks | Aprende con recompensas y penalizaciones (tipo videojuegos) |

* * *

### 📘 En resumen:

*   **Apriori** no predice valores ni clasifica.
    
*   Lo que hace es **descubrir reglas ocultas** en grandes volúmenes de datos.
    
*   Es ideal cuando querés analizar **comportamientos** (por ejemplo, qué productos se compran juntos), sin tener una "respuesta correcta" como objetivo.
    

* * *

¿Querés un gráfico tipo esquema para visualizar esto mejor?



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)