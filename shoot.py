import pygame
from constants import *
import circleshape from CircleShape

class Shot(CircleShape):
    """
    Represents a shot fired by the player.
    Handles drawing and updating the shot's position.
    """

    def __init__(self, x, y):
        """
        Initialize a Shot object.

        Args:
            x (float): The x-coordinate of the shot's starting position.
            y (float): The y-coordinate of the shot's starting position.
        """
        super().__init__(x, y, SHOT_radius)

    def draw(self, screen):
        """
        Draw the shot as a circle on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the shot on.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """
        Update the shot's position based on its velocity and the time delta.

        Args:
            dt (float): Time elapsed since the last update.
        """
        self.position += self.velocity * dt
