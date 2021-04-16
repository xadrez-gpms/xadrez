# Documento responsável por conter classes e/ou funções auxiliares
# TODO escrever controlador de lógica para estruturar melhor o projeto
from enum import Enum

class Coord: # Classe auxiliar
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class TipoPeca(Enum):
    Peao = 100,
    Bispo = 300,
    Cavalo = 300,
    Torre = 500,
    Rainha = 900,
    Rei = 1500

class CorPeca(Enum):
    Preta = True,
    Branca = False

class Peca: 
    def __init__(self, tipo, cor, coord):
        self.type = TipoPeca(tipo);
        self.cor = CorPeca(cor); 
        self.pos = Coord(coord.x, coord.y);
        self.lastPos = Coord(coord.x, coord.y);

    