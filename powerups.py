import pygame
import random
from constants import *

class PowerUp(pygame.sprite.Sprite):
    containers = None

    def __init__(self, x, y, power_type):
        pygame.sprite.Sprite.__init__(self)
        self.add(self.containers)
        self.position = pygame.Vector2(x, y)
        self.power_type = power_type
        # Create a surface for the power-up
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        if power_type == "shield":
            # Draw a blue shield power-up
            pygame.draw.circle(self.image, "blue", (10, 10), 10)
        elif power_type == "speed":
            # Draw a green speed power-up
            pygame.draw.circle(self.image, "green", (10, 10), 10)
        
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = 10  # For collision detection

    def update(self, dt):
        # Make the power-up float or pulse for visual effect
        # You could add movement or animation here
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)