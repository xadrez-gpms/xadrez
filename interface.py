import sys, pygame
import tabuleiro
from pygame import *

BOARD_OFFSET = 14 # sprite do tabuleiro possui borda de 14 pixels
BOARD_WIDTH = 800 # largura da janela
BOARD_HEIGHT = 800 # altura da janela
SPRITE_SIZE = 52 # tamanho do sprite das peças

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

#adjust the width of the board
size = width, height = BOARD_WIDTH, BOARD_HEIGHT
adjustedBoard = pygame.transform.scale(board, (size))

class Coord: # Classe auxiliar
    x = 0;
    y = 0;

class App:

    boardSurface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT));

    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF);
    piecesLayer = Surface(size, flags=SRCALPHA);
    clock = pygame.time.Clock();


    w_delimiter = BOARD_WIDTH / 8;
    h_delimiter = BOARD_HEIGHT / 8;
    w_offset = 0;
    h_offset = 0;

    # ajustes na posição dos sprites
    if w_delimiter > SPRITE_SIZE:
        w_offset = (w_delimiter - SPRITE_SIZE) / 2;
    if h_delimiter > SPRITE_SIZE:
        h_offset = (h_delimiter - SPRITE_SIZE) / 2;

    origin = Coord();
    origin.x = 0;
    origin.y = 0;

    spriteOffset = Coord();
    spriteOffset.x = w_offset;
    spriteOffset.y = h_offset;

    # tabuleiro
    tab = tabuleiro.getTab();
    tabuleiro.printTabuleiro(tab);

    pickUpCord = None;

    def obterSprites():
        sprites = {
            VB : white_cell,
            VP : black_cell,
            PP : black_pawn,
            PB : black_bishop,
            PT : black_rook,
            PC : black_knight,
            PQ : black_queen,
            PR : black_king,
            BP : white_pawn,
            BB : white_bishop,
            BT : white_rook,
            BC : white_knight,
            BQ : white_queen,
            BR : white_king,
            BOARD : board,
        }
        return sprites

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = BOARD_WIDTH, BOARD_HEIGHT
 
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
            if (self.pickUpCord != None): print(tabuleiro.getPeca(self.pickUpCord[0], self.pickUpCord[1]))
            if (self.pickUpCord == None):
                self.pickUpCord = self.getPosClick();
            else:
                piece = tabuleiro.getPeca(self.pickUpCord[0], self.pickUpCord[1])
                newPos = self.getPosClick();
                tabuleiro.movimentaPeca(piece, self.pickUpCord[0], self.pickUpCord[1], newPos[0], newPos[1])
                self.pickUpCord = None;
        # input do teclado
        if event.type == KEYDOWN: 
            if event.key == pygame.K_f:
                tabuleiro.printTabuleiro(self.tab) # printa o tabuleiro no console quando aperta a tecla F


    def getPosClick(self):
        pos = pygame.mouse.get_pos()
        x = pos[1];
        y = pos[0];
        lin = int(x // self.w_delimiter);
        col = int(y // self.h_delimiter);
        print('{}{}'.format(chr(col+65), lin+1)) # Conversão para Coluna de A~H
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
                if tab[i][j] == tabuleiro.PB:
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
            self.clock.tick(60); # define o FPS em 60 fps. | Alterar o valor para alterar o FPS.
            
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


