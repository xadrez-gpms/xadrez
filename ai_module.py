import tabuleiro, random
from auxiliares import AuxiliarCacheMovimentacao, Coord, TipoPeca, CorPeca, Peca

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

    def aplicarMovimentoNoTabuleiro(tab, movimento: AuxiliarCacheMovimentacao):
        tabuleiro.movimentaPeca(tab, 
                               Peca.convertePecaParaTipoTabuleiro(movimento.peca.type, movimento.peca.cor),
                               movimento.peca.pos.x, movimento.peca.pos.y, 
                               movimento.pos_fin.x, movimento.pos_fin.y);

    def selecionarMovimento(tabuleiro, cacheMovimentacao: [AuxiliarCacheMovimentacao], cor: CorPeca):

        jogadas = [];
        tipoPecaDisponivel = [];
        for i in range(len(cacheMovimentacao)):
            if(cacheMovimentacao[i].peca.cor != cor): 
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
        return jogadasPeca[randomHelper];

    def __init__(self, cache=None):
        self.cache = cache;


