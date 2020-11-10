import random
import pygame
pygame.init()

window_width = 500
window_height = 500
window_title = 'Snake'
window_icon = pygame.image.load('images/Icon.png')
window_fps = 5
window_pixel = 25

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
