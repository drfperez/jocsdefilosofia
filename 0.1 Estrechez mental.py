import pygame
import time

def pantalla_inicial():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    fuente = pygame.font.SysFont(None, 36)
    mensaje1 = fuente.render("Resetea tus ideas o morirás", True, (255, 255, 255))
    mensaje2 = fuente.render("aplastado por tu estrechez mental.", True, (255, 255, 255))
    mensaje3 = fuente.render("Solo una tecla te permitirá empezar desde cero...", True, (255, 255, 255))
    pantalla.blit(mensaje1, (100, 200))
    pantalla.blit(mensaje2, (100, 250))
    pantalla.blit(mensaje3, (100, 300))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

def pantalla_final(ganaste):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    fuente = pygame.font.SysFont(None, 50)
    if ganaste:
        mensaje = fuente.render("Pienso luego existo", True, (255, 255, 255))
    else:
        mensaje = fuente.render("Muerto por no pensar", True, (255, 255, 255))
    pantalla.blit(mensaje, (200, 200))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

pantalla_inicial()

ancho = 1000
ganaste = False
while ancho > 0 and not ganaste:
    ancho -= 100
    pantalla = pygame.display.set_mode((ancho,500))
    pantalla.fill((50, 150, 50))
    pygame.display.update()
    time.sleep(1)

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_0:
                ganaste = True

pantalla_final(ganaste)
