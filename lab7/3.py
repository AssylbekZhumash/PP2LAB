import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 25
STEP = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")

ball_x, ball_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), BALL_RADIUS)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP and ball_y - BALL_RADIUS - STEP >= 0:
                ball_y -= STEP
            elif event.key == K_DOWN and ball_y + BALL_RADIUS + STEP <= HEIGHT:
                ball_y += STEP
            elif event.key == K_LEFT and ball_x - BALL_RADIUS - STEP >= 0:
                ball_x -= STEP
            elif event.key == K_RIGHT and ball_x + BALL_RADIUS + STEP <= WIDTH:
                ball_x += STEP

pygame.quit()