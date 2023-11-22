# Final Pythansy


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
- [ ]  Capacidade de salvar progresso

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









