# BrickBreaker

import pygame
from game.app import Game

def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()