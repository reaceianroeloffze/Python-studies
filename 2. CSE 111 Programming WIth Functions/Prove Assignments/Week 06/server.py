import socket
from _thread import *
import pickle
from game import Game

# Server address.
# This is a locally assigned IP address for my specific network.
# You can access yours by typing in ipconfig in the command prompt
# (windows machine). Copy and paste your IPv4 address.
server = '192.168.0.25'
port = 5555

# Initialise socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind port & server to socket.
# Test to see if port is usable.
try:
    # Bind given port to specified IP address.
    sock.bind((server, port))
    
except socket.error as sock_err:
    print(sock_err) # Will fail if port is being used for something else.

# Store the IP addresses of clients 
# connected to the server.
connected_clients = set()

# Create a dictionary to store games.
games = {
    # id: game object
}

# Keep track of current gaming IDs.
id_count = 0

# Start listening for connections
# Speicified number indicates amount of permissable connections.
# No argument in the perentheses defaults to unlimited connections to server.
sock.listen() # Opens up the port.
print ('Serer start. Connection pending...')

# Define a threaded functon
# This functoin will be continuously running
# in the background. A threaded function allows
# A comupter to execute the program without first
# passing through that function. It will execute the
# threaded function and the rest of the program together.
def thread_client(connection, player, game_id):
    '''
    A threaded function that will continue to send and
    receive data from every client connecting to this
    server for as long as they are connected.
    
    Parameters:
        connection:
            Clients that are connected to the network
            on the server.
        player:
            The players connected to the server.
        game_id:
            The id of the currently active game
            being played.
    '''
    
    # Globalise id_count so that when a client disconnects
    # it is subtracted from the id count to keep accurate
    # track of all the game data, connection data, etc.
    global id_count
    
    # Let the players know which player they are.
    connection.send(str.encode(str(player)))
                    
    reply = ''
    
    # Loop through receiving and sending data.
    while True:
        try:
            data = connection.recv(4096).decode()
            
            # Check if game id still exists in games dict
            # and check which data is being sent.
            print (game_id)
            if game_id in games:
                game = games[game_id]
                print (f'Data - {data}')
                # get a game, reset a game or make a move:
                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset_turns() # Reset the game.
                    
                    elif data != 'get':    
                        game.play_game(player, data) # Make a move.
                        
                    print (game)
                    reply = game # Get a game.
                    print (f'seding - {pickle.dumps(game)}')
                    # Save all data in server memory.
                    connection.sendall(pickle.dumps(game))
            else:
                break # if the game is no longer in the dictionary.
        except Exception as exc:
            print (exc)
            break # If a client disconnects, e.g, or another issue arises.
    
    # If the loop us broken, delete the game.
    print ('Connection lost.')
    
    try:
        del games[game_id]
        print (f'ending game {game_id}')
    except:
        pass
    
    id_count -= 1
    
    connection.close()
        
# While the server is running:   
while True:
    connection, address = sock.accept()
    
    # print a successful connection.
    print (f'Connected to: {address}')
    
    
    # Keep track of how many peopl/clients
    # are connected to the server at once.
    id_count += 1
    
    current_player = 0
    
    # Keep track of what ID the game is going to be.
    game_id = (id_count - 1) // 2
    
    # Create a new game.
    if id_count % 2 == 1:
        games[game_id] = Game(game_id)
        print ('Creating new game...')
    
    # if 2 players connect, the game is ready
    # to start.
    else:
        games[game_id].ready = True
        current_player = 1
    # Threads allow multiple functions to run simultaneously
    # in the background.
    start_new_thread(thread_client, (connection, current_player, game_id))