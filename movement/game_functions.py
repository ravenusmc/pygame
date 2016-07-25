import pygame, sys
from pygame.locals import *

def check_events(ship):
  #Responde to key presses and mouse events
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        #Moves the ship to the right 
        ship.moving_right = True 

      if event.key == pygame.K_LEFT:
        ship.moving_right == True

    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        ship.moving_right = False

      if event.key == pygame.K_LEFT:
        ship.moving_left == False