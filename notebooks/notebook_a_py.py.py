#!/usr/bin/env python
# coding: utf-8

# # Projecto Final:  **Market Basket Analysis** for an Online Retail Bussines
# 
# **Date:**  
# April 2025
# 
# **Proyect Goal:**  
# Analizar las compras realizadas en una tienda online durante un año, para descubrir patrones sobre qué productos suelen comprarse juntos. Estos patrones permiten a la empresa entender mejor los hábitos de sus clientes y tomar decisiones inteligentes, como ofrecer sugerencias de compra, mejorar promociones o reorganizar productos en la tienda para aumentar las ventas.  
# <small>
# 
# * Ejemplos de lo que se puede lograr con este análisis:
# 
#     - **Sugerencias automáticas:** Si un cliente agrega una tetera al carrito, el sistema puede recomendarle también tazas de té.  
#     - **Promociones combinadas:** Ofrecer descuentos si alguien compra papel de regalo y tarjetas de felicitación juntas.  
#     - **Organización de la tienda online:** Mostrar cojines decorativos junto a sofás porque muchos clientes los compran juntos.  
#     - **Campañas de email personalizadas:** Enviar ofertas de velas perfumadas a clientes que anteriormente compraron ambientadores.  
#     - **Optimización del inventario:** Saber que los manteles se venden más cuando hay promociones de vajillas y preparar stock suficiente.

# 
# 
# 
# 
# **Dataset:**  
# Este dataset pertenece a la empresa **"Online Retail II"**, cuyo nombre no se especifica por motivos de confidencialidad, la cual se dedica a la venta de artículos de regalo para toda ocasión, y una parte importante de sus clientes son mayoristas. El dataset recopila un año completo de sus transacciones. 
# 
# <small> 
# 
# * Overview:  
#     - Time Range: 1 December 2010 – 9 December 2011 (one full year)
#     - Transactions: 541,909 rows
#     - Features: 8
#     - Business Type: Online giftware retailer (many wholesale customers)
#     - Region: Primarily UK
# 
# * Typical Columns (Features):
#     - InvoiceNo: Invoice number (unique ID for each transaction)
#     - StockCode: Product/item code
#     - Description: Item name
#     - Quantity: Number of items purchased
#     - InvoiceDate: Date and time of transaction
#     - UnitPrice: Price per item (in GBP)
#     - CustomerID: Unique ID for each customer
#     - Country: Customer’s country
# 
# * This dataset is often used for:
#     - Customer Segmentation (e.g., using RFM analysis)
#     - Sales Analysis & Forecasting
#     - Market Basket Analysis (e.g., association rules with Apriori)
#     - Data Cleaning & Preprocessing Practice
# 
# 
# * Source:  
#     - https://archive.ics.uci.edu/dataset/502/online+retail+ii  
#     - https://www.kaggle.com/datasets/thedevastator/online-retail-sales-and-customer-data/data

# ## ✔️ 0. CONFIGURACIÓN INICIAL

# In[25]:


# ◯ 0. CONFIGURACIÓN INICIAL
# -------------------------------------------------------------------------------------------------

# ✓ Ruta
ruta_archivo = '/workspaces/Final_Project_MBA/data/raw/data.csv'
output_dir = '/workspaces/Final_Project_MBA/app/models' # Ruta de salida para guardar resultados

# ✓ Parámetros de EDA
top_n_productos = 10  # Número de productos más vendidos a graficar

# ✓ Parámetros de Apriori
min_support = 0.01    # Soporte mínimo
min_lift = 1.0        # Lift mínimo
min_confidence = 0.5  # Confianza mínima (opcional si quieres filtrar más adelante)




# ## ✔️ 1. IMPORTAR LIBRERIAS

# In[26]:


# ◯ 1. IMPORTAR LIBRERÍAS
# ------------------------------------------------------------------

# ✓ Librerías para la manipulación de datos
import os
import pickle 
import numpy as np
import datetime as dt
import pandas as pd 


