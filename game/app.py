# BrickBreaker Game Logic

import pygame
import sys
from game import settings
from game.paddle import Paddle
from game.ball import Ball
from game.brick import Bricks
from game import InfoUi
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption("BrickBreaker")

        self.score = 0
        self.lives = settings.LIVES 

        self.info_ui = InfoUi.InfoUi(self)
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bricks = Bricks(self)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self._check_events()
            self._update_game_state()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update_game_state(self):
        self.paddle.update()
        self.ball.move()
        self.ball.check_wall_collision()
        self.ball.check_paddle_collision(self.paddle)
        self.ball.check_bricks_collision(self.bricks) 
        
        self.info_ui.update()

    def _update_screen(self):
        self.screen.fill(settings.BACKGROUND_COLOR)
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self.bricks.draw(self.screen)

        self.info_ui.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(settings.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()