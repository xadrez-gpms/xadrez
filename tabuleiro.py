from copy import copy, deepcopy
from auxiliares import Coord, Roque, EnPassant

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

BRANCO = 0;
PRETO  = 1;

"""
Dicionário com as torres e rei para movimentação do roque
Torre E -> Torre ao lado esquerdo do Rei (mais distante)
Torre D -> Torre ao lado direito do Rei (mais próxima)
True quando a peça ainda não foi movida
False quando a peça já foi movida
"""

status_roque = {
    "torre_jogador_E": True, # Coord(7, 0)
    "torre_jogador_D": True, # Coord(7, 7)
    "rei_jogador": True, # Coord(7, 4)
    "torre_IA_E": True, # Coord (0, 7)
    "torre_IA_D": True, # Coord (0, 0)
    "rei_IA": True # Coord (0, 4) 
}

status_en_passant = {
    "col_A": False, # Coord(0, ?)
    "col_B": False, # Coord(1, ?)
    "col_C": False, # Coord(2, ?)
    "col_D": False, # Coord(3, ?)
    "col_E": False, # Coord(4, ?)
    "col_F": False, # Coord(5, ?)
    "col_G": False, # Coord(6, ?)
    "col_H": False, # Coord(7, ?)
}

def initTab():
    # atenção para não se confundir no tabuleiro. Eixo vertical está sendo chamado de X e o eixo horizontal de Y.
    tabuleiro = [
        [PT, PC, PB, PQ, PR, PB, PC, PT], # x = 0
        [PP, PP, PP, PP, PP, PP, PP, PP], # x = 1
        [VV, VV, VV, VV, VV, VV, VV, VV], # x = 2
        [VV, VV, VV, VV, VV, VV, VV, VV], # x = 3
        [VV, VV, VV, VV, VV, VV, VV, VV], # x = 4
        [VV, VV, VV, VV, VV, VV, VV, VV], # x = 5
        [BP, BP, BP, BP, BP, BP, BP, BP], # x = 6
        [BT, BC, BB, BQ, BR, BB, BC, BT]  # x = 7
    ]
    return tabuleiro;

def is_branca (type):
    brancas = [BT, BC, BB, BQ, BR, BB, BC, BT, BP];
    if type in brancas:
        return True;
    else:
        return False;
def is_preta (type):
    preta = [PT, PC, PB, PQ, PR, PB, PC, PT, PP];
    if type in preta:
        return True;
    else:
        return False;

def printMovmentosPossiveis(mov):
    print("#########################")
    print("MOVIMENTAÇÕES POSSIVEIS")
    for i in range(len(mov)):
        print(mov[i]);
    print("#########################")

def printMovmentosPossiveisPiece(mov, type):
    print("#########################")
    print("MOVIMENTAÇÕES POSSIVEIS")
    for i in range(len(mov)):
        if mov[i][0] == type: print(mov[i]);
    print("#########################")
def verificaEmpate(tab):
    brancas = [];
    pretas  = [];
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if is_branca(tab[i][j]):
                brancas.append(tab[i][j]);
            if is_preta(tab[i][j]):
                pretas.append(tab[i][j]);
    if len(brancas) <= 1 or len(pretas) <= 1:
        return True;

def printTabuleiro(tab):
    tabStr = "";
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tabStr = tabStr + str(tab[i][j]) + "\t";
        tabStr = tabStr + "\n";
    print(tabStr);

def auxiliarCasoRoque(tab, type, x_ori, y_ori, x_dest, y_dest):

    if(y_ori == 4): # posição inicial do rei
        otherType = getPeca(tab, x_dest, y_dest);
        res = None;

        if(x_ori == 0 and status_roque.get("rei_IA")): # Validar se roque está disponível
            res = verificaRoque(tab, type, otherType, Coord(x_dest, y_dest));
        elif(x_ori == 7 and status_roque.get("rei_jogador")): 
            res = verificaRoque(tab, type, otherType, Coord(x_dest, y_dest));

        if(res == Roque.PEQUENO or res == Roque.GRANDE):
            return True;
        else:
            return False;
    else:
        return False;

def verificaMovRei (tab, type, x_ori, y_ori, x_dest, y_dest):
    
    if ((abs(x_dest - x_ori) == 1 and abs(y_dest - y_ori) == 1) 
        or (abs(x_dest - x_ori) == 0 and abs(y_dest - y_ori) == 1)
        or (abs(x_dest - x_ori) == 1 and abs(y_dest - y_ori) == 0)
        ):
        return True;

    return False;

