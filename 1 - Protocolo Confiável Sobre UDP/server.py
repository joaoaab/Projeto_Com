import socket
import pickle

#Criar Socket para poupar Tempo (não ficar pegando o endereço toda vez que vai enviar algo)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "localhost"
porta = 9000

def sendACK(sequenceNumber):
	mensagem = ["ACKPKT",sequenceNumber,1]
	sock.sendto(pickle.dumps(mensagem),(host,porta))


def main():
	expectedSequence = 0
	receiver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	host = "localhost"
	porta = 12000
	receiver.bind(("localhost",12000))
	while True:
		msg = receiver.recv(1024)
		dados = pickle.loads(msg)
		sequenceNumber = dados[1]
		data = dados[0]
		if data == "QuitConnection":
			print("Mensagens Recebidas com sucesso !")
			receiver.close()
			break
		elif sequenceNumber == expectedSequence:
			ack = sequenceNumber+1
			sendACK(ack)
			print ("Recebido sequencia : " + str(sequenceNumber) + "---- Ack enviado : " + str(ack))
			with open("copia.txt","ab") as output:
				output.write(data)
			expectedSequence += 1


if __name__ == '__main__':
	main()