# ✓ Librerías para la visualización
import matplotlib.pyplot as plt 
import seaborn as sns

# ✓ Librerías para el análisis de datos
#! pip install --upgrade pip
#! pip install mlxtend
from mlxtend.frequent_patterns import apriori, association_rules

# ✓ Parámetros de visualización
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.2f}'.format)


# Verificar si el archivo de datos existe
if os.path.exists(ruta_archivo):
    print(f"El archivo {ruta_archivo} existe.")
else:
    print(f"El archivo {ruta_archivo} no existe.")
   
# Verificar si el directorio de salida existe
if os.path.exists(output_dir):
    print(f"El directorio {output_dir} existe.")
else:
    print(f"El directorio {output_dir} no existe, creando directorio...")
    os.makedirs(output_dir, exist_ok=True)




# ## ✔️ 2. CARGA DE DATOS
# 
# Objective: Obtain the data from source and get a first glimpse of their properties and presentation

# In[27]:


# ◯ 2. CARGA DE DATOS
# ------------------------------------------------------------------

df_raw = pd.read_csv(ruta_archivo, encoding="ISO-8859-1")       # Cargar datos originales
df_baking = df_raw.copy()                                       # Copia para el procesamiento (aplicar limpieza y procesamiento sobre df_baking)
df = df_baking.copy()                                           # Copia final para el Analisis   

# data = pd.read_csv('data.csv', encoding="ISO-8859-1")


# ## ✔️ 3. EDA INICIAL

# In[28]:


# ◯ 3. EDA INICIAL
# -------------------------------------------------------------------------------------------------

print("\n✅ Shape inicial:", df_raw.shape)
print("\n✅ Muestra Aleatoria de Observaciones:\n")
print(df_raw.sample(10,random_state=2025))
print("\n✅ Info general:")
print(df_raw.info())
print("\n✅ Valores nulos por columna:\n", df_raw.isnull().sum().loc[lambda x: x > 0])


# ## ✔️ 4. PROCESASMIENTO DE DATOS
# 
# Objectives: Perform the data cleaning, data transformation and data reduction steps to avoid data mistmatching, noisy data or data not wrangled
# 

# In[29]:


# ◯ 4. PROCESAMIENTO DE DATOS
# -------------------------------------------------------------------------------------------------

# ✓ Eliminar filas con valores nulos en columnas
df_baking = df_baking.dropna()  

# ✓ (Opcional) Si no se usa Customer ID, puede omitirse o eliminarse
# df = df.drop(columns=['Customer ID'])


# ✓ Renombrar columnas pasandolas a minuscula
df_baking.columns = df_baking.columns.str.lower()

# ✓ Filtrar United Kingdom
#    El dataset contiene transacciones de varios países, pero nos enfocaremos en el Reino Unido,
#    ya que es donde se encuentran la mayoria de transaccciones (91.5%). 
df_baking = df_baking[df_baking['country'] == 'United Kingdom'].copy()

# ✓ Limpieza de descripciones: Normalizar y limpiar los nombres de productos
#                              Convertimos los nombres de productos (Description) a minúsculas y eliminamos espacios extra.
df_baking['description'] = df_baking['description'].str.strip().str.lower()


# ✓  Tipos de datos
#    Cambiamos los tipos de datos de las columnas a los más adecuados para optimizar el rendimiento.

df_baking['invoice'] = df_baking['invoice'].astype(str)       # Convertimos los códigos de factura a string (evita errores de agrupación)
df_baking['stockcode'] = df_baking['stockcode'].astype('category')
df_baking['description'] = df_baking['description'].astype('category')
df_baking['country'] = df_baking['country'].astype('category')
df_baking['invoicedate'] = pd.to_datetime(df_baking['invoicedate'])


# ✓ Eliminar facturas canceladas:
#   Las devoluciones tienen valores negativos en Quantity y normalmente un código de factura que empieza con 'C'.
#   Estas transacciones no son útiles para MBA, ya que no representan compras reales.
#   En este caso lo resolveremos, asegurandonos que solo se incluyan transacciones de compra (cantidad > 0)
df_baking = df_baking[df_baking['quantity'] > 0]


