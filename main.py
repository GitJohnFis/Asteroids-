import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file


from player import Player
from constants import *

# this allows us to use the constants or magic #'s
def main():
    pygame.init()
    #initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create a screen object with the specified width and height
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

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