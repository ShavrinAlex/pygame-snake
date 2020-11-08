import sys
import pygame

pygame.init()

window_width = 400
window_height = 400
window_title = 'Snake'
window_icon = pygame.image.load('images/Icon.png')
window_fps = 5

clock = pygame.time.Clock()

pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
pygame.display.set_icon(window_icon)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()

    clock.tick(window_fps)