df = df_baking.copy()

# ✓ Revisar df
print("\n✅ Shape df:", df.shape)
print("\n✅ Muestra Aleatoria de Observaciones en df:\n")
print(df.sample(10,random_state=2025))
print("\n✅ Info general df:")
print(df.info())


# ## ✔️ 5. EDA DESCRIPTIVO

# In[30]:


print(df.describe(include='number').T)
print(df.describe(include='category').T)


# ## ✔️ 6. EDA VISUAL - TOP PRODUCTS

# In[31]:


# ◯ Obtener los 10 productos más comprados
# ----------------------------------------------------------------------------------

# Se selecciona la columna 'description' del DataFrame df, que contiene las descripciones de los productos.
# Luego se cuenta la frecuencia de cada producto utilizando value_counts()
top_products = (df['description']
                .value_counts()  # Cuenta las ocurrencias de cada valor único en 'description'
                .nlargest(10))  # Selecciona los 10 productos más frecuentes

# ◯ Crear un DataFrame con los productos más comprados
# ----------------------------------------------------------------------------------

# Convierte la serie 'top_products' en un DataFrame, con el índice (nombre del producto) convertido a una columna.
# 'reset_index()' reinicia el índice y agrega una columna llamada 'index' que contiene los nombres de los productos.
top_products_df = pd.DataFrame(top_products).reset_index()

# ◯ Mostrar el DataFrame con los 10 productos más comprados
top_products_df


# In[32]:


# ◯ Visualización de los productos más comprados
# ---------------------------------------------------------------------------------

# ✓ Visualización de los productos más comprados
#    Se utiliza un gráfico de barras horizontales para mostrar los 10 productos más comprados.
#    Se ordenan de mayor a menor frecuencia de compra.

# Paleta de colores degradados de rosa (color fuerte arriba)
colors = sns.color_palette("husl", len(top_products))  # Paleta de colores viridis

# Crear gráfico
plt.figure(figsize=(12, 6))
top_products.sort_values().plot(kind='barh', color=colors)  # sort para que el más alto esté arriba
plt.title('Top 10 productos más comprados', fontsize=14)
plt.xlabel('Frecuencia de compra')
plt.ylabel('Producto')
plt.grid(axis='x', alpha=0.8)
plt.tight_layout()
plt.show()


# ## ✔️ 7. CREAR LA MATRIZ DE TRANSACCIONES (Basket Matrix)
# 
# The basket matrix contendra la cantidad comprada de cada producto por transaccion (invoice).
# 
# Este data frame es básicamente la cesta que nuestros clientes llevan al cajero de nuestra tienda.  
# Nos muestra cuánto compró este cliente/transacción (N.º de factura) por un artículo en particular.  
# Si el número es 0, el cliente no compró ese artículo.  
# Si muestra otro valor (8, por ejemplo), significa que el cliente ha comprado hasta 8 artículos.  
# 
# Para esto:  
# Agrupamos los productos por factura y convertimos cada factura en una fila con los productos como columnas.

# In[33]:


# ◯ Paso 1: Agrupar por factura y producto para construir la cesta
# ---------------------------------------------------------------------------------

# ✓ Sumamos las cantidades de cada producto dentro de cada factura
basket = df.groupby(['invoice', 'description'], observed=True)['quantity'].sum()
basket


# In[34]:


# ◯ Paso 2: Convertir la serie a una tabla con productos como columnas
# ---------------------------------------------------------------------------------

# ✓ Convertimos la serie a un DataFrame

basket = basket.unstack() # Unstack convierte las combinaciones (invoice, description) en una matriz
basket


# In[35]:


# ◯ Paso 3: Reemplazar valores faltantes (productos no comprados) por 0
# ---------------------------------------------------------------------------------

