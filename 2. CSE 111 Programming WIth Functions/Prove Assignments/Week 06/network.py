import socket
# import the pickle module to serialise objects.
import pickle

# Set up a reusable class.
class Network:
    
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.0.25'
        self.port = 5555
        self.address = (self.server, self.port)
        self.current_player = self.connect()
        
    def get_player(self):
        '''
        Get the player object from the server.
        
        Parameters:
            self: the Network.
        Return:
            The starting position of in-game characters.
        '''
        return self.current_player
        
    def connect(self):
        '''
        Connect server to specified network.
        
        Parameters:
            self:
                the network.
        Return:
            decoded data sent back to the
            client from the server.
        '''
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        
        except Exception as exc:
            print (exc)
            print ('THE SERVER IS NOT RUNNING!')
    
    def send(self, data):
        '''
        Send string data from the client to the server
        and return object data.
        
        Prameters:
            self:
                The network.
            data:
                Encoded data sent from the
                client to the server.
        Return:
            decoded data sent back to the
            client from the server.
        '''
        try:
            print (f'sending - {str.encode(data)}')
            self.client.send(str.encode(data))
            received = self.client.recv(2048*2)
            print (f'received - {received}')
            game = pickle.loads(received)
            print (game)
            return game
        except socket.error as sock_err:
            print (sock_err)