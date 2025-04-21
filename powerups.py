class PowerUp:
    def __init__(self, x, y, power_type):
        self.x = x
        self.y = y
        self.radius = 15  # smaller than asteroids
        self.power_type = power_type  # "shield", "speed", etc
        # Load appropriate sprite based on type
        
    def update(self):
        # Movement logic - maybe they float around?
        
    def draw(self, screen):
        # Draw the power-up sprite