# ✓ Reemplazamos los valores NaN por 0
#   Así sabemos qué productos no fueron comprados en cada factura

basket = basket.reset_index().fillna(0).set_index('invoice')
    #   reset_index() convierte el índice en una columna normal
    #   fillna(0) reemplaza los NaN por 0
    #   set_index('invoice') vuelve a establecer la columna 'invoice' como índice
basket


# ### → ENCODE DE DATA:
# 
# En el market basket analysis, lo importante no es la cantidad comprada de cada artículo, sino que lo importante es saber si un artículo fue comprado o no.
# Ya que nuestro fin es saber cuál es la asociación entre comprar ciertos artículos y comprar otros.
# Por lo tanto, necesitamos codificar los datos de la canasta en datos binarios que indiquen si un artículo fue comprado (1) o no (0).
# 
# De esta forma, generamos un data frame que nos muestra si un artículo en particular fue comprado o no.

# In[36]:


# Aplicamos map a cada columna para convertir los valores a 1 o 0

basket = basket.apply(lambda col: col.map(lambda x: 1 if x > 0 else 0))
basket


# ### → FILTRAR TRANSACCIONES (Solo compras con mas de un articulo)
# 
# En el Market Basket Analysis, vamos a descubrir la asociación entre 2 o más productos que se compran según los datos históricos.  
# Por lo tanto, las transacciones que solo mueven un artículo, no nos seria de utilidad.   
# Es decir, ¿cómo podríamos descubrir la asociación entre 2 o más productos si solo se compró 1 producto?  
# Entonces, el siguiente paso es filtrar las transacciones que compraron más de 1 artículo.  
# 
# Según el resultado, podemos ver que hay 15,376 transacciones que compraron más de 1 artículo.  
# Esto significa que el 92.35 % de los datos de la canasta son transacciones en las que se compraron más de 1 artículo.

# In[37]:


basket = basket[(basket > 0).sum(axis=1) >= 2]

# ◯ Filtrar transacciones con al menos 2 productos
# ---------------------------------------------------------------------------------
# Paso 1: (basket > 0) crea un DataFrame booleano donde cada celda es True si ese producto fue comprado (> 0) y False si no.
# Paso 2: .sum(axis=1) suma los valores True por fila (es decir, cuenta cuántos productos fueron comprados en cada transacción).
# Paso 3: >= 2 mantiene solo las transacciones donde se compraron al menos 2 productos.
# Paso 4: Finalmente, se aplica ese filtro al DataFrame original 'basket', dejando solo las transacciones útiles para análisis de canasta
basket


# ## ✔️ 8. APLICO EL ALGORITMO
# 
# Después de generar la cesta de productos en el formato necesario, es el momento de aplicar el algoritmo.  
# Este algoritmo usa dos funciones que provienen de la libreria mlxtend:
# 1. **apriori:** Encontrar los conjuntos de productos frecuentes y 
# 2. **association_rules:** Generar las reglas de asociación entre esos productos.
# 

# ### → Conjunto de productos Frecuentes (Funcion **Apriori**)
# 
# - Encuentra los conjuntos frecuentes en un conjunto de datos, es decir, grupos de artículos que se compran juntos con una frecuencia superior al valor de soporte especificado.
# - Se utiliza para identificar qué combinaciones de artículos son compradas con mayor frecuencia.
# 
# Al aplicar el algoritmo Apriori, podemos definir los datos frecuentes que deseamos dando el valor de soporte.
# En este caso, defino los artículos comprados con mayor frecuencia como aquellos que se compran al menos un 3% del total de las transacciones.
# Esto significa que asignaré un valor de soporte de 0.03.
# Después de eso, agregué otra columna llamada "length" que contiene el número de artículos que se compraron.

# In[38]:


# ◯ Paso 1: Aplicamos el algoritmo Apriori para encontrar conjuntos de artículos frecuentes

basket = basket.astype(bool)  # Convertimos a booleano (True/False) para el algoritmo Apriori