def verificaMovCavalo (tab, type, x_ori, y_ori, x_dest, y_dest):
    return (abs(x_dest - x_ori) == 2 and abs(y_dest - y_ori) == 1) or (abs(x_dest - x_ori) == 1 and abs(y_dest - y_ori) == 2);

def verificaMovTorre(tab, type, x_ori, y_ori, x_dest, y_dest):
    return verificaMovReto(tab, type, x_ori, y_ori, x_dest, y_dest)

def verificaMovBispo(tab, type, x_ori, y_ori, x_dest, y_dest):
    return verificaMovDiagonal(tab, type, x_ori, y_ori, x_dest, y_dest)

def verificaMovDiagonal(tab, type, x_ori, y_ori, x_dest, y_dest):
    x_direction = 1 if x_ori < x_dest else -1;
    y_direction = 1 if y_ori < y_dest else -1;
    if abs(x_ori - x_dest) != abs(y_ori - y_dest):
        return False;
    for i in range (abs(x_ori - x_dest)):
        x = x_ori + (i * x_direction);
        y = y_ori + (i * y_direction);
        if x == x_ori and y == y_ori: continue; #quando i for 1 o valor de x e y sao iguais ao originais
        if getPeca(tab, x, y) != VV: #verifica se todas as casas ate o dest estao vazias
            return False;
    return True;

def verificaMovReto(tab, type, x_ori, y_ori, x_dest, y_dest):
    direction = 1;
    if y_ori == y_dest: #anda em x
        if x_ori > x_dest: direction = -1;  # verifica direcao
        for i in range(x_ori + direction, x_dest, direction):
            if not checaPeca(tab, VV, i, y_dest): #verifica se esta vazio ate a penultima posição
                return False
        return True;
    elif x_ori == x_dest: #anda em y
        if y_ori > y_dest: direction = -1;  # verifica direcao
        for i in range(y_ori + direction, y_dest, direction):
            if not checaPeca(tab, VV, x_dest, i): #verifica se esta vazio ate a penultima posição
                return False
        return True;
    return False;

def verificaMovPeao(tab, type, x_ori, y_ori, x_dest, y_dest):
    if y_ori == y_dest:  # movimentação normal para frente
        limit = 1;
        if (is_branca(type) and x_ori == 6) or \
                (is_preta(type) and x_ori == 1):  # se for primeira rodada anda ate 2
            limit = 2;
        if (is_branca(type) and x_dest - x_ori >= (limit * -1) and x_dest < x_ori) or (
                is_preta(type) and x_dest - x_ori <= limit and x_dest > x_ori):  # verifica se esta dentro do limite
            movLen = x_dest - x_ori;
            if tab[x_dest][y_dest] == VV:  # verifica se a casa final esta vazia
                if movLen == 2 or movLen == -2: # caso seja movimento duplo
                    if tab[x_ori + int(movLen / 2)][y_dest] == VV:  # verifica se a casa intermediaria esta vazia
                        return True;  # peça anda para frente 2 casas
                else:
                    return True;  # peça anda para frente 1 casa
    elif (y_dest == y_ori + 1 or y_dest == y_ori - 1): # Destino é movimentação para comer peça inimiga
       if(tab[x_dest][y_dest] != VV):  # verifica se o tipo de peca da posicao de destino e uma peca inimiga
           if (is_branca(type) and x_dest - x_ori == -1) or (is_preta(type) and x_dest - x_ori == 1): #andando pra frente no eixo X
               return True;  # peca comida
       else: #destino é casa vazia, só pode movimentar se for En Passant
           return verificaEnPassant(tab, type, Coord(x_ori, y_ori));
    return False;  # movimento invalido

def promocaoPeao(type, y): # TODO implementar escolha
    if type != PP and type != BP: return False;
    if (is_branca(type) and y == 0) or (is_preta(type) and y == 7):
       return True;
    return False;

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def getPeca(tab, x,y):
    return tab[x][y]

def setPeca(tab,type, x,y):
    tab[x][y] = type;

def checaPeca(tab, type, x, y):
    if getPeca(tab,x,y) == type:
        return True;
    return False;

