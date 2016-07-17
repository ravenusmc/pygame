#Ensure that pygame is imported to get access to it. 
import pygame, sys
from pygame.locals import *

def run_game():

  #This line inits background settings for pygame to work correctly. 
  #It creates a screen object. 
  pygame.init()

  #Sets the screen size. 
  screen = pygame.display.set_mode((600, 600))
  #Here we are setting the title to the screen that was declared on the above line. 
  pygame.display.set_caption('Hello World!')

  #To change the color, of the background of the display, create a variable and set it 
  #equal to the colors you want to use using rgb color guides. 
  bg_color = (100,30,200)

  #Starting the main game loop:
  while True: 
    #Watching for keyboard and mouse events. 
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

    #To actually change the color of the background you have to use screen.fill and send in your 
    #variable that was set equal to some colors. 
    screen.fill(bg_color)
    #This line constantly updates the screen. 
    pygame.display.flip()

run_game()