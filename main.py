import pygame
import random
pygame.init()
WIDTH,HEIGHT = 800,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ping Pong")
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,150,255)
RED = (255,100,100)
paddle_width,paddle_height = 10,80
paddle_speed = 1
ball_radius = 15
score1 = 0
score2 = 0
font = pygame.font.SysFont(None,40)
# ball_speedx = 1*random.choice((1,-1))
# ball_speedy = 1*random.choice((1,-1))
ball_speedx = 1
ball_speedy = 1
paddle1 = pygame.Rect(5,200-paddle_height//2, 10, 80)
paddle2 = pygame.Rect(785,200-paddle_height//2, 10, 80)
ball = pygame.Rect(400-ball_radius//2,200-ball_radius//2, 15, 15)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle1.y -= paddle_speed
        if paddle1.y <= 0:
            paddle1.y = 0
    if keys[pygame.K_DOWN]:
        paddle1.y += paddle_speed
        if paddle1.y >= 320:
            paddle1.y = 320
    if paddle2.centery < ball.centery:
        paddle2.y += paddle_speed
    if paddle2.centery > ball.centery:
        paddle2.y -= paddle_speed 
    ball.x += ball_speedx
    ball.y += ball_speedy
    if ball.top <= 0 or ball.bottom >= 800:
        ball_speedy *= -1
    if ball.colliderect(paddle1):
        ball_speedx *= -1
        score1 += 1
    if ball.colliderect(paddle2):
        ball_speedx *= -1
        score2 += 1
    if ball.left <= 0:
        ball.x,ball.y = WIDTH//2,HEIGHT//2
        ball_speedx *= random.choice((1,-1))
        ball_speedy *= random.choice((1,-1))
    if ball.right >= 800:
        ball.x,ball.y = WIDTH//2,HEIGHT//2
        ball_speedx *= random.choice((1,-1))
        ball_speedy *= random.choice((1,-1))
    screen.fill(BLACK)
    pygame.draw.rect(screen,BLUE,paddle1)
    pygame.draw.rect(screen,RED,paddle2)
    pygame.draw.ellipse(screen,WHITE,ball)
    text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(text,(370,20))
    pygame.display.flip()
pygame.quit()
