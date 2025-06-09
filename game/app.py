# BrickBreaker Game Logic

import pygame
import sys
from game import settings
# from game.paddle import Paddle
# from game.ball import Ball
from game.brick import Bricks

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption("BrickBreaker")
        
        # self.paddle = Paddle(self)
        # self.ball = Ball(self)
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

        # ball.move()
        # ball.check_wall_collision()
        # ball.check_paddle_collision(paddle)
        # bricks.handle_collision(ball.rect) 
        pass

    def _update_screen(self):
        self.screen.fill(settings.BACKGROUND_COLOR)
        surface = pygame.display.get_surface()
        # self.paddle.draw()
        # self.ball.draw()
        self.bricks.draw(surface)


        pygame.display.flip()
        self.clock.tick(settings.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()