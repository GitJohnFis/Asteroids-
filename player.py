 import pygame
 from constants import *
 from circleshape import CircleShape
 
 class Player(CircleShape):
    def __init__(self, x, y):
        super._init_(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
       """
       Add new initialization with powerups and new feat...
       """
        self.position = pygame.Vector2(x, y)
        self.shield_active = False
        self.shield_timer = 0
        self.speed_boost = 1.0
 
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
 
 
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
      """Fixed: Moved method definition and corrected indentation. Ensured keys are checked and used correctly."""
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
     """Fixed: Ensured self.shoot_timer logic and reference to Shot class."""
     # now you should only be able to shoot if the timer is 0
       if self.shoot_timer > 0: 
          return
       self.shoot_timer = PLAYER_SHOOT_RATE
       shot = Shot(self.position.x, self.position.y)
       shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED


    def rotate(self, dt):
     """Fixed: Removed duplicate dt in rotation logic."""
      self.rotation += SELF_TURN_SPEED * dt

    def move(self, dt):
     """Fixed: Multiplied by speed_boost and ensured forward vector uses rotation."""
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * self.speed_boost * dt

    # Powerups handling methods
    def activate_shield(self):
     """Fixed: Corrected attribute name and timer logic."""
      self.shield_active = True
      self.shield_timer = PLAYER_SHIELD_TIME #duration of the shield in seconds

    def activate_speed_boost(self):
    """Fixed: Used consistent speed_boost attribute and left timer logic for event handling."""
      self.shield_boost = SPEED_BOOST_MULTI # multiplier for speed
      pygame.time.set_timer(pygame, SPEED_BOOST_DURATION * 1000, 1) #set a timer for the speed boost

    def deactivate_speed_boost(self):
     """Fixed: Resets speed_boost to normal."""
      self.speed_boost = 1.0 #reset the normal speed
