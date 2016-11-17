import player
import socket
import pickle

# Estruturas
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
Port = 12000


def enviar(dados):
    dados = pickle.dumps(dados)
    socket.send(dados)


def main():
    name = input("Dale jogador!, qual o seu nome ?")
    socket.connect((IP, Port))
    enviar(name)