frequent_itemsets = apriori(
    basket,                # ✓ DataFrame binario donde 1 indica que el artículo fue comprado y 0 que no
    min_support=0.03,      # ✓ Umbral mínimo de soporte: solo se consideran combinaciones presentes en al menos el 3% de las transacciones
    use_colnames=True      # ✓ Muestra los nombres reales de los artículos en lugar de índices
)


# ◯ Paso 2: Ordenamos los conjuntos frecuentes por soporte en orden descendente
frequent_itemsets = frequent_itemsets.sort_values(
    'support',             # ✓ Ordenamos en función del soporte (frecuencia relativa del conjunto)
    ascending=False        # ✓ De mayor a menor soporte
)


# ◯ Paso 3: Reiniciamos los índices del DataFrame ordenado
frequent_itemsets = frequent_itemsets.reset_index(drop=True)  # ✓ Eliminamos el índice anterior y creamos uno nuevo desde cero


# ◯ Paso 4: Agregamos una nueva columna que indica la cantidad de artículos en cada conjunto frecuente
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(
    lambda x: len(x)       # ✓ Contamos cuántos artículos hay en cada conjunto de ítems
)


# ◯ Mostramos el DataFrame final con:
# ✓ Conjuntos frecuentes de artículos
# ✓ Su soporte (frecuencia)
# ✓ Y la cantidad de artículos en cada conjunto
frequent_itemsets


# Como puedes ver, hay 108 transacciones que se consideran como artículos comprados con mayor frecuencia.  
# El "White Hanging Heart T-Light Holder" es el artículo más comprado con un valor de soporte de 12.1%.  
# Esto significa que el artículo se compró 1866 veces de todas las transacciones.

# Si solo queremos los conjuntos de 2 ítems que aparecen en al menos el 3% de las transacciones:

# In[39]:


frequent_itemsets[ 
    (frequent_itemsets['length']  == 2) &       # ✓ Conjuntos que tienen exactamente 2 artículos
    (frequent_itemsets['support'] >= 0.03)      # ✓ Cuyo soporte (frecuencia) es mayor o igual a 3%
]


# ###  → Encontrar Reglas de Asociación entre los productos (Funcion **association rules**) 
# - Genera reglas de asociación a partir de los conjuntos frecuentes obtenidos con el algoritmo Apriori.
# - Estas reglas muestran las relaciones entre los productos, por ejemplo, si un cliente compra un producto A, ¿qué tan probable es que compre también el producto B?
# - Se pueden filtrar las reglas utilizando métricas como confianza, soporte y lift para encontrar las relaciones más significativas.
# 
# Cada regla se evalúa con 3 métricas:
# 
# * Soporte (support): frecuencia de la combinación en todas las transacciones  
#     - Soporte({A,B}) = ocurrencias de A y B juntos / total transacciones
# 
# * Confianza (confidence): probabilidad de que B ocurra dado que ocurrió A  
#     - Confianza(A => B) = Soporte({A,B}) / Soporte({A})
# 
# * Elevación (lift): mide si la aparición de B está realmente relacionada con A  
#     - Lift(A => B) = Confianza(A => B) / Soporte(B)  
# Si:  
#     - Lift > 1: A y B están positivamente relacionados  
#     - Lift = 1: A y B son independientes  
#     - Lift < 1: A y B tienen relación negativa  
# 
# **Metricas:**
# * **support**:      Frecuencia conjunta del antecedente y consecuente
# * **confidence**:   Probabilidad de que ocurra el consecuente dado el antecedente
# * **lift**: 	    Relación entre A y B: si es > 1 hay asociación positiva, si < 1 es débil
# 
# Después de aplicar el algoritmo Apriori y encontrar los artículos que se compran con frecuencia, ahora es momento de aplicar las reglas de asociación.
# A partir de estas reglas, podemos extraer información e incluso descubrir conocimientos sobre qué artículos son más efectivos para venderse juntos.
# Ese es el objetivo principal de este proyecto.

# In[40]:


