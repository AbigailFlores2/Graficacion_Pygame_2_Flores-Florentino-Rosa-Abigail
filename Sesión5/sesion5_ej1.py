import pygame
import math

pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)

imagen_original = pygame.image.load("Sesión5/lotus_flower.png")
escala = 1.0  # Factor de escala inicial

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                escala += 0.1
            elif evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                escala = max(0.1, escala - 0.1)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    angulo = math.atan2(mouse_y - 300, mouse_x - 400) * 180 / math.pi

    ancho = int(500 * escala)
    alto = int(500 * escala)
    imagen_escalada = pygame.transform.scale(imagen_original, (ancho, alto))
    imagen_rotada = pygame.transform.rotate(imagen_escalada, -angulo)

    ventana.fill(blanco)
    ventana.blit(imagen_rotada, (400 - imagen_rotada.get_width() // 2, 300 - imagen_rotada.get_height() // 2))
    pygame.display.flip()

pygame.quit()