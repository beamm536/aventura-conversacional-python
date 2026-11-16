# aventura-conversacional-python

Aventura conversacional en Python

Proyecto de aventura conversacional desarrollado en Python utilizando Pygame.

Requisitos

* Python 3.13
* Git
* Pygame 2.6.1

1. **Clonar el repositorio**
```
git clone URL_DEL_REPOSITORIO
cd aventura
```

2. **Crear el entorno virtual**

`python3 -m venv .venv`

3. **Activar el entorno virtual**

`source .venv/bin/activate`

Cuando esté activado, aparecerá (.venv) al principio de la terminal.

4. **Instalar las dependencias**
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Esto instalará Pygame y sus dependencias necesarias.

5. **Ejecutar la aventura**

`python3 main.py`

6. **Desactivar el entorno virtual**

Cuando terminemos de trabajar:

`deactivate`

7. **Actualizar el proyecto**

Para descargar los últimos cambios del repositorio:

`git pull`

Si se han añadido nuevas dependencias a requirements.txt:

`python -m pip install -r requirements.txt`

Estructura del proyecto

```
aventura-conversacional-python/
├── .venv/
├── assets/
│   ├── images/
│   └── sounds/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

Notas

* La carpeta .venv no debe subirse al repositorio.
* Cada desarrollador debe crear su propio entorno virtual.
* Ambos desarrolladores deben utilizar la misma versión de Python y Pygame.
* No es necesario utilizar Docker para ejecutar el juego.


> para el funcionamiento en mac, he tenido que instalar las siguientes dependencias con homebrew
>`brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config`


INSTALACIONES PARA VER SI FUNCIONA DE UNA VEZ :D
`python -m pip uninstall pygame pygame-ce -y`
`python -m pip install --upgrade pip`
`python -m pip install pygame-ce`




### funciones

`pygame.font.SysFont()`	Selecciona una fuente y su tamaño.
`font.render()`	Convierte el texto en una imagen que Pygame puede dibujar.
`screen.blit()`	Dibuja esa imagen en una posición de la ventana.
