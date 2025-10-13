import pygame
import random
pygame.init()
WIDTH,HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
title = pygame.display.set_caption("Coin Collector")
person_img = pygame.image.load("person.png")
shell_img = pygame.image.load("shell.png")
key_img = pygame.image.load("key.png")
person_img = pygame.transform.scale(person_img,(50,50))
key_img = pygame.transform.scale(key_img,(35,37))
shell_img = pygame.transform.scale(shell_img,(30,27))
key = pygame.Rect(560,300,35,37)
person = pygame.Rect(-10,0,50,50)
shell = pygame.Rect(300,300,10,9)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
w1 = pygame.Rect(320,300,10,275)
w2 = pygame.Rect(415,0,315,10)
w3 = pygame.Rect(315,75,10,50)
w4 = pygame.Rect(200,90,248,10)
w5 = pygame.Rect(214,125,10,300)
w6 = pygame.Rect(69,170,10,100)
w7 = pygame.Rect(128,200,314,10)
w8 = pygame.Rect(128,500,314,10)
w9 = pygame.Rect(520,75,10,510)
w10 = pygame.Rect(300,375,600,10)
w11 = pygame.Rect(415,0,10,315)
w12 = pygame.Rect(0,75,150,10)
shell_speedx = 0.1
shell_speedy = 0.1
run = True
while run:
    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,w1)
    pygame.draw.rect(screen,RED,w2)
    pygame.draw.rect(screen,RED,w3)
    pygame.draw.rect(screen,RED,w4)
    pygame.draw.rect(screen,RED,w5)
    pygame.draw.rect(screen,RED,w6)
    pygame.draw.rect(screen,RED,w7)
    pygame.draw.rect(screen,RED,w8)
    pygame.draw.rect(screen,RED,w9)
    pygame.draw.rect(screen,RED,w10)
    pygame.draw.rect(screen,RED,w11)
    pygame.draw.rect(screen,RED,w12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            person.y -= 20
        if keys[pygame.K_DOWN]:
            person.y += 20
        if keys[pygame.K_LEFT]:
            person.x -= 20
        if keys[pygame.K_RIGHT]:
            person.x += 20
    if person.colliderect(w1):
        person.x,person.y = -10,0
    if person.colliderect(w2):
        person.x,person.y = -10,0
    if person.colliderect(w3):
        person.x,person.y = -10,0
    if person.colliderect(w4):
        person.x,person.y = -10,0
    if person.colliderect(w5):
        person.x,person.y = -10,0
    if person.colliderect(w6):
        person.x,person.y = -10,0
    if person.colliderect(w7):
        person.x,person.y = -10,0
    if person.colliderect(w8):
        person.x,person.y = -10,0
    if person.colliderect(w9):
        person.x,person.y = -10,0
    if person.colliderect(w10):
        person.x,person.y = -10,0
    if person.colliderect(w11):
        person.x,person.y = -10,0
    if person.colliderect(w12):
        person.x,person.y = -10,0
    if person.colliderect(shell):
        person.x,person.y = -10,0
    shell.x += 0.5
    shell.y += 0.5
    if shell.y > 600:
        shell.y = 0
    if shell.x > 600:
        shell.x = 0
    screen.blit(person_img,(person.x,person.y))
    screen.blit(key_img,(key.x,key.y))
    screen.blit(shell_img,(shell.x,shell.y))
    pygame.display.flip()
pygame.quit()