# Documento respons�vel por conter classes e/ou fun��es auxiliares
# TODO escrever controlador de l�gica para estruturar melhor o projeto
from enum import Enum

class Coord: # Classe auxiliar
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class TipoPeca(Enum):
    Peao = 100,
    Bispo = 301,
    Cavalo = 302,
    Torre = 500,
    Rainha = 900,
    Rei = 1500

class CorPeca(Enum):
    Preta = True,
    Branca = False

class Peca: 
    def __init__(self, tipo: TipoPeca, cor: CorPeca, coord: Coord):
        self.type = TipoPeca(tipo);
        self.cor = CorPeca(cor); 
        self.pos = Coord(coord.x, coord.y);
        self.lastPos = Coord(coord.x, coord.y);
    
    def descobreTipoPeca(tipo):

        if(tipo == '00'):
            return None;
        elif(tipo[1] == 'P'):
            return TipoPeca.Peao;
        elif(tipo[1] == 'B'):
            return TipoPeca.Bispo;
        elif(tipo[1] == 'C'):
            return TipoPeca.Cavalo;
        elif(tipo[1] == 'T'):
            return TipoPeca.Torre;
        elif(tipo[1] == 'Q'):
            return TipoPeca.Rainha;
        else:
            return TipoPeca.Rei;

    def descobreCorPeca(peca):
        
        peca_string = str(peca);
        
        if(peca == '00'):
            return None;
        elif(peca[0] == 'B'):
            return CorPeca.Branca;
        else:
            return CorPeca.Preta;

class AuxiliarCacheMovimentacao:

    def printMe(self):
        self.peca.printMe();
        print("\nPosição Final: ({},{})".format(self.pos_fin.x, self.pos_fin.y));

    def __init__(self, pos_ini: Coord, pos_fin: Coord, peca: str):
        self.pos_fin = Coord(pos_fin.x, pos_fin.y);
        self.peca = Peca(Peca.descobreTipoPeca(peca), Peca.descobreCorPeca(peca), pos_ini);
    