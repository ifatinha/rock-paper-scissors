"""
Este módulo contém uma função para exibir um menu de seleção de jogadas para um jogo de Pedra,
Papel e Tesoura.

A função `menu()` exibe um menu interativo onde o jogador pode escolher entre as opções de jogadas:
Papel, Pedra, Tesoura, ou sair do jogo.
"""


def menu():
    """
    Exibe um menu interativo para o jogador escolher sua jogada no jogo de Pedra, Papel e Tesoura.

    O menu apresenta as seguintes opções:
    - [1] Papel
    - [2] Pedra
    - [3] Tesoura
    - [0] Sair

    Retorna:
        str: A entrada do jogador, representando a escolha da jogada ou a opção de sair.
    """

    return """### Nova Jogada
    [1] Papel
    [2] Pedra
    [3] Tesoura
    [0] Sair
    => """
