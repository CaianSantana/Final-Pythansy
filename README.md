# Pythons-Duel

Precisamos implementar que ele seja Dual Thread com seus clientes

Cada playerMantem sua conexao viva ate o fim do jogo reutiliza aquele socket

precisamos de um loop no servidor

Seguinte precisamos de um protocolo para este projeto.

<h2>Run pip install websockets<h2>


<H1>Rastle protocol</H1>



cada letra deve simbolizar um evento

J -> Pedido para jogar deve seguir o formato "J {nome do jogador}\0"

H -> hit ou acerto formato "H de:{Id de quem acertou} to:{Id de quem foi acertado} Dano:{quantidade}"

M -> movimento nao sei como fazer isso mas os jogadores tem que que manter suas telas atualizadas com as posicoes dos jogadores

F -> fim de jogo servidor manda pros clientes fecha a conexao e envia "F -> {você venceu}" ou "F -> {você perdeu}"

tem algumas coisas que nos permitem usar Json pode facilitar a comunicacao