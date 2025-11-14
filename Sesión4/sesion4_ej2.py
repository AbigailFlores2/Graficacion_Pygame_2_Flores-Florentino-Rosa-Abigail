import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 100, 255)

x, y = 400, 300
radio = 20
cambio_radio = 1
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    radio += cambio_radio
    if radio >= 50 or radio <= 20:
        cambio_radio = -cambio_radio

    ventana.fill(blanco)
    pygame.draw.circle(ventana, azul, (x, y), int(radio))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()