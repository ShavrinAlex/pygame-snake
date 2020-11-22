import sys
import time
import pygame
from parameters import *


def check_events():
    """Проверка событий программы и клавиатуры"""
    global snake_direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    if keys[pygame.K_w] and snake_direction != 'down':
        snake_direction = 'up'
    elif keys[pygame.K_s] and snake_direction != 'up':
        snake_direction = 'down'
    elif keys[pygame.K_a] and snake_direction != 'right':
        snake_direction = 'left'
    elif keys[pygame.K_d] and snake_direction != 'left':
        snake_direction = 'right'


def draw_fon():
    """Рисуем фон окна"""
    window.fill(color_fon)

    for y in range(window_pixel, window_height, window_pixel):
        pygame.draw.line(window, color_grid, (0, y), (window_width, y))
    for x in range(window_pixel, window_width, window_pixel):
        pygame.draw.line(window, color_grid, (x, 0), (x, window_height))


def food_draw():
    """Рисуем еду"""
    pygame.draw.rect(window, color_food, (food_pos_x,
                                          food_pos_y, food_width, food_height))


def food_check_collision():
    """Проверка на пересечение координат змейки и еды"""
    global window_fps, snake_len

    if snake_pos_x == food_pos_x and snake_pos_y == food_pos_y:
        food_set_pos()
        window_fps += 1
        snake_len += 1


def food_set_pos():
    """Устанавливаем новые координаты для еды"""
    global food_pos_x, food_pos_y

    food_pos_x = random.randrange(0, window_width, window_pixel)
    food_pos_y = random.randrange(0, window_height, window_pixel)


def snake_draw():
    """Рисуем змейку"""

    snake_haed = []
    snake_haed.append(snake_pos_x)
    snake_haed.append(snake_pos_y)

    snake_body.append(snake_haed)
    for block in snake_body:
        pygame.draw.rect(window, color_snake,
                         (block[0], block[1], snake_width, shake_height))

    if len(snake_body) >= snake_len:
        snake_body.pop(0)


def snake_move():
    """Отвечает за передвижение змейки"""
    global snake_pos_x, snake_pos_y

    if snake_direction == 'up':
        snake_pos_y -= window_pixel
    elif snake_direction == 'down':
        snake_pos_y += window_pixel
    elif snake_direction == 'left':
        snake_pos_x -= window_pixel
    else:
        snake_pos_x += window_pixel


def snake_check_collision_wall():
    """Проверяем на столкновение змейки с стенкой"""
    global snake_pos_x, snake_pos_y

    if snake_pos_y < 0:
        snake_pos_y = window_height - window_pixel
    elif snake_pos_y > window_height - window_pixel:
        snake_pos_y = 0
    if snake_pos_x < 0:
        snake_pos_x = window_width - window_pixel
    elif snake_pos_x > window_width - window_pixel:
        snake_pos_x = 0


def snake_check_collision_tail():
    """Проверка на столкновение с хвостом"""
    for block in snake_body[:-1]:
        if snake_pos_x == block[0] and snake_pos_y == block[1]:
            time.sleep(2)
            sys.exit()


pygame.init()

clock = pygame.time.Clock()

# Создаем окно программы
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)
pygame.display.set_icon(window_icon)

while True:
    draw_fon()
    check_events()
    food_check_collision()
    food_draw()
    snake_move()
    snake_check_collision_wall()
    snake_check_collision_tail()
    snake_draw()
    pygame.display.update()

    clock.tick(window_fps)
