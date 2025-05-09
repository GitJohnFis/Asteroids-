import pygame 
import random
from constants import *
from circleshape import CircleShape



class asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

        def update(self, dt):
            self.position += self.velocity * dt

    def split(self):
        self.kill()
        # split the asteroid into two medium asteroids

        # split the asteroid into two MED asteroids THEN EACH OF THOSE INTO TWO SMALL asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

            #randomize the angle of the split
            random_angle = random.uniform(20, 50)



            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)

            new_self = self.radius - ASTEROOID_MIN_RADIUS
            asteroid.Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = a * 1.2
            asteroid.Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = a * 1.2
        # spawn two smaller asteroids
            self.spawn(self.radius / 2, self.position, self.velocity)
            self.spawn(self.radius / 2, self.position, self.velocity)