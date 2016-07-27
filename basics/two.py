#This file will contain basic information how to set up a basic screen for the game.
import pygame


pygame.init() 
screen = pygame.display.set_mode((600, 600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    #This line is what will draw a rectangle to the screen. 
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()


#Now we will example the rect line more closely here:
#pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
#Notice that this line takes three arguments.

#screen => This is the argument that set up the width. It is where the rect will appear.

#The second argument, (0, 128, 255), is what determines the color in RGB format. 

#The third argument is made up of four numbers. The first two re the location of where the top
#left point of the rectangle will appear. Please remember that 0,0 is in the top left of your screen. 
#60 and 60 are the width and height of the Rect. 
