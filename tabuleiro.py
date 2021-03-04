# peças brancas (1x)
BP = "BP";  # piao
BB = "BB";  # biscpo
BT = "BT";  # torre
BC = "BC";  # cavalo
BQ = "BQ";  # rainha
BR = "BR";  # rei

# peças pretas (2x)
PP = "PP";  # piao
PB = "PB";  # biscpo
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

def is_branca(type):
    brancas = [BT, BC, BB, BQ, BR, BB, BC, BT, BP];
    if (type in brancas):
        return True;
    else:
        return False;

def printTabuleiro(tab):
    tabStr = "";
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tabStr = tabStr + str(tab[i][j]) + "\t";
        tabStr = tabStr + "\n";
    print(tabStr);

def verificaMovTorre(type, x_ori, y_ori, x_dest, y_dest):
    global tabuleiro;
    direction = 1;
    if is_branca(type): direction = -1; #verifica direcao
    if y_ori == y_dest: #anda em x
        for i in range(x_ori + direction, x_dest, direction):
            if not checaPeca(VV, i, y_dest): #verifica se esta vazio ate a penultima posição
                return False
        return True;
    elif x_ori == x_dest: #anda em y
        for i in range(y_ori + 1, y_dest, direction):
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
    elif y_dest == y_ori + 1 or y_dest == y_ori - 1 and tabuleiro[x_dest][y_dest] != VV :  # verifica se o tipo de peca da posicao de destino e uma peca inimiga
        if (is_branca(type) and x_dest - x_ori == -1) or (not is_branca(type) and x_dest - x_ori == 1): #andando pra frente no eixo X
            return True;  # peca comida
    return False;  # movimento invalido

def promocaoPeao(type, x, y): #implementar escolha
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
    global tabuleiro;
    if tabuleiro[x][y] == type: return True;
    return False;

def movimentaPeca(type, x_ori, y_ori, x_dest, y_dest):
    global numJog, tabuleiro

    if not checaPeca(type, x_ori, y_ori) : return False; #tenta movimentar outra peca
    if x_dest > 7 or x_dest < 0 or y_dest > 7 or x_dest < 0 : return False; # se sair do tabuleiro
    if x_ori == x_dest and y_ori == y_dest : return False;       # peca fica nomesmo lugar;
    if getPeca(x_dest, y_dest) != VV and (is_branca(getPeca(x_ori, y_ori)) == is_branca(getPeca(x_dest, y_dest))):
        return False; #nao deixa sobrepor peca aliada

    if type == BP or type == PP:
        if verificaMovPeao(type, x_ori, y_ori, x_dest, y_dest):
            setPeca(VV, x_ori, y_ori);
            setPeca(type, x_dest, y_dest);
            promocaoPeao(type, x_dest, y_dest);
            return True;
    if type == BT or type == PT:
        if verificaMovTorre(type, x_ori, y_ori, x_dest, y_dest):
            setPeca(VV, x_ori, y_ori);
            setPeca(type, x_dest, y_dest);
            return True;

    return False;


print(movimentaPeca(BP, 6, 1, 5, 1));
print(movimentaPeca(PP, 1, 1, 2, 1));

print(movimentaPeca(BP, 6, 0, 4, 0));
print(movimentaPeca(PP, 1, 0, 3, 0));
print(movimentaPeca(PP, 3, 0, 1, 0));
#setPeca(VV, 4, 0);
print(movimentaPeca(BT, 7, 0, 5, 0));
printTabuleiro(tabuleiro);
