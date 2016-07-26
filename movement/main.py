import pygame, sys
from pygame.locals import *


#I am importing the ship class from the ship.py file. 
from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption('Learn PyGame!')

  #This is what will make a ship object:
  ship = Ship(screen)

  while True: 
    gf.check_events(ship)
    gf.update_screen(ai_settings, screen, ship)
    ship.update()
    

run_game()