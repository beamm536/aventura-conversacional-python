import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la Manzana - Pygame")

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (230, 50, 50)
VERDE = (50, 200, 50)
AZUL = (50, 150, 250)
GRIS = (100, 100, 100)

# Reloj para controlar los FPS (Fotogramas por segundo)
reloj = pygame.time.Clock()

# Fuente para el texto
fuente = pygame.font.SysFont("Arial", 28)

def mostrar_texto(texto, x, y, color):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

def juego():
    # Variables del jugador (Canasta)
    jugador_ancho = 100
    jugador_alto = 20
    jugador_x = ANCHO // 2 - jugador_ancho // 2
    jugador_y = ALTO - 50
    jugador_velocidad = 8

    # Variables de la manzana (Objeto bueno)
    manzana_radio = 15
    manzana_x = random.randint(manzana_radio, ANCHO - manzana_radio)
    manzana_y = -50
    manzana_velocidad = 5

    # Variables de la bomba (Objeto malo)
    bomba_radio = 18
    bomba_x = random.randint(bomba_radio, ANCHO - bomba_radio)
    bomba_y = -150
    bomba_velocidad = 6

    puntuacion = 0
    vidas = 3

    jugando = True
    while jugando:
        # 1. Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2. Movimiento del jugador con las teclas de flecha
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador_x > 0:
            jugador_x -= jugador_velocidad
        if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_ancho:
            jugador_x += jugador_velocidad

        # 3. Actualizar posición de la manzana
        manzana_y += manzana_velocidad
        if manzana_y > ALTO:
            manzana_y = -50
            manzana_x = random.randint(manzana_radio, ANCHO - manzana_radio)

        # 4. Actualizar posición de la bomba
        bomba_y += bomba_velocidad
        if bomba_y > ALTO:
            bomba_y = -150
            bomba_x = random.randint(bomba_radio, ANCHO - bomba_radio)

        # 5. Detección de colisiones
        # Colisión con la manzana
        if (jugador_x < manzana_x < jugador_x + jugador_ancho) and \
           (jugador_y < manzana_y + manzana_radio < jugador_y + jugador_alto):
            puntuacion += 1
            manzana_y = -50
            manzana_x = random.randint(manzana_radio, ANCHO - manzana_radio)
            # Aumentar dificultad ligeramente
            manzana_velocidad += 0.1

        # Colisión con la bomba
        if (jugador_x < bomba_x < jugador_x + jugador_ancho) and \
           (jugador_y < bomba_y + bomba_radio < jugador_y + jugador_alto):
            vidas -= 1
            bomba_y = -150
            bomba_x = random.randint(bomba_radio, ANCHO - bomba_radio)
            if vidas <= 0:
                jugando = False

        # 6. Dibujar elementos en pantalla
        pantalla.fill(AZUL) # Fondo de cielo

        # Dibujar jugador (Canasta)
        pygame.draw.rect(pantalla, VERDE, (jugador_x, jugador_y, jugador_ancho, jugador_alto))

        # Dibujar manzana
        pygame.draw.circle(pantalla, ROJO, (manzana_x, int(manzana_y)), manzana_radio)

        # Dibujar bomba
        pygame.draw.circle(pantalla, NEGRO, (bomba_x, int(bomba_y)), bomba_radio)
        pygame.draw.circle(pantalla, GRIS, (bomba_x - 4, int(bomba_y) - 4), 4) # Brillo de la bomba

        # Mostrar puntuación y vidas
        mostrar_texto(f"Puntuación: {puntuacion}", 20, 20, BLANCO)
        mostrar_texto(f"Vidas: {vidas}", ANCHO - 140, 20, BLANCO)

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(60)

    # Pantalla de Game Over
    pantalla.fill(NEGRO)
    mostrar_texto("¡JUEGO TERMINADO!", ANCHO // 2 - 130, ALTO // 2 - 50, ROJO)
    mostrar_texto(f"Puntuación final: {puntuacion}", ANCHO // 2 - 110, ALTO // 2, BLANCO)
    mostrar_texto("Presiona R para reiniciar o ESC para salir", ANCHO // 2 - 210, ALTO // 2 + 50, GRIS)
    pygame.display.flip()

    # Esperar reinicio o salida
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    juego()
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Iniciar el juego por primera vez
if __name__ == "__main__":
    juego()