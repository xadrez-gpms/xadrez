# Documento responsavel por conter classes e/ou funcoes auxiliares
# TODO escrever controlador de logica para estruturar melhor o projeto
from enum import Enum

class Coord: # Classe auxiliar
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class SceneState(Enum):
    EMPTY = 0,
    CREATED = 1,
    INITIALIZED = 2,
    LOADED = 3,
    RUNNING = 4,
    AWAITING = 5,
    TO_BE_DESTROYED = 6

class Roque(Enum):
    PEQUENO = 0,
    GRANDE = 1

class TipoPeca(Enum):
    PEAO = 100,
    BISPO = 301,
    CAVALO = 302,
    TORRE = 500,
    RAINHA = 900,
    REI = 1500

class GameMode(Enum):
    MENU = 0,
    PLAYER_VS_PLAYER = 1,
    PLAYER_VS_IA = 2,
    IA_VS_IA = 3

class CorPeca(Enum):
    PRETA = True,
    BRANCA = False

    def converteDeTabuleiro(cor_tab):
        if(cor_tab == 0):
            return CorPeca.BRANCA;
        elif(cor_tab == 1):
            return CorPeca.PRETA;
        else:
            return None;

class Peca: 
    def __init__(self, tipo: TipoPeca, cor: CorPeca, coord: Coord):
        self.type = TipoPeca(tipo);
        self.cor = CorPeca(cor); 
        self.pos = Coord(coord.x, coord.y);
        self.lastPos = Coord(coord.x, coord.y);

    def convertePecaParaTipoTabuleiro(tipo: TipoPeca, cor: CorPeca):
        
        if(tipo == TipoPeca.PEAO):
            if(cor == CorPeca.BRANCA):
                return "BP";
            else:
                return "PP";

        elif(tipo == TipoPeca.BISPO):
            if(cor == CorPeca.BRANCA):
                return "BB";
            else:
                return "PB";

        elif(tipo == TipoPeca.CAVALO):
            if(cor == CorPeca.BRANCA):
                return "BC";
            else:
                return "PC";

        elif(tipo == TipoPeca.TORRE):
            if(cor == CorPeca.BRANCA):
                return "BT";
            else:
                return "PT";

        elif(tipo == TipoPeca.RAINHA):
            if(cor == CorPeca.BRANCA):
                return "BQ";
            else:
                return "PQ";

        elif(tipo == TipoPeca.REI):
            if(cor == CorPeca.BRANCA):
                return "BR";
            else:
                return "PR";
        else:
            return None;
    
    def descobreTipoPeca(tipo):

        if(tipo == '00'):
            return None;
        elif(tipo[1] == 'P'):
            return TipoPeca.PEAO;
        elif(tipo[1] == 'B'):
            return TipoPeca.BISPO;
        elif(tipo[1] == 'C'):
            return TipoPeca.CAVALO;
        elif(tipo[1] == 'T'):
            return TipoPeca.TORRE;
        elif(tipo[1] == 'Q'):
            return TipoPeca.RAINHA;
        else:
            return TipoPeca.REI;

    def descobreCorPeca(peca):
        
        peca_string = str(peca);
        
        if(peca == '00'):
            return None;
        elif(peca[0] == 'B'):
            return CorPeca.BRANCA;
        else:
            return CorPeca.PRETA;

class AuxiliarCacheMovimentacao:

    def __init__(self, pos_ini: Coord, pos_fin: Coord, peca: str):
        self.pos_fin = Coord(pos_fin.x, pos_fin.y);
        self.peca = Peca(Peca.descobreTipoPeca(peca), Peca.descobreCorPeca(peca), pos_ini);
    