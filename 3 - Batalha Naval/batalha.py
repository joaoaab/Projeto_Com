import pygame
import socket
import threading
import pickle


# Defining Constants
ip = 'localhost'
port = 1234
client = None
server = None


class Server(threading.Thread):
    def __init__(self):
        self.Thread.__init__(self)
        self.connection = None
        self.addr = None
        self.sock = None
        self.running = 1

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind((ip, porta))
        self.listen(1)
        while self.running == 1:
            data = self.sock.recv(1024)
            data = pickle.loads(data)
            # faz alguma coisa ....


class Client(threading.Thread):
    def __init__(self):
        self.Thread.__init__(self)
        self.connection = None
        self.addr = None
        self.running = 1
        self.sock

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))
        # envia as mensagems
        while self.running == 1:
            data = self.sock.recv(1024)
            data = pickle.loads(data)
            # faz alguma coisa


class Sender(threading.Thread):
    def __init__(self):
        self.Thread.__init__(self)
        self.running = 1

    def run(self):

    def kill(self):
        self.running = 0


def main():
    ''' um começa tentando conexão, se não conseguir
     ele cria a conexão  e ganha o direito de jogar primeiro
    '''
    client = Client()
    server = Server()
if __name__ == '__main__':
    main()
