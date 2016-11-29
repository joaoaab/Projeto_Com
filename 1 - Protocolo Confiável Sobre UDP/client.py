# importar modulos
import socket
from time import gmtime, strftime
import pickle

# Formato do Frame -> |||x bytes de mensagem|Sequence Number|Ack|||


# Estruturas
packages = []  # lista dos pacotes

# Constantes
windowSize = 4
requestNumber = 0
sequenceNumber = 0
windowLeft = 0
windowRight = 3
qtdpacotes = 0
estimatedRTT = 1
enviados = 0
MsgFIM = "QuitConnection"
timeout = 0.001  # depende do computador / rede
Sn = 0
log = open("log_client.txt", "w+")

# Destino
destino = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
adest = "localhost"
aporta = 9000
destino.bind(("localhost", aporta))
destino.settimeout(timeout)


def Enviardef(conteudo):
    global windowSize
    global sequenceNumber
    global windowLeft
    global windowRight
    global qtdpacotes
    global packages
    global enviados
    global Sn
    global log
    nPacotesAcked = 0
    enviados = 0
    # desse jeito eu garanto 1 pacote por "fatia" do arquivo
    qtdpacotes = len(conteudo)
    # cria a lista final de pacotes a serem enviados
    packages = prepararParaEnvio(conteudo)
    # para não tentar enviar coisas que não existem na lista (segmentation
    # fault)
    windowRight = min(int(windowSize), qtdpacotes)
    recebido = ""
    while True:
        # se for a primeira transmissão (poderia melhorar a lógica but
        # deadline)
        if enviados == 0:
            while enviados < windowRight:
                # chama a função que envia para o destino
                socketar(packages[enviados])
                log.write("Enviando Pacote " + str(enviados) + "\n")
                enviados += 1
        try:
            recebido = destino.recv(1024)  # recebe um pacote
            dados = pickle.loads(recebido)  # desserializa
            if dados[2] == 1:  # checka se é ACK
                Sn = dados[1]  # pega o numero de sequencia do ACK
                log.write("ACK Recebido : " + str(Sn) + "\n")
                # numero de sequencia tem que estar entre o começo da janela e
                # a qtd total de pacotes
                if Sn >= windowLeft and Sn < qtdpacotes:
                    nPacotesAcked += Sn - windowLeft
                    temp = windowRight  # pra deslizar a janela
                    # pra garantir que não vou enviar um pacote fora da janela
                    windowRight = min(windowRight + Sn -
                                      windowLeft, qtdpacotes)
                    windowLeft = Sn  # pra deslizar o limite inferior da janela
                    for i in range(windowRight - temp):
                        socketar(packages[enviados])  # envia o pacote
                        log.write("Enviando pacote " + str(enviados) + "\n")
                        if enviados < qtdpacotes:
                            enviados += 1
                elif Sn == qtdpacotes:
                    print("Mensagens transferidas com sucesso! ")
                    fin = criarPacotes(MsgFIM, 0)
                    # manda uma mensagem que indica pro server que as mensagens
                    # acabaram
                    socketar(fin)
                    destino.close()  # fecha o socket de recebimento
                    break
        except socket.timeout:  # se o temporizador estourar ..
            log.write("Temporizador Estourou, entrando em modo de reenvio\n")
            timedout()


# Litrealmente envia um pacote ao destino
def socketar(pacote):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    adress = "localhost"
    porta = 12000
    sock.sendto(pacote, (adress, porta))
    sock.close()


def prepararParaEnvio(conteudo):
    numeroSequencia = 0
    fila = []  # cria a lista de pacotes a serem enviados
    for mensagem in conteudo:
        # coloca na fila o retorno da função cria pacotes
        fila.append(criarPacotes(mensagem, numeroSequencia))
        numeroSequencia = numeroSequencia + 1
    return fila  # retorna os pacotes prontos para envio


def criarPacotes(mensagem, Sn):
    templista = [mensagem, Sn, 0]  # criando o frame
    pacote = pickle.dumps(templista)  # serializa para uma string o conteudo
    return pacote  # retorna a string serializada


# Quando o temporizador estoura
def timedout():
    global windowRight
    global windowLeft
    global windowSize
    global Sn
    global qtdpacotes
    global packages
    temp = windowLeft
    # envia a janela toda dnv e volta pra esperar os acks :)
    while temp <= windowRight and temp < qtdpacotes:
        socketar(packages[temp])
        log.write("Reenviando Pacote : " + str(temp) + "\n")
        temp += 1


def main():
    conteudo = []
    # Ler o arquivo e criar as "fatias" para colocar nos pacotes
    with open("sherlock.txt", "rb") as arquivo:
        while True:
            fatia = arquivo.read(128)
            if fatia:
                conteudo.append(fatia)
            else:
                break
    log.write("Começando programa, Registrar LOG,data : " +
              strftime("%c ", gmtime()) + "\n")
    Enviardef(conteudo)


if __name__ == '__main__':
    main()
