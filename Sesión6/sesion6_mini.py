import pygame
import random
import math

pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)
font = pygame.font.Font(None, 36)

nave_img = pygame.image.load("Sesión6/Astronaut clipart.jpeg")
nave = pygame.transform.scale(nave_img, (60, 60))
x, y = 400, 300
velocidad = 300
clock = pygame.time.Clock()
puntos = 0

# Objetos y obstáculos
objetivo = pygame.Rect(random.randint(0, 740), random.randint(0, 540), 20, 20)
obstaculo = pygame.Rect(0, 100, 30, 30)
vel_obs = 150

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000.0

    if teclas[pygame.K_LEFT]: x -= velocidad * dt
    if teclas[pygame.K_RIGHT]: x += velocidad * dt
    if teclas[pygame.K_UP]: y -= velocidad * dt
    if teclas[pygame.K_DOWN]: y += velocidad * dt

    x = max(0, min(800 - nave.get_width(), x))
    y = max(0, min(600 - nave.get_height(), y))

    nave_rect = pygame.Rect(int(x), int(y), nave.get_width(), nave.get_height())

    if nave_rect.colliderect(objetivo):
        puntos += 1
        objetivo.x = random.randint(0, 740)
        objetivo.y = random.randint(0, 540)

    obstaculo.x += vel_obs * dt
    if obstaculo.x < 0 or obstaculo.x > 770:
        vel_obs = -vel_obs

    ventana.fill(blanco)
    ventana.blit(nave, (x, y))
    pygame.draw.rect(ventana, (0, 255, 0), objetivo)
    pygame.draw.circle(ventana, (255, 0, 0), obstaculo.center, obstaculo.width // 2)
    texto = font.render(f"Puntos: {puntos}", True, (0, 0, 0))
    ventana.blit(texto, (10, 10))

    if nave_rect.colliderect(obstaculo):
        texto = font.render("¡Colisión! Juego terminado", True, (0, 0, 0))
        ventana.blit(texto, texto.get_rect(center=(400, 300)))
        pygame.display.flip()
        pygame.time.wait(2000)
        corriendo = False
    pygame.display.flip()
pygame.quit()
