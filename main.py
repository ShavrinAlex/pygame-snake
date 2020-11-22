import time
import random
import pygame as pg

class App:
    """
    Управляет всеми процессами приложения.
    """
    def __init__(self):
        """инициализация настроек приложения"""
        pg.init()

        self.WIDTH = 600
        self.HEIGHT = 600
        self.PIXEL = 20
        self.COLOR_FON = (20, 20, 20)
        self.FPS = 8
        self.CLOCK = pg.time.Clock()
        self.TITLE = "Snake"
        self.ICON = pg.image.load('images/icon.png')
        self.WINDOW = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption(self.TITLE)
        pg.display.set_icon(self.ICON)

        self.snake = Snake(self.WINDOW, self.PIXEL)

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

        # Управление змейкой
        if keys[pg.K_w] and self.snake.direction != 'down':
            self.snake.direction = 'up'
        elif keys[pg.K_a] and self.snake.direction != 'right':
            self.snake.direction = 'left'
        elif keys[pg.K_s] and self.snake.direction != 'up':
            self.snake.direction = 'down'
        elif keys[pg.K_d] and self.snake.direction != 'left':
            self.snake.direction = 'right'

    def _draw(self):
        """Отрисовка всех объектво в окне приложения."""

        self.WINDOW.fill(self.COLOR_FON)
        self.snake.draw()

        self.CLOCK.tick(self.FPS)
        pg.display.update()

    
class Snake:
    """Класс змейки."""

    def __init__(self, WINDOW, PIXEL):
        """Инициализация настроек змейки."""

        self.WINDOW = WINDOW
        self.PIXEL = PIXEL
        self.WIDTH = self.PIXEL
        self.HIGHT = self.PIXEL
        self.STEP = self.PIXEL
        self.COLOR = (20, 250, 20)
        self.direction = 'up'
        self.pos_x = pg.display.get_window_size()[0] // 2
        self.pos_y = pg.display.get_window_size()[1] // 2
        self.len = 1
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
        """Отрисовка змейки."""
        self._move()
        self.add_block_in_body()

        for block in self.body:
            pg.draw.rect(self.WINDOW, self.COLOR, (block[0], block[1], self.WIDTH, self.HIGHT))
        
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
        

    @property
    def is_collision_tail(self):
        """Проверка пересечения координат с хвостом."""

        for block in self.body[:-1]:
            if self.pos_x == block[0] and self.pos_y == block[1]:
                return True
        return False


class Food:

    """
    Класс еды.
    """

    pass



def main():
    """Точка входа в программу"""

    # Экземпляр приложения
    app = App()

if __name__ == "__main__":
    main()