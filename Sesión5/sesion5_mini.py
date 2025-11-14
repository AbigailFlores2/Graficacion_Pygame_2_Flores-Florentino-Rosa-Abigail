import pygame
import math

pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)

comet_original = pygame.image.load("Sesión5/comet.png")
comet = pygame.transform.scale(comet_original, (100, 100))

x, y = 400, 300
velocidad = 5
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angulo_rad = math.atan2(mouse_y - y, mouse_x - x)
    angulo_deg = -math.degrees(angulo_rad)

    if teclas[pygame.K_SPACE]:
        x += math.cos(angulo_rad) * velocidad
        y += math.sin(angulo_rad) * velocidad

    comet_rotada = pygame.transform.rotate(comet, angulo_deg)
    ventana.fill(blanco)
    ventana.blit(comet_rotada, (x - comet_rotada.get_width() // 2, y - comet_rotada.get_height() // 2))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()