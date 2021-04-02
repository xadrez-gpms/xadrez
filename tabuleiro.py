# peças brancas (1x)
BP = "BP";  # peao
BB = "BB";  # bispo
BT = "BT";  # torre
BC = "BC";  # cavalo
BQ = "BQ";  # rainha
BR = "BR";  # rei

# peças pretas (2x)
PP = "PP";  # peao
PB = "PB";  # bispo
PT = "PT";  # torre
PC = "PC";  # cavalo
PQ = "PQ";  # rainha
PR = "PR";  # rei

VV = "00";  # vazio
tabuleiro = [
    [PT, PC, PB, PQ, PR, PB, PC, PT],
    [PP, PP, PP, PP, PP, PP, PP, PP],
    [VV, VV, VV, VV, VV, VV, VV, VV],
    [VV, VV, VV, VV, VV, VV, VV, VV],
    [VV, VV, VV, VV, VV, VV, VV, VV],
    [VV, VV, VV, VV, VV, VV, VV, VV],
    [BP, BP, BP, BP, BP, BP, BP, BP],
    [BT, BC, BB, BQ, BR, BB, BC, BT]
]
def getTab():
    return tabuleiro;

def is_branca (type):
    brancas = [BT, BC, BB, BQ, BR, BB, BC, BT, BP];
    if type in brancas:
        return True;
    else:
        return False;

def printMovmentosPossiveis(mov):
    print("#########################")
    print("MOVIMENTAÇÕES POSSIVEIS")
    for i in range(len(mov)):
        print(mov[i]);
    print("#########################")

def printTabuleiro(tab):
    tabStr = "";
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tabStr = tabStr + str(tab[i][j]) + "\t";
        tabStr = tabStr + "\n";
    print(tabStr);

def verificaMovRei (type, x_ori, y_ori, x_dest, y_dest):
    return (abs(x_dest - x_ori) == 1 and abs(y_dest - y_ori) == 1) or (abs(x_dest - x_ori) == 0 and abs(y_dest - y_ori) == 1) or (abs(x_dest - x_ori) == 1 and abs(y_dest - y_ori) == 0);

def verificaMovCavalo (type, x_ori, y_ori, x_dest, y_dest):
    return (abs(x_dest - x_ori) == 2 and abs(y_dest - y_ori) == 1) or (abs(x_dest - x_ori) == 1 and abs(y_dest - y_ori) == 2);

def verificaMovTorre(type, x_ori, y_ori, x_dest, y_dest):
    return verificaMovReto(type, x_ori, y_ori, x_dest, y_dest)

def verificaMovBispo(type, x_ori, y_ori, x_dest, y_dest):
    return verificaMovDiagonal(type, x_ori, y_ori, x_dest, y_dest)

def verificaMovDiagonal(type, x_ori, y_ori, x_dest, y_dest):
    x_direction = 1 if x_ori < x_dest else -1;
    y_direction = 1 if y_ori < y_dest else -1;
    if abs(x_ori - x_dest) != abs(y_ori - y_dest):
        return False;
    for i in range (abs(x_ori - x_dest)):
        x = x_ori + (i * x_direction);
        y = y_ori + (i * y_direction);
        if x == x_ori and y == y_ori: continue; #quando i for 1 o valor de x e y sao iguais ao originais
        if getPeca(x, y) != VV: #verifica se todas as casas ate o dest estao vazias
            return False;
    return True;

def verificaMovReto(type, x_ori, y_ori, x_dest, y_dest):
    global tabuleiro;
    direction = 1;
    if y_ori == y_dest: #anda em x
        if x_ori > x_dest: direction = -1;  # verifica direcao
        for i in range(x_ori + direction, x_dest, direction):
            if not checaPeca(VV, i, y_dest): #verifica se esta vazio ate a penultima posição
                return False
        return True;
    elif x_ori == x_dest: #anda em y
        if y_ori > y_dest: direction = -1;  # verifica direcao
        for i in range(y_ori + direction, y_dest, direction):
            if not checaPeca(VV, x_dest, i): #verifica se esta vazio ate a penultima posição
                return False
        return True;
    return False;

