import pygame
import sys
from constantes import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

pj_x = ANCHO_VENTANA // 2
pj_y = ALTO_VENTANA // 2

ob1_x = 1500
ob1_y = 100

ob2_x = 1000
ob2_y = 1100

mapa = pygame.Surface((ANCHO_MAPA,ALTO_MAPA))

while True:
    tiempo = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    teclas = pygame.key.get_pressed()
    velocidad_pj = 5
    if teclas[pygame.K_x]:
        velocidad_pj = 25
    if teclas[pygame.K_LEFT]:
        pj_x -= velocidad_pj    
    if teclas[pygame.K_RIGHT]:
        pj_x += velocidad_pj
    if teclas[pygame.K_UP]:
        pj_y -= velocidad_pj
    if teclas[pygame.K_DOWN]:
        pj_y += velocidad_pj
         

    

    mapa_visible_x = pj_x - ANCHO_VENTANA // 2
    mapa_visible_y = pj_y - ALTO_VENTANA // 2

    mapa_visible_x = max(0, min(mapa_visible_x, ANCHO_MAPA - ANCHO_VENTANA))
    mapa_visible_y = max(0, min(mapa_visible_y, ALTO_MAPA - ALTO_VENTANA))

    screen.fill((0, 0, 0))  
    mapa.fill((0, 0, 0))  

    mapa_cargado = pygame.Rect(0, 0, ANCHO_VENTANA + 30, ALTO_VENTANA + 30)
    mapa_cargado.center = pj_x + 10, pj_y + 10

    pj_hit_box = pygame.Rect(pj_x, pj_y, 20, 20)

    ob1_hit_box = pygame.Rect(ob1_x, ob1_y, 15, 15)
    ob1_vision_box = pygame.Rect(0, 0, 150, 150)
    ob1_vision_box.center = ob1_x + 5, ob1_y + 5

    ob2_hit_box = pygame.Rect(ob2_x, ob2_y, 15, 15)
    ob2_vision_box = pygame.Rect(0, 0, 200, 200)
    ob2_vision_box.center = ob2_x + 5, ob2_y + 5

    if mapa_cargado.colliderect(ob1_hit_box):
        pygame.draw.circle(mapa, (0, 255, 0), (ob1_x, ob1_y), 15)

    if mapa_cargado.colliderect(ob2_hit_box):
        pygame.draw.circle(mapa, (0, 0, 255), (ob2_x, ob2_y), 15)

    if pj_hit_box.colliderect(ob1_vision_box):
        velocidad_enemy = 3
        if pj_x < ob1_x:
            ob1_x -= velocidad_enemy
        elif pj_x > ob1_x:
            ob1_x += velocidad_enemy

        if pj_y < ob1_y:
            ob1_y -= velocidad_enemy
        elif pj_y > ob1_y:
            ob1_y += velocidad_enemy

        pygame.draw.circle(mapa, (0, 255, 0), (ob1_x, ob1_y), 15)

    if pj_hit_box.colliderect(ob2_vision_box):
        velocidad_enemy = 3
        if pj_x < ob2_x:
            ob2_x -= velocidad_enemy
        elif pj_x > ob2_x:
            ob2_x += velocidad_enemy

        if pj_y < ob2_y:
            ob2_y -= velocidad_enemy
        elif pj_y > ob2_y:
            ob2_y += velocidad_enemy
        pygame.draw.circle(mapa, (0, 0, 255), (ob2_x, ob2_y), 15)    
    
       
    pygame.draw.circle(mapa, (0, 255, 0), (ob1_x + 10, ob1_y + 10), 5)
    pygame.draw.circle(mapa, (0, 0, 255), (ob2_x + 10, ob2_y + 10), 5) 
    screen.blit(mapa, (0, 0), (mapa_visible_x, mapa_visible_y, ANCHO_VENTANA, ALTO_VENTANA))
    pygame.draw.circle(screen, (255, 0, 0), (pj_x - mapa_visible_x, pj_y - mapa_visible_y), 20)

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    






