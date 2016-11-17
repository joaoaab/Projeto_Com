class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.deck = []
        self.won = 0

    def compareTopCard(self, enemy, attr):
        # Compara o status da carta do topo do deck e retorna ele mesmo se
        # ganhou o turno ou o outro se perdeu
        pass

    def playerWins(self, enemy):
        # Chamada quando o jogador ganha um turno, tira a carta, e coloca a
        # carta do inimigo e a sua no final do deck
        pass
        
    def playerLoses(self):
        del self.deck[0]
        return self
