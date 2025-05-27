import pygame
import sys
import random

"""
Main entry point for the Asteroids game.
Handles game initialization, main loop, event processing, updates, and rendering.
"""

from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
from powerups import PowerUp

def main():
    """
    Main function to run the Asteroids game.
    Initializes pygame, sets up game objects and groups, and runs the main game loop.
    """
    pygame.init()
    # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a screen object with the specified width and height
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    # Create groups for updatable and drawable objects

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    PowerUp.containers = (powerups, updatable, drawable)

    # Update and draw power-ups
    for powerup in powerups[:]:
        powerup.update(dt)
        powerup.draw(screen)

    players.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        """
        Main game loop.
        Handles events, updates game state, checks collisions, and renders objects.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game
                return

        updatable.update(dt)
        # Update the game state

        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(player):
                print("Game Over!")
                sys.exit()
        # Check for collisions between the player and powerups
        for powerup in powerups:
            if player.collides_with(powerup):
                if power_up.power_type == "shield":
                    player.activate_shield()
                elif power_up.power_type == "speed":
                    player.activate_speed_boost()
                powerups.remove(powerup)
                # powerup.kill()

        for shot in shots:
            if shot.collides_with(shot):
                shot.kill()
                asteroid.split()

                # 20% chance to spawn a powerup where asteroid was destroyed
                if random.random() <= 0.2:
                    power_type = random.choice(["shield", "speed"])
                    spawn_powerup = PowerUp(asteroid.position.x, asteroid.position.y, power_type)
                    powerups.append(spawn_powerup)  # Add the powerup to the group

        screen.fill("black")  # Fill the screen with black color
        for obj in drawable:
            obj.draw(screen)
        player.draw(screen)  # Draw the player
        pygame.display.flip()
        # Update the display
        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
