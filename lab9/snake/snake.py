import pygame
import random
import sys
import time


WIDTH, HEIGHT = 640, 640
PIXELS = 32
SQUARES_X, SQUARES_Y = WIDTH // PIXELS, HEIGHT // PIXELS


BG1 = (156, 210, 54)  
BG2 = (147, 203, 57)  
RED = (255, 0, 0)  
CYAN = (0, 255, 255)  
GOLD = (255, 215, 0)  
BLUE = (0, 0, 255)  
BLACK = (0, 0, 0)  

class Snake:
    def __init__(self):
        self.color = BLUE
        self.headX = SQUARES_X // 2
        self.headY = SQUARES_Y // 2
        self.body = [(self.headX, self.headY)]
        self.direction = (1, 0)  
        self.grow = False
        self.points = 0
        self.level = 1
        self.speed = 5
        self.high_score = self.load_high_score()  
        self.next_level_score = 4 

        
        self.font = pygame.font.SysFont("Arial", 24, bold=True)

    def move(self, event):
        """Handles user input for movement"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != (0, 1):
                self.direction = (0, -1)
            elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                self.direction = (0, 1)
            elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                self.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                self.direction = (1, 0)

    def update_position(self):
        """Updates snake's position and checks collisions"""
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])

        
        if not (0 <= new_head[0] < SQUARES_X and 0 <= new_head[1] < SQUARES_Y):
            self.reset()
            return False

        
        if new_head in self.body:
            self.reset()
            return False

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

            
            if self.points >= self.next_level_score:
                self.level += 1
                self.speed += 0.3
                self.next_level_score += (self.level * 4)

        return True

    def reset(self):
        """Resets the snake after losing and updates high score"""
        if self.points > self.high_score:
            self.high_score = self.points
            self.save_high_score()
        self.__init__()  

    def save_high_score(self):
        """Saves the high score to a file"""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        """Loads the high score from a file"""
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def draw(self, surface):
        """Draws the snake on the screen"""
        for segment in self.body:
            pygame.draw.rect(surface, self.color, (segment[0] * PIXELS, segment[1] * PIXELS, PIXELS, PIXELS))

    def show(self, surface, apple):
        """Displays the score, level, record, and fruit timer"""
        lbl_score_level = self.font.render(f'Score: {self.points}  Level: {self.level}', True, BLACK)
        lbl_record = self.font.render(f'Record: {self.high_score}', True, BLACK)

        surface.blit(lbl_score_level, (10, 10))
        surface.blit(lbl_record, (10, 40))

        
        time_left = max(0, 10 - int(time.time() - apple.spawn_time))
        timer_lbl = self.font.render(f'Time: {time_left}s', True, BLACK)
        surface.blit(timer_lbl, (WIDTH - 100, 10))

class Apple:
    def __init__(self):
        self.spawn()

    def spawn(self):
        """Spawns a new apple with weighted chances"""
        chance = random.randint(1, 100)
        if chance <= 50:
            self.type = "regular"
            self.color = RED
            self.points = 1
        elif chance <= 80: 
            self.type = "ice"
            self.color = CYAN
            self.points = 3
        else:  
            self.type = "golden"
            self.color = GOLD
            self.points = 5
        
        while True:
            self.posX = random.randint(0, SQUARES_X - 1)
            self.posY = random.randint(0, SQUARES_Y - 1)
            if (self.posX, self.posY) not in snake.body:
                break
        
        self.spawn_time = time.time()  

    def draw(self, surface):
        """Draws the apple on the screen"""
        pygame.draw.rect(surface, self.color, (self.posX * PIXELS, self.posY * PIXELS, PIXELS, PIXELS))

def draw_grid(surface):
    """Draws a checkered grid background"""
    surface.fill(BG1)
    for row in range(SQUARES_Y):
        for col in range(SQUARES_X):
            if (row + col) % 2 == 0:
                pygame.draw.rect(surface, BG2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    global snake
    snake = Snake()
    apple = Apple()

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(snake.speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            snake.move(event)  

        if not snake.update_position():
            apple.spawn()  

        
        if (snake.body[0][0], snake.body[0][1]) == (apple.posX, apple.posY):
            snake.points += apple.points  
            apple.spawn()
            snake.grow = True

        
        if time.time() - apple.spawn_time > 10:
            apple.spawn()

        draw_grid(screen)
        apple.draw(screen)
        snake.draw(screen)
        snake.show(screen, apple)  
        pygame.display.update()

    pygame.quit()
    sys.exit()

main()
