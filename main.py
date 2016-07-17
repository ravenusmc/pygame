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

  bg_color = (100,30,200)

  #Starting the main game loop:
  while True: 
    #Watching for keyboard and mouse events. 
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()


    screen.fill(bg_color)
    #This line constantly updates the screen. 
    pygame.display.flip()

run_game()