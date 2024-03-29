import player
import socket
import pickle

# Estruturas
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "localhost"
Port = 12000
BUFFER_SIZE = 1024
control = "go"


def enviar(data):
    global sock
    data = pickle.dumps(data)
    sock.sendall(data)


def printCard(carta):

    print("|||Codigo : {} Nome :{}" .format(carta.key, carta.name))
    print("----------------------------------------------------------------")
    print("|||Imaginação : " + str(carta.imag) + "   ",end="")
    for i in range(carta.imag):
        print("|", end="")
    print ("")
    print("----------------------------------------------------------------")
    print("|||Coragem : " + str(carta.coragem) + "   ",end="")
    for i in range(carta.coragem):
        print("|", end="")
    print ("")
    print("----------------------------------------------------------------")
    print("|||Bom Humor : " + str(carta.bom_humor) + "   ",end="")
    for i in range(carta.bom_humor):
        print("|", end="")
    print ("")
    print("----------------------------------------------------------------")
    print("|||Agilidade : " + str(carta.agilidade) + "   ",end="")
    for i in range(carta.agilidade):
        print("|", end="")
    print ("")
    print("----------------------------------------------------------------")


def receber():
    global sock
    global BUFFER_SIZE
    data = sock.recv(BUFFER_SIZE)
    data = pickle.loads(data)
    return data


def checkarResultados(jogador, outrem):
    global control
    resultados = receber()
    eu = jogador.name
    inimigo = outrem.name
    if resultados[eu][0] and resultados[eu][1]:
        print("Você ganhou o jogo !")
        control = "exit"
        jogador = jogador.playerWins(outrem)
        outrem = outrem.playerLoses()
    elif resultados[eu][0]:
        print("Você ganhou o round !!")
        jogador = jogador.playerWins(outrem)
        outrem = outrem.playerLoses()
    elif resultados[inimigo][0] and resultados[inimigo][1]:
        print("Você perdeu jogo :/")
        jogador = jogador.playerLoses()
        outrem = outrem.playerWins(jogador)
        control = "exit"
    elif resultados[inimigo][0]:
        print("Você Perdeu o Round :/")
        jogador = jogador.playerLoses()
        outrem = outrem.playerWins(jogador)


def main():
    global sock
    global IP
    global Port
    global control

    name = input("Dale jogador!, qual o seu nome ?")
    eu = player.player(name)
    sock.connect((IP, Port))
    enviar(name)
    received = receber()
    inimigo = player.player(received)

    # Após enviar o nome cada jogador recebe seu deck
    # e o deck inimigo

    received = receber()
    eu.setDeck(received)
    received = receber()
    inimigo.setDeck(received)

    # E fica num loop até o server falar que o jogo acabou
    while control != "exit":
        received = receber()
        if received == 1:
            print("|||Você tem {} cartas |||" .format(len(eu.deck)))
            print("----------------------------------------------------------------")
            print("|||Seu inimigo tem {} cartas |||" .format(len(inimigo.deck)))
            print("----------------------------------------------------------------")
            print("|||Sua Carta do topo é  :")
            print("----------------------------------------------------------------")
            printCard(eu.deck[0])
            validationMSG = "jogada não valida"
            while validationMSG == "jogada não valida":
                atributo = input(
                    "escolha um atributo(imag,coragem,bom humor,agilidade):")
                enviar(atributo)
                validationMSG = receber()
            print("Esperando Avaliação...")

        else:
            print("|||Você tem {} cartas |||" .format(len(eu.deck)))
            print("----------------------------------------------------------------")
            print("|||Seu inimigo tem {} cartas |||" .format(len(inimigo.deck)))
            print("----------------------------------------------------------------")
            print("|||Sua Carta do topo é  :")
            print("----------------------------------------------------------------")
            printCard(eu.deck[0])
            print("|||seu oponente está escolhendo o atributo ...")
            print("----------------------------------------------------------------")
            received = receber()
            print("seu oponente escolheu :" + received)
            print("Esperando Avaliação...")
        checkarResultados(eu, inimigo)
    print("Game Over!!!")
    sock.close()


if __name__ == '__main__':
    main()
