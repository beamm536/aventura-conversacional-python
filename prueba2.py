import pygame
import random
import math
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Defensor Galáctico - Pygame Ultimate")

# Colores (RGB)
NEGRO = (10, 10, 25)
BLANCO = (255, 255, 255)
AZUL_NEON = (0, 255, 255)
ROJO_ALERTA = (255, 50, 50)
AMARILLO = (255, 220, 0)
NARANJA = (255, 120, 0)
GRIS = (120, 120, 140)

# Reloj y fuentes
reloj = pygame.time.Clock()
fuente_grande = pygame.font.SysFont("Arial", 40, bold=True)
fuente_med = pygame.font.SysFont("Arial", 24)
fuente_chica = pygame.font.SysFont("Arial", 18)

def juego():
    # Variables del jugador
    jugador_x = ANCHO // 2
    jugador_y = ALTO - 80
    jugador_ancho = 45
    jugador_alto = 50
    velocidad_jugador = 6

    # Listas del juego
    balas = []
    enemigos = []
    particulas = []
    estrellas = [[random.randint(0, ANCHO), random.randint(0, ALTO), random.randint(1, 3)] for _ in range(80)]

    # Temporizadores y estadísticas
    tiempo_enemigo = 0
    puntuacion = 0
    vidas = 3
    nivel = 1
    cadencia_disparo = 0

    jugando = True
    while jugando:
        # 1. Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2. Controles del jugador (Movimiento y Disparo)
        teclas = pygame.key.get_pressed()
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and jugador_x > 20:
            jugador_x -= velocidad_jugador
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and jugador_x < ANCHO - jugador_ancho - 20:
            jugador_x += velocidad_jugador
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and jugador_y > ALTO // 2:
            jugador_y -= velocidad_jugador
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and jugador_y < ALTO - jugador_alto - 20:
            jugador_y += velocidad_jugador

        # Disparar con la barra espaciadora
        if cadencia_disparo > 0:
            cadencia_disparo -= 1

        if teclas[pygame.K_SPACE] and cadencia_disparo == 0:
            balas.append([jugador_x + jugador_ancho // 2 - 3, jugador_y])
            cadencia_disparo = 12  # Controla la velocidad de fuego

        # 3. Actualizar Estrellas (Fondo con efecto parallax)
        for est in estrellas:
            est[1] += est[2]
            if est[1] > ALTO:
                est[1] = 0
                est[0] = random.randint(0, ANCHO)

        # 4. Generar Enemigos automáticamente según el nivel
        tiempo_enemigo += 1
        frecuencia_spawn = max(15, 45 - (nivel * 4))
        if tiempo_enemigo > frecuencia_spawn:
            enemigo_x = random.randint(30, ANCHO - 50)
            tipo = random.choice(["normal", "rapido"])
            velocidad_en = random.randint(2, 4) + (nivel * 0.5) if tipo == "normal" else random.randint(5, 7) + (nivel * 0.5)
            ancho_en = 40 if tipo == "normal" else 30
            enemigos.append({"rect": pygame.Rect(enemigo_x, -50, ancho_en, ancho_en), "tipo": tipo, "vel": velocidad_en})
            tiempo_enemigo = 0

        # 5. Actualizar Balas
        for bala in balas[:]:
            bala[1] -= 10
            if bala[1] < -20:
                balas.remove(bala)

        # 6. Actualizar Enemigos y Colisiones
        jugador_rect = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)
        
        for enemigo in enemigos[:]:
            enemigo["rect"].y += int(enemigo["vel"])

            # Si el enemigo sale por debajo, quita vida
            if enemigo["rect"].y > ALTO:
                enemigos.remove(enemigo)
                vidas -= 1
                if vidas <= 0:
                    jugando = False
                continue

            # Colisión con balas del jugador
            enemigo_destruido = False
            for bala in balas[:]:
                bala_rect = pygame.Rect(bala[0], bala[1], 6, 16)
                if bala_rect.colliderect(enemigo["rect"]):
                    enemigos.remove(enemigo)
                    if bala in balas:
                        balas.remove(bala)
                    puntuacion += 10 if enemigo["tipo"] == "normal" else 20
                    
                    # Crear partículas de explosión
                    for _ in range(12):
                        particulas.append([
                            enemigo["rect"].centerx, enemigo["rect"].centery,
                            random.uniform(-3, 3), random.uniform(-3, 3),
                            random.randint(15, 25), random.choice([AMARILLO, NARANJA, ROJO_ALERTA])
                        ])

                    # Subir de nivel cada 150 puntos
                    nivel = 1 + puntuacion // 150
                    enemigo_destruido = True
                    break

            if enemigo_destruido:
                continue

            # Colisión directa con la nave del jugador
            if jugador_rect.colliderect(enemigo["rect"]):
                enemigos.remove(enemigo)
                vidas -= 1
                for _ in range(20):
                    particulas.append([
                        jugador_x + jugador_ancho//2, jugador_y + jugador_alto//2,
                        random.uniform(-4, 4), random.uniform(-4, 4),
                        random.randint(20, 30), AZUL_NEON
                    ])
                if vidas <= 0:
                    jugando = False

        # 7. Actualizar Partículas
        for part in particulas[:]:
            part[0] += part[2]
            part[1] += part[3]
            part[4] -= 1
            if part[4] <= 0:
                particulas.remove(part)

        # 8. Renderizado Gráfico
        pantalla.fill(NEGRO)

        # Dibujar estrellas
        for est in estrellas:
            brillo = 200 if est[2] > 2 else 100
            pygame.draw.circle(pantalla, (brillo, brillo, brillo), (est[0], est[1]), est[2])

        # Dibujar partículas de explosión
        for part in particulas:
            pygame.draw.circle(pantalla, part[5], (int(part[0]), int(part[1])), max(1, part[4] // 4))

        # Dibujar Balas Láser
        for bala in balas:
            pygame.draw.rect(pantalla, AZUL_NEON, (bala[0], bala[1], 6, 16), border_radius=3)

        # Dibujar Enemigos
        for enemigo in enemigos:
            e_rect = enemigo["rect"]
            if enemigo["tipo"] == "normal":
                pygame.draw.polygon(pantalla, ROJO_ALERTA, [
                    (e_rect.centerx, e_rect.bottom),
                    (e_rect.left, e_rect.top),
                    (e_rect.right, e_rect.top)
                ])
            else: # Rápido / Kamikaze
                pygame.draw.polygon(pantalla, NARANJA, [
                    (e_rect.centerx, e_rect.bottom),
                    (e_rect.left + 5, e_rect.top),
                    (e_rect.right - 5, e_rect.top)
                ])

        # Dibujar Nave del Jugador (Diseño vectorial detallado)
        # Alas
        pygame.draw.polygon(pantalla, GRIS, [
            (jugador_x + jugador_ancho // 2, jugador_y),
            (jugador_x, jugador_y + jugador_alto),
            (jugador_x + jugador_ancho, jugador_y + jugador_alto)
        ])
        # Cabina central
        pygame.draw.polygon(pantalla, AZUL_NEON, [
            (jugador_x + jugador_ancho // 2, jugador_y + 10),
            (jugador_x + 12, jugador_y + jugador_alto - 5),
            (jugador_x + jugador_ancho - 12, jugador_y + jugador_alto - 5)
        ])
        # Propulsor trasero
        pygame.draw.rect(pantalla, NARANJA, (jugador_x + jugador_ancho // 2 - 6, jugador_y + jugador_alto, 12, 6))

        # HUD / Interfaz superior
        texto_score = fuente_med.render(f"Puntuación: {puntuacion}", True, BLANCO)
        texto_vidas = fuente_med.render(f"Vidas: {'❤️ ' * vidas}", True, ROJO_ALERTA)
        texto_nivel = fuente_med.render(f"Nivel: {nivel}", True, AMARILLO)
        
        pantalla.blit(texto_score, (20, 15))
        pantalla.blit(texto_nivel, (ANCHO // 2 - 50, 15))
        pantalla.blit(texto_vidas, (ANCHO - 200, 15))

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(60)

    # Pantalla de Game Over
    pantalla.fill(NEGRO)
    t_over = fuente_grande.render("¡MISIÓN TERMINADA!", True, ROJO_ALERTA)
    t_score = fuente_med.render(f"Puntuación final: {puntuacion} | Nivel alcanzado: {nivel}", True, BLANCO)
    t_reintentar = fuente_chica.render("Presiona 'R' para jugar de nuevo o 'ESC' para salir", True, GRIS)

    pantalla.blit(t_over, (ANCHO // 2 - t_over.get_width() // 2, ALTO // 2 - 60))
    pantalla.blit(t_score, (ANCHO // 2 - t_score.get_width() // 2, ALTO // 2))
    pantalla.blit(t_reintentar, (ANCHO // 2 - t_reintentar.get_width() // 2, ALTO // 2 + 50))
    pygame.display.flip()

    # Bucle de reinicio o salida
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

if __name__ == "__main__":
    juego()