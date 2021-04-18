import tabuleiro, random
from auxiliares import AuxiliarCacheMovimentacao, Coord, TipoPeca, CorPeca

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

    def selecionarMovimento(tabuleiro, cacheMovimentacao: [AuxiliarCacheMovimentacao]): #assume-se que sempre a cor da sua peça é preta

        jogadas = [];
        tipoPecaDisponivel = [];
        for i in range(len(cacheMovimentacao)):
            if(cacheMovimentacao[i].peca.cor != CorPeca.Preta): # para tornar adaptavel basta adicionar um parametro de cor e substitui-lo aqui
                continue;
            else:
                jogadas.append(cacheMovimentacao[i]);

            if(not(cacheMovimentacao[i].peca.type in tipoPecaDisponivel)):
                tipoPecaDisponivel.append(cacheMovimentacao[i].peca.type);

        if(len(jogadas) == 0):
            return None;
        
        randomHelper = random.randint(0, len(tipoPecaDisponivel)-1);
        tipoPeca = tipoPecaDisponivel[randomHelper];
        jogadasPeca = [];

        for i in range(len(jogadas)):
            if(jogadas[i].peca.type == tipoPeca):
                jogadasPeca.append(jogadas[i]);
        
        randomHelper = random.randint(0, len(jogadasPeca)-1);
        print(randomHelper);
        return jogadasPeca[randomHelper];

    def __init__(self, cache=None):
        self.cache = cache;


