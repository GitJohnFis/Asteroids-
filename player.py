import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    """
    Player class representing the user's ship.
    Handles movement, rotation, shooting, and power-up effects.
    """

    def __init__(self, x, y):
        """
        Initialize the Player object.

        Args:
            x (float): The x-coordinate of the player's starting position.
            y (float): The y-coordinate of the player's starting position.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.position = pygame.Vector2(x, y)
        self.shield_active = False
        self.shield_timer = 0
        self.speed_boost = 1.0

    def draw(self, screen):
        """
        Draw the player ship as a triangle on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the player on.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        """
        Calculate the vertices of the player's triangular ship.

        Returns:
            list[pygame.Vector2]: List of three points representing the triangle.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        """
        Update the player's state based on input and timers.

        Args:
            dt (float): Time elapsed since the last update.
        """
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        """
        Fire a shot if the shoot timer allows.
        """
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_RATE
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def rotate(self, dt):
        """
        Rotate the player ship.

        Args:
            dt (float): Time elapsed since the last update.
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """
        Move the player ship forward or backward.

        Args:
            dt (float): Time elapsed since the last update.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * self.speed_boost * dt

    def activate_shield(self):
        """
        Activate the player's shield for a set duration.
        """
        self.shield_active = True
        self.shield_timer = PLAYER_SHIELD_TIME

    def activate_speed_boost(self):
        """
        Activate a temporary speed boost for the player.
        """
        self.speed_boost = SPEED_BOOST_MULTI
        pygame.time.set_timer(pygame, SPEED_BOOST_DURATION * 1000, 1)

    def deactivate_speed_boost(self):
        """
        Deactivate the speed boost and reset to normal speed.
        """
        self.speed_boost = 1.0
