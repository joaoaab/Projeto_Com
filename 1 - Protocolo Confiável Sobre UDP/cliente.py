# importar modulos
from socket import *
from collections import namedtuple
import time
import pickle


####### Formato do Frame -> |||256 bytes de mensagem|Sequence Number|Ack|||


# Constantes
Window_Size = 1024
requestNumber = 0
sequenceNumber = 0
windowLeft = 0
windowRight = 1000
qtdpacotes = 0


#def criarPacotes(conteudo,numeroSequencia):
#	package = pass 

def Enviar(conteudo):
	global Window_Size
	global sequenceNumber
	global windowLeft
	global windowRight
	global qtdpacotes
	qtdpacotes = len(conteudo) # desse jeito eu garanto 1 pacote por "fatia" do arquivo
	packages = prepararParaEnvio(conteudo)


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


	
def main():
	conteudo = []
	#Ler o arquivo e criar as "fatias" para colocar nos pacotes
	with open("hamlet.txt","rb") as arquivo :
		while True:
			fatia = arquivo.read(int(sequenceMax))
			if fatia:
				conteudo.append(fatia)
			else:
				break
	Enviar(conteudo)

	#sock = socket(AF_INET,SOCK_DGRAM)
	#serverPort = 12000
	#serverAdress = "localhost"
	#message = ""
	#while message != "quit":
	#	message = input("mensagem a ser enviada \n")
	#	sock.sendto(message.encode(),(serverAdress,serverPort))
		#echo,addr = sock.recvfrom(1024)
		#print(echo.decode())


if __name__ == '__main__':
	main()