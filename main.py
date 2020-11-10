import sys
import random
import pygame

pygame.init()

window_width = 500
window_height = 500
window_title = 'Snake'
window_icon = pygame.image.load('images/Icon.png')
window_fps = 5
window_pixel = 25

clock = pygame.time.Clock()

color_snake = (10, 200, 10)
color_fon = (0, 0, 0)
color_grid = (60, 60, 60)
color_food = (150, 10, 10)

snake_pos_x = 0
snake_pos_y = 0
snake_width = window_pixel
shake_height = window_pixel

food_width = window_pixel
food_height = window_pixel
food_pos_x = random.randrange(0, window_width - food_width, window_pixel)
food_pos_y = random.randrange(0, window_height - food_height, window_pixel)



window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
pygame.display.set_icon(window_icon)

while True:
    window.fill(color_fon)

    for y in range(window_pixel, window_height, window_pixel):
        pygame.draw.line(window, color_grid, (0, y), (window_width, y))
    for x in range(window_pixel, window_width, window_pixel):
        pygame.draw.line(window, color_grid, (x, 0), (x, window_height))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    if keys[pygame.K_w] and snake_pos_y > 0:
        snake_pos_y -= window_pixel
    elif keys[pygame.K_s] and snake_pos_y + shake_height < window_height:
        snake_pos_y += window_pixel
    elif keys[pygame.K_a] and snake_pos_x > 0:
        snake_pos_x -= window_pixel
    elif keys[pygame.K_d] and snake_pos_x + snake_width < window_width:
        snake_pos_x += window_pixel

    pygame.draw.rect(window, color_food, (food_pos_x, food_pos_y, food_width, food_height))

    pygame.draw.rect(window, color_snake, (snake_pos_x, snake_pos_y, snake_width, shake_height))

    pygame.display.update()

    clock.tick(window_fps)