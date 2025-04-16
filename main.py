import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *

# this allows us to use the constants or magic #'s
def main():
    #print startup message
    pygame.init()
    #initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create a screen object with the specified width and height

    while True:
        # run the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # check for quit event
                pygame.quit()
                # quit the game
                return
        screen.fill(black)
        # fill the screen with black color
        pygame.display.flip()
        # update the display

# Add statement to show the game has begun in a pythonic way
if __name__ == "__main__":
    main()