import time
import random
import socket
import player
import threading
import pickle

# Constantes
TCP_IP = "localhost"
TCP_PORT = 2004
BUFFER_SIZE = 1024
ackConnection = "ACK"
qtdJogadores = 2

Caixa = {
    "A1": ["toddynho e scrat", 9, 7, 8, 8],
    "A2": ["Scrat e Manny", 7, 8, 6, 6],
    "A3": ["Diego", 2, 6, 1, 6],
    "B1": ["Toddynho e Sid", 9, 6, 9, 8],
    "B2": ["Crash e Eddie", 6, 7, 8, 9],
    "B3": ["Scrat", 3, 2, 5, 5],
    "C1": ["Toddynho e Manny", 9, 9, 7, 7],
    "C2": ["Sid e Shangrillama", 8, 6, 7, 8],
    "C3": ["Ellie", 3, 4, 6, 5],
    "D1": ["Toddynho e Diego", 7, 9, 6, 9],
    "D2": ["Sid e Manny", 6, 6, 7, 5],
    "D3": ["Shanrillama", 4, 4, 5, 6],
    "E1": ["Super Vantagem", 10, 10, 10, 10],
    "E2": ["Scrat e Diego", 4, 7, 5, 9],
    "E3": ["Shira", 4, 5, 3, 6],
    "F1": ["Ellie,  Crash e Eddie", 9, 7, 8, 6],
    "F2": ["Sid e Scrat", 8, 3, 9, 8],
    "F3": ["Brooke", 4, 4, 6, 5],
    "G1": ["Sid e Brooke", 8, 6, 9, 8],
    "G2": ["Manny e Diego", 3, 9, 4, 6],
    "G3": ["Buck", 4, 6, 3, 5],
    "H1": ["Diego e Shira", 6, 9, 7, 9],
    "H2": ["Noz", 0, 0, 0, 0],
    "H3": ["Vovó", 3, 2, 3, 2],
    "I1": ["Ellie e Manny", 5, 8, 7, 6],
    "I2": ["Sid", 5, 2, 6, 5],
    "I3": ["Toddynho,  Crash e Eddie", 4, 5, 7, 6],
    "J1": ["Sid e Diego", 7, 7, 6, 9],
    "J2": ["Manny", 1, 5, 3, 2],
    "J3": ["Toddynho", 8, 3, 5, 6]}


# Storages & Structures

Players = []
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []


# Classes do jogo


class Card:
    def __init__(self, key, name, att1, att2, att3, att4):
        self.name = name
        self.key = key
        self.imag = att1
        self.coragem = att2
        self.bom_humor = att3
        self.agilidade = att4


class Game:

    def __init__(self, player1, player2):
        self.player1 = player(player1)
        self.player2 = player(player2)
        self.deck = []
        self.winner = 0
        self.turno = None

    def fillDeck(self):
        # Pra cada carta na caixa cria um objeto Carta e coloca no deck do
        # server
        for i in Caixa:
            self.deck.append(Card(i, Caixa[i][0], Caixa[i][1], Caixa[
                             i][2], Caixa[i][3], Caixa[i][4]))

    def distributeCards(self):
        # Distribui as cartas nos decks do players
        self.player1.deck = self.deck[:len(self.deck) // 2]
        self.player2.deck = self.deck[len(self.deck) // 2:]

    def batalha(self,numero,atributo):
        # faz a batalha entre as cartas
        pass


def handshake():
    data = tcpServer.recv(1024)
    data = pickle.loads(data)


def printcard(carta):

    print("Codigo : {}\n Nome : " .format(carta.key, carta.name))
    print("Imaginação : " + str(carta.imag))
    print("Coragem : " + str(carta.coragem))
    print("Bom Humor : " + str(carta.bom_humor))
    print("Agilidade : " + str(carta.agilidade))


def main():
    global qtdJogadores
    global tcpServer
    # fazer handshake e etc...
    tcpServer.listen(2)
    qtdConexões = 0

    while qtdConexões < qtdJogadores:
        conex, (ip, port) = tcpServer.accept()
        newthread = threading.Thread(target=handshake)
        newthread.start()
        threads.append(newthread)
        qtdConexões += 1

    if(len(Players) == 2):
        jogo = Game(Players[0], Players[1])
    else:
        print("Erro, não conseguiu ler os 2 nomes")

    jogo.fillDeck()

    # a partir daqui o jogo rola

    jogo.turno = random.randint(0, 1)
    print("Quem vai jogar primeiro é : player " + str(jogo.turno + 1))

    while jogo.winner == 0:
        jogo.jogarturno()
        if jogo.player1.won:
            jogo.turno = 0
        else:
            jogo.turno = 1

    print("Game over!!! Vencedor : Player " + str(jogo.winner))

    # mandar mensagems de vitoria / derrota ...


if __name__ == '__main__':

    main()
