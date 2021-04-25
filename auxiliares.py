# Documento responsavel por conter classes e/ou funcoes auxiliares
# TODO escrever controlador de logica para estruturar melhor o projeto
from enum import Enum

class Coord: # Classe auxiliar
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class SceneState(Enum):
    Empty = 0,
    Created = 1,
    Initialized = 2,
    Loaded = 3,
    Running = 4,
    Awaiting = 5,
    ToBeDestroyed = 6

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

    def converteDeTabuleiro(cor_tab):
        if(cor_tab == 0):
            return CorPeca.Branca;
        elif(cor_tab == 1):
            return CorPeca.Preta;
        else:
            return None;

class Peca: 
    def __init__(self, tipo: TipoPeca, cor: CorPeca, coord: Coord):
        self.type = TipoPeca(tipo);
        self.cor = CorPeca(cor); 
        self.pos = Coord(coord.x, coord.y);
        self.lastPos = Coord(coord.x, coord.y);

    def convertePecaParaTipoTabuleiro(tipo: TipoPeca, cor: CorPeca):
        
        if(tipo == TipoPeca.Peao):
            if(cor == CorPeca.Branca):
                return "BP";
            else:
                return "PP";

        elif(tipo == TipoPeca.Bispo):
            if(cor == CorPeca.Branca):
                return "BB";
            else:
                return "PB";

        elif(tipo == TipoPeca.Cavalo):
            if(cor == CorPeca.Branca):
                return "BC";
            else:
                return "PC";

        elif(tipo == TipoPeca.Torre):
            if(cor == CorPeca.Branca):
                return "BT";
            else:
                return "PT";

        elif(tipo == TipoPeca.Rainha):
            if(cor == CorPeca.Branca):
                return "BQ";
            else:
                return "PQ";

        elif(tipo == TipoPeca.Rei):
            if(cor == CorPeca.Branca):
                return "BR";
            else:
                return "PR";
        else:
            return None;
    
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

    def __init__(self, pos_ini: Coord, pos_fin: Coord, peca: str):
        self.pos_fin = Coord(pos_fin.x, pos_fin.y);
        self.peca = Peca(Peca.descobreTipoPeca(peca), Peca.descobreCorPeca(peca), pos_ini);
    