import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi aventura")

#creamos una fuente de texto y su tamaño
font = pygame.font.SysFont("Arial", 40)

#texto a mostrar
texto = font.render("¡Bienvenido a la aventura!", True, (255, 255, 255))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Fondo
    screen.fill((30, 30, 40))

    # Dibujar el texto en la ventana
    screen.blit(texto, (150, 250))

    pygame.display.flip()


pygame.quit()