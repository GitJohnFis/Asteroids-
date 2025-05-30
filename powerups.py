class PowerUp:
    """
    Represents a power-up item in the game.
    Power-ups can grant temporary abilities such as shields or speed boosts.
    """

    def __init__(self, x, y, power_type):
        """
        Initialize a PowerUp object.

        Args:
            x (float): The x-coordinate of the power-up's position.
            y (float): The y-coordinate of the power-up's position.
            power_type (str): The type of power-up ("shield", "speed", etc).
        """
        self.x = x
        self.y = y
        self.radius = 15  # smaller than asteroids
        self.power_type = power_type  # "shield", "speed", etc
        # Load appropriate sprite based on type
        
    def update(self):
        """
        Update the power-up's state.
        Handles movement or animation if needed.
        """
        # Movement logic - maybe they float around?
        
    def draw(self, screen):
        """
        Draw the power-up on the given screen.

        Args:
            screen (pygame.Surface): The surface to draw the power-up on.
        """
        # Draw the power-up sprite