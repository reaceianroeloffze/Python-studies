import pygame

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