import pygame
import random
import math

class Particle:
    def __init__(self, pos, color, angle=None, speed_range=(1, 3)):
        self.x, self.y = pos
        self.radius = random.randint(2, 4)
        self.angle = angle if angle is not None else random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(*speed_range)
        self.color = color
        self.lifetime = random.randint(20, 40)

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.lifetime -= 1
        if self.radius > 0:
            self.radius -= 0.05

    def draw(self, surface):
        if self.lifetime > 0 and self.radius > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

class ParticleEffect:
    def __init__(self, pos, color, amount=20):
        self.particles = [Particle(pos, color) for _ in range(amount)]
        self.active = True

    def update(self):
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.lifetime > 0 and p.radius > 0]
        if not self.particles:
            self.active = False

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)


class DustParticleEffect(ParticleEffect):
    """Particles falling downward to simulate debris/dust."""

    def __init__(self, pos, color, amount=15):
        super().__init__(pos, color, amount)
        # Override particle directions so that dust falls downward
        for p in self.particles:
            downward_angle = random.uniform(math.pi * 0.7, math.pi * 1.3)
            p.angle = downward_angle
            p.speed = random.uniform(1, 2)
