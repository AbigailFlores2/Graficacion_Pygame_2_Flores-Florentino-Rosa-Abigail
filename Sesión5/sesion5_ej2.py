import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))
blanco = (255, 255, 255)

sprite_sheet = pygame.image.load("Sesión5/conch.png") 
frame_ancho = sprite_sheet.get_width() // 4
frame_alto = sprite_sheet.get_height()
frames = [sprite_sheet.subsurface(pygame.Rect(i * frame_ancho, 0, frame_ancho, frame_alto)) for i in range(4)]

indice_frame = 0
temporizador = 0
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    temporizador += reloj.get_time()
    if temporizador >= 100:
        indice_frame = (indice_frame + 1) % 4
        temporizador = 0

    ventana.fill(blanco)
    ventana.blit(frames[indice_frame], (350, 250))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()