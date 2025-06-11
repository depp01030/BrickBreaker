# BrickBreaker Game Logic

import pygame
import sys
import random
from game import settings
from game.paddle import Paddle
from game.ball import Ball
from game.brick import Bricks
from game.particle_effect import ParticleEffect, DustParticleEffect
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
        self.particle_effects = []
        self.shake_frames = 0
        self.shake_magnitude = 0
        self.draw_surface = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.running = True

    def spawn_particle_effect(self, pos, color):
        self.particle_effects.append(ParticleEffect(pos, color))

    def spawn_dust_effect(self, pos, color=(180, 180, 180)):
        self.particle_effects.append(DustParticleEffect(pos, color))

    def trigger_shake(self, frames=5, magnitude=5):
        self.shake_frames = frames
        self.shake_magnitude = magnitude

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

        for effect in self.particle_effects[:]:
            effect.update()
            if not effect.active:
                self.particle_effects.remove(effect)
        
        self.info_ui.update()

    def _update_screen(self):
        self.draw_surface.fill(settings.BACKGROUND_COLOR)
        self.paddle.draw(self.draw_surface)
        self.ball.draw(self.draw_surface)
        self.bricks.draw(self.draw_surface)
        for effect in self.particle_effects:
            effect.draw(self.draw_surface)

        self.info_ui.draw(self.draw_surface)

        offset_x = offset_y = 0
        if self.shake_frames > 0:
            offset_x = random.randint(-self.shake_magnitude, self.shake_magnitude)
            offset_y = random.randint(-self.shake_magnitude, self.shake_magnitude)
            self.shake_frames -= 1

        self.screen.fill(settings.BACKGROUND_COLOR)
        self.screen.blit(self.draw_surface, (offset_x, offset_y))
        pygame.display.flip()
        self.clock.tick(settings.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