rules = association_rules(
    frequent_itemsets,     # ✓ Conjuntos frecuentes generados previamente con Apriori
    metric='lift',         # ✓ Métrica principal que se va a evaluar para filtrar reglas
    min_threshold=1        # ✓ Se seleccionan solo reglas con lift >= 1 (asociación no trivial)
).sort_values('lift', ascending=False)  # ✓ Se ordenan de mayor a menor lift

rules = rules.reset_index(drop=True)   # ✓ Se reinicia el índice del DataFrame resultante

rules                                   # ✓ Se muestra el DataFrame de reglas generadas


# ###  → Mostrar Reglas Legibles
# Definimos una funcion que muestre las reglas de asociación en formato legible.  
# Convierte sets en texto y redondea columnas clave si existen.

# In[41]:


def mostrar_reglas_legibles(rules_df):
    """
    Muestra reglas de asociación en formato legible.
    Convierte sets en texto y redondea columnas clave si existen.
    """
    df = rules_df.copy()

    # Convertir conjuntos a strings legibles
    df['antecedents'] = df['antecedents'].apply(lambda x: ', '.join(sorted(list(x))))
    df['consequents'] = df['consequents'].apply(lambda x: ', '.join(sorted(list(x))))

    # Columnas clave (si existen)
    columnas = ['support', 'confidence', 'lift']
    columnas_existentes = [col for col in columnas if col in df.columns]

    # Redondear columnas numéricas existentes
    df[columnas_existentes] = df[columnas_existentes].round(4)

    # Formatear support como porcentaje con 1 decimal
    if 'support' in columnas_existentes:
        df['support'] = (df['support'] * 100).map('{:.2f}%'.format)

    # Crear clave de comparación que sea independiente del orden
    df['combinacion'] = df.apply(lambda x: frozenset([x['antecedents'], x['consequents']]), axis=1)

    # Eliminar duplicados con la misma combinación y mismo lift
    df = df.drop_duplicates(subset=['combinacion', 'lift'])

    return df[['antecedents', 'consequents'] + columnas_existentes]

# Mostrar reglas legibles
rules_legibles = mostrar_reglas_legibles(rules)
rules_legibles


# <small>
# 
# 
# ### 1. **Lift (Mayor Asociación)**
# 
# A partir de los resultados de `association_rules`, podemos observar que:  
# - **ROSES REGENCY TEACUP AND SAUCER** (Taza y Platillo Regency Rosas), y  
# - **GREEN REGENCY TEACUP AND SAUCER** (Taza y Platillo Regency Verdes)  
# 
# son los artículos que tienen la **mayor asociación entre sí**, ya que presentan el **valor más alto de "lift"**.  
# **Cuanto más alto sea el valor del lift, mayor será la asociación entre los artículos.**  
# **Si el valor de lift es mayor a 1, ya es suficiente para considerar que existe una asociación significativa entre ellos.**  
# 
# En este caso, el valor más alto es **17.717**, lo cual es extremadamente alto.  
# Esto indica que estos dos productos se venden **muy bien juntos**.
# 
# ---
# 
# ### 2. **Soporte**
# 
# El valor de **soporte** para la combinación de:  
# - **ROSES REGENCY TEACUP AND SAUCER**, y  
# - **GREEN REGENCY TEACUP AND SAUCER**  
# 
# es de **0.0309**, lo que significa que en el **3.09% de todas las transacciones** estos dos productos se vendieron juntos.  
# En números absolutos, esto representa **476 veces**.
# 
# ---
# 
# ### 3. **Confianza**
# 
# El valor de **confianza (confidence)** permite extraer más información.  
# Recordemos que **la confianza depende del orden entre antecedente y consecuente**.  
# Si el antecedente es más frecuente que el consecuente, se aplica la **regla número 1** (y no la número 2), y viceversa.
# 
# En este caso, el producto **GREEN REGENCY TEACUP AND SAUCER** tiene mayor frecuencia como antecedente que el producto **ROSES REGENCY TEACUP AND SAUCER** como consecuente.  
# Por lo tanto, se aplica la siguiente regla:
# 
# > **GREEN REGENCY TEACUP AND SAUCER → ROSES REGENCY TEACUP AND SAUCER**
# 
# Esto significa que **los clientes tienden a comprar la taza y platillo de Rosas *después* de haber comprado la de color Verde**, y **no al revés**.
# 
# ---
# 
# Esta es una información muy valiosa, ya que nos indica **sobre qué producto podríamos aplicar descuentos estratégicos**.  
# Por ejemplo, podríamos ofrecer un **descuento en la taza y platillo de Rosas** si un cliente compra la de color Verde.
# 

