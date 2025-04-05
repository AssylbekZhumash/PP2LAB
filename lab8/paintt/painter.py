import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)  


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")


background = pygame.Surface(screen.get_size())
background.fill(WHITE)


icon_size = (40, 40)
try:
    pen_icon = pygame.image.load("pen.png")
    pen_icon = pygame.transform.scale(pen_icon, icon_size)
    rect_icon = pygame.image.load("rectangle.png")
    rect_icon = pygame.transform.scale(rect_icon, icon_size)
    circle_icon = pygame.image.load("circle.png")
    circle_icon = pygame.transform.scale(circle_icon, icon_size)
    eraser_icon = pygame.image.load("eraser.png")
    eraser_icon = pygame.transform.scale(eraser_icon, icon_size)
    color_icon = pygame.image.load("color-change.png")
    color_icon = pygame.transform.scale(color_icon, icon_size)
    clear_icon = pygame.image.load("clear.png")
    clear_icon = pygame.transform.scale(clear_icon, icon_size)
except pygame.error:
    print("Warning: Some icons not found! Creating placeholder icons.")
    
    pen_icon = pygame.Surface(icon_size)
    pen_icon.fill((255, 0, 0))
    rect_icon = pygame.Surface(icon_size)
    rect_icon.fill((0, 255, 0))
    circle_icon = pygame.Surface(icon_size)
    circle_icon.fill((0, 0, 255))
    eraser_icon = pygame.Surface(icon_size)
    eraser_icon.fill((200, 200, 200))
    color_icon = pygame.Surface(icon_size)
    color_icon.fill((255, 255, 0))
    clear_icon = pygame.Surface(icon_size)
    clear_icon.fill((255, 0, 255))

buttons = {
    "pen": (10, 10, pen_icon),
    "rect": (60, 10, rect_icon),
    "circle": (110, 10, circle_icon),
    "eraser": (160, 10, eraser_icon),
    "color": (210, 10, color_icon),
    "clear": (260, 10, clear_icon)
}

font = pygame.font.Font(None, 36)


drawing = False
last_pos = None
color = BLACK
brush_size = 5
tool = None
start_pos = None

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                for key, (x, y, icon) in buttons.items():
                    if x <= event.pos[0] <= x + icon_size[0] and y <= event.pos[1] <= y + icon_size[1]:
                        if key == "color":
                            color = get_random_color()
                        elif key == "clear":
                            background.fill(WHITE)
                        else:
                            tool = key if tool != key else None
                        break
                else:
                    drawing = True
                    last_pos = event.pos
                    start_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if tool == "rect" and start_pos:
                    end_pos = event.pos
                    width = end_pos[0] - start_pos[0]
                    height = end_pos[1] - start_pos[1]
                    pygame.draw.rect(background, color, (*start_pos, width, height), 2)
                elif tool == "circle" and start_pos:
                    radius = int(((event.pos[0] - start_pos[0])**2 + (event.pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(background, color, start_pos, radius, 2)

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "pen":
                    pygame.draw.line(background, color, last_pos, event.pos, brush_size)
                    last_pos = event.pos
                elif tool == "eraser":
                    pygame.draw.line(background, WHITE, last_pos, event.pos, brush_size)
                    last_pos = event.pos
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "pen" if tool != "pen" else None
            elif event.key == pygame.K_2:
                tool = "rect" if tool != "rect" else None
            elif event.key == pygame.K_3:
                tool = "circle" if tool != "circle" else None
            elif event.key == pygame.K_4:
                tool = "eraser" if tool != "eraser" else None
            elif event.key == pygame.K_5:
                color = get_random_color()
            elif event.key == pygame.K_6:
                background.fill(WHITE)
            elif event.key == pygame.K_UP:
                brush_size = min(50, brush_size + 1)
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)
    
    
    screen.blit(background, (0, 0))
    
    
    for key, (x, y, icon) in buttons.items():
        screen.blit(icon, (x, y))
        if tool == key:
            pygame.draw.rect(screen, BLUE, (x-2, y-2, icon_size[0]+4, icon_size[1]+4), 2)
    
    
    pygame.draw.rect(screen, color, (WIDTH-50, 10, 40, 40))
    brush_text = font.render(f"Size: {brush_size}", True, BLACK)
    screen.blit(brush_text, (WIDTH-150, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()