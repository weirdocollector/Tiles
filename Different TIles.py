import pygame
from pygame.locals import *
from sys import exit
from time import sleep

pygame.init()

# Screen 
s_x = 0
s_y = 0
s_height = 640
s_width = 1280

# Tiles 
t_x = 0
t_y = 0
t_height = 64
t_width = t_height * 2

# Screen Map Origin
s_origin_x = int(s_width/2) - int(t_width/2)                    # Middle X axis
s_origin_y = int(s_height/2) - int(t_height/2) - (t_height*4)   # Middle Y axis - Offset

# Tiles Map
m_tiles =  [[1,1,1,1,1,1,1,1],
            [1,0,0,1,1,0,0,1],
            [1,0,0,1,1,0,0,1],
            [1,0,0,3,3,0,0,1],
            [1,0,0,4,4,0,0,1],
            [1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,1],
            [1,1,1,0,0,1,1,1]]
m_side = len(m_tiles)

screen = pygame.display.set_mode((s_width, s_height), 0, 32)
pygame.display.set_caption('Tiles Test')
tile_0 = pygame.image.load('Flat_Tile.png').convert_alpha() 
tile_1 = pygame.image.load('Cube.png').convert_alpha()
tile_2 = pygame.image.load('Half_Cube.png').convert_alpha()
tile_3 = pygame.image.load('Slope_S.png').convert_alpha()
tile_4 = pygame.image.load('Slope_End_S.png').convert_alpha()
tiles = [tile_0, tile_1, tile_2, tile_3, tile_4]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    for m_x in range(m_side):
        for m_y in range(m_side):
            s_x = (m_x - m_y) * int(t_width/2) + s_origin_x
            s_y = (m_x + m_y) * int(t_height/2) + s_origin_y
            screen.blit(tiles[m_tiles[m_x][m_y]],(s_x, s_y))
            # sleep(0.2)
            # pygame.display.update()

    # s_map_x = (x / int(t_width/2) + y / int(t_height/2))/2 
    # s_map_y = (y / int(t_height/2) + x / int(t_width/2))/2

    pygame.display.update()