import time
import random
import socket

Caixa = {"A1":["toddynho e scrat",9,7,8,8],
"A2":["Scrat e Manny",7,8,6,6],
"A3":["Diego",2,6,1,6],
"B1":["Toddynho e Sid",9,6,9,8],
"B2":["Crash e Eddie",6,7,8,9],
"B3":["Scrat",3,2,5,5],
"C1":["Toddynho e Manny",9,9,7,7],
"C2":["Sid e Shangrillama",8,6,7,8],
"C3":["Ellie",3,4,6,5],
"D1":["Toddynho e Diego",7,9,6,9],
"D2":["Sid e Manny",6,6,7,5],
"D3":["Shanrillama",4,4,5,6],
"E1":["Super Vantagem",10,10,10,10],
"E2":["Scrat e Diego",4,7,5,9],
"E3":["Shira",4,5,3,6],
"F1":["Ellie, Crash e Eddie",9,7,8,6],
"F2":["Sid e Scrat",8,3,9,8],
"F3":["Brooke",4,4,6,5],
"G1":["Sid e Brooke",8,6,9,8],
"G2":["Manny e Diego",3,9,4,6],
"G3":["Buck",4,6,3,5], 
"H1":["Diego e Shira",6,9,7,9],
"H2":["Noz",0,0,0,0],
"H3":["Vovó",3,2,3,2],
"I1":["Ellie e Manny",5,8,7,6],
"I2":["Sid",5,2,6,5],
"I3":["Toddynho, Crash e Eddie",4,5,7,6],
"J1":["Sid e Diego",7,7,6,9],
"J2":["Manny",1,5,3,2],
"J3":["Toddynho",8,3,5,6]} #dicionário key = nome e value = lista com os atributos, vai servir para criar o deck do servidor #dicionário key = nome e value = lista com os atributos, vai servir para criar o deck do servidor #dicionário key = nome e value = lista com os atributos, vai servir para criar o deck do servidor

class Card:
	def __init__(self,key,name,att1,att2,att3,att4):
		self.name = name
		self.key = key
		self.att1 = att1
		self.att2 = att2
		self.att3 = att3
		self.att4 = att4

class Server:

	def __init__(self,player1,player2):
		self.player1 = player1
		self.player2 = player2
		self.deck = []
		self.winner = none

	def fillDeck(self):
		for i in Caixa:
			self.deck.append(Card(i,Caixa[i][0],Caixa[i][1],Caixa[i][2],Caixa[i][3],Caixa[i][4])) # Pra cada carta na caixa cria um objeto Carta e coloca no deck do server

	def startGame(self):
		random.shuffle(self.deck)
		while len(self.deck) > 0:
			pass
			#coloca cartas nos 2 decks



def main():
	print (Caixa["A1"][0])


if __name__ == '__main__':
	main()
