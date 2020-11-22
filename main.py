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

        self.run()
    

    def run(self):
        """Главный цикл приложения"""

        while True:
            self.check_events()
            self.draw()

    def _quit(self):
        """Завершение программы."""
        print('Программа завершилась')
        pg.quit()
        quit()
    
    def check_events(self):
        """Проверка всех событий программы."""

        # Нажатие на крестик
        [self._quit() for event in pg.event.get() if event.type == pg.QUIT]

        # Управление змейкой
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and self.snake.direction != 'down':
            self.snake.direction = 'up'
        elif keys[pg.K_a] and self.snake.direction != 'right':
            self.snake.direction = 'left'
        elif keys[pg.K_s] and self.snake.direction != 'up':
            self.snake.direction = 'down'
        elif keys[pg.K_d] and self.snake.direction != 'left':
            self.snake.direction = 'right'
    
    def draw(self):
        """Отрисовка всех объектво в окне приложения."""

        self.WINDOW.fill(self.COLOR_FON)
        self.snake.draw()

        self.CLOCK.tick(self.FPS)
        pg.display.update()

    



    

class Snake:
    """Класс змейки."""

    def __init__(self, WINDOW, PIXEL):
        """
        Инициализация настроек змейки.
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
        self.len = 1
        self.body = []
        self.head = []

        
    def draw(self):
        """
        Рисует змейку.
        """
        self._move()
        pg.draw.rect(self.WINDOW, self.COLOR, (self.pos_x, self.pos_y, self.WIDTH, self.HIGHT))

    
    def _move(self):
        """
        Движение змейки.
        """


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
        """
        Столкновение змейки со стенкой.
        """

        if self.pos_y < 0:
            self.pos_y = pg.display.get_window_size()[1] - self.PIXEL
        elif self.pos_y >= pg.display.get_window_size()[1]:
            self.pos_y = 0
        elif self.pos_x < 0:
            self.pos_x = pg.display.get_window_size()[0] - self.PIXEL
        elif self.pos_x >= pg.display.get_window_size()[0]:
            self.pos_x = 0
        

        


class Food:

    """
    Класс еды.
    """

    pass



def main():
    app = App()

if __name__ == "__main__":
    main()