# Final Pythansy

<<<<<<<< HEAD:Game/README.md
========
Precisamos implementar que ele seja Dual Thread com seus clientes

Cada player Mantem sua conexao viva ate o fim do jogo reutiliza aquele socket

precisamos de um loop no servidor

Seguinte precisamos de um protocolo para este projeto.

<h2>Run pip install websockets<h2>

<H1>Rastle protocol</H1>

cada letra deve simbolizar um evento

J -> Pedido para jogar deve seguir o formato "J {nome do jogador}\0"

A -> aceito -> devolve o id do player

H -> hit ou acerto formato "H from:{Id de quem acertou} to:{Id do boneco do inimigo} Dano:{quantidade}"

E -> fim da jogada fez todas as suas ações ou escolheu terminar

T -> {Numero do turno} diz pros clientes quem possui o turno no momento 

F -> fim de jogo servidor manda pros clientes fecha a conexao e envia "F -> {você venceu}" ou "F -> {você perdeu}"

tem algumas coisas que nos permitem usar Json pode facilitar a comunicacao

>>>>>>>> branch2:README.md

## To-Do List

Para criar o jogo, devemos concluir certas etapas que estarão listadas a seguir. Trocar o "- [ ] " por "- [X] " quando concluir algum item da lista.

### Etapa artistica:
***Sprites dos personagens devem ser .png e ter a seguinte resolução de imagem: 80x131****
*Inimigos maiores são excessão

* Escolher Tema do jogo
    - [ ]  Feito
    > Ou seja, os personagens pertencem à um contexto específico?
        (ex.: temática asiática, só podem personagens com esse estilo, como samurais e etc).

* Direção de arte 
    - [ ]  Feito
    > Qual o padrão artístico devemos seguir para os sprites?
         (ex.: personagens são "sticks", então todos os personagens tem que seguir esse modelo de sprite)

### Etapa Desenvolvimento:
***Seguir princípios SOLID*** 

- [ ]  Estabelescer conexão com servidor quando o jogo iniciar
- [ ]  Capacidade de salvar progresso -> melhor mudar para um sistema de torneio continuo desafiante 1 2 e 3

#### Etapa de Menu:

- [ ]  Criar um menu inicial: 
    - [ ]  Criar uma seleção de personagens 
    - [ ]  Carregar progresso salvo 

#### Etapa de Jogo:
 
* classe Cenário:
    - [ ]  conteúdo do Cenário(Posição dos jogadores e monstros conforme sua formação)

* classe Mapa: 
    - [ ]   Possuir um objeto do tipo Cenário 
    - [ ]   Preencher a tela com elementos de acordo com um objeto do tipo Cenário 
    - [ ]   Colocar os sprites do mapa 

* classe Personagem:    
    - [ ]   Possuir atributos de vida, dano, velocidade e etc
    - [ ]   Possuir uma forma de "função"(ex.: Mago, Guerreiro)

* classe Jogador: 
    - [ ]   Possuir objeto do tipo Personagens
    - [ ]   Cada personagem deve agir conforme input do jogador em seu respectivo turno
* classe Combate:
    - [ ]   Possuir objeto do tipo Jogador
    - [ ]   Possuir objeto do tipo inimigos
    - [ ]   Deve ser capaz de dizer quando o combate terminar


* classe Main:
    - [ ]   Possuir as regras gerais do jogo conforme personagens, inimigos e combate

* classe App:
    - [ ]   Possuir o método rodar que utiliza uma instância da classe main para fazer o jogo funcionar

* classe Configuração:
    - [ ] Possuir as configurações gerais do jogo, que podem ser utilizadas por todas as outras classes do jogo









