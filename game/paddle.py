# paddle.py

from game import settings 
import pygame

class Paddle:
    def __init__(self):
        self.width = settings.PADDLE_WIDTH
        self.height = settings.PADDLE_HEIGHT
        self.x = (settings.SCREEN_WIDTH - self.width) // 2
        self.y = (settings.SCREEN_HEIGHT) - self.height - 10
        self.speed = 10

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < (settings.SCREEN_WIDTH - self.width):
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)