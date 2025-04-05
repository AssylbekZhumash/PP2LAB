import pygame
import random

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
load_icon = lambda name: pygame.transform.scale(pygame.image.load(name), icon_size)

pen_icon = load_icon("pen.png")
rect_icon = load_icon("rectangle.png")
circle_icon = load_icon("circle.png")
eraser_icon = load_icon("eraser.png")
color_icon = load_icon("color-change.png")
clear_icon = load_icon("clear.png")
square_icon = load_icon("square.png")
triangle_icon = load_icon("triangle.png")
eq_triangle_icon = load_icon("equilateral-triangle.png")
rhombus_icon = load_icon("rhombus.png")


buttons = {
    "pen": (10, 10, pen_icon),
    "rect": (60, 10, rect_icon),
    "circle": (110, 10, circle_icon),
    "eraser": (160, 10, eraser_icon),
    "color": (210, 10, color_icon),
    "clear": (260, 10, clear_icon),
    "square": (310, 10, square_icon),
    "triangle": (360, 10, triangle_icon),
    "eq_triangle": (410, 10, eq_triangle_icon),
    "rhombus": (460, 10, rhombus_icon)
}


font = pygame.font.Font(None, 36)


drawing = False
last_pos = None
color = BLACK
brush_size = 5
tool = None
start_pos = None

def get_random_color():
    return [random.randint(0, 255) for _ in range(3)]


running = True
while running:
    screen.blit(background, (0, 0))

    
    for key, (x, y, icon) in buttons.items():
        screen.blit(icon, (x, y))
        if tool == key:
            pygame.draw.rect(screen, BLUE, (x - 2, y - 2, icon_size[0] + 4, icon_size[1] + 4), 2)

    
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
                if start_pos is not None:
                    x1, y1 = start_pos
                    x2, y2 = event.pos

                    if tool == "rect":
                        pygame.draw.rect(background, color, (x1, y1, x2 - x1, y2 - y1), 2)
                    elif tool == "circle":
                        radius = max(abs(x2 - x1), abs(y2 - y1))
                        pygame.draw.circle(background, color, start_pos, radius, 2)
                    elif tool == "square":
                        side = min(abs(x2 - x1), abs(y2 - y1))
                        pygame.draw.rect(background, color, (x1, y1, side, side), 2)
                    elif tool == "triangle":
                        pygame.draw.polygon(background, color, [(x1, y2), (x2, y2), (x1, y1)], 2)
                    elif tool == "eq_triangle":
                        height = (3 ** 0.5 / 2) * (x2 - x1)
                        pygame.draw.polygon(background, color, [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)], 2)
                    elif tool == "rhombus":
                        dx = abs(x2 - x1) // 2
                        dy = abs(y2 - y1) // 2
                        pygame.draw.polygon(background, color, [
                            (x1 + dx, y1),
                            (x2, y1 + dy),
                            (x1 + dx, y2),
                            (x1, y1 + dy)
                        ], 2)

                start_pos = None

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
                tool = "square" if tool != "square" else None
            elif event.key == pygame.K_7:
                tool = "triangle" if tool != "triangle" else None
            elif event.key == pygame.K_8:
                tool = "eq_triangle" if tool != "eq_triangle" else None
            elif event.key == pygame.K_9:
                tool = "rhombus" if tool != "rhombus" else None
            elif event.key == pygame.K_x:
                background.fill(WHITE)
            elif event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)

    
    pygame.draw.rect(screen, color, (WIDTH - 50, 10, 40, 40))

    
    brush_text = font.render(f"Size: {brush_size}", True, BLACK)
    screen.blit(brush_text, (WIDTH - 150, 20))

    pygame.display.flip()

pygame.quit()
