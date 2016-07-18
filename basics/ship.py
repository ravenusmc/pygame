#Look out for pygame.error: File is not a Windows BMP file error!
import pygame 

class Ship():

  def __init__(self, screen):
    #inits the ship and creates starting position. 
    self.screen = screen

    #Load the ship image. It is stored as self.image.
    self.image = pygame.image.load('images/ship5.bmp')
    #The self.rect() method treats the image as a rectangle. 
    #Also, working with a rectangle allows one to use x and y coordinates of the top, bottom, left
    #right edges of the rectangle as well as the center. 
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    #Start the ship at the bottom center. 
    self.rect.centerx = self.screen_rect.centery
    self.rect.bottom = self.screen_rect.bottom

  def blitme(self):
    #This is where the ship actually gets drawn. 
    self.screen.blit(self.image, self.rect)