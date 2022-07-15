'''
Tic-Tac-Toe game
CSE 210 Solo Code Assignment Week 02
Author: Reace Ian Roeloffze
'''

# Create a dictionary for the game board.
game_board = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

# Create a list of the dictionary keys to be used when selecting
# a space to fill.
board_keys = [key for key in game_board]

def main():
    
    # Print intro message and game menu:
    print ('\nWelcome to Tic-Tac-Toe! Please choose an option:')
    print ('\n1. Play Game')
    print ('2. Quit')
    
    while True:
        choice = input('\n1 or 2? ')
    
        if choice == '1':
            
            player = "\033[35;1mX\033[0m"
            count = 0
            
            # Loop through the game eliminating invalid inputs.
            while count < 9:
                display_game_board(game_board)
                player_move = input('\nPlease mark your position on a numbered square: ')
                
                # Display an error message if incorrect values are input and prompt a retry.
                if not player_move in('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    print("Invalid entry. Please enter a number from 1 to 9.")
                    continue
                else:
                    if game_board[player_move] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                        game_board[player_move] = player
                        count += 1
                    else:
                        print ('This space is already occupied. Please fill an unoccupied space. ')
                        continue

                # Set a condtion to verify inputs to determine a winner or if it's a tie.
                if count >= 5:
                    if (game_board['1'] == game_board['2'] == game_board['3'] != ' ') or \
                            (game_board['4'] == game_board['5'] == game_board['6'] != ' ') or \
                            (game_board['7'] == game_board['8'] == game_board['9'] != ' ') or \
                            (game_board['1'] == game_board['4'] == game_board['7'] != ' ') or \
                            (game_board['2'] == game_board['5'] == game_board['8'] != ' ') or \
                            (game_board['3'] == game_board['6'] == game_board['9'] != ' ') or \
                            (game_board['1'] == game_board['5'] == game_board['9'] != ' ') or \
                            (game_board['3'] == game_board['5'] == game_board['7'] != ' '):
                        display_game_board(game_board)
                        print(f'\nCongratulations, {player}! You won!')
                        break

                if count == 9:
                    display_game_board(game_board)
                    print("\nIt's a tie!")

                if player == '\033[35;1mX\033[0m':
                    player = '\033[33;1mO\033[0m'
                else:
                    player = '\033[35;1mX\033[0m'

            # Choose to restart the game or quit.
            restart = input('Would you like to play again? (Y/N) \n').upper()
            if restart == "Y":
                for key in game_board:
                    game_board[key] = " "
                main()
            
            elif restart == 'N':
                break
            else:
                print ('\nInvalid input.')
            
        elif choice == '2':
            break
        
        else:
            print ('\nInvalid option.')
            
    print ('\nThank you for playing!')
        
def display_game_board(board):
    '''
    Displays a game board for the game
    tic-tac-toe.
    
    Parameters:
        board:
            The game board to be displayed.
    '''
    # Create a dictionary for the game board.
    
    print (f"\n{board['1']} | {board['2']} | {board['3']} ")
    print ('- + - + -')
    print (f"{board['4']} | {board['5']} | {board['6']} ")
    print ('- + - + -')
    print (f"{board['7']} | {board['8']} | {board['9']} ")

if __name__ == '__main__':
    main()
    
