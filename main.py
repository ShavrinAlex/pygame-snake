import sys
import pygame
from parameters import *


def check_events():
    global snake_pos_x, snake_pos_y

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

def draw_fon():
    window.fill(color_fon)

    for y in range(window_pixel, window_height, window_pixel):
        pygame.draw.line(window, color_grid, (0, y), (window_width, y))
    for x in range(window_pixel, window_width, window_pixel):
        pygame.draw.line(window, color_grid, (x, 0), (x, window_height))

def food_draw():
    pygame.draw.rect(window, color_food, (food_pos_x, food_pos_y, food_width, food_height))

def snake_draw():
    pygame.draw.rect(window, color_snake, (snake_pos_x, snake_pos_y, snake_width, shake_height))

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
pygame.display.set_icon(window_icon)

while True:
    draw_fon()
    check_events()
    food_draw()
    snake_draw()
    pygame.display.update()
    clock.tick(window_fps)