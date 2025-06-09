# settings.py

import random
# Global settings for the BrickBreaker game

# Colors
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = BLACK
# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_SPEED = 10

# Ball settings
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = -5

# Brick settings
BRICK_PADDING = 5 
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_COLOR = GREEN
HORIZONTAL_BRICKS_PADDING = 20
BRICKS_DISTANCE_TO_BUTTOM = 100
# Other settings
LIVES = 3
SCORE = 0