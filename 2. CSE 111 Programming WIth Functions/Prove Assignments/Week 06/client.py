# Call the external pygame module.
import pygame

# Import Network class from network.py file.
from network import Network

import pickle

pygame.font.init()

width = 800
height = 800

# Set the size of the game window by specifying
# a width and a height.
win = pygame.display.set_mode((width, height))

# Give the game window a name.
pygame.display.set_caption('Rock, Paper, Scissors.')

def main():
    
    runtime = True
    
    # Store the framerate [fps (frames per second)] in a variable.
    clock = pygame.time.Clock()
    
    # Connect client to server and store connection.
    network = Network()
    
    player = int(network.get_player())
    
    print (f'You are player {player}.')
    
    while runtime:
        
        # Loop through specified framerate.
        clock.tick(90) # specify the framerate in the perentheses.
        
        # Get a game from the server.
        try:
            game = network.send('get')
        except:
            runtime = False
            print ("Couldn't get game.")
            break
        
        # If both players each took their turn,
        # determine winner/loser/tie.
        # print (f'client game: {game}')
        if game.get_player_turns():
            redraw_window(win, game, player)
            pygame.time.delay(500)
            
            # Reset a game after winner/loser/tie have
            # been determined.
            try:
                game = network.send('reset')
            except:
                runtime = False
                print ("Couldn't get game.")
                break
        
        font = pygame.font.SysFont('fanstasy', 90)
        
        if (game.get_winner() == 1 and player == 1) or (game.get_winner() == 0 and player == 0):
            text = font.render('Congratulations! You won!', 1, (150, 150, 70))
        elif game.get_winner() == -1:
            text = font.render('You are tied!', 1, (150, 150, 70))
        else:
            text = font.render('You were beaten! Better luck next time!', 1, (150, 150, 70))
            
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
        pygame.display.update()
        
        pygame.time.delay(2000)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtime = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                
                for button in buttons:
                    
                    if button.click_button(position) and game.get_connected_players():
                        if player == 0:
                            if not game.player_1_turn:
                                network.send(button.text)
                            else:
                                if not game.player_1_turn:
                                    network.send(button.text)
        
        redraw_window(win, game, player)
    
class Button:
    
    def __init__(self, text, x, y, colour):
        '''
        Initialise initial state of buttons.
        
        Parameters:
            self:
                The buttons.
            text:
                The buttons that will
                appear on the buttons.
            x:
                the width of the buttons.
            y:
                The height of the buttons.
            Colour:
                The colour of the buttons.
        '''
        self.text = text
        self.x = x
        self.y = y
        self.colour = colour
        self.width = 200
        self.height = 150
        
    def draw_items(self, win):
        pygame.draw.rect(win, self.colour, self.x, self.y, self.width, self.height)
        
        font = pygame.font.SysFont('Impact', 50)
        text = font.render(self.text, 1, (12, 137, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2), \
            self.y + round(self.height / 2) - round(text.get_height() / 2)))
        
    def click_button(self, position):
        '''
        Determine if the mouse cursor position 
        is wihin the dimensions of the button.
        
        Parameters:
            self:
                The game:
            position:
                the position of the mouse cursor.
        
        Return:
            A button click if condition is True.
        '''
        x1 = position[0]
        y1 = position[1]

        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

# Customise the buttons.
buttons = [Button('Rock', 60, 600, (125,60,100)),
           Button('Paper', 300, 600, (255,255,255)),
           Button('Scissors', 500, 600, (160,255,70))]
        
def redraw_window(win, game, player):
    '''
    Change the property of our gaming
    window like colour and size.
    
    Parameters:
        win:
            the game window to be redrawn.
        player:
            the players and their opponents
            that will have the appropriate text
            displayed to them.
        Game:
            The game.
    Return: Nothing.
    '''
    # Colour the window.
    win.fill((156,134,205))
    
    if not (game.get_connected_players()):
        font = pygame.font.SysFont('impact', 80)
        text = font.render('Waiting for opponent.', 1, (70, 70, 150), True)
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    else:
        font = pygame.font.SysFont('impact', 80)
        text = font.render('Your turn.', 1, (0, 255, 255))
        win.blit(text, (100, 220))
        
        text = font.render("Opponent's turn.", 1, (0, 255, 255))
        win.blit(text, (400, 220))
        
        turn_1 = game.get_player_turn(0)
        turn_2 = game.get_player_turn(1)
        
        if game.both_turns():
            text_1 = font.render(turn_1, 1, (255, 0, 0))
            text_2 = font.render(turn_2, 1, (255, 0, 0))
        else: 
            if game.player_1_turn and player == 0:
                text_1 = font.render(turn_1, 1, (255, 0, 0))
            elif game.player_1_turn:
                text_1 = font.render("Move made", 1, (255, 0, 0))
            else:
                text_1 = font.render("Waiting for move.", 1, (255, 0, 0))
                
            if game.player_2_turn and player == 1:
                text_2 = font.render(turn_2, 1, (255, 0, 0))
            elif game.player_2_turn:
                text_2 = font.render("Move made", 1, (255, 0, 0))
            else:
                text_2 = font.render("Waiting for move.", 1, (255, 0, 0))
                
        if player == 1:
            win.blit(text_2, (150, 400))
            win.blit(text_1, (450, 400))
        else:
            win.blit(text_1, (150, 400))
            win.blit(text_2, (450, 400))
            
        for button in buttons:
            button.draw_items(win)
    
    pygame.display.update()
    
def make_menu_screen():
    '''
    When the game starts, display
    a message to click to start the game.
    '''
    runtime = True
    
    clock = pygame.time.Clock()
    
    while runtime:
        
        clock.tick(90)
        
        win.fill((156,134,205))
        
        # Set the font and text properties for the text to be displayed.
        font = pygame.font.SysFont('impact', 80)
        text = font.render('Click to play!', 1, (200, 100, 55))
        
        # Draw the text.
        win.blit(text, (200, 300))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                runtime = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                runtime = False

    if __name__ == '__main__':
        main()

while True:
    if __name__ == '__main__':
        make_menu_screen()