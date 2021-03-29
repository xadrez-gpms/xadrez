import sys, pygame
import tabuleiro
from pygame.locals import *

BOARD_OFFSET = 14 # sprite do tabuleiro possui borda de 14 pixels
BOARD_WIDTH = 423 # largura da janela
BOARD_HEIGHT = 423 # altura da janela

## Início da lista dos sprites

#tabuleiro
board = pygame.image.load('sprites/chess_board.png')
boardRect = board.get_rect();
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

black = 0, 0, 0;
size = width, height = BOARD_WIDTH, BOARD_HEIGHT

class App:

    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF);
    w_delimiter = BOARD_WIDTH / 8;
    h_delimiter = BOARD_HEIGHT / 8;

    tab = tabuleiro.initTab();
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
 
    def on_init(self):
        pygame.init()
        screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF);
        self._display_surf = screen;
        self._running = True;
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONUP:
            self.pickUpCord = self.getPosClick();
            print(self.pickUpCord)

    def getPosClick(self):
        pos = pygame.mouse.get_pos()
        x = pos[1];
        y = pos[0];
        lin = int(x // self.w_delimiter);
        col = int(y // self.h_delimiter);
        return [lin, col]

    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.fill(black);
        self._display_surf.blit(board, boardRect);
        #draw tab
        self.displayTab();
        self.displayTab();
        pass
    def on_cleanup(self):
        pygame.quit()

    def displayTab(self):
        tab = self.tab;
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                lin = int(i * self.w_delimiter);
                col = int(j * self.h_delimiter);
                if tab[i][j] == tabuleiro.PB:
                    self.screen.blit(black_bishop, (col, lin))
                if tab[i][j] == tabuleiro.PR:
                    self.screen.blit(black_king, (col, lin))
                if tab[i][j] == tabuleiro.PQ:
                    self.screen.blit(black_queen, (col, lin))
                if tab[i][j] == tabuleiro.PT:
                    self.screen.blit(black_rook, (col, lin))
                if tab[i][j] == tabuleiro.PP:
                    self.screen.blit(black_pawn, (col, lin))
                if tab[i][j] == tabuleiro.PC:
                    self.screen.blit(black_knight, (col, lin))
                if tab[i][j] == tabuleiro.BB:
                    self.screen.blit(white_bishop, (col, lin))
                if tab[i][j] == tabuleiro.BR:
                    self.screen.blit(white_king, (col, lin))
                if tab[i][j] == tabuleiro.BQ:
                    self.screen.blit(white_queen, (col, lin))
                if tab[i][j] == tabuleiro.BT:
                    self.screen.blit(white_rook, (col, lin))
                if tab[i][j] == tabuleiro.BP:
                    self.screen.blit(white_pawn, (col, lin))
                if tab[i][j] == tabuleiro.BC:
                    self.screen.blit(white_knight, (col, lin))






    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.update()
        self.on_cleanup()


 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

class inheritance(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


