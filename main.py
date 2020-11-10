import sys
import pygame

pygame.init()

window_width = 400
window_height = 400
window_title = 'Snake'
window_icon = pygame.image.load('images/Icon.png')
window_fps = 5

color_snake = (10, 200, 10)
color_fon = (0, 0, 0)

snake_pos_x = 0
snake_pos_y = 0
snake_width = 20
shake_height = 20

clock = pygame.time.Clock()



window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
pygame.display.set_icon(window_icon)

while True:
    window.fill(color_fon)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    if keys[pygame.K_w] and snake_pos_y > 0:
        snake_pos_y -= 20
    elif keys[pygame.K_s] and snake_pos_y + shake_height < window_height:
        snake_pos_y += 20
    elif keys[pygame.K_a] and snake_pos_x > 0:
        snake_pos_x -= 20
    elif keys[pygame.K_d] and snake_pos_x + snake_width < window_width:
        snake_pos_x += 20

    pygame.draw.rect(window, color_snake, (snake_pos_x, snake_pos_y, snake_width, shake_height))

    pygame.display.update()

    clock.tick(window_fps)