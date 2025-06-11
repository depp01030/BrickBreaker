import pygame
import random
from game import settings
from game.particle_effect import ParticleEffect, DustParticleEffect


class Brick:
    """Base brick class with health and destruction logic."""

    def __init__(self, game, row, col, x, y, color, health=10, destructible=True):
        self.game = game
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.color = color
        self.max_health = health
        self.health = health
        self.destructible = destructible
        self.rect = pygame.Rect(x, y, settings.BRICK_WIDTH, settings.BRICK_HEIGHT)

    def hit(self, damage):
        if not self.destructible:
            return False
        self.health -= damage
        if self.health <= 0:
            self.destroy()
            return True
        return False

    def destroy(self):
        if hasattr(self.game, "spawn_particle_effect"):
            self.game.spawn_particle_effect(self.rect.center, self.color)
            if hasattr(self.game, "spawn_dust_effect"):
                self.game.spawn_dust_effect(self.rect.midbottom)
        self.game.bricks.remove_brick(self)

    def draw(self, surface):
        # Adjust color intensity based on remaining health
        ratio = self.health / self.max_health if self.max_health else 1
        color = tuple(int(c * ratio) for c in self.color)
        pygame.draw.rect(surface, color, self.rect, border_radius=2)
        # Draw simple cracks
        if ratio < 1.0:
            crack_lines = int((1 - ratio) * 3)
            for _ in range(crack_lines):
                start = (
                    self.rect.left + random.randint(0, self.rect.width),
                    self.rect.top + random.randint(0, self.rect.height),
                )
                end = (
                    self.rect.left + random.randint(0, self.rect.width),
                    self.rect.top + random.randint(0, self.rect.height),
                )
                pygame.draw.line(surface, (30, 30, 30), start, end, 1)


class ThickBrick(Brick):
    def __init__(self, game, row, col, x, y):
        super().__init__(game, row, col, x, y, settings.BLUE, health=30)


class ExplosiveBrick(Brick):
    def destroy(self):
        super().destroy()
        neighbors = self.game.bricks.get_adjacent_bricks(self)
        random.shuffle(neighbors)
        count = random.randint(1, min(3, len(neighbors)))
        for b in neighbors[:count]:
            b.hit(b.health)


class IndestructibleBrick(Brick):
    def __init__(self, game, row, col, x, y):
        super().__init__(game, row, col, x, y, (150, 150, 150), health=1, destructible=False)

    def hit(self, damage):
        # Cannot be destroyed
        return False


class Bricks:
    def __init__(self, game):
        self.game = game
        self.bricks = []
        self.rows, self.cols = self._calculate_bricks_rows_and_cols()
        self.create_bricks()

    def _calculate_bricks_rows_and_cols(self):
        padding = settings.BRICK_PADDING
        cols = (settings.SCREEN_WIDTH - padding) // (settings.BRICK_WIDTH + padding)
        rows = (settings.SCREEN_HEIGHT - settings.BRICKS_DISTANCE_TO_BUTTOM - padding) // (
            settings.BRICK_HEIGHT + padding
        )
        return rows, cols

    def create_bricks(self):
        padding = settings.BRICK_PADDING
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * (settings.BRICK_WIDTH + padding) + padding
                y = row * (settings.BRICK_HEIGHT + padding) + padding

                # decide brick type based on row for variety
                if row % 6 == 0:
                    brick = IndestructibleBrick(self.game, row, col, x, y)
                elif row % 6 == 1:
                    brick = ThickBrick(self.game, row, col, x, y)
                elif row % 6 == 2:
                    brick = ExplosiveBrick(self.game, row, col, x, y)
                else:
                    brick = Brick(self.game, row, col, x, y, settings.get_random_color())
                self.bricks.append(brick)

    def get_adjacent_bricks(self, brick):
        neighbors = []
        for b in self.bricks:
            if b is brick:
                continue
            if abs(b.row - brick.row) <= 1 and abs(b.col - brick.col) <= 1:
                neighbors.append(b)
        return neighbors

    def remove_brick(self, brick):
        if brick in self.bricks:
            self.bricks.remove(brick)

    def draw(self, surface):
        for brick in self.bricks:
            brick.draw(surface)

