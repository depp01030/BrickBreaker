# paddle.py

import pygame
from game import settings 


class Paddle:
    def __init__(self, game):
        width = settings.PADDLE_WIDTH
        height = settings.PADDLE_HEIGHT
        x = (settings.SCREEN_WIDTH - width) // 2
        y = (settings.SCREEN_HEIGHT) - height - 10

        self.rect = pygame.Rect(x, y, width, height)

        self.speed = 10

    # def move_left(self):
    #     if self.x > 0:
    #         self.x -= self.speed

    # def move_right(self):
    #     if self.x < (settings.SCREEN_WIDTH - self.width):
    #         self.x += self.speed
    def update(self):
        # 獲取滑鼠位置
        mouse_pos = pygame.mouse.get_pos()
        # 獲取滑鼠位置並設置 paddle 位置
        # 假設希望滑鼠與 paddle 左邊緣保持一定距離
        mouse_pos = pygame.mouse.get_pos()
        offset = 50  # 滑鼠與 paddle 左邊緣的距離
        self.rect.left = mouse_pos[0] - offset

        # # 確保 paddle 不會超出螢幕邊界
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # elif self.rect.right > settings.SCREEN_WIDTH:
        #     self.rect.right = settings.SCREEN_WIDTH
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def get_rect(self):
        return self.rect