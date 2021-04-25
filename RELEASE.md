# RELEASE 1

### 20 commits

- 0610532 (Initial commit)
> Commit inicial para iniciar o repositório

- 3834378 (comit inicial tabuleiro + movimentação peao)
> Inicializando o tabuleiro com o pygame e adicionando a movimentação inicial do peão

- 31dc341 (get and set da celula)
> Adionando metodos para pegar e setar células do tabuleiro

- f27468d (movimento torre)
> Adicionando a movimentação inicial da torre

- 4123070 (fix movimento torre)
> Correção do commit anterior para consertar a movimentação da torre

- 1887c14 (movimento bispo)
> Adicionando a movimentação inicial do bispo

- 58bed89 (movimento rainha)
> Adicionando movimentação inicial da rainha

- 384f157 (implementando movimento cavalo) 
> Adicionando movimentação inicial do cavalo

- 4e38fab (implementando movimentação do rei)
> Adicionando movimentação inicial do rei

- d835be0 (feat: adição da pasta com os sprites. adição da classe para interface. Atualização do readme.md)
> Adicionando a pasta com as sprites das peças e do tabuleiro, a classe de interface para o jogo e atualização do readme com informações sobre o projeto.

- d10b933 (feat: inserção de licença no readme.md)
> Adicionando a licença que faltou no commit anterior

- dbc6799 (fix: interface não exibindo o tabuleiro.)
> Consertando um problema que não estava exibindo o tabuleiro corretamente

- 9e96e5d (chore: remoção das bordas na imagem do tabuleiro. | fix: correção do bug de duplicação do tabuleiro)
> Remoção da borda do tabuleiro e removendo o problema de duplicar o tabuleiro ao exibí-lo

- c0fbaca (chore: remoção dos prints de debug do commit anterior)
> Removendo prints que ficaram faltando do commit anterior

- ab84a12 (GetClickCelPosiiton)
> Adicionando método para pegar o clique do usuário e a posição que foi clicada

- 25588cb (Show pieces)
> Adicionando as sprites das peças no tabuleiro antes e durante o jogo

- 56dda65 (doc: adicionado comentários para facilitar entendimento. feat: tabuleiro agora pode ter seu tamanho alterado. style: peças tiveram seu posicionamento centralizado)
> Atualização de comentários no código, adicionando tamanho variável para o tabuleiro e centralizar as figuras das peças nas células do tabuleiro

- 207573d (feat: adicionado controle de FPS, verificação para clique somente do botão esquerdo do mouse e pequenas otimizações)
> adicionado controle de FPS, verificação para clique somente do botão esquerdo do mouse e pequenas otimizações

- c54f016 (Merge)
> Merge do commit anterior

- dd61dc5 (Adicionando o release da primeira versão jogada)
> Commit para a primeira versão jogada junto com a tag

# RELEASE 2

### 32 commits

- 1a7bd9e (Controle de rodada e correção de rodada iniciando na célula vazia - V1.1)
> Adicionando método para verificação de rodada (controla se é vez do branco ou do preto)

- 69d0e36 (Calculo das movimentações possiveis e melhoria no log do console)
> Ao pressionar "M" com jogo aberto sera printado as movimentações possíveis

- 18cd296 (Correção de bug de movimentação fora da rodada e peao movimentando lateralmente de forma invalida)
> Correção da movimentação (acerto na lógica)

- 995118b (Alterando ordem de log)
> Mudança nos logs do console

- 6d6a3c7 (verificação xeque e xeque-mate + refactor do tabuleiro)
> Adicionando tabuleiro nos metodos de verificação de movimentos e adicionando verificação para o xeque e xeque-mate

- 54c73a8 (forçando jogador salvar o rei de xeque)
> Desabilitar movimentos que não salvam o rei quando este estiver em xeque

- 0f42954 (O jogador agora nao pode colocar o proprio rei em cheque, e jogo reinicia ao apertar R)
> Desabilitar movimentos que colocam o rei em xeque e adicionando comando para reiniciar o jogo

