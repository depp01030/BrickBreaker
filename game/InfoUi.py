import pygame
from game import settings

class InfoUi:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 24)  # 將字體大小從 36 改為 24
        self.score = 0
        self.lives = settings.LIVES
        self.mouse_pos = pygame.mouse.get_pos()

    def update(self):
        # 更新分數和生命值
        self.score = self.game.score
        self.lives = self.game.lives
        self.mouse_pos = pygame.mouse.get_pos()

    def draw(self, surface):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        lives_text = self.font.render(f'Lives: {self.lives}', True, (255, 255, 255))

        surface.blit(score_text, (10, 10))
        surface.blit(lives_text, (10, 35))  # 調整垂直位置

        mouse_text = self.font.render(f'Mouse Position: {self.mouse_pos}', True, (255, 255, 255))
        surface.blit(mouse_text, (10, 60))  # 調整垂直位置