import pygame
import sys
import enemies as en
from constantes import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

pj_x = ANCHO_VENTANA // 2
pj_y = ALTO_VENTANA // 2
pj_health = 15


ob1_x = 1500
ob1_y = 100
ob1_health = 7
ob1_damage = 2
ob1_hit_box = pygame.Rect(ob1_x, ob1_y, 15, 15)
ob1_vision_box = pygame.Rect(0, 0, 150, 150)
ob1_vision_box.center = ob1_x + 5, ob1_y + 5

enemy1 = en.generate_enemy(ob1_x, ob1_y, ob1_hit_box, ob1_vision_box, ob1_health, ob1_damage)

ob2_x = 1000
ob2_y = 1100
ob2_health = 5
ob2_damage = 3
ob2_hit_box = pygame.Rect(ob2_x, ob2_y, 15, 15)
ob2_vision_box = pygame.Rect(0, 0, 200, 200)
ob2_vision_box.center = ob2_x + 5, ob2_y + 5

enemy2 = en.generate_enemy(ob2_x, ob2_y, ob2_hit_box, ob2_vision_box, ob2_health, ob2_damage)

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
         

    screen.fill((0, 0, 0))  
    mapa.fill((0, 0, 0))  

    pj_hit_box = pygame.Rect(pj_x, pj_y, 20, 20)

    mapa_visible_x = pj_x - ANCHO_VENTANA // 2
    mapa_visible_y = pj_y - ALTO_VENTANA // 2

    mapa_visible_x = max(0, min(mapa_visible_x, ANCHO_MAPA - ANCHO_VENTANA))
    mapa_visible_y = max(0, min(mapa_visible_y, ALTO_MAPA - ALTO_VENTANA))

    mapa_cargado = pygame.Rect(0, 0, ANCHO_VENTANA + 30, ALTO_VENTANA + 30)

    mapa_cargado.center = pj_x + 10, pj_y + 10


    if mapa_cargado.colliderect(enemy1.hit_box):
        pygame.draw.circle(mapa, (0, 255, 0), (enemy1.en_x, enemy1.en_y), 15)
        font = pygame.font.SysFont("Arial Narrow", 30)
        text = font.render(str(enemy1.health), True, (49, 186, 155))
        mapa.blit(text,(enemy1.en_x, enemy1.en_y - 40))

    if mapa_cargado.colliderect(enemy2.hit_box):
        pygame.draw.circle(mapa, (0, 0, 255), (enemy2.en_x, enemy2.en_y), 15)
        font = pygame.font.SysFont("Arial Narrow", 30)
        text = font.render(str(enemy2.health), True, (49, 186, 155))
        mapa.blit(text,(enemy2.en_x, enemy2.en_y - 40))

    if pj_hit_box.colliderect(enemy1.vision_box):
        velocidad_enemy = 3
        if pj_x < enemy1.en_x:
            aux = enemy1.en_x
            aux -= velocidad_enemy
            enemy1.en_x = aux
        elif pj_x > enemy1.en_x:
            aux = enemy1.en_x
            aux += velocidad_enemy
            enemy1.en_x = aux
        if pj_y < enemy1.en_y:
            aux = enemy1.en_y
            aux -= velocidad_enemy
            enemy1.en_y = aux
        elif pj_y > enemy1.en_y:
            aux = enemy1.en_y
            aux += velocidad_enemy
            enemy1.en_y = aux

        pygame.draw.circle(mapa, (0, 255, 0), (enemy1.en_x, enemy1.en_y), 15)

    if pj_hit_box.colliderect(enemy2.vision_box):
        velocidad_enemy = 3
        if pj_x < enemy2.en_x:
            aux = enemy2.en_x
            aux -= velocidad_enemy
            enemy2.en_x = aux
        elif pj_x > enemy2.en_x:
            aux = enemy2.en_x
            aux += velocidad_enemy
            enemy2.en_x = aux

        if pj_y < enemy2.en_y:
            aux = enemy2.en_y
            aux -= velocidad_enemy
            enemy2.en_y = aux
        elif pj_y > enemy2.en_y:
            aux = enemy2.en_y
            aux += velocidad_enemy
            enemy2.en_y = aux
        pygame.draw.circle(mapa, (0, 0, 255), (enemy2.en_x, enemy2.en_y), 15)    

    enemy1.hit_box = pygame.Rect(enemy1.en_x, enemy1.en_y, 15, 15)
    enemy1.vision_box = pygame.Rect(0, 0, 150, 150)
    enemy1.vision_box.center = enemy1.en_x + 5, enemy1.en_y + 5

    enemy2.hit_box = pygame.Rect(enemy2.en_x, enemy2.en_y, 15, 15)
    enemy2.vision_box = pygame.Rect(0, 0, 200, 200)
    enemy2.vision_box.center = enemy2.en_x + 5, enemy2.en_y + 5    
    
    screen.blit(mapa, (0, 0), (mapa_visible_x, mapa_visible_y, ANCHO_VENTANA, ALTO_VENTANA))
    pygame.draw.circle(screen, (255, 0, 0), (pj_x - mapa_visible_x, pj_y - mapa_visible_y), 20)
    font = pygame.font.SysFont("Arial Narrow", 30)
    text = font.render(str(pj_health), True, (49, 186, 155))
    screen.blit(text,(pj_x - mapa_visible_x, pj_y - mapa_visible_y - 60))

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    






