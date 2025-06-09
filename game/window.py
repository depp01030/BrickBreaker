import pygame

class GameWindow:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = None
        self.clock = pygame.time.Clock()

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def update(self):
        pygame.display.flip()
        self.clock.tick(60)

    def clear(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black

    def close(self):
        pygame.quit()