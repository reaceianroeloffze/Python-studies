# Call the external pygame module.
import pygame

# Import Network class from network.py file.
from network import Network

import pickle

pygame.font.init()

width = 800
height = 800

def main():
    
    # Set the size of the game window by specifying
    # a width and a height.
    win = pygame.display.set_mode((width, height))
    
    # Give the game window a name.
    pygame.display.set_caption('Rock, Paper, Scissors.')
    
    runtime = True
    
    # Connect client to server and store connection.
    network = Network()
    
    # Call the get_player from the network file and store it.
    plyr = network.get_player()
    
    # Set the framerate [fps (frames per second)]
    clock = pygame.time.Clock()
    
    # Set a loop to continously run while the
    # program is running to check for collisions,
    # send server information, events, etc.
    while runtime:
        
        # Loop through the framerate
        clock.tick(90) # specify the framerate in the perentheses.
        
        
        plyr_2 = network.send(plyr)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtime = False
                pygame.quit

        # Call the move function.
        plyr.move()
        
        # Call the redraw_window function.
        redraw_window(win, plyr, plyr_2)

class Button:
    def __init__(self, text, x, y, colour):
        '''
        '''

def redraw_window(win, player, player_2):
    '''
    Change the property of our gaming
    window like colour and size.
    
    Parameters:
        win:
            the game window to be redrawn.
        player:
            The first character that will be drawn
            in the game window.
        player_2:
            The second character that will be drawn
            in the game window.
    Return: Nothing.
    '''
    # Colour the window.
    win.fill((156,134,205))
    
    # Draw the characters onto the window.
    player.draw_character(win)
    player_2.draw_character(win)
    
    # Apply the changes.
    pygame.display.update()
        

if __name__ == '__main__':
    main()