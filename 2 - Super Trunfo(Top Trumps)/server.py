import time
import random
import socket
import player
import threading
import pickle

# Constantes
TCP_IP = "localhost"
TCP_PORT = 12000
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
sockets = []
data = ""
locker = threading.Lock()

# Classe do jogo

class Game:

    def __init__(self, player1, player2):
        self.player1 = player.player(player1)
        self.player2 = player.player(player2)
        self.deck = []
        self.winner = 0
        self.turno = None
        self.isthereawinner = 0

    def fillDeck(self):
        # Pra cada carta na caixa cria um objeto Carta e coloca no deck do
        # server
        for i in Caixa:
            self.deck.append(player.Card(i, Caixa[i][0], Caixa[i][1], Caixa[
                             i][2], Caixa[i][3], Caixa[i][4]))

    def distributeCards(self):
        # Distribui as cartas nos decks do players
        random.shuffle(self.deck)
        self.player1.deck = self.deck[:len(self.deck) // 2]
        self.player2.deck = self.deck[len(self.deck) // 2:]

    def batalha(self, atributo):
        global sockets
        # faz a batalha entre as cartas
        if atributo == "imag":
            enviar("ACK", sockets[self.turno])
            higher = self.player1.compareTopCard(self.player2, "imag")
            if higher == self.player1:
                self.player1 = self.player1.playerWins(self.player2)
                self.player2 = self.player2.playerLoses()
                self.player1.won = 1
                self.player2.won = 0
                time.sleep(4)
            else:
                self.player2 = self.player2.playerWins(self.player1)
                self.player1 = self.player1.playerLoses()
                self.player1.won = 0
                self.player2.won = 1
                time.sleep(4)

        elif atributo == "coragem":
            enviar("ACK", sockets[self.turno])
            higher = self.player1.compareTopCard(self.player2, "coragem")
            if higher == self.player1:
                self.player1 = self.player1.playerWins(self.player2)
                self.player2 = self.player2.playerLoses()
                self.player1.won = 1
                self.player2.won = 0
                time.sleep(4)

            else:
                self.player2 = self.player2.playerWins(self.player1)
                self.player1 = self.player1.playerLoses()
                self.player1.won = 0
                self.player2.won = 1
                time.sleep(4)

        elif atributo == "bom humor":
            enviar("ACK", sockets[self.turno])
            higher = self.player1.compareTopCard(self.player2, "bom_humor")
            if higher == self.player1:
                self.player1 = self.player1.playerWins(self.player2)
                self.player2 = self.player2.playerLoses()
                self.player1.won = 1
                self.player2.won = 0
                time.sleep(4)
            else:
                self.player2.playerWins(self.player2)
                self.player1 = self.player1.playerLoses()
                self.player1.won = 0
                self.player2.won = 1
                time.sleep(4)

        elif atributo == "agilidade":
            enviar("ACK", sockets[self.turno])
            higher = self.player1.compareTopCard(self.player2, "agilidade")
            if higher == self.player1:
                self.player1 = self.player1.playerWins(self.player2)
                self.player2 = self.player2.playerLoses()
                self.player1.won = 1
                self.player2.won = 0
                time.sleep(4)
            else:
                self.player2 = self.player2.playerWins(self.player1)
                self.player1 = self.player1.playerLoses()
                self.player1.won = 0
                self.player2.won = 1
                time.sleep(4)

        else:
            enviar("jogada não valida", sockets[self.turno])
            self.jogarturno()

        # mandar mensagem avisando e atualizando o deck dos 2
        if len(self.player1.deck) == 0:
            # significa que player1 perdeu
            self.isthereawinner = 1
        elif len(self.player2.deck) == 0:
            # significa que player 2 perdeu
            self.isthereawinner = 1

        whowon = {self.player1.name: [self.player1.won, self.isthereawinner],
                  self.player2.name: [self.player2.won, self.isthereawinner]}

        broadcast(whowon)
        time.sleep(2)

    def jogarturno(self):
        global sockets
        # Recebe o atributo escolhido da carta e anuncia para o que
        # não tem o turno
        recebido = receber(sockets[self.turno])
        time.sleep(2)
        enviar(recebido, sockets[(self.turno + 1) % 2])
        # Checkar as cartas dos players e ver quem ganhou o turno
        self.batalha(recebido)

# só pra criar a conexão entre players e servidor


def handshake(sock):
    global Players
    global locker
    data = sock.recv(1024)
    data = pickle.loads(data)
    locker.acquire()
    Players.append(data)
    locker.release()


def broadcast(data):
    global sockets
    data = pickle.dumps(data)
    for s in sockets:
        s.sendall(data)


def enviar(data, socki):
    data = pickle.dumps(data)
    socki.sendall(data)


def receber(socki):
    global BUFFER_SIZE
    data = socki.recv(BUFFER_SIZE)
    data = pickle.loads(data)
    return data


def enviarturnos(sockets, jogo):
    if jogo.turno == 0:
        enviar(1, sockets[0])
        enviar(0, sockets[1])
    else:
        enviar(0, sockets[0])
        enviar(1, sockets[1])


def main():
    global qtdJogadores
    global tcpServer
    global sockets
    global threads
    global Players
    global ackConnection
    # fazer handshake e etc...
    tcpServer.listen(2)
    qtdConexoes = 0

    while qtdConexoes < qtdJogadores:
        conex, (ip, port) = tcpServer.accept()
        sockets.append(conex)
        newthread = threading.Thread(target=handshake, args=(conex,))
        newthread.start()
        threads.append(newthread)
        qtdConexoes += 1

    for t in threads:
        t.join()
    threads = []

    if(len(Players) == qtdJogadores):
        jogo = Game(Players[0], Players[1])
        enviar(Players[1], sockets[0])
        enviar(Players[0], sockets[1])
        time.sleep(1)
    else:
        print("Erro, não conseguiu ler os 2 nomes")

    # Cria Decks e envia para os clientes
    jogo.fillDeck()
    jogo.distributeCards()
    enviar(jogo.player1.deck, sockets[0])
    enviar(jogo.player2.deck, sockets[0])
    enviar(jogo.player2.deck, sockets[1])
    enviar(jogo.player1.deck, sockets[1])

    time.sleep(2)

    # a partir daqui o jogo rola

    jogo.turno = random.randint(0, 1)
    print("Quem vai jogar primeiro é : player " + str(jogo.turno + 1))

    while jogo.winner == 0:
        enviarturnos(sockets, jogo)
        print("enviados turnos!")
        jogo.jogarturno()
        print("turno jogado!")
        if jogo.player1.won:
            jogo.turno = 0
        else:
            jogo.turno = 1

    print("Game over!!! Vencedor : Player " + str(jogo.winner))

    # mandar mensagems de vitoria / derrota ...


if __name__ == '__main__':

    main()
