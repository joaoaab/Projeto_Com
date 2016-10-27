from socket import *

# Constantes
Window_Size = 1024

def main():
	serverName = 'localhost'
	serverPort = 12000
	clientSocket = socket(AF_INET,SOCK_DGRAM)
	message = ""
	contador = 0
	while message != "quit":
		message = input('input message to deliver\n')
		clientSocket.sendto(bytes(message,"UTF-8"),(serverName,serverPort))
		print("pacote enviado, numero = ",contador)
		contador = contador + 1
	clientSocket.close()


if __name__ == '__main__':
	main()