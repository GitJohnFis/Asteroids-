import pygame 
import random
from constants import *
from circleshape impirt CircleShape



class asteroid(pygame.sprite.Sprite):
    """
    Represents an asteroid in the game. Handles drawing, updating position, and splitting into smaller asteroids.
    """

    def __init__(self, x, y, radius):
        """
        Initialize an asteroid object.

        Args:
            x (float): The x-coordinate of the asteroid's position.
            y (float): The y-coordinate of the asteroid's position.
            radius (float): The radius of the asteroid.
        """
        super().__init__(x, y, radius)

        def draw(self, screen):
            """
            Draw the asteroid on the given screen.

            Args:
                screen (pygame.Surface): The surface to draw the asteroid on.
            """
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

        def update(self, dt):
            """
            Update the asteroid's position based on its velocity and the time delta.

            Args:
                dt (float): Time elapsed since the last update.
            """
            self.position += self.velocity * dt

    def split(self):
        """
        Split the asteroid into smaller asteroids if its radius is above the minimum threshold.
        Removes the current asteroid and spawns two smaller ones with randomized velocities.
        """
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