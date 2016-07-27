#Everything in this file will be able getting an image to display to the screen. 

#Please note that I have only added comments above new lines. 

import pygame, sys
from pygame.locals import *

#I am importing the ship class from the ship.py file. 
from ship import Ship

def run_game():

  pygame.init()

  screen = pygame.display.set_mode((600, 600))
  pygame.display.set_caption('Learn PyGame!')

  #This is what will make a ship object:
  ship = Ship(screen)


  bg_color = (255,255,255)

  while True: 
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

    screen.fill(bg_color)
    #Calling the ship object to appear on the screen. This line MUST come after the screen.fill line.
    #If it does not come after then the background will cover up the image. 
    ship.blitme() 
    pygame.display.flip()

run_game()