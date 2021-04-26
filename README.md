# Xadrez
Trabalho da Disciplina [***Gerência de Projeto e Manutenção de Software***](http://www.ic.uff.br/~troy/courses/2020.2/gpms.html) da **UNIVERSIDADE FEDERAL FLUMINENSE** para o segundo período letivo de 2020 (2020.2).

- No momento o jogo possui uma **IA BÁSICA**:
	> Movimentação aleatória.
	
	> IA mais sofisticada está nos planos de desenvolvimento.
- Está validando os movimentos do jogador. 
	> Não há feedback visual no momento.
	
	> Todo o feedback está sendo dado no console por hora.
- Atualmente o jogo está configurado para rodar a 60 quadros por segundo (60 FPS).
___

# Como Jogar?
1. Navegar até a pasta do projeto e executar o arquivo *interface.py*.
2. Escolha o modo de jogo no menu
    > No momento não está implementado, sempre inicia no modo __Jogador vs Jogador__ independente da sua escolha.

    > ![Imagem do Menu Inicial do Jogo](https://i.imgur.com/Xs23UTW.png "Menu Inicial do Jogo")
1. Para mover as peças utilize o mouse clicando com o botão esquerdo.
    >![Imagem do Tabuleiro com as peças em posição inicial](https://i.imgur.com/czQfjVv.png "Imagem do Tabuleiro com as peças em posição inicial")
1. O jogador **SEMPRE** está com as peças **brancas** no modo __Jogador vs IA__.
1. O jogador **PODE** mover as peças de ambas as cores, *alternadamente*, no modo __Jogador vs Jogador__.
    1. Em qualquer turno você pode ativar a IA para realizar __1 jogada__ por você. 
        > ~~No turno das peças pretas você pode ativar o uso da IA.~~ 
    1. Para ativar o uso da IA utilize a tecla ***A***.



# Problemas Conhecidos:

- O movimento especial *En Passant* não está disponível.
- A movimentação da IA **não está fazendo validação da jogada**.
    > Isso significa que a IA pode realizar jogadas ilegais. 
    > Exemplo: Rei Preto está em xeque mas a IA move o Cavalo preto de G8 para H6, ainda mantendo o Rei Preto em xeque.
- O Menu para escolha de Modo de Jogo não tem efeito prático.
- ~~Os movimentos "Pequeno Roque" e "Grande Roque" ainda não estão disponíveis.~~ 
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
