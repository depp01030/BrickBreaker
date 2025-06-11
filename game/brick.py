import pygame
import random
from game import settings


class Bricks:
    def __init__(self, game):
        self.game = game
        self.bricks = []
        self.rows, self.cols = self._calculate_bricks_rows_and_cols()
        self.create_bricks()

    def _calculate_bricks_rows_and_cols(self):
        screen_width = settings.SCREEN_WIDTH
        screen_height = settings.SCREEN_HEIGHT
        width = settings.BRICK_WIDTH
        height = settings.BRICK_HEIGHT
        
        # 使用更小的間距值使磚塊排列更緊密
        padding = settings.BRICK_PADDING 
        bottom_margin = settings.BRICKS_DISTANCE_TO_BUTTOM

        cols = (screen_width - padding) // (width + padding)
        rows = (screen_height - bottom_margin - padding) // (height + padding)

        return rows, cols

    def create_bricks(self):
        # 使用與上面相同的較小間距
        padding = settings.BRICK_PADDING 
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * (settings.BRICK_WIDTH + padding) + padding
                y = row * (settings.BRICK_HEIGHT + padding) + padding

                brick = ExplosiveBrick(self.game, row, col, x, y)
                self.bricks.append(brick)

    def draw(self, surface):
        for brick in self.bricks:
            brick.draw(surface)

    def collide(self, ball):
        for brick in self.bricks:
            if brick.collide(ball):
                return True
        return False

    def reset(self):
        for brick in self.bricks:
            brick.reset()

class Brick:
    def __init__(self, game, row, col, x, y, color):
        self.game = game
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        width, height = settings.BRICK_WIDTH, settings.BRICK_HEIGHT
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        # 👇 增加更多 glow layer 
        pygame.draw.rect(surface, self.color, self.rect, border_radius=2)


class ExplosiveBrick(Brick):
    def __init__(self, game, row, col, x, y):
        super().__init__(game, row, col, x, y, settings.RED)