def verificaMovPeao(type, x_ori, y_ori, x_dest, y_dest):
    global tabuleiro;
    if y_ori == y_dest:  # movimentação normal para frente
        limit = 1;
        if (is_branca(type) and x_ori == 6) or \
                (not is_branca(type) and x_ori == 1):  # se for primeira rodada anda ate 2
            limit = 2;
        if (is_branca(type) and x_dest - x_ori >= (limit * -1) and x_dest < x_ori) or (
                not is_branca(type) and x_dest - x_ori <= limit and x_dest > x_ori): #verifica se esta dentro do limite
            if tabuleiro[x_dest][y_dest] == VV:  # verifica se a casa esta vazia
                return True;  # peça anda simples
    elif (y_dest == y_ori + 1 or y_dest == y_ori - 1) and tabuleiro[x_dest][y_dest] != VV:  # verifica se o tipo de peca da posicao de destino e uma peca inimiga
        if (is_branca(type) and x_dest - x_ori == -1) or (not is_branca(type) and x_dest - x_ori == 1): #andando pra frente no eixo X
            return True;  # peca comida
    return False;  # movimento invalido

def promocaoPeao(type, x, y): #implementar escolha
    if type != PP or type != BP: return;
    if is_branca(type) and x == 7 :
        tabuleiro[x][y] == BQ;
    elif not is_branca(type) and x == 0 :
        tabuleiro[x][y] == PQ;

def getPeca(x,y):
    global tabuleiro;
    return tabuleiro[x][y]

def setPeca(type, x,y):
    global tabuleiro;
    tabuleiro[x][y] = type;

def checaPeca(type, x, y):
    if getPeca(x,y) == type:
        return True;
    return False;

def movimentosPossiveis(tab):
    arr = [];
    for x_ori in range(len(tab)):
        for y_ori in range(len(tab[x_ori])):
            if tabuleiro[x_ori][y_ori] != VV:
                piece = getPeca(x_ori, y_ori);
                for x_dest in range(len(tab)):
                    for y_dest in range(len(tab[x_ori])):
                        if checaMovimentaPeça(piece, x_ori, y_ori, x_dest, y_dest):
                            arr.append([piece, x_ori, y_ori, x_dest, y_dest]);
    return arr;

def checaMovimentaPeça(type, x_ori, y_ori, x_dest, y_dest):
    if   (type == BP or type == PP) and verificaMovPeao(type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BT or type == PT) and verificaMovTorre(type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BB or type == PB) and verificaMovBispo(type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BC or type == PC) and verificaMovCavalo(type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BR or type == PR) and verificaMovRei(type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BQ or type == PQ): #rainha
        if x_ori == x_dest or y_ori == y_dest:
            if verificaMovTorre(type, x_ori, y_ori, x_dest, y_dest):
                return True;
        else:
            if verificaMovBispo(type, x_ori, y_ori, x_dest, y_dest):
                return True;

def movimentaPeca(type, x_ori, y_ori, x_dest, y_dest):
    global tabuleiro

    if not checaPeca(type, x_ori, y_ori) : return False; #tenta movimentar outra peca
    if x_dest > 7 or x_dest < 0 or y_dest > 7 or x_dest < 0 : return False; # se sair do tabuleiro
    if x_ori == x_dest and y_ori == y_dest : return False;       # peca fica nomesmo lugar;
    if getPeca(x_dest, y_dest) != VV and (is_branca(getPeca(x_ori, y_ori)) == is_branca(getPeca(x_dest, y_dest))):
        return False; #nao deixa sobrepor peca aliada

    if checaMovimentaPeça(type, x_ori, y_ori, x_dest, y_dest):
        setPeca(VV, x_ori, y_ori);
        setPeca(type, x_dest, y_dest);
        promocaoPeao(type, x_dest, y_dest);
        return True;

    return False;

