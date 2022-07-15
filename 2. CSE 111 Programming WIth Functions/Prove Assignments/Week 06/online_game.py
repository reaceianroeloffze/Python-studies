# Call the external pygame module.
import pygame

# Import Network class from network.py file.
from network import Network

width = 600
height = 600

# Store the current number of clients in a variable.
client_number = 0

def main():
    
    # Set the size of the game window by specifying
    # a width and a height.
    win = pygame.display.set_mode((width, height))
    
    # Give the game window a name.
    pygame.display.set_caption('Game')
    
    runtime = True
    
    # Connect client to server and store connection.
    network = Network()
    
    # Call the get_position function to get the
    # starting position of every character who joins
    # the game and store it in a variable.
    starting_position = read_position(network.get_position())
    
    # Create playable characters.
    character = Player(starting_position[0], starting_position[1], 75, 100, (0, 50, 255))
    character_2 = Player(0, 0, 75, 100, (50, 170, 255))
    
    # Set the framerate [fps (frames per second)]
    clock = pygame.time.Clock()
    
    # Set a loop to continously run while the
    # program is running to check for collisions,
    # send server information, events, etc.
    while runtime:
        
        # Get position integers for second player.
        character_2_position = read_position(network.send(make_position((character.x, character.y))))
        
        # Store the 2 positions of the second character.
        character_2.x = character_2_position[0]
        character_2.y = character_2_position[1]
        character_2.update()
        
        # Loop through the framerate
        clock.tick(90) # specify the framerate in the perentheses.
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtime = False
                pygame.quit

        # Call the move function.
        character.move()
        
        # Call the redraw_window function.
        redraw_window(win, character, character_2)

# Set a class for the player/character.
class Player():
    
    def __init__(self, x, y, width, height, colour):
        '''
        Define and initialise the specifics for drawing 
        the character.
        
        parameters:
        self:
            The character.
        x:
            placement of the character along the x-axis.
        y:
            Placement of the character along the y-axix.
        width:
            width of the drawn character.
        height:
            height of the drawn character.
        colour:
            colour of the drawn character.
        '''
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.vel = 6 # Sets the movement speed of the character.
        
    def draw_character(self, win):
        '''
        Draw a rectangular character.
        
        Parameters:
            self:
                The Character.
            win:
                The window into which the character will
                be drawn.
        '''
        # Draw a rectangular character.
        pygame.draw.rect(win, self.colour, self.rect)

    def process_character_move(self, keys):
        '''
        Determine the keys for the movement of 
        the character on screen.
        
        Parameters:
            self:
                The character.
        '''

        # Left arrow key
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            
        # Right arrow key
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        
        # Co-ordinate system in pygame has its
        # origin at the top left corner of the
        # window making y positive downwards,
        # which means that upwards is negative.
        
        # Up arrow key
        if keys[pygame.K_UP]:
            self.y -= self.vel
        
        # Down arrow key
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            
        self.update()
        
    def update(self):  
        self.rect = (self.x, self.y, self.width, self.height)
        
    def move(self):
        '''
        Determine the keys for the movement of 
        the character on screen.
        
        Parameters:
            self:
                The character.
        '''
        # This will return a dictionary of all keyboard
        # keys that will either be numbered 0 or 1. 1 means
        # a key is being pressed and 0 means no key is being
        # pressed.
        
        keys = pygame.key.get_pressed()
        self.process_character_move(keys)

def make_position(tup):
    '''
    Convert a tuple of numerical values into
    a string.
    
    Parameters:
        tup:
            The tuple containing the Integers.
        
    Return:
        A string.
    '''
    
    return str(tup[0]) + ',' + str(tup[1])
   
def read_position(string):
    '''
    Read numerical values from a string tuple
    and return them as integers.
    
    Parameters:
        string: The tuple containing the
            numerical values.
    
    return:
        Integers.
    '''
    
    string = string.split(',')
    return int(string[0]), int(string[1])

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