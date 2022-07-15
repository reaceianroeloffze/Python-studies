import socket
from _thread import *
import pickle

from player import Player
# import sys

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
    
# Start listening for connections
# Speicified number indicates amount of permissable connections.
# No argument in the perentheses defaults to unlimited connections to server.
sock.listen(2) # Opens up the port.
print ('Serer start. Connection pending...')

# Create a list of players and their specific starting position, shape and colour.
players = [Player(10, 10, 50, 50, (50, 170, 255)), Player(120, 120, 50, 50, (255, 20, 130))]

# Define a threaded functon
# This functoin will be continuously running
# in the background. A threaded function allows
# A comupter to execute the program without first
# passing through that function. It will execute the
# threaded function and the rest of the program together.
def thread_client(connection, player):
    '''
    A threaded function that will continue to send and
    receive data from clients connecting to this
    server for as long as the client is connected.
    
    Parameters:
        connection:
            Clients that are connected to the network
            on the server.
        player:
            The players connected to the server.
    '''
    # Use the pickle.dumps method to store data in the server.
    connection.send(pickle.dumps(players[player]))
    
    reply = ''
    
    # Set a loop to continuously receive
    # data from clients who connect.
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            
            # numner in () is bitrate - how much information we want to
            # be receiving at a time from connecting clients.
            # The smaller the size the quicker information is processed
            # bigger sizes means more information that is processed which
            # takes more time.

            # Update the positions of the players.
            players[player] = data
            
            if not data:
                print ('Disconnected from the client.')
                break
            
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                
                print (f'Received: {data} from {player}')
                # print (f'Current player = {player}')
                print (f'Sending: {reply}')
            
            connection.sendall(pickle.dumps(reply))
        except UnicodeDecodeError as code_err:
            print (code_err)
            break
        
    print ('Connection lost.')
    connection.close()

# Keep track of all players connecting to the server &
# Continuously accept any incoming players wishing to
# connect to the server.
player_amount = 0

while True:
    connection, address = sock.accept()
    
    # print a successful connection.
    print (f'Connected to: {address}')
    
    # Threads allow multiple functions to run simultaneously
    # in the background.
    start_new_thread(thread_client, (connection, player_amount))
    
    player_amount += 1 