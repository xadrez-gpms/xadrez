# Xadrez
Trabalho da Disciplina [***Ger�ncia de Projeto e Manuten��o de Software***](http://www.ic.uff.br/~troy/courses/2020.2/gpms.html) da **UNIVERSIDADE FEDERAL FLUMINENSE** para o segundo per�odo letivo de 2020 (2020.2).

- No momento o jogo possui uma **IA B�SICA**:
	> Movimenta��o aleat�ria.
	> IA mais sofisticada est� nos planos de desenvolvimento.
- Est� validando os movimentos do jogador. 
	> N�o h� feedback visual no momento.
	> Todo o feedback est� sendo dado no console por hora.
- Atualmente o jogo est� configurado para rodar a 60 quadros por segundo (60 FPS).
___

# Como Jogar?
1. Navegar at� a pasta do projeto e executar o arquivo *interface.py*.
2. Escolha o modo de jogo no menu
    > No momento n�o est� implementado, sempre inicia no modo __Jogador vs Jogador__ independente da sua escolha.
![Imagem do Menu Inicial do Jogo](https://i.imgur.com/Xs23UTW.png "Menu Inicial do Jogo")
1. Para movimenta��o do jogador utilize o mouse clicando com o bot�o esquerdo.
    >![Imagem do Tabuleiro com as pe�as em posi��o inicial](https://i.imgur.com/czQfjVv.png "Imagem do Tabuleiro com as pe�as em posi��o inicial")
1. O jogador **SEMPRE** est� com as pe�as **brancas** no modo __Jogador vs IA__.
1. O jogador **PODE** mover as pe�as de ambas as cores, *alternadamente*, no modo __Jogador vs Jogador__.
    1. Em qualquer turno voc� pode ativar a IA para realizar __1 jogada__ por voc�. ~~No turno das pe�as pretas voc� pode ativar o uso da IA.~~ 
    1. Para ativar o uso da IA utilize a tecla ***A***.



# Problemas Conhecidos:

- O movimento especial *En Passant* n�o est� dispon�vel.
- A movimenta��o da IA **n�o est� fazendo valida��o da jogada**.
    >> Isso significa que a IA pode realizar jogadas ilegais. 
    >> Exemplo: Rei Preto est� em xeque mas a IA move o Cavalo preto de G8 para H6, ainda mantendo o Rei Preto em xeque.
- O Menu para escolha de Modo de Jogo n�o tem efeito pr�tico.
- ~~Os movimentos "Pequeno Roque" e "Grande Roque" ainda n�o est�o dispon�veis.~~ 
___

# Releases:

Informa��es sobre o release est�o [dispon�veis aqui](https://github.com/xadrez-gpms/xadrez/blob/main/RELEASE.md)

Voc� pode realizar o download de um bin�rio para instala��o atrav�s deste link. (*indispon�vel no momento*)
___
# Recursos

 Imagens utilizadas no projeto obtidas na plataforma OpenGameArt.Org:
> https://opengameart.org/content/chess-pieces-and-a-board
> Alguns sprites foram modificados.

# Licen�a

Este produto � distribu�do atrav�s da licen�a MIT, dispon�vel em: https://mit-license.org/

___

# Integra��o com o PyGames:

1. Instalar o Python em seu sistema. Para o Windows 10 h� a vers�o 3.9 dispon�vel na *Microsoft Store*.
2. Ap�s confirmar a instala��o do Python em seu sistema, seguir as intru��es em linha de comando para instalar o PyGames.

## Instala��o do Python
https://docs.python.org/3/using/windows.html#installation-steps

## Instala��o do PyGames
https://www.pygame.org/wiki/GettingStarted

## Documenta��o Python 3
https://docs.python.org/3/index.html

___