# <small>
# 
# ## ✔️ 9. **Análisis de reglas de asociación**
# 
# ### 1. Regla: `roses regency teacup and saucer → green regency teacup and saucer`
# 
# **Interpretación:**
# - En el 3.10% de las transacciones aparecen ambos productos juntos.
# - Cuando hay "roses regency teacup and saucer", en el 71% de los casos también hay "green regency teacup and saucer".
# - El **lift = 17.72**, muy por encima de 1, indica una relación extremadamente fuerte.
#   
# ✅ **Esta es una regla muy útil** para estrategias de venta conjunta.
# 
# **📌 Acción recomendada:**  
# *Product bundling* → Ofrecer ambos productos como un set de té de colección.
# 
# ---
# 
# ### 2. Regla: `lunch bag red retrospot → lunch bag pink polkadot`
# 
# **Interpretación:**
# - El 3.06% de las transacciones contienen ambas lunch bags.
# - Cuando hay "lunch bag red retrospot", en el 42% de los casos también está la versión rosa.
# - El **lift = 7.63**, indica fuerte asociación.
# 
# 🟡 **Es útil**, aunque la confianza es moderada (42%).
# 
# **📌 Acción recomendada:**  
# *Item placement* → Colocar juntas ambas versiones en tienda física o ecommerce.
# 
# ---
# 
# ### 3. Regla: `jumbo bag red retrospot → jumbo bag pink polkadot`
# 
# **Interpretación:**
# - El 3.29% de las transacciones contienen ambas jumbo bags.
# - Cuando alguien compra la versión roja, solo el 35% también lleva la rosa.
# - Sin embargo, **lift = 6.70**, lo que sugiere una fuerte conexión relativa.
# 
# 🟡 **Útil**, pero con menor confianza que otras reglas.
# 
# **📌 Acción recomendada:**  
# *Customer recommendation + descuento cruzado* → Sugerir el otro color al finalizar la compra, con un descuento.
# 
# ---
# 
# ### 4. Regla: `lunch bag black skull. → lunch bag red retrospot`
# 
# **Interpretación:**
# - En el 3.15% de las transacciones están ambos artículos.
# - Si hay "black skull", hay un 49% de probabilidad de que también esté "red retrospot".
# - **Lift = 6.68**, asociación fuerte.
# 
# ✅ **Es una excelente regla**, con buena confianza y alto valor predictivo.
# 
# **📌 Acción recomendada:**  
# *Product bundling o cross-sell automatizado* → Ofrecer combo o sugerencia automática durante el checkout.
# 
# ---
# 
# ### ✅ Conclusión general
# 
# | Regla                                         | ¿Útil? | ¿Por qué?                                                              | Acción recomendada / Oportunidad de mejora                |
# |----------------------------------------------|--------|------------------------------------------------------------------------|------------------------------------------------------------|
# | roses regency → green regency                | ✅     | Relación extremadamente fuerte (lift alto) y confianza elevada.       |  Product bundling: vender las tazas en conjunto como set |
# | lunch bag red retrospot → pink polkadot      | 🟡     | Alta asociación (lift), pero la confianza es moderada.                |  Item placement: ubicarlas juntas en tienda o web         |
# | jumbo bag red retrospot → pink polkadot      | 🟡     | Buena asociación, pero con confianza más baja (35%).                  |  Customer recommendation con descuento cruzado            |
# | lunch bag black skull. → red retrospot       | ✅     | Buena combinación de confianza (49%) y alto lift (6.68).              |  Product bundling o cross-sell automatizado              |
# 

