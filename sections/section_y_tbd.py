
# 1. ◯ Sección: INICIO
# ............................................................................................
if section.startswith("OLD 1."):
    st.title("Bienvenido a Market Basket Analysis de compras para Retail")
    # Ruta a la imagen 
    st.image("app/images/Img3.png", use_container_width=True)
    st.markdown("""
    Esta app te ayudará a descubrir `relaciones entre productos` en base a transacciones reales.  
    
    Pensada especialmente para **gerentes de negocio**, permite:
    * → visualizar `reglas de asociación`,
    * → generar `bundles sugeridos` y
    * → `aplicar estrategias` basadas en datos.
    
    ¿Ejemplo?  
    Si muchos clientes compran *tazas de té* junto con *bandejas decorativas*, 
    podrías  
        → ofrecer estos productos como un combo o   
        → ubicarlos juntas en tu tienda.
    
    Usá el menú lateral para navegar por cada sección.
    """)
     
    # Imagen de portada debajo
    st.image("app/images/Img3.png", width=500)  # Ajustás el tamaño según necesidad

     
    # ✏️ Introducción general
    st.markdown("""
    Market Basket Analysis (MBA) es una técnica de minería de datos que permite descubrir patrones de compra entre productos. 
    Analiza qué artículos suelen adquirirse juntos por los clientes durante una misma transacción.

    Este enfoque ayuda a:
    - ✅ Optimizar la disposición de productos en tienda
    - ✅ Diseñar promociones más efectivas
    - ✅ Aumentar las ventas mediante estrategias de **cross-selling**
    - ✅ Mejorar la experiencia del cliente
                
    En esta aplicación interactiva podrás:
    - Explorar reglas de asociación entre productos
    - Visualizar productos frecuentemente comprados juntos
    - Evaluar oportunidades de mejora en ventas y layout
    """)

    # Info del proyecto
    st.markdown("""
    **🗂️ Fuente de datos:**  
    Dataset *Online Retail II* de la UCI Machine Learning Repository.  
    Incluye transacciones realizadas por un minorista online entre 2009 y 2011.

    **📅 Período Analizado:**  
    Del 01/12/2009 al 09/12/2011

    **📍 Enfoque:**  
    Filtramos exclusivamente las compras realizadas por clientes en **Reino Unido**, para facilitar la visualización y generar recomendaciones más específicas.

    """)


# 9. ◯ Sección: CRÉDITOS Y TECNOLOGÍAS
# ............................................................................................
elif section.startswith("OLD 9."):
    st.title("📎 Créditos y recursos del proyecto")

    st.markdown("""
    Este proyecto fue desarrollado como parte del proyecto final del **Bootcamp de Data Science & Machine Learning en 4Geeks Academy**,  
    por **Valentina Larrañaga**.

    ---
    #### 🚀 Tecnologías utilizadas
    - Python 🐍
    - pandas, numpy
    - mlxtend (reglas de asociación)
    - plotly, matplotlib
    - Streamlit (app)
    
    ---
    #### 📁 Recursos
    - Código fuente: [GitHub del proyecto](https://github.com/mvlarra/Final_Project_MBA)
    - Dataset: Online Retail Dataset (UCI / Kaggle)
    - Herramientas: GitHub Codespaces, VS Code, Docker

    ---
    #### 💬 Agradecimientos
    Gracias a los instructores, tutores y compañeros del bootcamp, y a quienes colaboraron brindando feedback y motivación para completar este proyecto.

    ---
    #### 📫 Contacto profesional
    - [LinkedIn](https://www.linkedin.com/in/valentinalarra)  
    - [GitHub](https://github.com/mvlarra)
    """)