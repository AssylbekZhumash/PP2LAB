import pygame
import time
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("mickeyclock.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

right_hand = pygame.image.load("rightarm.png")
left_hand = pygame.image.load("leftarm.png")

right_hand = pygame.transform.scale(right_hand, (right_hand.get_width() // 2, right_hand.get_height() // 2))
left_hand = pygame.transform.scale(left_hand, (left_hand.get_width() // 2, left_hand.get_height() // 2))

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    min_angle = -(minutes * 6) + 90
    sec_angle = -(seconds * 6) + 90
    
    min_rotated = pygame.transform.rotate(right_hand, min_angle)
    sec_rotated = pygame.transform.rotate(left_hand, sec_angle)
    
    min_rect = min_rotated.get_rect(center=CENTER)
    sec_rect = sec_rotated.get_rect(center=CENTER)
    
    screen.blit(min_rotated, min_rect)
    screen.blit(sec_rotated, sec_rect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()