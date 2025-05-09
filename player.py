import pygame
from asteroid import Asteroid
from circleshape import CircleShape
from constants import *
from shoot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.speed_boost = 1.0
        self.shield_active = False
        self.shield_timer = 0

    def collides_with(self, other):
        # shield logic  check if the shield is active
        if shield.shield_active and isinstance(other, Asteroid):
            self.shield_active = False  # shield gets used up
            return False  # no collision registered
            # this keeps code DRY by reusing the collision logic from circle shape
            # return super().collides_with(other)

            return (
                self.position.distance_to(other.position) <= self.radius + other.radius
            )
        # check if the distance between the two objects is less than or equal to the sum of their radii
        # if so, they are colliding

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

        # apply the speed boost to movements
        actual_speed = self.speed * self.speed_boost

        self.position.y += actual_speed * dt
        self.position.x += actual_speed * dt

        # update the shield timer
        if self.shield_active:
            self.shield_timer -= dt
        if self.shield_timer <= 0:
            self.shield_active = False
            self.shield_timer = 0


def shoot(self):
    # now you should only be able to shoot if the timer is 0
    if self.shoot_timer > 0:
        return


self.shoot_timer = PLAYER_SHOOT_RATE
shot = Shot(self.position.x, self.position.y)
shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


def rotate(self, dt):
    self.rotation += dt * PLAYER_TURN_SPEED * dt


def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt


# Powerups handling methods activation and deactivation
def activate_shield(self):
    self.shield_active = True
    self.shield_timer = PLAYER_SHIELD_TIME  # duration of the shield in seconds


def activate_speed_boost(self):
    self.shield_boost = SPEED_BOOST_MULTI  # multiplier for speed
    pygame.time.set_timer(
        SPEED_BOOST_END_EVENT, int(SPEED_BOOST_RATE * 1000), 1
    )  # set a timer for the speed boost


def deactivate_speed_boost(self):
    self.speed_boost = 1.0  # reset the normal speed
