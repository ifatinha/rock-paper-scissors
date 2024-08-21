"""
Módulo principal para o jogo de Pedra, Papel e Tesoura.

Este módulo implementa a lógica principal do jogo de Pedra, Papel e Tesoura, onde
o jogador pode escolher uma jogada, competir contra a máquina e acompanhar o placar
atualizado em tempo real. O jogo continua até que o jogador escolha a opção de encerrar.

O módulo depende dos seguintes submódulos:
- `util.menu`: Fornece as opções de jogada disponíveis no jogo.
- `util.prompt`: Captura a entrada do usuário para selecionar uma jogada.
- `functions.game`: Contém a lógica do jogo, incluindo a verificação da jogada e
  a atualização do placar.

Classes e funções principais:
- `initialize`: Função que inicializa o loop principal do jogo, gerenciando as jogadas
  e o placar até que o jogador decida encerrar o jogo.
"""


from util.menu import menu
from util.prompt import get_user_input
from util.clear import clear_terminal
from functions.game import Game


def initialize():
    """
    Inicializa o jogo de Pedra, Papel e Tesoura.

    Este método inicia o loop principal do jogo, onde o jogador pode escolher
    entre as opções de jogadas ou encerrar o jogo. O jogo continua até que o
    jogador escolha a opção de encerrar. O placar do jogador e da máquina é
    atualizado e exibido a cada jogada.
    """

    pontos_jogador = 0
    pontos_maquina = 0

    while True:
        opcao = get_user_input(menu())

        if opcao in [1, 2, 3]:
            pontos_jogador, pontos_maquina = Game.verifica_jogada(opcao, pontos_jogador, pontos_maquina)
            Game.mostra_placar(pontos_jogador=pontos_jogador, pontos_maquina=pontos_maquina)
        elif opcao == 0:
            print("@@@ Encerrando jogo!!! @@@")
            break
        else:
            print("@@@ Opção inválida. Tente novamente! @@@")

    clear_terminal()
    print("RESULTADO")
    Game.mostra_placar(pontos_jogador=pontos_jogador, pontos_maquina=pontos_maquina)


if __name__ == "__main__":
    initialize()
