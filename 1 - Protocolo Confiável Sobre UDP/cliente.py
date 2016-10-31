from socket import *

# Constantes
Window_Size = 1024

def main():
	sock = socket(AF_INET,SOCK_DGRAM)
	serverPort = 12000
	serverAdress = "localhost"
	message = ""
	while message != "quit":
		message = input("mensagem a ser enviada \n")
		sock.sendto(message.encode(),(serverAdress,serverPort))
		#echo,addr = sock.recvfrom(1024)
		#print(echo.decode())

if __name__ == '__main__':
	main()