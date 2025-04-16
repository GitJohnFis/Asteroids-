import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file



from constants import *

# this allows us to use the constants or magic #'s
def main():
    pygame.init()
    #initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create a screen object with the specified width and height
    clock = pygame.time.Clock()
    dt = 0
    while True:
        # run the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# quit the game
                return
        screen.fill("black") # fill the screen with black color
        pygame.display.flip()
        # update the display
        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000
# Add statement to show the game has begun in a pythonic way
if __name__ == "__main__":
    main()