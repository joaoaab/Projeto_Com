import socket
import pickle
import copy
import sys
import time

# constantes e estruturas
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
receiver.bind(("", 0))


def printar_tabuleiro(s, board):

    player = "Enemy"
    if s == "u":
        player = "User"

    print "o tabuleiro do jogador " + player + ": \n"

    # printa os numeros horizontais
    print " ",
    for i in range(10):
        print "  " + str(i + 1) + "  ",
    print "\n"

    for i in range(10):

        # printa os numeros verticais
        if i != 9:
            print str(i + 1) + "  ",
        else:
            print str(i + 1) + " ",

        # printa os valores e vazio se for -1
        for j in range(10):
            if board[i][j] == -1:
                print ' ',
            elif s == "u":
                print board[i][j],
            elif s == "e":
                if board[i][j] == "X" or board[i][j] == "@":
                    print board[i][j],
                else:
                    print " ",

            if j != 9:
                print " | ",
        print

        # printa uma linha
        if i != 9:
            print "   ----------------------------------------------------------"
        else:
            print


def vertical_or_horizontal():

    while(True):
        user_input = raw_input("vertical or horizontal (v,h) ? ")
        if user_input == "v" or user_input == "h":
            return user_input
        else:
            print "digite h para horizontal e v para vertical!"


def solicitar_coordenada():

    while (True):
        user_input = raw_input("digite as coordenadas (linha,coluna)")
        try:
            coor = user_input.split(",")
            if len(coor) != 2:
                raise Exception("Entrada invalida.")

            coor[0] = int(coor[0]) - 1
            coor[1] = int(coor[1]) - 1

            if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
                raise Exception(
                    "somente valores dentro dos limites !")

            return coor

        except ValueError:
            print "somente valores numericos por favor"
        except Exception as e:
            print e


def place_ship(board, ship, s, ori, x, y):
    ship = ship[0]
    # coloca navio
    if ori == "v":
        for i in range(ship):
            board[x + i][y] = s
    elif ori == "h":
        for i in range(ship):
            board[x][y + i] = s

    return board


def validate(board, ship, x, y, ori):
		# se tentar colocar vertical e a posicao x + o tamanho do navio for > 10
    if ori == 'v' and x + ship > 10:
        return False
    # se for vertical e a posicao y + tamanho for > 10
    elif ori == "h" and y + ship > 10:
        return False
    else:
        if ori == 'v':
            for i in range(ship):
                if board[x + i][y] != -1:
                    return False
        elif ori == 'h':
            for i in range(ship):
                if board[x][y + i] != -1:
                    return False

    return True


def colocar_navios(board, ships):
    # Pede ao usuario coordenadas e orientacaoo e dispoe o navio no tabuleiro
    for ship in sorted(ships.keys()):

        qtd = ships[ship]
        qtd = qtd[1]
        i = 0
        print "Colocar " + str(qtd) + " " + ship
        while i < qtd:
            valid = False
            while(not valid):
                printar_tabuleiro("u", board)
                print "Colocando um " + ship
                x, y = solicitar_coordenada()
                ori = vertical_or_horizontal()
                valid = validate(board, ships[ship][0], x, y, ori)
                if not valid:
                    print "Nao se pode colocar um navio aqui, tente dnv."
                    raw_input("Pressione enter para continuar")
                i += 1

            board = place_ship(board, ships[ship], ship[0], ori, x, y)
            printar_tabuleiro("u", board)

    print "Navios Colocados"
    return board


def cond_vitoria(board):
    funciona = True
    # se tiver algum pedaco de barco ainda dentro do tabuleiro retorn False
    for i in range(10):
        for j in range(10):
            if board[i][j] != -1 and board[i][j] != "X" and board[i][j] != "@":
                funciona = False
    # se nao, retorna True
    return funciona


