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

    #These properties are all set to false. When the key is pressed down they will be turned true. 
    self.moving_right = False 
    self.moving_left = False
    self.moving_up = False
    self.moving_down = False

  #Movement of ship by a certain amount for the key presses. You are able to change the value to move the
  #ship faster or slower. 
  def update(self):
    #Updating ships movement I also added in code that will prevent the ship from leaving the screen. 
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.centerx += 7
    if self.moving_left and self.rect.left > 0:
      self.rect.centerx -= 7
    if self.moving_up and self.rect.top > 0:
      self.rect.centery -= 7
      #Please note that I used 750 here because the screen height is 800. So, nothing else was working 
      #so I put in a value and found that 750 worked perfectly. (I started checking with 600)
    if self.moving_down and self.rect.bottom < 750:
      self.rect.centery += 7


  def blitme(self):
    #This is where the ship actually gets drawn. 
    self.screen.blit(self.image, self.rect)
