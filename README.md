# aventura-conversacional-python

Estamos haciendo uso de python:3.13-slim

1. contruimos la imagen - `docker build -t aventura-conversacional-grafica .`
2. arrancamos el contendor 
    `docker run -d --name contenedor-AC-python -it -v "$(pwd):/app" aventura-conversacional-grafica`
3. para acceder a nuestro contenedor de python `docker exec -it contenedor-AC-python /bin/bash`


---

### Implementación

**CLONAR REPOSITORIO**

*1. Clonar repositorio* &rarr; `git clone https://github.com/beamm536/aventura-conversacional-python.git`

*2. Acceder a la carpeta del repo*  &rarr; `cd aventura-conversacional-python`

**CONSTRUIR LA IMAGEN**

`docker build -t aventura-conversacional-grafica .`

Para que el comando funcione, desde la terminal deberemos de estar dentro de la misma carpeta que contiene el `Dockerfile`

**ARRANCAR EL CONTENEDOR - Y EDITAR**

`docker run -d --name [CONTAINER NAME] -v "$(pwd):/app" aventura-conversacional-grafica`

Si solo quiere probar la aplicación &rArr;
`docker run -it --rm aventura-conversacional-grafica python main.py`