def movimentosPossiveis(tab):
    arr = [];
    for x_ori in range(len(tab)):
        for y_ori in range(len(tab[x_ori])):
            if tab[x_ori][y_ori] != VV:
                piece = getPeca(tab, x_ori, y_ori);
                for x_dest in range(len(tab)):
                    for y_dest in range(len(tab[x_ori])):
                        if checaMovimentaPeça(tab, piece, x_ori, y_ori, x_dest, y_dest):
                            arr.append([piece, x_ori, y_ori, x_dest, y_dest]);
    return arr;

def checaMovimentaPeça(tab, type, x_ori, y_ori, x_dest, y_dest):

    if not checaPeca(tab, type, x_ori, y_ori) : return False; #tenta movimentar outra peca
    if x_dest > 7 or x_dest < 0 or y_dest > 7 or x_dest < 0 : return False; # se sair do tabuleiro
    if x_ori == x_dest and y_ori == y_dest : return False;       # peca fica nomesmo lugar;
    if (type != BR and type != PR):
        if(getPeca(tab, x_dest, y_dest) != VV 
        and (is_branca(getPeca(tab, x_ori, y_ori)) == is_branca(getPeca(tab, x_dest, y_dest)))
        ):
            return False; #nao deixa sobrepor peca aliada
    elif(type == BR):
        destPeca = getPeca(tab, x_dest, y_dest);
        if(destPeca == BT): # caso de roque
            return auxiliarCasoRoque(tab, type, x_ori, y_ori, x_dest, y_dest);
        elif(destPeca != VV
             and (is_branca(getPeca(tab, x_ori, y_ori)) == is_branca(getPeca(tab, x_dest, y_dest)))
            ):
            return False;
    elif(type == PR):
        destPeca = getPeca(tab, x_dest, y_dest);
        if(destPeca == PT): # caso de roque
            return auxiliarCasoRoque(tab, type, x_ori, y_ori, x_dest, y_dest);
        elif(destPeca != VV
             and (is_branca(getPeca(tab, x_ori, y_ori)) == is_branca(destPeca))
             ):
            return False;

    if   (type == BP or type == PP):
        ver = verificaMovPeao(tab, type, x_ori, y_ori, x_dest, y_dest);
        if(ver == True):
            return True;
        elif(ver == EnPassant.ESQUERDA or ver == EnPassant.DIREITA):
            return ver;
    elif (type == BT or type == PT) and verificaMovTorre(tab, type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BB or type == PB) and verificaMovBispo(tab, type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BC or type == PC) and verificaMovCavalo(tab, type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BR or type == PR) and verificaMovRei(tab, type, x_ori, y_ori, x_dest, y_dest):
            return True;
    elif (type == BQ or type == PQ): #rainha
        if x_ori == x_dest or y_ori == y_dest:
            if verificaMovTorre(tab, type, x_ori, y_ori, x_dest, y_dest):
                return True;
        else:
            if verificaMovBispo(tab, type, x_ori, y_ori, x_dest, y_dest):
                return True;

def verificaXeque(tab, movs, game_round):
    for i in range(len(movs)):
        piece = movs[i][0];
        x_dest = movs[i][3];
        y_dest = movs[i][4];
        if (is_branca(piece) and game_round == BRANCO) or (is_preta(piece) and game_round == PRETO):
            if is_preta(piece) and tab[x_dest][y_dest] == BR :
                return True;
            elif is_branca(piece) and tab[x_dest][y_dest] == PR:
                return True;
    return False

def verificaXequeMate(tab, movs, game_round):
    tabAux = deepcopy(tab);
    nextRound = PRETO if game_round == BRANCO else BRANCO;
    for i in range(len(movs)):
        piece = movs[i][0];
        x_ori = movs[i][1];
        y_ori = movs[i][2];
        x_dest = movs[i][3];
        y_dest = movs[i][4];
        if (is_branca(piece) and nextRound == BRANCO) or (is_preta(piece) and nextRound == PRETO):
            setPeca(tabAux,VV, x_ori, y_ori);
            setPeca(tabAux, piece, x_dest, y_dest);
            newMov = movimentosPossiveis(tabAux);
            if not verificaXeque(tabAux, newMov, game_round) :
                return False;
            else:
                tabAux = deepcopy(tab);

    return True

