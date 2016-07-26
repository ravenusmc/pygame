#Look out for pygame.error: File is not a Windows BMP file error!
import pygame 

class Ship():

  def __init__(self, screen):
    #inits the ship and creates starting position. 
    self.screen = screen

    #Load the ship image. It is stored as self.image.
    self.image = pygame.image.load('../basics/images/ship5.bmp')

    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.center = self.screen_rect.center

    self.moving_right = False 
    self.moving_left = False
    self.moving_up = False

  def update(self):
    #Updating ships movement 
    if self.moving_right:
      self.rect.centerx += 7
    if self.moving_left:
      self.rect.centerx -= 7
    if self.moving_up:
      self.rect.centery -= 7


  def blitme(self):
    #This is where the ship actually gets drawn. 
    self.screen.blit(self.image, self.rect)
