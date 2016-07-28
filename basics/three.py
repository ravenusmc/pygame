#This file will work a little bit more with shapes and background colors.
import pygame

pygame.init() 
screen = pygame.display.set_mode((600, 600))
done = False

#Setting up background color:
bg_color = (100,200,100)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    #This line will actually create the background color.
    #This line should come first or else it will cover up everything else.
    screen.fill(bg_color)

    #This line is what will draw a rectangle to the screen. 
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(screen, (200, 100, 200), pygame.Rect(400, 400, 60, 60))

    #Drawing a circle:
    pygame.draw.circle(screen, (100, 200, 200), (200,200), 100)

    #Drawing a line: 
    pygame.draw.line(screen, (100, 200, 200), (0, 0), (600, 600), 10)

    #Drawing a polygon
    pygame.draw.polygon(screen, (0,180,0), ((250,100),(300,0),(350,50)))

    pygame.display.flip()


#Please note the parameters:
#one-is the display variable
#two-is the color of the object in RGB format
#three-point list in the following format: ((250,100),(300,0),(350,50)) add more x,y points for more 'points'
#pygame.draw.polygon(surface, color, point_list)