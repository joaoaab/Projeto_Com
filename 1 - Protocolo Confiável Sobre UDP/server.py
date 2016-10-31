from socket import *

def main():
	serverPort = 12000
	serverSocket = socket(AF_INET,SOCK_DGRAM)
	serverSocket.bind(("",serverPort))
	print("The server is ready to receive")
	message = ""
	while message != "quit":
		message,clientAdress = serverSocket.recvfrom(1024)
		message = message.decode()
		print("recebido %d bytes na forma de %s\n" % (len(message),message))
		serverSocket.sendto(message.encode(),clientAdress)

	serverSocket.close()

if __name__ == '__main__':
	main()