# importar modulos
import socket
from collections import namedtuple
import time
import pickle
import threading


####### Formato do Frame -> |||256 bytes de mensagem|Sequence Number|Ack|Timer|||


# Estruturas
packages = []

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


# Destino
destino = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
adest = "localhost"
aporta = 9000
destino.bind(("localhost",aporta))



#Envia a primeira Janela de pacotes e chama a função que vai ficar recebendo os acks e "deslizando" a janela
def Enviar(conteudo):
	global windowSize
	global sequenceNumber
	global windowLeft
	global windowRight
	global qtdpacotes
	global packages
	global enviados
	enviados = 0
	qtdpacotes = len(conteudo) # desse jeito eu garanto 1 pacote por "fatia" do arquivo
	packages = prepararParaEnvio(conteudo)
	windowRight = min(int(windowSize),qtdpacotes)#para não tentar enviar coisas que não existem na lista (segmentation fault)
	while enviados < windowRight: 
		socketar(packages[enviados]) #chama a função que envia para o destino
		print ("Enviando Pacote " + str(enviados)) 
		enviados += 1
	Controle() #chama a função que faz o controle dos acks


#Litrealmente envia um pacote ao destino
def socketar(pacote):
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	adress = "localhost"
	porta = 12000
	sock.sendto(pacote,(adress,porta))
	sock.close()


def prepararParaEnvio(conteudo):
	numeroSequencia = 0
	fila = [] #cria a lista de pacotes a serem enviados
	for mensagem in conteudo:
		fila.append(criarPacotes(mensagem,numeroSequencia)) #coloca na fila o retorno da função cria pacotes
		numeroSequencia = numeroSequencia + 1 
	return fila #retorna os pacotes prontos para envio

def criarPacotes(mensagem,Sn):
	templista = [mensagem,Sn,0] #criando o frame
	pacote = pickle.dumps(templista) #serializa para uma string o conteudo
	return pacote #retorna a string serializada


def Controle():
	global destino
	global aporta
	global adest
	global windowRight
	global windowLeft
	global windowSize
	global qtdpacotes
	global enviados
	nPacotesAcked = 0
	while True :
		recebido = destino.recv(1024) #recebe um pacote
		dados = pickle.loads(recebido) #desserializa
		if dados[2] == 1: #checka se é ACK
			Sn = dados[1] #pega o numero de sequencia do ACK
			print("ACK Recebido : " + str(Sn))
			if Sn >= windowLeft and Sn < qtdpacotes: #numero de sequencia tem que estar entre o começo da janela e a qtd total de pacotes 
				nPacotesAcked += Sn - windowLeft 
				temp_windowRight = windowRight #pra deslizar a janela
				windowRight = min( windowRight + Sn - windowLeft ,qtdpacotes) #pra garantir que não vou enviar um pacote fora da janela
				windowLeft = Sn # pra deslizar o limite inferior da janela
				for i in range(windowRight-temp_windowRight): 
					socketar(packages[enviados]) #envia o pacote
					print("Enviando pacote " + str(enviados))
					if enviados < qtdpacotes:
						enviados +=1
			elif Sn == qtdpacotes:
				print("Mensagens transferidas com sucesso! ")
				fin = criarPacotes(MsgFIM,0)
				socketar(fin)
				destino.close()
				break







def main():
	conteudo = []
	#Ler o arquivo e criar as "fatias" para colocar nos pacotes
	with open("sherlock.txt","rb") as arquivo :
		while True:
			fatia = arquivo.read(512)
			if fatia:
				conteudo.append(fatia)
			else:
				break
	Enviar(conteudo)


if __name__ == '__main__':
	main()