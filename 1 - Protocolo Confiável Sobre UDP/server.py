from socket import *

def main():
	serverPort = 12000
	serverSocket = socket(AF_INET,SOCK_DGRAM)
	serverSocket.bind(("",serverPort))
	print("The server is ready to receive")
	message = ""
	while message != "quit":
		message,clientAdress = serverSocket.recvfrom(2048)
		message = message.decode()
		print(message)
	serverSocket.close()

if __name__ == '__main__':
	main()