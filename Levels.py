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
s_origin_x = s_width //2 - t_width //2                      # Middle X axis
s_origin_y = s_height //2 - t_height //2 - t_height*3.5     # Middle Y axis - Offset

# Full Screen Dictionary 
map_screen ={}

for level in range (8): # Initialize eight map screen levels
    map_screen[level]= []

# Tiles Map
m_sides = 8
m_tiles = [None] * 8 # Level Tiles

m_tiles[0]= [[1,1,1,1,1,1,1,1], 
             [1,0,0,1,1,0,0,1],
             [1,0,0,3,3,0,0,1],
             [1,0,0,2,2,0,0,1],
             [1,0,0,4,4,0,0,1],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [1,1,1,0,0,1,1,1]]

m_tiles[1]= [[1,5,5,5,5,5,5,1],
             [5,5,5,5,5,5,5,5],
             [5,5,5,5,5,5,5,5],
             [5,5,5,5,5,5,5,5],
             [5,5,5,5,5,5,5,5],
             [5,5,5,5,5,5,5,5],
             [5,5,5,5,5,5,5,5],
             [1,5,5,5,5,5,5,1]]

# for key in range (0):
map_screen[0] = m_tiles[0]
map_screen[1] = m_tiles[1]

screen = pygame.display.set_mode((s_width, s_height), 0, 32)
pygame.display.set_caption('Assets/Tiles Test')
tile_0 = pygame.image.load('Assets/Flat_Tile.png').convert_alpha() 
tile_1 = pygame.image.load('Assets/Cube.png').convert_alpha()
tile_2 = pygame.image.load('Assets/Half_Cube.png').convert_alpha()
tile_3 = pygame.image.load('Assets/Slope_S.png').convert_alpha()
tile_4 = pygame.image.load('Assets/Slope_End_S.png').convert_alpha()
tile_5 = pygame.image.load('Assets/Empty_Tile.png').convert_alpha()
tiles = [tile_0, tile_1, tile_2, tile_3, tile_4, tile_5]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    for m_z in range(2):
        for m_x in range(m_sides):
            for m_y in range(m_sides):
                s_x = (m_x - m_y) * t_width //2 + s_origin_x 
                s_y = (m_x + m_y) * t_height //2 + (s_origin_y- t_height * m_z)
                screen.blit(tiles[map_screen[m_z][m_x][m_y]],(s_x, s_y)) 
                # sleep(0.2)
                # pygame.display.update()

    # s_map_x = (x / int(t_width/2) + y / int(t_height/2))/2 
    # s_map_y = (y / int(t_height/2) + x / int(t_width/2))/2

    pygame.display.update()