def movimentaPeca(tab, type, x_ori, y_ori, x_dest, y_dest):
    if(movimentaPecasRoque(tab, type, x_ori, y_ori, x_dest, y_dest)): # movimento foi 1 roque
        ajustarStatusEnPassant();
        return True;

    aux = checaMovimentaPeça(tab, type, x_ori, y_ori, x_dest, y_dest);
    if (aux == True):
        setPeca(tab, VV, x_ori, y_ori);
        setPeca(tab, type, x_dest, y_dest);
        if(type == BR or type == PR or type == BT or type == PT): # Se for movimentação da torre ou do rei, ajusta o dicionário para o roque
            ajustaStatusRoque(type, Coord(x_ori, y_ori));
        elif((type == BP or type == PB) and ((x_dest - x_ori) == 2 or (x_dest - x_ori) == -2)): # movimento abre espaço para En Passant
            ajustarStatusEnPassant();
            status_en_passant.update({"col_{}".format(chr(65+(y_ori))): True});
            return True;
        ajustarStatusEnPassant();
        return True;
    elif(aux == EnPassant.ESQUERDA):
        setPeca(tab, VV, x_ori, y_ori);
        setPeca(tab, VV, x_ori, y_ori-1);
        setPeca(tab, type, x_dest, y_dest);
        ajustarStatusEnPassant();
        return True;
    elif(aux == EnPassant.DIREITA):
        setPeca(tab, VV, x_ori, y_ori);
        setPeca(tab, type, x_dest, y_dest);
        setPeca(tab, VV, x_ori, y_ori+1);
        ajustarStatusEnPassant();
        return True;

    return False;

# Roque, por definição, é uma movimentação do Rei. Logo só será implementado sua funcionalidade a partir do rei.
def movimentaPecasRoque(tab, type, x_ori, y_ori, x_dest, y_dest): 
    
    otherType = getPeca(tab, x_dest, y_dest);
    otherTab = tab;
    
    if(type != PR and type != BR): #clique inicial no rei, peça no destino deve ser uma torre
        return False;
    if(otherType != PT and otherType != BT):
        return False;

    tipoRoque = verificaRoque(otherTab, type, otherType, Coord(x_dest, y_dest));
    turno = None;

    if(type == PR and otherType == PT): # roque preto
        turno = "Preto";

        if(tipoRoque == Roque.PEQUENO):
            # rei
            setPeca(otherTab, type, x_dest, y_dest-1); 
            setPeca(otherTab, VV, x_ori, y_ori);
            # torre
            setPeca(otherTab, otherType, x_dest, y_dest-2);
            setPeca(otherTab, VV, x_dest, y_dest);

        elif(tipoRoque == Roque.GRANDE):
            # rei
            setPeca(otherTab, type, x_ori, y_ori-2); 
            setPeca(otherTab, VV, x_ori, y_ori);
            # torre
            setPeca(otherTab, otherType, x_ori, y_ori-1);
            setPeca(otherTab, VV, x_dest, y_dest);

        else: 
            return False;

    elif(type == BR and otherType == BT): # roque branco
        turno = "Branco";

        if(tipoRoque == Roque.PEQUENO):
            # rei
            setPeca(otherTab, type, x_dest, y_dest-1); 
            setPeca(otherTab, VV, x_ori, y_ori);
            # torre
            setPeca(otherTab, otherType, x_dest, y_dest-2);
            setPeca(otherTab, VV, x_dest, y_dest);

        elif(tipoRoque == Roque.GRANDE):
            # rei
            setPeca(otherTab, type, x_ori, y_ori-2); 
            setPeca(otherTab, VV, x_ori, y_ori);
            # torre
            setPeca(otherTab, otherType, x_ori, y_ori-1);
            setPeca(otherTab, VV, x_dest, y_dest);

        else: 
            return False;

    otherMoves = movimentosPossiveis(otherTab);
    if(verificaXeque(otherTab, otherMoves, turno)):
        return False;
    print("{}: {} Roque!".format(turno, "Grande" if tipoRoque == Roque.GRANDE else "Pequeno"));
    tab = otherTab;
    return True;

