import pygame
import random
pygame.init()
game_level = 1
WIDTH,HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
title = pygame.display.set_caption("Coin Collector")
person_img = pygame.image.load("person.png")
shell_img = pygame.image.load("shell.png")
key_img = pygame.image.load("key.png")
game_over_img = pygame.image.load("game_over.png")
person_img = pygame.transform.scale(person_img,(50,50))
key_img = pygame.transform.scale(key_img,(35,37))
shell_img = pygame.transform.scale(shell_img,(30,27))
game_over_img = pygame.transform.scale(game_over_img,(400,225))
key = pygame.Rect(560,300,35,37)
person = pygame.Rect(-10,0,50,50)
shell1 = pygame.Rect(300,300,10,9)
shell2 = pygame.Rect(300,300,10,9)
shell3 = pygame.Rect(300,300,10,9)
game_over = pygame.Rect(1000,187.5,400,225)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
lives = 3
clock = pygame.time.Clock()
x = random.randint(0,600)
y = random.randint(0,600)
w = random.randint(10,320)
h = random.randint(0,320)
walls = [
pygame.Rect(320,300,10,275),
pygame.Rect(415,0,315,10),
pygame.Rect(315,75,10,50),
pygame.Rect(200,90,248,10),
pygame.Rect(214,125,10,300),
pygame.Rect(69,170,10,100),
pygame.Rect(128,200,314,10),
pygame.Rect(128,500,314,10),
pygame.Rect(520,75,10,510),
pygame.Rect(300,375,600,10),
pygame.Rect(415,0,10,315),
pygame.Rect(0,75,150,10)
]
shell1_speed = 3
shell2_speed = 3
shell3_speed = 3
shell1x = random.choice([-1,1])
shell1y = random.choice([-1,1])
shell2x = random.choice([-1,1])
shell2y = random.choice([-1,1])
shell3x = random.choice([-1,1])
shell3y = random.choice([-1,1])
run = True
while run:
    clock.tick(30)
    screen.fill(WHITE)
    font = pygame.font.SysFont(None,35)
    ltext = font.render(f"LIVES: {lives}",True, BLACK)
    screen.blit(ltext,(-10,0))
    for w in walls:
        pygame.draw.rect(screen,RED,w)
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
    for w in walls:
        if person.colliderect(w):
            person.x,person.y = -10,0
    if person.colliderect(shell1):
        person.x,person.y = -10,0
        lives -= 1
    if person.colliderect(shell2):
        person.x,person.y = -10,0
        lives -= 1
    if person.colliderect(shell3):
        person.x,person.y = -10,0
        lives -= 1
    if lives == 0:
        game_over = pygame.Rect(100,187.5,400,225)
        screen.blit(game_over_img,(game_over.x,game_over.y))
        shell1_speed = 0
        shell2_speed = 0
        shell3_speed = 0
        person = pygame.Rect(-10,0,0,0)
    if person.colliderect(key):
        font = pygame.font.SysFont(None,35)
        text = font.render("Congratulations! You made it to Level 2", True, BLACK)
        screen.blit(text,(75,270))
    if random.randint(0,50) == 0:
        shell1x = random.choice([-1,0,1])
        shell1y = random.choice([-1,0,1])
    shell1.x += shell1_speed * shell1x
    shell1.y += shell1_speed * shell1y
    if shell1.left <= 0 or shell1.right >= WIDTH:
        shell1x *= -1
    if shell1.top <= 0 or shell1.bottom >= HEIGHT:
        shell1y *= -1
    if random.randint(0,50) == 0:
        shell2x = random.choice([-1,0,1])
        shell2y = random.choice([-1,0,1])
    shell2.x += shell2_speed * shell2x
    shell2.y += shell2_speed * shell2y
    if shell2.left <= 0 or shell2.right >= WIDTH:
        shell2x *= -1
    if shell2.top <= 0 or shell2.bottom >= HEIGHT:
        shell2y *= -1
    if random.randint(0,50) == 0:
        shell3x = random.choice([-1,0,1])
        shell3y = random.choice([-1,0,1])
    shell3.x += shell3_speed * shell3x
    shell3.y += shell3_speed * shell3y
    if shell3.left <= 0 or shell3.right >= WIDTH:
        shell3x *= -1
    if shell3.top <= 0 or shell3.bottom >= HEIGHT:
        shell3y *= -1
    if person.left <= -25 or person.right >= WIDTH+100:
        person.x,person.y = -10,0
    if person.top <= -25 or person.bottom >= HEIGHT:
        person.x,person.y = -10,0
    screen.blit(person_img,(person.x,person.y))
    screen.blit(key_img,(key.x,key.y))
    screen.blit(shell_img,(shell1.x,shell1.y))
    screen.blit(shell_img,(shell2.x,shell2.y))
    screen.blit(shell_img,(shell3.x,shell3.y))
    pygame.display.flip()
pygame.quit()