def cond_afundar(board, x, y):
    # checa a quantidade de pecas no tabuleiro do navio, se nao houver
    # printa afundado
    if board[x][y] == "A":
        ship = "Aircraft Carrier"
    elif board[x][y] == "B":
        ship = "Battleship"
    elif board[x][y] == "S":
        ship = "Submarine"
    elif board[x][y] == "P":
        ship = "Patrol Boat"

    board[-1][ship][0] -= 1
    if board[-1][ship][0] == 0:
        print ship + " Afundado"


def jogada(board, x, y):
    if board[x][y] == -1:
        return "miss"
    elif board[x][y] == "X" or board[x][y] == "@":
        return "tente outra vez"
    else:
        return "hit"


def jogar(board):
    while True:
        x, y = solicitar_coordenada()
        resposta = jogada(board, x, y)
        if resposta == "hit":
            print "Acertou em: " + str(x + 1) + "," + str(y + 1)
            cond_afundar(board, x, y)
            board[x][y] = '@'
            time.sleep(2)
            if cond_vitoria(board):
                return "WIN"
        elif resposta == "miss":
            print "Errou em " + str(x + 1) + "," + str(y + 1)
            board[x][y] = "X"
        elif resposta == "tente outra vez":
            print "Coordenada ja tentada antes, tente novamente"

        if resposta != "tente outra vez":
            return board


def receber_jogada(receptor):
    mensagem = receptor.recv(1024)
    resposta = pickle.loads(mensagem)
    return resposta


def enviar_jogada(board, receptor):
    mensagem = pickle.dumps(board)
    receptor.sendall(mensagem)


def main():
    global receiver
    state = None
    if len(sys.argv) == 1:
        receiver.listen(1)
        porta = receiver.getsockname()[1]
        print "porta que estou esperando a conexao" + str(porta)
        conn, addr = receiver.accept()
        state = 1
    else:
        porta = raw_input("digite a porta fornecida pelo outro player:")
        porta = int(porta)
        receiver.connect(("localhost", porta))
        state = 0

    # dicionario com cada navio e com a quantidade deles e tamanho
    ships = {"Aircraft Carrier": [5, 1],
             "Battleship": [4, 1],
             "Submarine": [3, 3],
             "Patrol Boat": [2, 2]}
    # cria o tabuleiro
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(-1)
        board.append(row)

    # copia o tabuleiro para as variaveis
    user = copy.deepcopy(board)
    enemy = copy.deepcopy(board)
    # Coloca lista de navios no final do tabuleiro (fica mais facil)
    temp = copy.deepcopy(ships)
    user.append(temp)
    enemy.append(temp)
    # pede para o usuario colocar os navios no tabuleiro
    user = colocar_navios(user, ships)
    # se for o cara que foi conectado
    if state == 1:
        mensagem = pickle.dumps(user)
        conn.sendall(mensagem)
        mensagem = conn.recv(1024)
        enemy = pickle.loads(mensagem)
    # se for o cara que conectou
    else:
        msg = receiver.recv(1024)
        enemy = pickle.loads(msg)
        msg = pickle.dumps(user)
        receiver.sendall(msg)

    time.sleep(1)
    print "@ siginifica que acertou e X que errou"
    while(1):
        if state == 1:
            printar_tabuleiro("e", enemy)
            enemy = jogar(enemy)

            if enemy == "WIN":
                print "Voce Ganhou!"
                temp = "WIN"
                if len(sys.argv) == 1:
                    conn.sendall(pickle.dumps(temp))

                else:
                    receiver.sendall(pickle.dumps(temp))
                receiver.close()
                quit()
                
            else:
                if len(sys.argv) == 1:
                    enviar_jogada(enemy, conn)
                else:
                    enviar_jogada(enemy, receiver)
            printar_tabuleiro("e", enemy)
            print "Acabou o turno, Espere a jogada inimiga"
            state = 0

        elif state == 0:
            if len(sys.argv) == 1:
                user = receber_jogada(conn)
            else:
                user = receber_jogada(receiver)

            if user == "WIN":
                print "Ele Ganhou !"
                receiver.close()
                quit()

            printar_tabuleiro("u", user)
            state = 1



if __name__ == '__main__':
    main()
