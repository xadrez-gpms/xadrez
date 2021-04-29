# Xadrez
Trabalho da Disciplina [***Ger�ncia de Projeto e Manuten��o de Software***](http://www.ic.uff.br/~troy/courses/2020.2/gpms.html) da **UNIVERSIDADE FEDERAL FLUMINENSE** para o segundo per�odo letivo de 2020 (2020.2).

- No momento o jogo possui uma **IA B�SICA**:
	> Movimenta��o aleat�ria.
	
	> IA mais sofisticada est� nos planos de desenvolvimento. (fora do escopo da entrega final da disciplina) 
- Est� validando os movimentos do jogador. 
	> N�o h� feedback visual no momento.
	
	> Todo o feedback est� sendo dado no console por hora.
- Atualmente o jogo est� configurado para rodar a 60 quadros por segundo (60 FPS).
___

# Como Jogar?
1. Navegar at� a pasta do projeto e executar o arquivo *interface.py*.
2. Escolha o modo de jogo no *menu inicial.*
    > ~~No momento n�o est� implementado, sempre inicia no modo __Jogador vs Jogador__ independente da sua escolha.~~
	
    1. Escolha o modo de jogo desejado.
	<img title="Imagem do Menu Inicial do Jogo" src="https://i.imgur.com/Xs23UTW.png" width="400"/>
	
	**Observa��es:**
    	1. Caso deseje jogar contra a IA ou assistir � uma partida de __IA vs IA__, lembre-se que a IA utiliza um temporizador para realizar cada movimento.
        1. Por padr�o este temporizador est� configurado para 800 ms (4/5 de 1 segundo).
        1. Voc� pode utilizar as teclas 0 a 5 para alterar o temporizador da IA enquanto estiver em uma partida.
        **Os temporizadores por tecla s�o os seguintes:**
            1. Tecla ***0*** --> 0 ms
            1. Tecla ***1*** --> 200 ms
            1. Tecla ***2*** --> 400 ms
            1. Tecla ***3*** --> 600 ms
            1. Tecla ***4*** --> 800 ms
            1. Tecla ***5*** --> 1000 ms
		1. Lembrando que este � um delay **adicional** para a movimenta��o da IA, n�o considerando o tempo de processamento da jogada.

    1. Alternativamente, ao apertar a tecla ***Esc*** no menu voc� fecha o jogo.
1. Para mover as pe�as utilize o mouse clicando com o bot�o esquerdo.
    <img title="Imagem do Tabuleiro com as pe�as em posi��o inicial" src="https://i.imgur.com/czQfjVv.png" width="400" />
1. O jogador **SEMPRE** est� com as pe�as **brancas** no modo __Jogador vs IA__.
1. O jogador **PODE** mover as pe�as de ambas as cores, *alternadamente*, no modo __Jogador vs Jogador__.
    1. ~~Em qualquer turno voc� pode ativar a IA para realizar __1 jogada__ por voc�.~~
    > Fun��o desabilitada!
    1. ~~Para ativar o uso da IA utilize a tecla ***A***.~~
    > Fun��o desabilitada!
1. O jogador **PODE** pressionar a tecla ***Esc*** a qualquer momento durante a partida para retornar ao *menu inicial*.

## Teclas

- __0 ~ 5__ - Ajustam o temporizador de espera da IA.
- __R__ - Reinicia a partida atual.
- __Esc__ 
	- Em partida, volta para o *menu inicial*.
	- No *menu inicial*, fecha o jogo.
**�teis para Debug**
- __F__ - Exibe o tabuleiro l�gico, no momento atual, no console.
- __M__ - Exibe no console a estrutura de dado com todas as jogadas dispon�veis na rodada atual.
**Removidas (dispon�veis at� o Release 2)**
- __A__ - Realiza uma movimenta��o para o jogador utilizando a IA.


## Movimentos Especiais

### [Roque](https://pt.wikipedia.org/wiki/Roque_(xadrez))
> O Roque � uma jogada especial que envolve a movimenta��o de duas pe�as em um �nico lance, o rei e uma das torres. O objetivo da jogada � proteger o rei, tirando-o do centro.

- Antes de executar a jogada, � necess�rio o atendimento aos seguintes requisitos:

    1. O rei e a torre envolvida n�o podem ter se movimentado nenhuma vez desde o in�cio do jogo;
    1. As casas entre o rei e a torre devem estar desocupadas;
    1. O rei n�o pode estar em xeque, e tamb�m n�o pode ficar em xeque depois do roque;
    1. ~~Nenhuma das casas onde o rei passar ou ficar dever� estar no raio de a��o de uma pe�a advers�ria. Isto n�o se aplica � torre envolvida.~~ 
        **N�o Implementado!**
___
- ##### Exemplo de tabuleiro onde � poss�vel fazer o ***Roque***:
<div width="810">
<img src="https://i.imgur.com/ri5m0ZU.png" title="Tabuleiro de xadrez onde as pe�as brancas podem fazer um pequeno roque e as pe�as pretas podem fazer um grande roque" width="400" />
<img src="https://i.imgur.com/gpC0au4.png" title="Tabuleiro de xadrez ap�s as pe�as brancas realizarem um pequeno roque e as pe�as pretas realizarem um grande roque." width="400"/>
</div>
1. Selecionar o Rei Branco.
1. Selecionar a Torre Branca.
    - O resultado � um Pequeno Roque nas pe�as Brancas.
1. Selecionar o Rei Preto.
1. Selecionar a Torre Preta.
    - O resultado � um Grande Roque nas pe�as Pretas.

___

1. Tecnicamente � tratada como uma **jogada do Rei**, portanto para realizar um roque voc� deve primeiro clicar no Rei.
1. Uma vez que tenha selecionado o Rei, selecione a Torre a qual deseja realizar o Roque.
1. Lembre-se que, caso n�o atenda aos requisitos, a jogada n�o ser� realizada.

### [En Passant](https://pt.wikipedia.org/wiki/En_passant)
>En passant � um movimento especial de captura do Pe�o no jogo de xadrez. Na ocasi�o do avan�o por duas casas do pe�o, caso haja um pe�o advers�rio na coluna adjacente na quarta fileira para as brancas, ou quinta para as pretas, este pode capturar o pe�o como se "de passagem", movendo-o para a casa por onde o pe�o capturado passou sobre. 

- A captura en passant deve ser feita imediatamente ap�s o pe�o ter sido movido por duas casas, caso contr�rio o jogador advers�rio perde o direito de faz�-lo posteriormente. 
- Tal movimento � a �nica ocasi�o no xadrez na qual a pe�a que captura n�o � movida para a casa ocupada pela pe�a capturada. 
- Para realizar um ***En Passant*** � necess�rio ter um pe�o podendo interceptar o pe�o advers�rio que moveu-se por duas casas.

___
- ##### Exemplo de tabuleiro onde � poss�vel fazer o ***En Passant***:
<div width="810">
<img src="https://i.imgur.com/VAQsNet.png" title="Imagem do Tabuleiro de Xadrez com a possibilidade de En Passant" width="400" />
<img src="https://i.imgur.com/lo1zZ8U.png" title="Imagem de um tabuleiro de Xadrez ap�s a execu��o de uma jogada En Passant" width="400"/>
</div>

1. O pe�o branco se movimentou duas casas para frente.
2. O pe�o preto est� em uma posi��o que pode interceptar seu movimento enquanto o pe�o branco atravessa a casa (condi��o do En Passant).
3. O pe�o preto intercepta o pe�o branco, concluindo assim a jogada.


- Clique no pe�o que est� em tal situa��o.
- Clique na casa a qual o seu pe�o se moveria caso o pe�o advers�rio tivesse se movido apenas 1 casa.
___
# Problemas Conhecidos:

- Visto que a IA � simples e utiliza movimenta��o aleat�ria ela pode ficar presa em um loop para escolher sua jogada quando estiver em xeque.
- ~~O Menu para escolha de Modo de Jogo n�o tem efeito pr�tico.~~
- ~~Os movimentos "Pequeno Roque" e "Grande Roque" ainda n�o est�o dispon�veis.~~ 
- ~~O movimento especial *En Passant* n�o est� dispon�vel.~~
- ~~A movimenta��o da IA **n�o est� fazendo valida��o da jogada.~~
___

# Releases:

Informa��es sobre o release est�o [dispon�veis aqui.](https://github.com/xadrez-gpms/xadrez/blob/main/RELEASE.md)

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
