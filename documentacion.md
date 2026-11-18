
### funciones especificas pygame

- `pygame.init()` -> funcion necesaria para inicializar todos los modulos de pygame para que funcione correctamente
- `pygame.font.SysFont()` -> Selecciona una fuente y su tamaño.
- `font.render()` -> Convierte el texto en una imagen que Pygame puede dibujar.
- `screen.blit()` -> Dibuja esa imagen en una posición de la ventana.
- `display.flip()` -> Actualiza la pantalla para mostrar todo lo que hemos dibujado.`


*bucle principal* -> que se ejecutará mientras que la ventana de pygame siga abierta
- `for event` - revisa todos los eventos que ocurren, como cerrar la ventana, pulsacion teclas, raton...
- `if` - si el tipo de evento que se ha detectado ha sido cerrar la ventana, se ejecutará la funcion `QUIT`
  
```python
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
```