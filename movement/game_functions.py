import pygame, sys
from pygame.locals import *

def check_events(ship):
  #Responde to key presses and mouse events
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()
    #Here are the commands to move the ship. I made it so that it can move in all four 
    #directions. Review the code here, for KEYDOWN and then for KEYUP to understand 
    #What is happening.
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        ship.moving_right = True 
      elif event.key == pygame.K_LEFT:
        ship.moving_left = True
      elif event.key == pygame.K_UP:
        ship.moving_up = True
      elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    #KEYUP stops the movement of the ship. Head over to ship.py to see more about what is going on.
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        ship.moving_right = False
      elif event.key == pygame.K_LEFT:
        ship.moving_left = False
      elif event.key == pygame.K_UP:
        ship.moving_up = False
      elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_screen(ai_settings, screen, ship):
  #Update images on the screen and flip to the new screen 
  screen.fill(ai_settings.bg_color)
  ship.blitme() 

  #Make the most recently drawn screen visible 
  pygame.display.flip()