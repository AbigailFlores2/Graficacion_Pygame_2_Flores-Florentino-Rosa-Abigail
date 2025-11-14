import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
verde = (0, 200, 0)

x, y = 400, 50
velocidad_y = 0
gravedad = 0.5
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    velocidad_y += gravedad
    y += velocidad_y

    if y >= 570:  # Suelo (600 - radio)
        y = 570
        velocidad_y = -velocidad_y * 0.8  # Rebote con pérdida de energía

        if abs(velocidad_y) < 1:
            velocidad_y = 0  # Detener si es muy pequeño

    ventana.fill(blanco)
    pygame.draw.circle(ventana, verde, (x, int(y)), 30)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()