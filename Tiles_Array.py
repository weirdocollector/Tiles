import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Screen 
s_height = 640
s_width = 640

# Tiles 
t_x = 0
t_y = 0
t_height = 64
t_width = 64

screen = pygame.display.set_mode((s_width, s_height), 0, 32)
pygame.display.set_caption('Tiles Test')
tile = pygame.image.load('Assets\Tile.png').convert()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    for count_x in range(int(s_width/t_width)):
        for count_y in range(int(s_height/t_height)):
            if count_x == count_y:
                screen.blit(tile,(count_x*t_width, count_y*t_height))

    pygame.display.update()