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


from util.menu import keep_playing
from util.prompt import get_user_input
from functions.game import Game


def initialize():
    """
    Inicializa o jogo de Pedra, Papel e Tesoura.

    Este método inicia o loop principal do jogo, onde o jogador pode escolher
    entre iniciar uma nova rodada ou encerrar o jogo. Caso o jogador opte por
    jogar, o método `Game.play_round()` é chamado para executar a rodada. O jogo
    continua até que o jogador escolha a opção de encerrar. Mensagens de encerramento
    e de opções inválidas são exibidas conforme necessário.
    """

    while True:
        new_game = get_user_input(keep_playing())

        if new_game == 1:
            Game.play_round()
        elif new_game == 0:
            print("@@@ Encerrando jogo! @@@")
            break
        else:
            print("@@@ Opção inválida. Tente novamente! @@@")


if __name__ == "__main__":
    initialize()
