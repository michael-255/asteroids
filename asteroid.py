import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            dir1 = self.velocity.rotate(angle)
            dir2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(*self.position, new_radius)
            a1.velocity = dir1 * 1.2
            a2 = Asteroid(*self.position, new_radius)
            a2.velocity = dir2 * 1.2
        self.kill()
