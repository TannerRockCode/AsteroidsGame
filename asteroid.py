import pygame
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid_velocity_vector1 = self.velocity.rotate(random_angle)
        asteroid_velocity_vector2 = self.velocity.rotate(-random_angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        x = self.position[0]
        y = self.position[1]
        small_asteroid1 = Asteroid(x, y, new_radius)
        small_asteroid2 = Asteroid(x, y, new_radius)
        small_asteroid1.velocity = asteroid_velocity_vector1 * 1.2
        small_asteroid2.velocity = asteroid_velocity_vector2 * 1.2

    
        
        

