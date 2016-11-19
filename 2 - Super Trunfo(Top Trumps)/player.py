class player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.deck = []
        self.won = 0

    def setDeck(self, deck):
        self.deck = deck

    def compareTopCard(self, outrem, attr):
        # Compara o atributous da carta do topo do deck e retorna ele mesmo se
        # ganhou o turno ou o outro se perdeu
        if(self.deck[0].compare(outrem.deck[0], attr)) == 0:
            return self
        else:
            return outrem

    def playerWins(self, outrem):
        # Chamada quando o jogador ganha um turno, tira a carta, e coloca a
        # carta do inimigo e a sua no final do deck
        winner_card = self.deck[0]
        loser_card = outrem.deck[0]
        del self.deck[0]
        self.deck.append(winner_card)
        self.deck.append(loser_card)
        return self

    def playerLoses(self):
        del self.deck[0]
        return self


class Card:
    def __init__(self, key, name, att1, att2, att3, att4):
        self.name = name
        self.key = key
        self.imag = att1
        self.coragem = att2
        self.bom_humor = att3
        self.agilidade = att4

    def compare(self, outrem, atributo):
        if atributo == "imag":
            if self.imag >= outrem.imag:
                return 0
            else:
                return 1
        elif atributo == "coragem":
            if self.coragem >= outrem.coragem:
                return 0
            else:
                return 1
        elif atributo == "bom_humor":
            if self.bom_humor >= outrem.bom_humor:
                return 0
            else:
                return 1
        elif atributo == "agilidade":
            if self.agilidade >= outrem.agilidade:
                return 0
            else:
                return 1
