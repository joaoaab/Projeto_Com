# Projeto da disciplina Infraestrutura de Comunicação 2016.2
__Objetivos__ :

1. Introdução:
Este projeto é dividido em 3 questões, as quais estão relacionadas com
temas abordados em sala de aula. As questões devem ser entregues juntas,
juntamente com um relatório especificando o que foi feito em cada uma delas.

2. Regras
- Os códigos podem ser implementados em C/C++, Java ou Python (altamente recomendado).
- O relatório final deve conter uma explicação bem detalhada do que está no código.
- É proibido usar o módulo select.
- Cópias acarretarão em 0 (Zero) para todas as equipes pegas.
- A data de entrega só poderá ser alterada com a permissão do professor.

- __Protocolo confiável sobre UDP (Camada de Transporte)__:

- [X] Deverá ser implementada uma camada de confiabilidade sobre UDP.
- [X] Podem ser utilizados os métodos vistos em sala, GBN e retransmissão seletiva. (escolhido : GBN)
- [X] Para melhor controle e visualização do processo, o programa deverá indicar sempre que uma transmissão ou retransmissão ocorrer.
- [x] A aplicação será a transmissão de strings de um programa para outro (podem ser diferentes).

- __Super-Trunfo (Cliente e Servidor)__:

- [x] Deverá ser implementado o jogo de super-trunfo.

- [x] Sobre o jogo:
• O baralho possui 32 cartas, cada com um número de 1 a 8 e uma letra de A a D.
• As regras do jogo encontram-se em:https://docs.google.com/document/d/18CkS7rS9JrRdxTYo33Ao3xUjYASJNG412ACeF2Sep3c/preview
- [x] Servidor: Deverá controlar toda a lógica do jogo. Inclui: Distribuição das cartas, avaliação do resultado de cada turno e verificação da condição de vitória.
- [x] Cliente: Deverá receber as jogadas do usuário e as mandar para o servidor. Deverá mostrar as cartas escolhidas pelos adversários a cada turno.

- __Batalha Naval (P2P)__:

- [ ] Deverá ser implementado apenas um programa, que rodará para cada usuário.
 
__Sobre o jogo___:

- Jogam dois jogadores.

- Cada um possui uma grade 10x10, escondida do adversário.

- Cada um possui navios de diferentes tamanhos: 1 de tamanho 5, 1 de tamanho 4, 3 de tamanho 3 e 2 de tamanho 2.

- Inicialmente, cada um põe seus navios horizontalmente ou verticalmente em sua grade.

- O resto do jogo é jogado em turnos. Cada jogador escolhe uma posição da grade adversária para atacar.

- Ele só saberá se acertou alguma coisa ou se destruiu um navio por completo.

- Ganha o adversário que destruir todos os navios inimigos.
