#####################
# Spinning Top Sprite
#####################

# Import libraries
import pygame, sys, random

# Define Spinning Top sprite as instance of Pygame Sprite class
class Spinning_Top(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/Spin_Top_1.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

# Define Jewel sprite as instance of Pygame Sprite class
class Jewel(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Assets/Jewel.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():

    pygame.init()

    # Set screen
    screen_width = 1280
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Spinning Top Sprite")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create Spinning Top sprite group (needed to display the sprite)
    spinning_top = Spinning_Top()
    spinning_top_group = pygame.sprite.Group()
    spinning_top_group.add(spinning_top)

    # Create Jewel sprite group (needed to display the sprite)
    jewel_group = pygame.sprite.Group()
    for jewel in range(20):
        new_jewel = Jewel(random.randrange(0, screen_width), random.randrange(0, screen_height))
        jewel_group.add(new_jewel)

    # Loop until the user clicks the close button.
    done = False

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        
        # Draw sprite groups
        jewel_group.draw(screen)
        spinning_top_group.draw(screen)
        spinning_top_group.update()
        print(spinning_top.rect.bottom)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # If the Spinning Top collides with one Jewel remove it from the screen
        pygame.sprite.spritecollide(spinning_top, jewel_group, True)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
