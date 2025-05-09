"""Main module for Asteroids.

Handles game setup, main loop, and user input.
"""

import sys
import random
import pygame

# this allows us to use code from
# the open-source pygame library

from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
from powerups import PowerUp


# this allows us to use the constants or magic #'s
def main():
    """Main game loop for Asteroids."""
    pygame.init()
    # initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create a screen object with the specified width and height
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    # create a group for updatable objects

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    PowerUp.containers = (powerups, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        # run the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit the game
                return
            elif event.type == SPEED_BOOST_END_EVENT:
                player.deactivate_speed_boost()
        updatable.update(dt)
        # update the game state

        # check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                sys.exit()

        # check for collisions between the player and powerups
        for power_up in powerups:
            if player.collides_with(power_up):
                if power_up.power_type == "shield":
                    player.activate_shield()
                elif power_up.power_type == "speed":
                    player.activate_speed_boost()
                power_up.kill()  # powerups.remove(power_up)

        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    # 20% chance to spawn a power_up where asteroid was destroyed
                if random.random() <= 0.2:
                    power_type = random.choice(["shield", "speed"])
                    PowerUp(asteroid.position.x, asteroid.position.y, power_type)  #
                    """
                        unecessary to append manully to the group
                        power_up should NOT spawn after every asteroid
                        is destroyed but linked to the asteriod-shot pair 
                        """

        screen.fill("black")
        """
         fill the screen with black color
        """
        for obj in drawable:
            obj.draw(screen)
        player.draw(screen)  # draw the player
        pygame.display.flip()
        # update the display
        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000


# Add statement to show the game has begun in a pythonic way
if __name__ == "__main__":
    main()
