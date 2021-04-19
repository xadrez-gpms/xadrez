from copy import copy, deepcopy
import sys, pygame
import tabuleiro
import ai_module
from auxiliares import Coord, Peca
from pygame import *

BOARD_OFFSET = 14 # sprite do tabuleiro possui borda de 14 pixels
BOARD_WIDTH = 900 # largura da janela
BOARD_HEIGHT = 900 # altura da janela
SPRITE_SIZE = 52 # tamanho do sprite das peças
TARGET_FPS = 60 # Taxa Desejada de Quadros por segundo

## Início da lista dos sprites

#tabuleiro
board = pygame.image.load('sprites/chess_board.png')
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

## Fim da lista dos sprites

BRANCO = tabuleiro.BRANCO;
PRETO  = tabuleiro.PRETO;

#adjust the width of the board
size = width, height = BOARD_WIDTH, BOARD_HEIGHT
adjustedBoard = pygame.transform.scale(board, (size))





class App:

    boardSurface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT));

    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF);
    piecesLayer = Surface(size, flags=SRCALPHA);
    clock = pygame.time.Clock();


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

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = BOARD_WIDTH, BOARD_HEIGHT
        self.movimentos = tabuleiro.movimentosPossiveis(self.tab);
        print(self.movimentos)
        self.ai = ai_module.ai_module();
        self.ai.cache = self.ai.estruturarCache(self.movimentos);
    
    # Executa na Inicialização | Somente 1 Vez
    def on_init(self):
        pygame.init()
        screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF);
        self._display_surf = screen;
        self.piecesLayer = screen.copy();
        self._running = True;

        #tabuleiro ajustado ao tamanho da tela
        self._display_surf.blit(adjustedBoard, (0,0))
        pygame.display.update()
 
    # TRATAR INPUTS DO USUÁRIO AQUI | Executa sempre que um evento novo é detectado
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # clique com o botão esquerdo
            self.movimentacao();
            self.movimentos = tabuleiro.movimentosPossiveis(self.tab);
            print(self.movimentos);
        # input do teclado
        if event.type == KEYDOWN: 
            if event.key == pygame.K_f:
                tabuleiro.printTabuleiro(self.tab) # printa o tabuleiro no console quando aperta a tecla F

            if event.key == pygame.K_m:
                tabuleiro.printMovmentosPossiveis(tabuleiro.movimentosPossiveis(self.tab)); # printa o tabuleiro no console quando aperta a tecla F
            
            # Por hora a IA está sendo ativada por aqui
            if event.key == pygame.K_a:
                if(self.game_round != PRETO):
                    return;

                movimento = self.ai.selecionarMovimento(self.ai.cache);
                tabuleiro.movimentaPeca(self.tab, 
                        Peca.convertePecaParaTipoTabuleiro(movimento.peca.type, movimento.peca.cor),
                        movimento.peca.pos.x, movimento.peca.pos.y, 
                        movimento.pos_fin.x, movimento.pos_fin.y);
                self.game_round = BRANCO;


            if event.key == pygame.K_r:
                self.initGame();

            if event.key == pygame.K_ESCAPE:
                exit(0);

    def movimentacao(self):
        if self.pickUpCord == None :
            pos = self.getPosClick();
            piece = tabuleiro.getPeca(self.tab, pos[0], pos[1]);
            if piece == tabuleiro.VV:  # Garante que a peça seja válida
                print("Nenhuma peça selecionada");
            elif not self.verificaRodada(piece):  # controlar a rodada aqui tbm
                print("Não é sua rodada");
            else:
                self.pickUpCord = pos;
        else:
            piece = tabuleiro.getPeca(self.tab, self.pickUpCord[0], self.pickUpCord[1])
            newPos = self.getPosClick();

            # Verifica se o movimento deixa o rei em cheque ou se tira condição de xeque
            tabAux = deepcopy(self.tab);
            tabuleiro.setPeca(tabAux, tabuleiro.VV, self.pickUpCord[0], self.pickUpCord[1]);
            tabuleiro.setPeca(tabAux, piece, newPos[0], newPos[1]);
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
                if tabuleiro.movimentaPeca(self.tab, piece, self.pickUpCord[0], self.pickUpCord[1], newPos[0], newPos[1]):
                    self.movPossiveis = tabuleiro.movimentosPossiveis(self.tab);
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
                    else:
                        if self.game_round == BRANCO:
                            self.xeque_branco = False;
                        if self.game_round == PRETO:
                            self.xeque_preto = False;
                    self.proximaRodada();
            self.pickUpCord = None;

    def proximaRodada(self):
        if self.game_round == PRETO:
            self.game_round = BRANCO;
        else:
            self.game_round = PRETO;

    def verificaRodada(self, piece):
        if self.game_round == PRETO:
            if not tabuleiro.is_branca(piece):
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
        pass
    # VISUAL LOGIC | Tudo relacionado a interface deve entrar aqui
    def on_render(self):
        self._display_surf.blit(adjustedBoard, (0, 0)) # Necessário para não duplicar as peças no tabuleiro
        self.displayTab();
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
            
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

class inheritance(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


