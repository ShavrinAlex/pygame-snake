import random
import pygame
pygame.init()

# Настройки параметров экрана
window_width = 500
window_height = 500
window_title = 'Snake'
window_icon = pygame.image.load('images/Icon.png')
window_fps = 5
window_pixel = 25

# Настройки цветов
color_snake = (10, 200, 10)
color_fon = (0, 0, 0)
color_grid = (60, 60, 60)
color_food = (150, 10, 10)

# Настройки параметров змейки
snake_pos_x = window_width // 2
snake_pos_y = window_height // 2
snake_width = window_pixel
shake_height = window_pixel
snake_direction = 'up'
snake_block = [snake_pos_x, snake_pos_y]
snake_body = []
snake_len = 4

# Настройки параметров еды
food_width = window_pixel
food_height = window_pixel
food_pos_x = random.randrange(0, window_width, window_pixel)
food_pos_y = random.randrange(0, window_height, window_pixel)

