df[df['nombre_columna'] < 0]# ‼️VL: Como aprovechar este template:  

> ### 1. Descargar archivos de este repo, y subirlos al repo de mi nuevo proyecto.  
>> devcontainer.json, dockerfile, notebooks, readme devcontainer.md, requirements.txt, .gitignore
> ### 2. Luego precionar F1 → Dev Containers: Rebuild Container  
> ### 3. Abre un notebook y En el selector de kernel deberías seleccionar: Python 3 (devcontainer)
> ### 4. Confirmar que tu entorno está listo para trabajar en los notebooks:  
      *  correr todas las celdas del Notebook llamado prueba, 
      * ver en la terminal "(devcontainer)" al principio.
> .

  

---

# 🐳 Mini Proyecto de Data Science con Docker + Jupyter + DevContainer

Este repositorio incluye:

- Un contenedor Docker preconfigurado con Python 3.11
- Librerías de ciencia de datos (`pandas`, `numpy`, `matplotlib`, `scikit-learn`)
- Un archivo `devcontainer.json` para trabajar en GitHub Codespaces o VS Code
- Un notebook de ejemplo para probar el entorno



## ▶️ Cómo usar

### Opción 1: GitHub Codespaces

Haz clic en este botón para abrir el proyecto directamente en un Codespace (requiere una cuenta GitHub):

[![Abrir en Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repo=mvlarra/ds-docker-example&machine=basicLinux32gb)




### Opción 2: Local con VS Code y Docker

1. Asegúrate de tener instalado:
   - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - [Visual Studio Code](https://code.visualstudio.com/)
   - La extensión **Dev Containers** en VS Code

2. Clona este repositorio:
```bash
git clone https://github.com/mvlarra/ds-docker-example.git
cd ds-docker-example

