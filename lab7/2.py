
import pygame
import os

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

songs = ["s1.mp3", "s2.mp3", "s3.mp3"]
covers = ["bluehair.jpg", "lilpeep.jpg", "sundownimup.jpeg"]
current_song = 0
playing = False

play_img = pygame.image.load("play.png")
pause_img = pygame.image.load("pause.png")
prev_img = pygame.image.load("prev.png")
next_img = pygame.image.load("next.png")

button_size = (50, 50)
play_img = pygame.transform.scale(play_img, button_size)
pause_img = pygame.transform.scale(pause_img, button_size)
prev_img = pygame.transform.scale(prev_img, button_size)
next_img = pygame.transform.scale(next_img, button_size)

pygame.mixer.music.load(songs[current_song])

def draw_ui():
    screen.fill((30, 30, 30))

    cover = pygame.image.load(covers[current_song])
    cover = pygame.transform.scale(cover, (300, 300))
    screen.blit(cover, (150, 20))

    text = font.render(f"Now Playing: {os.path.basename(songs[current_song])}", True, (255, 255, 255))
    screen.blit(text, (50, 350))

    button_y = 420
    prev_rect = screen.blit(prev_img, (100, button_y))
    play_rect = screen.blit(play_img if not playing else pause_img, (250, button_y))
    next_rect = screen.blit(next_img, (400, button_y))

    pygame.display.flip()

    return prev_rect, play_rect, next_rect

prev_rect, play_rect, next_rect = draw_ui()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if prev_rect.collidepoint(event.pos):
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                playing = True
            elif play_rect.collidepoint(event.pos):
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif next_rect.collidepoint(event.pos):
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                playing = True
            
            prev_rect, play_rect, next_rect = draw_ui()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                playing = True
            elif event.key == pygame.K_x:
                pygame.mixer.music.stop()
                playing = False
            elif event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif event.key == pygame.K_c:
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                playing = True

            prev_rect, play_rect, next_rect = draw_ui()

pygame.quit()