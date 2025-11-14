import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
font = pygame.font.Font(None, 36)

jugador = pygame.Rect(400, 500, 50, 50)
obstaculo = pygame.Rect(0, 200, 30, 30)
velocidad = 300
vel_obs = 200
clock = pygame.time.Clock()
player_x = float(jugador.x)
player_y = float(jugador.y)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000.0

    if teclas[pygame.K_LEFT]: player_x -= velocidad * dt
    if teclas[pygame.K_RIGHT]: player_x += velocidad * dt
    if teclas[pygame.K_UP]: player_y -= velocidad * dt
    if teclas[pygame.K_DOWN]: player_y += velocidad * dt

    player_x = max(0, min(800 - jugador.width, player_x))
    player_y = max(0, min(600 - jugador.height, player_y))
    jugador.x = int(player_x)
    jugador.y = int(player_y)

    obstaculo.x += vel_obs * dt
    if obstaculo.x > 800 or obstaculo.x < 0:
        vel_obs = -vel_obs

    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, jugador)
    pygame.draw.circle(ventana, rojo, obstaculo.center, obstaculo.width // 2)

    if jugador.colliderect(obstaculo):
        texto = font.render("¡Colisión! Juego terminado", True, (0, 0, 0))
        ventana.blit(texto, texto.get_rect(center=(400, 300)))
        pygame.display.flip()
        pygame.time.wait(2000)
        corriendo = False

    pygame.display.flip()

pygame.quit()