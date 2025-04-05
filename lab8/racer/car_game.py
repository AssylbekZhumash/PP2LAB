import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

GRAY = (100, 100, 100)
GREEN = (76, 208, 56)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 232, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 650
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

ENEMY_SPEED = 8
COIN_SPEED = ENEMY_SPEED // 2
SCORE = 0
COINS_COLLECTED = 0
RECORD = 0

road_width = 340
border_width = (SCREEN_WIDTH - road_width) // 2
lane_width = road_width // 3
road_x = border_width
lane_positions = [
    road_x + lane_width // 2,
    road_x + lane_width + lane_width // 2,
    road_x + 2 * lane_width + lane_width // 2
]

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
restart_text = font_small.render("Press R to Restart or Q to Quit", True, BLACK)

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
try:
    pygame.mixer.music.load("background.wav")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    crash_sound = pygame.mixer.Sound("crash.wav")
    crash_sound.set_volume(0.8)
except:
    class DummySound:
        def play(self): pass
    crash_sound = DummySound()

marker_width = 10
marker_height = 50
lane_marker_move_y = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        try:
            self.image = pygame.image.load("taxi.png")
        except:
            self.image = pygame.Surface((50, 100))
            self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(lane_positions), -50)

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.choice(lane_positions), -50)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        try:
            self.image = pygame.image.load("car.png")
        except:
            self.image = pygame.Surface((50, 100))
            self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.current_lane = 1
        self.rect.center = (lane_positions[self.current_lane], 520)
    
    def move(self, direction):
        if direction == -1 and self.current_lane > 0:
            self.current_lane -= 1
        elif direction == 1 and self.current_lane < 2:
            self.current_lane += 1
        self.rect.centerx = lane_positions[self.current_lane]

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("Coin.png")
            self.image = pygame.transform.scale(self.image, (30, 30))
        except:
            self.image = pygame.Surface((30, 30))
            self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.respawn()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.choice(lane_positions), random.randint(-100, 0))

def reset_game():
    global SCORE, COINS_COLLECTED, P1, E1, C1, all_sprites, enemies, coins, RECORD
    if SCORE > RECORD:
        RECORD = SCORE
    SCORE = 0
    COINS_COLLECTED = 0
    P1 = Player()
    E1 = Enemy()
    C1 = Coin()
    
    coins = pygame.sprite.Group()
    coins.add(C1)
    
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(C1)
    all_sprites.add(P1)
    all_sprites.add(E1)

reset_game()

running = True
while running:
    direction = 0
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                reset_game()
            if event.key == K_q:
                running = False
            if event.key == K_LEFT:
                direction = -1
            if event.key == K_RIGHT:
                direction = 1
    
    DISPLAYSURF.fill(GREEN)
    pygame.draw.rect(DISPLAYSURF, GRAY, (road_x, 0, road_width, SCREEN_HEIGHT))
    pygame.draw.rect(DISPLAYSURF, YELLOW, (road_x - 5, 0, 5, SCREEN_HEIGHT))
    pygame.draw.rect(DISPLAYSURF, YELLOW, (road_x + road_width, 0, 5, SCREEN_HEIGHT))

    lane_marker_move_y += ENEMY_SPEED * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, SCREEN_HEIGHT, marker_height * 2):
        pygame.draw.rect(DISPLAYSURF, WHITE, (lane_positions[0] + lane_width // 2, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(DISPLAYSURF, WHITE, (lane_positions[1] + lane_width // 2, y + lane_marker_move_y, marker_width, marker_height))

    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    record_text = font_small.render(f"Record: {RECORD}", True, BLACK)
    
    DISPLAYSURF.blit(coins_text, (10, 10))
    DISPLAYSURF.blit(scores, (SCREEN_WIDTH - 150, 10))
    DISPLAYSURF.blit(record_text, (SCREEN_WIDTH - 150, 40))
    
    for entity in all_sprites:
        if isinstance(entity, Player):
            entity.move(direction)
        else:
            entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        SCORE += 1
        C1.respawn()
    
    if pygame.sprite.spritecollideany(P1, enemies):
        try:
            crash_sound.play()
        except:
            pass
        time.sleep(1)
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30))
        DISPLAYSURF.blit(restart_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 30))
        pygame.display.update()
        time.sleep(2)
        reset_game()

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
sys.exit()