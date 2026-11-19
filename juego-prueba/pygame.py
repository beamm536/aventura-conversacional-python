import pygame
import constantes
# llamamos a la clase Personaje - al objeto personaje
from personaje import Personaje


jugador = Personaje(350, 50);


def calcular_movimiento_jugador():
    delta_x = 0;
    delta_y = 0;

    if mover_derecha == True:
        delta_x = 5
    if mover_izquierda == True:
        delta_x = -5
    if mover_arriba == True:
        delta_x = -5
    if mover_abajo == True:
        delta_x = 5



pygame.init();

screen = pygame.display.set_mode((constantes.WIDTH_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("primer juego :D");

# definir variables movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False





# bucle en continua ejecucion hasta que 
# detecta evento de cerrar la ventana
running = True
while running:
    # llamamos al metodo dibujar que hemos creado dentro de la clase Personaje,
    # para la cual hemos establecido las coordenadas, y en la interfaz en la que se va a mostrar - screen
    jugador.dibujar(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT:
                mover_derecha = True
            if event.key == pygame.K_UP:
                mover_arriba = True
            if event.key == pygame.K_DOWN:
                mover_abajo = True
    # que se vaya actualizando la pantalla        
    pygame.display.update()

pygame.quit(); #se cierra la ventana del juego
