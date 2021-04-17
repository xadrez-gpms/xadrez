import tabuleiro
from auxiliares import AuxiliarCacheMovimentacao, Coord

# dicionário com o valor das peças para cálculo da ia
valor_pecas = {
    "peao": 100,
    "bispo": 300,
    "cavalo": 300,
    "torre": 500,
    "rainha": 900,
    "rei": 1500
}

class ai_module:

    def estruturarCache(self, cache):
        resultado = [];
        for elemento in cache: # elemento -> ['PC', 0, 1, 2, 0]
                atual = AuxiliarCacheMovimentacao(
                   Coord(elemento[1], elemento[2]),
                   Coord(elemento[3], elemento[4]),
                   elemento[0]
                   )
                resultado.append(atual);
        return resultado;

    #cacheEstruturada = estruturarCache(cacheMovimentacao);

    def selecionarPeça(tabuleiro, cacheMovimentacao): #assume-se que sempre a cor da sua peça é preta
        for x_ori in range(len(tab)):
            for y_ori in range(len(tab[x_ori])):
                if(tabuleiro[x_ori][y_ori] == tabuleiro.VV):
                    continue;
    def __init__(self, cache=None):
        self.cache = cache;


