import pygame
import constantes

# cuando creemos un personaje vamos a pasarle por parametros las 
# coordenadas x / y 
# forma del personaje lo establecemos con pygame.Rect , por lo que estamos 
# creando un cuadrado de 20 x 20 --- pero aun no mostramos nada en la screen

class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0,0, constantes.ALTO_PERSONAJE,constantes.ANCHO_PERSONAJE);
        self.forma.center = (x,y);

    # funcion para hacer que el personaje se muestre en screen
    def dibujar(self, interfaz):
        # dibuja la interfaz, representalo en amarillo, y pinta la forma ya definida en la funcion anterior
        pygame.draw.rect(interfaz, constantes.COLOR, self.forma);