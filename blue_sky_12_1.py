"""Make a blue screen."""
import pygame
import sys

#initialize pygame
pygame.init()

#define screen size 
screen = pygame.display.set_mode((1200, 800))

#define screen color
bg_color = (0, 0, 230)

#continuosly run until window is closed
while True:
    #if event is quit then close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #fill screen with color and update. 
    screen.fill(bg_color)
    # Make the most recently drawn screen visible -- if not included the white background will not update to bg_color value. 
    pygame.display.flip()