- fcadfb6 (Promoção do peao por console)
> adicionando comando no console para promover o peão quando este chegar ao final do tabuleiro

- 38544e6 (Removendo tabuleiro de teste)
> Removendo tabuleiro que não é mais utilizado

- f81067c (Removendo função desnecessária na interface e escurecendo as peças pretas)
> Refactor do código para remover método e escurecer peças pretas

- c9f4dc7 (feat: criado arquivo para o módulo da IA.)
> feat:criado arquivo para classes e funções auxiliares. feat: adicionado informações sobre o jogo no README.feat: adicionado métodos auxiliares para a movimentação de 'roque' do rei.

- 742ed04 (feat: criado arquivo para o módulo da IA.)
>feat:criado arquivo para classes e funções auxiliares.
feat: adicionado informações sobre o jogo no README.
feat: adicionado métodos auxiliares para a movimentação de 'roque' do rei.
amend: ajuste nos comentários e remoção de prints para desenvolvimento.

- 2667e3a (merge-fix)
> Retornando arquivo do commit anterior

- 193d587 (feat: criado arquivo para o módulo da IA.)
> feat:criado arquivo para classes e funções auxiliares.
feat: adicionado informações sobre o jogo no README.
feat: adicionado métodos auxiliares para a movimentação de 'roque' do rei.
amend: ajuste nos comentários e remoção de prints para desenvolvimento.

- 8c8c076 (feat: adicionado cache de movimentos disponíveis do tabuleiro)
> feat: adicionado método para estruturar os dados da cache de movimentos
feat: adicionado métodos para conversão de dados para o formato aproriado em algumas classes auxiliares.

- 3796460 (feat:Adicionado suporte no módulo de IA para selecionar o próximo movimento a ser realizado.)
> feat: adicionado chamada do módulo de movimento ao apertar a tecla A para fins de debug.

- fddc473 (feat: Implementado a movimentação da IA ao apertar a tecla 'a'.)
> Adicionando a movimentação da IA toda vez que for o turno do oponente e o usuário apertar a tecla 'a'

- 13ea1a8 (fix: Ajustado para atualizar o status do jogo e a lista da cache de movimentos para cálculo da IA.)
> Ajuste para atualização durante o jogo.

- 70cbb16 (chore: Atualizando README)
> Ajuste no README para refletir as mudanças no jogo até o momento

- a2f0d18 (chore: atualizando o branch de bug com a main e adicionando .gitignore.)
> Atualização das branches e gitignore

- 7426f05 (chore: adicionado o Release.md no readme)
> Adicionando link para o arquivo de releases no README

- cefb8be (fix: correção do erro de movimentação introduzido no commit anterior)
> Fix do commit anterior

- 2af9ba2 (fix: adição de parâmetro na função de movimentação que estava causando erros.)
> Adicionando tabuleiro como parâmetro na função de movimentação

- 91be056 (Tamanho da tela responsiva)
> Adicionando lib para fazer o jogo responsivo para qualquer tela de computador

- b448893 (chore: atualização do gitignore)
> Adicionando o gitignore novamente

- 70f2dde (feat: adicionado alternativa condicional para importação da biblioteca do sistema)
> a fim de facilitar o desenvolvimento, evita merges desnecessários quando não acha a lib

- 8bfa65b (Correção de bug de movimentação do peão)
> Foi corrigido o bug em que o peão podia pular uma peça durante sua primeira jogada

- b2e6b72 (fix: correção da movimentação do jogador, agora chama o método correto)
> feat: adicionado suporte para a IA poder movimentar peças de ambas as cores (antes estava limitado à peças pretas).

- 00996c9 (Menu de promoção do peao)
> Adicionando menu quando o peão chega ao final do tabuleiro (promoção)

- dacdd80 (Menu de modo de jogo)
> Adicionando menu inicial do jogo (escolha de modo de jogo)

-  (Adicionando lista de bugs a serem corrigidos e commits da release 2 no arquivo de releases)

# To Do list (bugs)

- Peão está passando por cima de algumas peças de adversários (Resolvido commit: 8bfa65b)

- IA não está respeitando os turnos