# ## ✔️ 10. Conclusion:
# 
# 
# En el presente análisis se aplicó la técnica de Análisis de Canasta de Compras (Market Basket Analysis) sobre un conjunto de datos reales provenientes de transacciones de un comercio electrónico en el Reino Unido.
# Los resultados permitieron identificar patrones de compra que pueden ser aprovechados para mejorar las estrategias de marketing, aumentar el ticket promedio y tomar decisiones basadas en evidencia.
# Entre los principales hallazgos, se destacaron las siguientes oportunidades:
# 
# 1. **Item Placements:**  (Optimización de la presentación de productos en la tienda online)  
#      Se recomienda mostrarlos juntos en el sitio web, por ejemplo, en secciones como “productos relacionados” o “frecuentemente comprados juntos”, con el fin de incentivar ventas combinadas y mejorar la experiencia del usuario.
# 
# 2. **Products Bundling:** (Ofertas agrupadas (bundles))    
#     Considerando la asociación entre artículos, es conveniente ofrecerlos como un paquete promocional a un precio reducido en comparación con su compra por separado.
#     Esta estrategia puede aumentar la conversión y mejorar el margen por transacción al fomentar compras múltiples.
# 
# 3. **Customer Recommendation and Discounts:**  (Recomendaciones personalizadas y promociones dirigidas)  
#     Se sugiere implementar campañas en las que, al detectar la compra o visualización de uno de estos productos, se recomiende el complemento con un incentivo adicional (por ejemplo, un descuento limitado).
#     Esto puede aplicarse tanto en el sitio como en correos automatizados o notificaciones, impulsando así la venta cruzada y la fidelización del cliente.

# 
# ##  ✔️ 11. SOURCES:
# 
#     Halim, Octavia, and Alianto. 2019. Designing Facility Layout of an Amusement Arcade using Market Basket Analysis. Procedia Computer Science, Vol 161, Page 623–629.
#     (https://www.sciencedirect.com/science/article/pii/S1877050919318769)
# 
#     Maitra, Sarit. 2019. Association Rule Mining using Market Basket Analysis.
#     (https://towardsdatascience.com/market-basket-analysis-knowledge-discovery-in-database-simplistic-approach-dc41659e1558)
# 
#     Subramanian, Dhilip. 2019. Association Discovery — the Apriori Algorithm.
#     (https://medium.com/towards-artificial-intelligence/association-discovery-the-apriori-algorithm-28c1e71e0f04)
# 
#     Chauhan, Nagesh Singh. 2019. Market Basket Analysis.
#     (https://towardsdatascience.com/market-basket-analysis-978ac064d8c6)
# 
#     Li, Susan. 2017. A Gentle Introduction on Market Basket Analysis — Association Rules.
#     (https://towardsdatascience.com/a-gentle-introduction-on-market-basket-analysis-association-rules-fa4b986a40ce)
# 
#     https://archive.ics.uci.edu/ml/datasets/Online+Retail+II
# 
# 

# ## ✔️ 12. GUARDAR RESULTADOS

# In[42]:


# ◯ GUARDAR RESULTADOS

# Crear la ruta si no existe
output_dir = "/workspaces/Final_Project_MBA/app/models"
os.makedirs(output_dir, exist_ok=True)

# Guardar el pickle en la ruta deseada
with open(os.path.join(output_dir, "basket.pkl"), "wb") as f:
    pickle.dump(basket, f)

print("✅ basket.pkl guardado en /app/models")

# ◯ Guardar el DataFrame de reglas legibles como CSV
rules_legibles.to_csv('../app/models/association_rules_final.csv', index=False)
print("\n✅ Reglas exportadas como 'association_rules_final.csv' en el mismo directorio.")

