#This file will contain basic information how to set up a basic screen for the game.
import pygame

#This line initializes all the modules required for PyGame.
pygame.init()
#This creates the screen object. One can change the width and height by changing the numbers. 
screen = pygame.display.set_mode((600, 600))
done = False

while not done:
    #This line empties the event queue
    for event in pygame.event.get():
        #pygame.QUIT is what allows you to quit the game when you click the x in the upper left 
        #corner of the screen
        if event.type == pygame.QUIT:
            done = True
    #This line is needed to make any update to the screen   
    pygame.display.flip()