# Proyecto RetoDevSecOps

****Bienvenido al proyecto RetoDevSecOps. Este proyecto proporciona una solución para la visualización de vulnerabilidades reportadas en la etapa de análisis de dependencias de una aplicación.****

## Requisitos

- [PostgreSQL](https://www.postgresql.org/download/)
- [Docker](https://www.docker.com/get-started)

## Pasos para ejecutar (Para Ubuntu)
1. Clona el repositorio en  la rama `main`
2. Abre la terminal de Ubuntu.
3. Inicia el servicio de Docker: `sudo service docker start`.
4. Verifica que no haya conflictos en los puertos ejecutando: `docker ps`.
5. Ejecuta Docker Compose para construir y levantar la aplicación(**_Debes estar en la carpeta raiz del proyecto_**): `docker-compose up --build`.

La aplicación se ejecutará y te proporcionará la dirección IP en la línea de comandos. Puedes acceder a la interfaz desde tu navegador en esa dirección. En la página de inicio, encontrarás dos cuadros: uno con el icono de GitHub que enlaza al repositorio y otro que lleva a una página con las vulnerabilidades encontradas durante el análisis de dependencias ( http://127.0.0.1:5000/vulnerabilidades ).

También puedes revisar las tareas ejecutadas en el archivo `main.yml` para SonarQube, que se dispara automáticamente al enviar un PR (ver [aquí](https://github.com/sebastianyacup/RetoDevSecOps/actions/workflows/main.yml)), y el análisis de dependencias (ver [aquí](https://github.com/sebastianyacup/RetoDevSecOps/actions/workflows/analisis-dependencias.yml)).

