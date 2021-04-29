# Xadrez
Trabalho da Disciplina [***Gerência de Projeto e Manutenção de Software***](http://www.ic.uff.br/~troy/courses/2020.2/gpms.html) da **UNIVERSIDADE FEDERAL FLUMINENSE** para o segundo período letivo de 2020 (2020.2).

- No momento o jogo possui uma **IA BÁSICA**:
	> Movimentação aleatória.
	
	> IA mais sofisticada está nos planos de desenvolvimento. (fora do escopo da entrega final da disciplina) 
- Está validando os movimentos do jogador. 
	> Não há feedback visual no momento.
	
	> Todo o feedback está sendo dado no console por hora.
- Atualmente o jogo está configurado para rodar a 60 quadros por segundo (60 FPS).
___

# Como Jogar?
1. Navegar até a pasta do projeto e executar o arquivo *interface.py*.
2. Escolha o modo de jogo no *menu inicial.*
    > ~~No momento não está implementado, sempre inicia no modo __Jogador vs Jogador__ independente da sua escolha.~~
    1. Escolha o modo de jogo desejado.
        > Caso deseje jogar contra a IA ou assistir à uma partida de __IA vs IA__ lembre-se que a IA utiliza um temporizador para realizar cada movimento.
        > Atualmente este temporizador está configurado para 750 ms (3/4 de 1 segundo).
    1. Alternativamente, ao apertar a tecla ***Esc*** no menu você fecha o jogo.

    > <img title="Imagem do Menu Inicial do Jogo" src="https://i.imgur.com/Xs23UTW.png" width="400"/>
1. Para mover as peças utilize o mouse clicando com o botão esquerdo.
    > <img title="Imagem do Tabuleiro com as peças em posição inicial" src="https://i.imgur.com/czQfjVv.png" width="400" />
1. O jogador **SEMPRE** está com as peças **brancas** no modo __Jogador vs IA__.
1. O jogador **PODE** mover as peças de ambas as cores, *alternadamente*, no modo __Jogador vs Jogador__.
    1. ~~Em qualquer turno você pode ativar a IA para realizar __1 jogada__ por você.~~
        > ~~No turno das peças pretas você pode ativar o uso da IA.~~ 
    1. ~~Para ativar o uso da IA utilize a tecla ***A***.~~
        > Função desabilitada!
1. O jogador **PODE** pressionar a tecla ***Esc*** a qualquer momento durante a partida para retornar ao *menu inicial*.

## Movimentos Especiais

### Roque
> O Roque é uma jogada especial que envolve a movimentação de duas peças em um único lance, o rei e uma das torres. O objetivo da jogada é proteger o rei, tirando-o do centro.

- Antes de executar a jogada, é necessário o atendimento aos seguintes requisitos:

    1. O rei e a torre envolvida não podem ter se movimentado nenhuma vez desde o início do jogo;
    1. As casas entre o rei e a torre devem estar desocupadas;
    1. O rei não pode estar em xeque, e também não pode ficar em xeque depois do roque;
    1. ~~Nenhuma das casas onde o rei passar ou ficar deverá estar no raio de ação de uma peça adversária. Isto não se aplica à torre envolvida.~~
        **Não Implementado!**

1. Tecnicamente é tratada como uma jogada do Rei, portanto para realizar um roque você deve primeiro clicar no Rei.
1. Uma vez que tenha selecionado o Rei, selecione a Torre a qual deseja realizar o Roque.
1. Lembre-se que, caso não atenda aos requisitos, a jogada não será realizada.

### En Passant
>En passant é um movimento especial de captura do Peão no jogo de xadrez. Na ocasião do avanço por duas casas do peão, caso haja um peão adversário na coluna adjacente na quarta fileira para as brancas, ou quinta para as pretas, este pode capturar o peão como se "de passagem", movendo-o para a casa por onde o peão capturado passou sobre. 

- A captura en passant deve ser feita imediatamente após o peão ter sido movido por duas casas, caso contrário o jogador adversário perde o direito de fazê-lo posteriormente. 
- Tal movimento é a única ocasião no xadrez na qual a peça que captura não é movida para a casa ocupada pela peça capturada. 
- Para realizar um ***En Passant*** é necessário ter um peão podendo interceptar o peão adversário que moveu-se por duas casas.
> <img src="https://i.imgur.com/VAQsNet.png" title="Imagem do Tabuleiro de Xadrez com a possibilidade de En Passant" width="400"/>
    1. O peão branco se movimentou duas casas para frente.
    2. O peão preto está em uma posição que pode interceptar seu movimento enquanto o peão branco atravessa a casa (condição do En Passant).
    
> <img src="https://i.imgur.com/lo1zZ8U.png" title="Imagem de um tabuleiro de Xadrez após a execução de uma jogada En Passant" width="400"/>
    3. O peão preto intercepta o peão branco, concluindo assim a jogada.

1. Clique no peão que está em tal situação.
1. Clique na casa a qual o seu peão se moveria caso o peão adversário tivesse se movido apenas 1 casa.

# Problemas Conhecidos:

- Visto que a IA é simples e utiliza movimentação aleatória ela pode ficar presa em um loop para escolher sua jogada quando estiver em xeque.
- ~~O Menu para escolha de Modo de Jogo não tem efeito prático.~~
- ~~Os movimentos "Pequeno Roque" e "Grande Roque" ainda não estão disponíveis.~~ 
- ~~O movimento especial *En Passant* não está disponível.~~
- ~~A movimentação da IA **não está fazendo validação da jogada.~~
___

# Releases:

Informações sobre o release estão [disponíveis aqui](https://github.com/xadrez-gpms/xadrez/blob/main/RELEASE.md)

Você pode realizar o download de um binário para instalação através deste link. (*indisponível no momento*)
___
# Recursos

 Imagens utilizadas no projeto obtidas na plataforma OpenGameArt.Org:
> https://opengameart.org/content/chess-pieces-and-a-board
> Alguns sprites foram modificados.

# Licença

Este produto é distribuído através da licença MIT, disponível em: https://mit-license.org/

___

# Integração com o PyGames:

1. Instalar o Python em seu sistema. Para o Windows 10 há a versão 3.9 disponível na *Microsoft Store*.
2. Após confirmar a instalação do Python em seu sistema, seguir as intruções em linha de comando para instalar o PyGames.

## Instalação do Python
https://docs.python.org/3/using/windows.html#installation-steps

## Instalação do PyGames
https://www.pygame.org/wiki/GettingStarted

## Documentação Python 3
https://docs.python.org/3/index.html

___
