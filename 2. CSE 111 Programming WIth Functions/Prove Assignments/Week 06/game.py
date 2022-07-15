# This file will contain a class to
# hold all the in-game information.

# Set up a class named game which will be
# imported by both client and server.
class Game:
    
    def __init__(self, id):
        '''
        Define the game's initial state.
        
        Parameters:
            self:
                The Game.
            id:
            The game ids.
        '''
        self.player_1_turn = False
        self.player_2_turn = False
        self.ready = False
        self.id = id # Current game's id.
        self.moves = [None, None] # [player 1, player 2]
        self.wins = [0, 0] # [player 1, player 2]
        self.ties = 0
        
    def get_player_moves(self, players):
        '''
        Get the moves of the players.
    
        paramerters:
            self:
                The game.
            players:
                The 2 players.
                    0 is player 1 &
                    1 is player 2.
        
        return:
            The moves the players make.
        '''
        return self.moves[players]
    
    def play_game(self, player, move):
        '''
        Update moves list with each player's
        moves.
        
        parameters:
            self:
                The game.
            player:
                Each player.
            move:
                Each player's moves.
        '''
        self.moves[player] = move
        
        # Determine which player made a move.
        if player == 0:
            self.player_1_turn = True
        else:
            self.player_2_turn = True

    def get_connected_players(self):
        '''
        Will determine if both players
        are connected to the game,
        which if they are will allow for
        a load in.
        
        parmeters:
            self:
                The game.
        return:
            A connection and ready to play.
        '''
        return self.ready
    
    def get_player_turns(self):
        '''
        Returns each player's turns.
        
        parameters:
            self:
                The game.
        '''
        return self.player_1_turn and self.player_2_turn
    
    def get_winner(self):
        '''
        Returns the winner of each game.
        
        Parameters:
            self:
                The game.
        '''
        # Get the first letter of each word
        # (Rock, Paper, Scissors) when either one
        # is chosen.
        player_1 = self.moves[0].upper()[0] # Player 1
        player_2 = self.moves[1].upper()[0] # Player 2
        
        winner = -1
        
        # Determine winning conditions for the game.
        if player_1 == 'R' and player_2 == 'S':
            winner = 0
        elif player_1 == 'S' and player_2 == 'R':
            winner = 1
        elif player_1 == 'P' and player_2 == 'R':
            winner = 0 
        elif player_1 == 'R' and player_2 == 'P':
            winner = 1
        elif player_1 == 'S' and player_2 == 'P':
            winner = 0
        elif player_1 == 'P' and player_2 == 'S':
            winner = 1
        
        return winner
    
    def reset_turns(self):
        '''
        Returns the game to its initial state.
        '''
        self.player_1_turn = False
        self.player_2_turn = False