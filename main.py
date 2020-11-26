import time
import random
import pygame as pg


class App:
    """
    Управляет всеми процессами приложения.
    """

    def __init__(self):
        """Инициализация настроек приложения"""
        # initialization pygame
        pg.init()

        # Window setings
        self.WIDTH = 600
        self.HEIGHT = 600
        self.PIXEL = 20
        self.COLOR_FON = (20, 20, 20)
        self.FPS = 5
        self.CLOCK = pg.time.Clock()
        self.TITLE = "Snake"
        self.ICON = pg.image.load('images/icon.png')
        self.WINDOW = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption(self.TITLE)
        pg.display.set_icon(self.ICON)

        # Example snake
        self.snake = Snake(self.WINDOW, self.PIXEL)

        # Example food
        self.food = Food(self.WINDOW, self.PIXEL, self.snake)

        # Program start
        self._run()

    def _run(self):
        """Главный цикл приложения"""

        while True:
            self._check_events()
            self._draw()

    def _quit(self):
        """Завершение программы."""
        print('Программа завершилась')
        pg.quit()
        quit()

    def _check_events(self):
        """Проверка всех событий программы."""

        # Нажатие на крестик
        [self._quit() for event in pg.event.get() if event.type == pg.QUIT]

        # События с клавиатуры
        keys = pg.key.get_pressed()

        # Завершение программы на Escape
        if keys[pg.K_ESCAPE]:
            self._quit()

        # Управление змейкой wasd or khjl or стрелочки
        if (keys[pg.K_w] or keys[pg.K_k] or keys[pg.K_UP]) and self.snake.direction != 'down':
            self.snake.direction = 'up'
        elif (keys[pg.K_a] or keys[pg.K_h] or keys[pg.K_LEFT]) and self.snake.direction != 'right':
            self.snake.direction = 'left'
        elif (keys[pg.K_s] or keys[pg.K_j] or keys[pg.K_DOWN]) and self.snake.direction != 'up':
            self.snake.direction = 'down'
        elif (keys[pg.K_d] or keys[pg.K_l] or keys[pg.K_RIGHT]) and self.snake.direction != 'left':
            self.snake.direction = 'right'

    def _draw(self):
        """Отрисовка всех объектво в окне приложения."""

        # Background color
        self.WINDOW.fill(self.COLOR_FON)

        # Draw food
        self.food.draw()

        # Draw snake
        self.snake.draw()

        # Framerate
        self.CLOCK.tick(self.FPS)

        # Update
        pg.display.update()


class Snake:
    """Класс змейки."""

    def __init__(self, WINDOW, PIXEL):
        """Инициализация настроек змейки.

        Args:
            WINDOW (Surface): Окно библеотеки pygame.
            PIXEL (Int): Размер стороны виртуального пикселя.
        """

        self.WINDOW = WINDOW
        self.PIXEL = PIXEL
        self.WIDTH = self.PIXEL
        self.HIGHT = self.PIXEL
        self.STEP = self.PIXEL
        self.COLOR = (20, 250, 20)
        self.direction = 'up'
        self.pos_x = pg.display.get_window_size()[0] // 2
        self.pos_y = pg.display.get_window_size()[1] // 2
        self.len = 15
        self.body = []
        self.head = []

    def add_block_in_body(self):
        """Добавляет новый блок в тело змейки."""

        self.head = []
        self.head.append(self.pos_x)
        self.head.append(self.pos_y)
        self.body.append(self.head)

    def check_len_body(self):
        """Проверяет фактическую и должную длинну змейки."""

        if len(self.body) >= self.len:
            self.body.pop(0)

    def draw(self):
        """Отрисовка змейки цветом self.COLOR в окне self.WINDOW в координатах self.pos_x, self_pos_y"""
        self._move()
        self.add_block_in_body()

        for block in self.body:
            pg.draw.rect(self.WINDOW, self.COLOR,
                         (block[0], block[1], self.WIDTH, self.HIGHT))

        self.check_len_body()

    def _move(self):
        """Изменение координат self.pos_x, self.pos_y."""

        if self.direction == 'up':
            self.pos_y -= self.PIXEL
        elif self.direction == 'down':
            self.pos_y += self.PIXEL
        elif self.direction == 'left':
            self.pos_x -= self.PIXEL
        else:
            self.pos_x += self.PIXEL

        self._collision_wall()
        self._collision_tail()

    def _collision_wall(self):
        """Проверка пересечения координат со стенкой."""

        if self.pos_y < 0:
            self.pos_y = pg.display.get_window_size()[1] - self.PIXEL
        elif self.pos_y >= pg.display.get_window_size()[1]:
            self.pos_y = 0
        elif self.pos_x < 0:
            self.pos_x = pg.display.get_window_size()[0] - self.PIXEL
        elif self.pos_x >= pg.display.get_window_size()[0]:
            self.pos_x = 0

    
    def _collision_tail(self):
        """Проверка пересечения координат с хвостом.

        Returns:
            [True]: Если координаты self.pos_x, self.pos_y
                    пересекаются с координатами блоков внутри тела змейки self.body.
                   
            [False]:Если координаты self.pos_x, self.pos_y
                    не пересекаются с координатами блоков внутри тела змейки self.body.
        """
        for block in self.body[:-1]:
            if self.pos_x == block[0] and self.pos_y == block[1]:
               quit()


class Food:

    """
    Класс еды.
    """

    def __init__(self, WINDOW, PIXEL, snake):
        """Инициализация нвстроек еды.


        Args:
            WINDOW (Surface): Окно библеотеки pygame.
            PIXEL (Int): Размер стороны виртуального пикселя.
        """
        self.WINDOW = WINDOW
        self.PIXEL = PIXEL
        self.WIDTH = PIXEL
        self.HEIGHT = PIXEL
        self.COLOR = (200, 20, 20)
        self.set_position()

        self.snake = snake


    def draw(self):
        
        self._is_eaten()
        pg.draw.rect(self.WINDOW, self.COLOR, (self.pos_x, self.pos_y, self.WIDTH, self.HEIGHT),
                    border_radius=self.PIXEL)
        

    def set_position(self):

        self.pos_x = random.randrange(0, pg.display.get_window_size()[0] - self.PIXEL, self.PIXEL)
        self.pos_y = random.randrange(0, pg.display.get_window_size()[1] - self.PIXEL, self.PIXEL)


    def _is_eaten(self):

        if self.pos_x == self.snake.pos_x and self.pos_y == self.snake.pos_y:
            self.set_position()
            self.snake.len += 1
    
        


def main():
    """Точка входа в программу"""

    # Example Program
    app = App()


if __name__ == "__main__":
    main()
