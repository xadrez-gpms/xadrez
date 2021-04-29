from copy import copy, deepcopy
import sys, pygame
import tabuleiro
import ai_module
import random

from auxiliares import Coord, Peca, CorPeca, GameMode
from pygame import *
try:
    from win32api import GetSystemMetrics
    BOARD_WIDTH = int(GetSystemMetrics(1)/3*2) # largura da janela
    BOARD_HEIGHT =int(GetSystemMetrics(1)/3*2) # altura da janela
except ImportError:
    BOARD_WIDTH = 600 # largura da janela
    BOARD_HEIGHT = 600 # altura da janela



BOARD_OFFSET = 14 # sprite do tabuleiro possui borda de 14 pixels
SPRITE_SIZE = 52 # tamanho do sprite das peças
TARGET_FPS = 60 # Taxa Desejada de Quadros por segundo
AI_TIMER = 800 # Tempo (em milisegundos) para aguardar antes de chamar a função da IA para movimentar a peça.
SCREEN_TITLE = "Xadrez GPMS UFF 2020.2"

## Início da lista dos sprites
menuGame = pygame.image.load('sprites/menuGame.png');
#tabuleiro
board = pygame.image.load('sprites/chess_board.png')
promocaoBranco = pygame.image.load('sprites/promocao_branco.png')
promocaoPreto = pygame.image.load('sprites/promocao_preto.png')
black_cell = pygame.image.load('sprites/squareB.png')
white_cell = pygame.image.load('sprites/squareW.png')

#peças pretas
black_bishop = pygame.image.load('sprites/bishopB3.png')
black_king = pygame.image.load('sprites/kingB3.png')
black_knight = pygame.image.load('sprites/knightB3.png')
black_pawn = pygame.image.load('sprites/pawnB3.png')
black_queen = pygame.image.load('sprites/queenB3.png')
black_rook = pygame.image.load('sprites/rookB3.png')

#peças brancas
white_bishop = pygame.image.load('sprites/bishopW3.png')
white_king = pygame.image.load('sprites/kingW3.png')
white_knight = pygame.image.load('sprites/knightW3.png')
white_pawn = pygame.image.load('sprites/pawnW3.png')
white_queen = pygame.image.load('sprites/queenW3.png')
white_rook = pygame.image.load('sprites/rookW3.png')

WHITE = 0;
BLACK = 1;

## Fim da lista dos sprites

BRANCO = tabuleiro.BRANCO;
PRETO  = tabuleiro.PRETO;

#adjust the width of the board
size = width, height = BOARD_WIDTH, BOARD_HEIGHT
adjustedBoard = pygame.transform.scale(board, (size))
promocaoBranco = pygame.transform.scale(promocaoBranco, (size))
promocaoPreto = pygame.transform.scale(promocaoPreto, (size))
menuGame = pygame.transform.scale(menuGame, (size))

