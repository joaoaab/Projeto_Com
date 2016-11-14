import socket
import pickle
from time import gmtime,strftime

#Criar Socket para poupar Tempo (não ficar pegando o endereço toda vez que vai enviar algo)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "localhost"
porta = 9000


#Criar arquivo de log
log = open("log_server.txt","w+")


def sendACK(sequenceNumber):
	mensagem = ["ACKPKT",sequenceNumber,1]
	sock.sendto(pickle.dumps(mensagem),(host,porta))


def main():
	log.write("Iniciar Log, Data : " + strftime("%c", gmtime()) + "\n")
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
			log.write("Mensagens Recebidas com sucesso !\n")
			receiver.close()
			break
		elif sequenceNumber == expectedSequence:
			ack = sequenceNumber+1
			sendACK(ack)
			log.write("Recebido sequencia : " + str(sequenceNumber) + "---- Ack enviado : " + str(ack) + "\n")
			with open("copia.txt","ab") as output:
				output.write(data)
			expectedSequence += 1
		elif sequenceNumber != expectedSequence:
			log.write("Recebido numero de sequencia fora de ordem !! Sn = " + str(sequenceNumber) + "\n")

if __name__ == '__main__':
	main()