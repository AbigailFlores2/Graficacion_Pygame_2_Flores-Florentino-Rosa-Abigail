import pygame
import random
pygame.init()

ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
azul = (0, 0, 255)
verde = (0, 255, 0)
font = pygame.font.Font(None, 36)

jugador = pygame.Rect(400, 300, 50, 50)
velocidad = 300
clock = pygame.time.Clock()
player_x = float(jugador.x)
player_y = float(jugador.y)

radio = 20
contador = 0
objetivo_x = random.randint(radio, 800 - radio)
objetivo_y = random.randint(radio, 600 - radio)

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

    distancia = ((jugador.centerx - objetivo_x)**2 + (jugador.centery - objetivo_y)**2)**0.5
    if distancia < radio + jugador.width // 2:
        contador += 1
        objetivo_x = random.randint(radio, 800 - radio)
        objetivo_y = random.randint(radio, 600 - radio)

    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, jugador)
    pygame.draw.circle(ventana, verde, (objetivo_x, objetivo_y), radio)
    texto = font.render(f"Objetos recogidos: {contador}", True, (0, 0, 0))
    ventana.blit(texto, (10, 10))
    pygame.display.flip()

pygame.quit()