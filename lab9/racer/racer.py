import pygame, sys
from pygame.locals import *
import random, time


pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()


GRAY = (100, 100, 100)
GREEN = (76, 208, 56)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 232, 0)
BLACK = (0, 0, 0)


SCREEN_WIDTH = 840
SCREEN_HEIGHT = 650
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")


ENEMY_SPEED = 8
COIN_SPEED = ENEMY_SPEED // 2
SCORE = 0
COINS_COLLECTED = 0
RECORD = 0
GAME_OVER = False


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
game_over_text = font.render("Game Over", True, BLACK)
restart_text = font_small.render("Press R to Restart or Q to Quit", True, BLACK)


pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
crash_sound = pygame.mixer.Sound("crash.wav")


marker_width = 10
marker_height = 50
lane_marker_move_y = 0

class Enemy(pygame.sprite.Sprite):
    """Enemy car moving downward"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("taxi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(lane_positions), -50)

    def move(self):
        if not GAME_OVER:
            self.rect.move_ip(0, ENEMY_SPEED)
            if self.rect.top > SCREEN_HEIGHT:
                self.rect.center = (random.choice(lane_positions), -50)

class Player(pygame.sprite.Sprite):
    """Player car controlled by left/right movement"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.current_lane = 1  
        self.rect.center = (lane_positions[self.current_lane], 520)
    
    def move(self, direction):
        if not GAME_OVER:
            if direction == -1 and self.current_lane > 0:
                self.current_lane -= 1
            elif direction == 1 and self.current_lane < 2:
                self.current_lane += 1
            self.rect.centerx = lane_positions[self.current_lane]

class Coin(pygame.sprite.Sprite):
    """Coins that give different scores and spawn randomly"""
    def __init__(self):
        super().__init__()
        self.images = {
            1: pygame.image.load("Coin.png"),       
            2: pygame.image.load("bluecoin.png"),  
            3: pygame.image.load("redcoin.png")    
        }
        self.respawn()

    def move(self):
        if not GAME_OVER:
            self.rect.move_ip(0, COIN_SPEED)
            if self.rect.top > SCREEN_HEIGHT:
                self.respawn()

    def respawn(self):
        """Respawns coin with a random value and corresponding image"""
        weights = [50, 30, 20]  
        values = [1, 2, 3]  
        self.value = random.choices(values, weights)[0]  
        self.image = pygame.transform.scale(self.images[self.value], (30, 30))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(lane_positions), random.randint(-100, 0))  


def reset_game():
    """Resets game variables and objects"""
    global SCORE, COINS_COLLECTED, P1, E1, C1, all_sprites, enemies, coins, RECORD, ENEMY_SPEED, GAME_OVER
    if SCORE > RECORD:
        RECORD = SCORE  
    SCORE = 0
    COINS_COLLECTED = 0
    ENEMY_SPEED = 8  
    GAME_OVER = False
    
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
    
    if not GAME_OVER:
       
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
            COINS_COLLECTED += C1.value  
            SCORE += C1.value  
            C1.respawn()

            
            if COINS_COLLECTED % 5 == 0:
                ENEMY_SPEED += 1
                COIN_SPEED = ENEMY_SPEED // 2  

        
        if pygame.sprite.spritecollideany(P1, enemies):
            crash_sound.play()
            GAME_OVER = True

    else:
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30))
        DISPLAYSURF.blit(restart_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 30))

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
sys.exit()
