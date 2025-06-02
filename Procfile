# web: streamlit run app.py --server.port=10000 --server.enableCORS=false

web: streamlit run app.py --server.port=$PORT
# Esto hace que tu app se conecte automáticamente al puerto que Render necesita, evitando errores como:
# ==> No open ports detected, continuing to scan...
# 💡 No necesitás forzar enableCORS=false en un entorno como Render, a menos que tengas una necesidad específica.
# Esto elimina la advertencia y es más compatible con el entorno productivo.