def ajustaStatusRoque(peca, start_pos):
    if(peca != BR or peca != PR or peca != BT or peca != PT): # Se a peça não for rei ou peão sai do método
        return;
    if(start_pos.x == 0): # Linha inicial das peças pretas
        if(peca == PR): #Rei Preto
            if(start_pos.y == 4 and status_roque.get("rei_IA")): # Rei Preto foi movimentado
                status_roque.update({"rei_IA": False});
                return;
        elif(peca == PT): #Torre Preta
            if(start_pos.y == 7 and status_roque.get("torre_IA_E")):
                status_roque.update({"torre_IA_E": False});
                return;
            elif(start_pos.y == 0 and status_roque.get("torre_IA_D")):
                status_roque.update({"torre_IA_D": False});
                return;
    elif(start_pos.x == 7): # Linha inicial das peças brancas
        if(peca == BR): #Rei Branco
            if(start_pos.y == 4 and status_roque.get("rei_jogador")): # Rei Branco foi movimentado
                status_roque.update({"rei_jogador": False});
                return;
        elif(peca == BT): #Torre Branca
            if(start_pos.y == 7 and status_roque.get("torre_jogador_D")):
                status_roque.update({"torre_jogador_D": False});
                return;
            elif(start_pos.y == 0 and status_roque.get("torre_jogador_E")):
                status_roque.update({"torre_jogador_E": False});
                return;
    # print(status_roque); # print utilizado para debug | usar quando for implementar o roque
    return;


def verificaRoque(tab, rei, torre, pos_torre: Coord):
   
    if(rei != BR and rei != PR):
        return False; # Não chegou um Rei
    elif(torre != PT and torre != BT):
        return False; # Não chegou torre
    
    if(rei == BR):
        if(not status_roque.get("rei_jogador")):
            return False; # Rei Branco já foi movido
        else:
            if(pos_torre.x != 7):
                return False; # Torre Branca fora da coluna inicial
            else:
                if(pos_torre.y == 0 and status_roque.get("torre_jogador_E")
                   and (getPeca(tab, 7, 1) == VV) and (getPeca(tab, 7, 2) == VV) and getPeca(tab, 7, 3) == VV):
                    return Roque.GRANDE; # Grande Roque para o Jogador (peças brancas)
                elif(pos_torre.y == 7 and status_roque.get("torre_jogador_D")
                     and (getPeca(tab, 7, 5) == VV) and (getPeca(tab, 7, 6) == VV)):
                    return Roque.PEQUENO; # Pequeno Roque para o Jogador (peças brancas)

    else:
        if(not status_roque.get("rei_IA")):
            return False; # Rei Preto já foi movido
        else:
            if(pos_torre.x != 0):
                return False; # Torre Preta fora da coluna inicial
            else:
                if(pos_torre.y == 0 and status_roque.get("torre_IA_E")
                   and (getPeca(tab, 0, 1) == VV) and (getPeca(tab, 0, 2) == VV) and getPeca(tab, 0, 3) == VV):
                    return Roque.GRANDE; # Grande Roque para a IA (peças pretas)
                elif(pos_torre.y == 7 and status_roque.get("torre_IA_D")
                     and (getPeca(tab, 0, 5) == VV) and (getPeca(tab, 0, 6) == VV)):
                    return Roque.PEQUENO; # Pequeno Roque para a IA (peças pretas)
    
    return False;

def ajustarStatusEnPassant():
    for i in range(8):
        if(status_en_passant.get("col_{}".format(chr(i+65))) != False): # Coluna i está com o En Passant disponível para ela
            status_en_passant.update({"col_{}".format(chr(i+65)): False});
            print("En Passant da col_{} não está mais disponível!".format(chr(i+65)));

def verificaEnPassant(tab, peao, pos_peao: Coord):
    left = False;
    right = False;
    cor = None;

    if(peao == PP):
        cor = PRETO;
    else:
        cor = BRANCO;

    if(pos_peao.y == 0):
        right = True;
    elif(pos_peao.y == 7):
        left = True;
    else:
        right = left = True;

    if(right): # verifica se a peça à direita é o peão para o En Passant
        dir = getPeca(tab, pos_peao.x, pos_peao.y+1);
        if(cor == BRANCO 
           and dir == PP
           and status_en_passant.get("col_{}".format(chr(65+(pos_peao.y+1))))
        ):
                return EnPassant.DIREITA;
        elif(cor == PRETO
           and dir == BP
           and status_en_passant.get("col_{}".format(chr(65+(pos_peao.y+1))))
        ):
                return EnPassant.DIREITA;

    if(left): # verifica se a peça à esquerda é o peão para o En Passant
        esq = getPeca(tab, pos_peao.x, pos_peao.y-1);
        if(cor == BRANCO 
           and esq == PP
           and status_en_passant.get("col_{}".format(chr(65+(pos_peao.y-1))))
        ):
                return EnPassant.ESQUERDA;
        elif(cor == PRETO
           and esq == BP
           and status_en_passant.get("col_{}".format(chr(65+(pos_peao.y-1))))
        ):
                return EnPassant.ESQUERDA;

    return False;