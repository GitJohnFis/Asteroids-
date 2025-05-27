import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """
    Base class for circular game objects.
    Provides position, velocity, radius, and collision detection.
    """

    def __init__(self, x, y, radius):
        """
        Initialize a CircleShape object.

        Args:
            x (float): The x-coordinate of the object's position.
            y (float): The y-coordinate of the object's position.
            radius (float): The radius of the object.
        """
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """
        Draw the object on the given screen.
        Subclasses should override this method.

        Args:
            screen (pygame.Surface): The surface to draw the object on.
        """
        # sub-classes must override
        pass

    def update(self, dt):
        """
        Update the object's state.
        Subclasses should override this method.

        Args:
            dt (float): Time elapsed since the last update.
        """
        # sub-classes must override
        pass

    def collides_with(self, other):
        """
        Check if this object collides with another CircleShape.

        Args:
            other (CircleShape): Another circular object to check collision with.

        Returns:
            bool: True if the objects are colliding, False otherwise.
        """
        return self.position.distance_to(other.position) <= self.radius + other.radius
        # check if the distance between the two objects is less than or equal to the sum of their radii
        # if so, they are colliding
