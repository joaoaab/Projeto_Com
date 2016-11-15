import time
import random
import socket

Caixa = {"carta1":[],"carta2":[]} #dicionário key = nome e value = lista com os atributos, vai servir para criar o deck do servidor

class Card:
	def __init__(self,name,att1,att2,att3,att4,att5,att6):
		self.name = name
		self.att1 = att1
		self.att2 = att2
		self.att3 = att3
		self.att4 = att4
		self.att5 = att5
		self.att6 = att6

class Server:

	def __init__(self,player1,player2):
		self.player1 = player1
		self.player2 = player2
		self.deck = []
		self.winner = none

	def fillDeck(self):
		for i in Caixa:
			self.deck.append(Card(i,Caixa[0],Caixa[1],Caixa[2],Caixa[3],Caixa[4],Caixa[5])) # Pra cada carta na caixa cria um objeto Carta e coloca no deck do server

	def startGame(self):
		random.shuffle(self.deck)
		while len(self.deck) > 0:
			pass
			#coloca cartas nos 2 decks



def main():
	Game = Server()


if __name__ == '__main__':
	main()