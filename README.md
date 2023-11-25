# Final Pythansy


========
Precisamos implementar que ele seja Dual Thread com seus clientes

Cada player Mantem sua conexao viva ate o fim do jogo reutiliza aquele socket

precisamos de um loop no servidor

Seguinte precisamos de um protocolo para este projeto.

<h2>Run pip install websockets<h2>

<H1>Rastle protocol</H1>

<h3>Para o Server</h3>

<p>todo json deve conter um campo "action". Exemplo: "action":"Join"</p> 


Join -> Pedido para jogar deve seguir o formato:

{
    "action":"Join",
    "nome":"Yasmin yaz bollaz"
}

Char -> cria personagem, formato:

{
    "action":"char",
    "class":"empty",
    "playerId":"0",
    "hp":"25",
    "attack":"30",
    "ability":"12",
    "armor":"10",
    "magicResistance":"15",
    "speed":"35",
    "mana":"20"
}

Hit -> hit ou acerto, formato:

{
    "action":"hit",
    "playerId":"0",
    "with":"0",
    "to":"0",
    "dano":"10"
}

E -> fim da jogada fez todas as suas ações ou escolheu terminar

<h3>Para o Cliente</h3>

<p>todo json deve conter um campo "Response". Exemplo: "Response":"accepted"</p> 

accepted -> aceitou o join, formato:

{   
    "Response":"accepted",
    "playerId":"0"
}

U -> update -> 

{
    "Response":"update"
    "attacker":"0",
    "target":"0",
    "dano":"10"
}

T -> {Numero do turno} diz pros clientes quem possui o turno no momento 

F -> fim de jogo servidor manda pros clientes fecha a conexao e envia "F -> {você venceu}" ou "F -> {você perdeu}"

tem algumas coisas que nos permitem usar Json pode facilitar a comunicacao

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
    - [x]   Possuir atributos de vida, dano, velocidade e etc
    - [ ]   Possuir uma forma de "função"(ex.: Mago, Guerreiro)

* classe Jogador: 
    - [x]   Possuir objeto do tipo Personagens
    - [x]   Cada personagem deve agir conforme input do jogador em seu respectivo turno
* classe Combate:
    - [x]   Possuir objeto do tipo equipe do jogador
    - [x]   Possuir objeto do tipo equipe do inimigo
    - [x]   Deve ser capaz de dizer quando o combate terminar


* classe Main:
    - [x]   Possuir as regras gerais do jogo conforme personagens, inimigos e combate

* classe App:
    - [x]   Possuir o método rodar que utiliza uma instância da classe main para fazer o jogo funcionar

* classe Configuração:
    - [x] Possuir as configurações gerais do jogo, que podem ser utilizadas por todas as outras classes do jogo









