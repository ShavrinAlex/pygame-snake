import time
import random
import pygame as pg

class App:
    """
    Управляет всеми процессами приложения.
    """

    pass


class Snake:
    """
    Класс змейки.
    """

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

        pg.draw.rect(self.WINDOW, self.COLOR, (self.pos_x, self.pos_y, self.WINDOW, self.HIGHT))

    
    def move(self):
        """
        Движение змейки.
        """

        self._collision_wall()

        if self.direction == 'up':
            self.pos_y -= self.PIXEL
        elif self.direction == 'down':
            self.pos_y += self.PIXEL
        elif self.direction == 'left':
            self.pos_x -= self.PIXEL
        else:
            self.pos_x += self.PIXEL
        
    

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
