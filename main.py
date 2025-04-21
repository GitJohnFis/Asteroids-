import pygame
# this allows us to use code from
# the open-source pygame library


from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# this allows us to use the constants or magic #'s
def main():
    pygame.init()
    #initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create a screen object with the specified width and height
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # create a group for updatable objects

    
    Asteroid.containerts = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    players.containers = (updatable, drawable)



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)

    dt = 0
    while True:
        # run the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# quit the game
                return
        
        updatable.update(dt)
        # update the game state

        # check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(player):
                print("Game Over!")
                sys.exit()

                for shot in shots:
                        if shot.collides_with(shot):
                            shot.kill()
                            asteroid.kill()

        screen.fill("black") # fill the screen with black color
        for obj in drawable:
            obj.draw(screen)
        player.draw(screen) #draw the player
        pygame.display.flip()
        # update the display
        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000
# Add statement to show the game has begun in a pythonic way
if __name__ == "__main__":
    main()