class App:

    boardSurface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT));

    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF);
    piecesLayer = Surface(size, flags=SRCALPHA);
    clock = pygame.time.Clock();

    #primeira rodada branca
    game_round = WHITE;

    # primeira rodada branca
    game_round = BRANCO;

    w_delimiter = BOARD_WIDTH / 8;
    h_delimiter = BOARD_HEIGHT / 8;
    w_offset = 0;
    h_offset = 0;

    # ajustes na posição dos sprites
    if w_delimiter > SPRITE_SIZE:
        w_offset = (w_delimiter - SPRITE_SIZE) / 2;
    if h_delimiter > SPRITE_SIZE:
        h_offset = (h_delimiter - SPRITE_SIZE) / 2;

    origin = Coord(0, 0);

    spriteOffset = Coord(w_offset, h_offset);

    tab = tabuleiro.initTab();
    #tabuleiro.printTabuleiro(tab);
    movPossiveis = tabuleiro.movimentosPossiveis(tab);
    xeque_branco    = False;
    xeque_preto     = False;
    rei_branco_mov  = False;
    rei_preto_mov   = False;
    pickUpCord      = None;
    promocaoPeao    = False;
    statusPromocao  = None;
    is_xeque_mate   = False;
    empate     = False;
    corJogador      = BRANCO;

    # tabuleiro
    def initGame(self):
        self.tab = tabuleiro.initTab();
        tabuleiro.printTabuleiro(self.tab);
        self.movPossiveis = tabuleiro.movimentosPossiveis(self.tab);
        self.xeque_branco = False;
        self.xeque_preto  = False;
        self.pickUpCord = None;
        self.rei_branco_mov = False;
        self.rei_preto_mov = False;
        self.game_round = BRANCO;
        self.promocaoPeao = False;
        self.statusPromocao = None;
        self.is_xeque_mate = False;
        self.empate = False;

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = BOARD_WIDTH, BOARD_HEIGHT
        self.movimentos = tabuleiro.movimentosPossiveis(self.tab);
        self.game_mode = GameMode.MENU;
        print(self.movimentos)
        self.ai = ai_module.ai_module();
        self.ai.cache = self.ai.estruturarCache(self.movimentos);

    # Executa na Inicialização | Somente 1 Vez
    def on_init(self):
        pygame.init()
        screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF);
        pygame.display.set_caption(SCREEN_TITLE);
        self._display_surf = screen;
        self.piecesLayer = screen.copy();
        self._running = True;

        #tabuleiro ajustado ao tamanho da tela
        self._display_surf.blit(adjustedBoard, (0,0))
        pygame.display.update()

    def proximaRodada(self):
        if self.game_round == BLACK:
            self.game_round = WHITE;
        else:
            self.game_round = BLACK;

    def verificaRodada(self, piece):
        if self.game_round == BLACK:
            if tabuleiro.is_preta(piece):
                return True;
        else:
            if tabuleiro.is_branca(piece):
                return True;
        return False;

    def verificaEmpate(self):
        if tabuleiro.verificaEmpate(self.tab):
            self.empate = True;
            print("Empate")

    def modoDeJogo(self):
        pos = pygame.mouse.get_pos()
        w_delimitador = int(self.weight / 10);
        h_delimitador = int(self.height / 10);
        if pos[0] >= 2.6 * h_delimitador and pos[0] <= 7.2 * h_delimitador:
            if pos[1] >= 1.6 * w_delimitador and pos[1] <= 3.3 * w_delimitador:
                self.game_mode = GameMode.PLAYER_VS_PLAYER;
            if pos[1] >= 4 * w_delimitador and pos[1] <= 5.5 * w_delimitador:
                self.game_mode = GameMode.PLAYER_VS_IA;
            if pos[1] >= 6.2 * w_delimitador and pos[1] <= 7.6 * w_delimitador:
                self.game_mode = GameMode.IA_VS_IA;

    # TRATAR INPUTS DO USUÁRIO AQUI | Executa sempre que um evento novo é detectado
    def on_event(self, event):
        global AI_TIMER;
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # clique com o botão esquerdo
            if self.game_mode != GameMode.MENU:
                if not self.promocaoPeao and not self.is_xeque_mate:
                    if not self.empate:
                        self.movimentacao();
                else: self.promovePeao();
            else:
                self.modoDeJogo();
        # input do teclado
        if event.type == KEYDOWN:
            if event.key == pygame.K_f:
                if self.game_mode != GameMode.MENU:
                    tabuleiro.printTabuleiro(self.tab) # printa o tabuleiro no console quando aperta a tecla F

            if event.key == pygame.K_m:
                if self.game_mode != GameMode.MENU:
                    tabuleiro.printMovmentosPossiveis(tabuleiro.movimentosPossiveis(self.tab)); # printa o tabuleiro no console quando aperta a tecla F

            if event.key == pygame.K_r:
                if self.game_mode != GameMode.MENU:
                    self.initGame();
            if event.key == pygame.K_0:
                AI_TIMER = 0;
            if event.key == pygame.K_1:
                AI_TIMER = 200;
            if event.key == pygame.K_2:
                AI_TIMER = 400;
            if event.key == pygame.K_3:
                AI_TIMER = 600;
            if event.key == pygame.K_4:
                AI_TIMER = 800;
            if event.key == pygame.K_5:
                AI_TIMER = 1000;
            if event.key == pygame.K_ESCAPE:
                if self.game_mode != GameMode.MENU:
                    self.game_mode = GameMode.MENU;
                    self.initGame();
                else: exit(0);

    def movimentaIA(self):

        movimentoValido = False;

        while not movimentoValido:

            movimento = self.ai.selecionarMovimento(self.ai.cache, CorPeca.converteDeTabuleiro(self.game_round));
            piece = Peca.convertePecaParaTipoTabuleiro(movimento.peca.type, movimento.peca.cor);
            if (self.game_round == BRANCO and tabuleiro.is_preta(piece)) or (self.game_round == PRETO and tabuleiro.is_branca(piece)):
                continue; # IA nao tenta movimentar peças da outra cor
            tabAux = deepcopy(self.tab);
            tabuleiro.movimentaPeca(tabAux, piece, movimento.peca.pos.x, movimento.peca.pos.y, movimento.pos_fin.x, movimento.pos_fin.y, True);
            newMov = tabuleiro.movimentosPossiveis(tabAux);
            nextRound = PRETO if self.game_round == BRANCO else BRANCO;
            if not tabuleiro.verificaXeque(tabAux, newMov, nextRound):
                movimentoValido = True;
            else: # else deve ser removido na versao final
                if self.xeque_preto or self.xeque_branco:
                    print("IA tentou movimento que não salva o rei")
                else:
                    print("IA tentou colocar seu proprio rei em cheque")


        tabuleiro.movimentaPeca(self.tab, piece, movimento.peca.pos.x, movimento.peca.pos.y,
                                movimento.pos_fin.x, movimento.pos_fin.y, False);

        self.movPossiveis = tabuleiro.movimentosPossiveis(self.tab);
        self.verificaXeque();

        self.promocaoPeao = tabuleiro.promocaoPeao(tabuleiro.getPeca(self.tab, movimento.pos_fin.x, movimento.pos_fin.y), movimento.pos_fin.x);
        if self.promocaoPeao:
            self.statusPromocao = [tabuleiro.getPeca(self.tab, movimento.pos_fin.x, movimento.pos_fin.y), movimento.pos_fin.x, movimento.pos_fin.y];
            self.promovePeao();
        else:
            self.proximaRodada();
        self.movimentos = tabuleiro.movimentosPossiveis(self.tab);
        self.ai.cache = self.ai.estruturarCache(self.movimentos);


    def promovePeao(self):
        type = self.statusPromocao[0];
        x = self.statusPromocao[1];
        y = self.statusPromocao[2];
        escolha = None;
        if (self.game_round != self.corJogador and self.game_mode == GameMode.PLAYER_VS_IA) or self.game_mode == GameMode.IA_VS_IA:
            pretas = [tabuleiro.PT,tabuleiro.PB,tabuleiro.PC,tabuleiro.PQ];
            branca = [tabuleiro.BT,tabuleiro.BB,tabuleiro.BC,tabuleiro.BQ];
            escolha = random.choices(branca if tabuleiro.is_branca(type) else pretas, cum_weights=[10, 15, 20, 40])[0];
        else:
            pos = pygame.mouse.get_pos()
            w_delimitador = int(self.weight/12);
            h_delimitador = int(self.height/10);
            if pos[1] >= 5.5 * w_delimitador and pos[1] <= 7 * w_delimitador:
                if pos[0] >= 2.1*h_delimitador and pos[0] <= 2.9*h_delimitador:
                    escolha = tabuleiro.BT if tabuleiro.is_branca(type) else tabuleiro.PT;
                if pos[0] >= 3.86 * h_delimitador and pos[0] <= 4.4 * h_delimitador:
                    escolha = tabuleiro.BB if tabuleiro.is_branca(type) else tabuleiro.PB;
                if pos[0] >= 5.5 * h_delimitador and pos[0] <= 6.29 * h_delimitador:
                    escolha = tabuleiro.BC if tabuleiro.is_branca(type) else tabuleiro.PC;
                if pos[0] >= 7.3 * h_delimitador and pos[0] <= 7.84 * h_delimitador:
                    escolha = tabuleiro.BQ if tabuleiro.is_branca(type) else tabuleiro.PQ;
        if escolha != None:
            tabuleiro.setPeca(self.tab, escolha, x, y);
            self.promocaoPeao = False;
            self.proximaRodada();

    def verificaXeque(self):
        if tabuleiro.verificaXeque(self.tab, self.movPossiveis, self.game_round):
            if not tabuleiro.verificaXequeMate(self.tab, self.movPossiveis, self.game_round):
                if self.game_round == PRETO and self.game_round == PRETO:
                    print("O Rei branco esta em xeque");
                    self.xeque_branco = True;
                elif self.game_round == BRANCO and self.game_round == BRANCO:
                    print("O Rei preto esta em xeque");
                    self.xeque_preto = True;
            else:
                print("Xeque mate");
                self.is_xeque_mate = True;
        else:
            if self.game_round == BRANCO:
                self.xeque_branco = False;
            if self.game_round == PRETO:
                self.xeque_preto = False;

    def movimentacao(self):
        if self.pickUpCord == None :
            pos = self.getPosClick();
            piece = tabuleiro.getPeca(self.tab, pos[0], pos[1]);
            if piece == tabuleiro.VV:  # Garante que a peça seja válida
                print("Nenhuma peça selecionada!");
            elif not self.verificaRodada(piece):  # controlar a rodada aqui tbm
                print("Não é sua rodada!\nRodada atual: {}".format("Peças Brancas." if self.game_round == BRANCO else "Peças Pretas."));
            else:
                self.pickUpCord = pos;
        else:
            piece = tabuleiro.getPeca(self.tab, self.pickUpCord[0], self.pickUpCord[1])
            newPos = self.getPosClick();

            # Verifica se o movimento deixa o rei em cheque ou se tira condição de xeque
            tabAux = deepcopy(self.tab);
            tabuleiro.movimentaPeca(tabAux, piece, self.pickUpCord[0], self.pickUpCord[1], newPos[0], newPos[1], True);
            newMov = tabuleiro.movimentosPossiveis(tabAux);
            nextRound = PRETO if self.game_round == BRANCO else BRANCO;
            if tabuleiro.verificaXeque(tabAux, newMov, nextRound):
                if self.xeque_preto or self.xeque_branco:
                    print("É necessario salvar o rei")
                else:
                    print("Você não pode colocar o rei em cheque")
                self.pickUpCord = None;
                return;
            else: # movimento valido
                if tabuleiro.movimentaPeca(self.tab, piece, self.pickUpCord[0], self.pickUpCord[1], newPos[0], newPos[1], False):
                    self.movPossiveis = tabuleiro.movimentosPossiveis(self.tab);
                    self.verificaXeque();
                    self.promocaoPeao = tabuleiro.promocaoPeao(piece, newPos[0]);
                    if self.promocaoPeao:
                        self.statusPromocao = [piece, newPos[0], newPos[1]];
                        self.promovePeao();
                    else: self.proximaRodada();
            self.pickUpCord = None;
            self.movimentos = tabuleiro.movimentosPossiveis(self.tab);
            self.ai.cache = self.ai.estruturarCache(self.movimentos);

    def proximaRodada(self):
        if self.game_round == PRETO:
            self.game_round = BRANCO;
        else:
            self.game_round = PRETO;

    def verificaRodada(self, piece):
        if self.game_round == PRETO:
            if tabuleiro.is_preta(piece):
                return True;
        else:
            if tabuleiro.is_branca(piece):
                return True;
        return False;

    def getPosClick(self):
        pos = pygame.mouse.get_pos()
        x = pos[1];
        y = pos[0];
        lin = int(x // self.w_delimiter);
        col = int(y // self.h_delimiter);
        # print('Mouse X:{} Mouse Y:{}\nLinha:{} Coluna:{}'.format(x, y, lin, col)); # Print auxiliar para desenvolvimento
        print('{}{}'.format(chr(col+65), lin+1)+" - "+tabuleiro.getPeca(self.tab,lin, col)) # Conversão para Coluna de A~H
        return [lin, col]

    #GAME LOGIC | Coisas necessárias para cada frame
    def on_loop(self):
        if not self.empate:
            self.verificaEmpate();
        if not self.is_xeque_mate and not self.empate:
            if(self.game_round != self.corJogador and self.game_mode == GameMode.PLAYER_VS_IA) or self.game_mode == GameMode.IA_VS_IA:
                pygame.time.wait(AI_TIMER)
                self.movimentaIA();
        pass
    # VISUAL LOGIC | Tudo relacionado a interface deve entrar aqui
    def on_render(self):
        if self.game_mode == GameMode.MENU:
            self._display_surf.blit(menuGame, (0, 0))
        else:
            self._display_surf.blit(adjustedBoard, (0, 0)) # Necessário para não duplicar as peças no tabuleiro
            self.displayTab();
            if self.promocaoPeao :
                if self.game_round == BRANCO:
                    self._display_surf.blit(promocaoBranco, (0, 0))
                else:
                    self._display_surf.blit(promocaoPreto, (0, 0))
        pygame.display.flip();

    # Quando estiver encerrando o programa
    def on_cleanup(self):
        pygame.quit()

    def displayTab(self):

        tab = self.tab;
        self.piecesLayer = self.screen.copy();
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                lin = int(i * self.w_delimiter) + self.spriteOffset.x
                col = int(j * self.h_delimiter) + self.spriteOffset.y;
                if tab[i][j] == tabuleiro.VV:
                    continue;
                elif tab[i][j] == tabuleiro.PB:
                    self.piecesLayer.blit(black_bishop, (col, lin))
                elif tab[i][j] == tabuleiro.PR:
                    self.piecesLayer.blit(black_king, (col, lin))
                elif tab[i][j] == tabuleiro.PQ:
                    self.piecesLayer.blit(black_queen, (col, lin))
                elif tab[i][j] == tabuleiro.PT:
                    self.piecesLayer.blit(black_rook, (col, lin))
                elif tab[i][j] == tabuleiro.PP:
                    self.piecesLayer.blit(black_pawn, (col, lin))
                elif tab[i][j] == tabuleiro.PC:
                    self.piecesLayer.blit(black_knight, (col, lin))
                elif tab[i][j] == tabuleiro.BB:
                    self.piecesLayer.blit(white_bishop, (col, lin))
                elif tab[i][j] == tabuleiro.BR:
                    self.piecesLayer.blit(white_king, (col, lin))
                elif tab[i][j] == tabuleiro.BQ:
                    self.piecesLayer.blit(white_queen, (col, lin))
                elif tab[i][j] == tabuleiro.BT:
                    self.piecesLayer.blit(white_rook, (col, lin))
                elif tab[i][j] == tabuleiro.BP:
                    self.piecesLayer.blit(white_pawn, (col, lin))
                elif tab[i][j] == tabuleiro.BC:
                    self.piecesLayer.blit(white_knight, (col, lin))


        self.screen.blit(self.piecesLayer, (0,0))


    # Inicialização do Programa
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            
            self.clock.tick(TARGET_FPS); # define o FPS em TARGET_FPS
            self.on_loop();

            for event in pygame.event.get():
                self.on_event(event);

            self.on_render();
        self.on_cleanup();

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

class inheritance(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


