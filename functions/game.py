"""
Módulo para o jogo de Pedra, Papel e Tesoura.

Este módulo contém a classe `Game` que implementa a lógica principal do jogo de Pedra, Papel e Tesoura.
A classe oferece métodos para determinar a jogada do jogador e da máquina, verificar o resultado
da jogada, atualizar e exibir o placar.

Importações:
- `random`: Para gerar números aleatórios.
- `GameMove` de `enums.game_move`: Enum que define os movimentos possíveis (Pedra, Papel, Tesoura).

Classes:
- `Game`: Contém métodos estáticos para manipulação do jogo, incluindo obtenção de jogadas,
  verificação de resultados, atualização de pontuação e exibição do placar.
"""


from enums.game_move import GameMove
from util.menu import menu
from util.prompt import get_user_input
from util.clear import clear_terminal
import random


class Game():

    """
    Classe que gerencia a lógica do jogo de Pedra, Papel e Tesoura.

    Esta classe fornece métodos para:
    - Obter a jogada correspondente a uma opção escolhida.
    - Gerar uma jogada aleatória para a máquina.
    - Verificar o resultado de uma jogada e atualizar o placar.
    - Atualizar a pontuação do jogador e da máquina.
    - Exibir o placar atual do jogo.

    Métodos Estáticos:
    - `get_move(opcao)`: Retorna a jogada correspondente à opção escolhida pelo jogador.
    - `jogada_maquina()`: Gera a jogada da máquina aleatoriamente.
    - `verifica_jogada(opcao_jogador, pontos_jogador, pontos_maquina)`: Verifica o resultado da jogada
      e atualiza a pontuação com base nas regras do jogo.
    - `atualiza_pontuacao(pontos)`: Atualiza a pontuação adicionando um ponto.
    - `mostra_placar(pontos_jogador, pontos_maquina)`: Exibe o placar atual do jogo.
    """

    @staticmethod
    def get_move(option):
        """
        Retorna a jogada correspondente à opção escolhida pelo jogador.

        Este método mapeia a opção numérica escolhida pelo jogador para a jogada
        correspondente no jogo de Pedra, Papel e Tesoura.

        Parâmetros:
        - option (int): A opção escolhida pelo jogador (1 para Papel, 2 para Pedra, 3 para Tesoura).

        Retorno:
        - str: A jogada correspondente (Papel, Pedra ou Tesoura).

        Exemplo:
            get_move(1) retorna "Papel".
        """

        moves = {
            1: GameMove.PAPEL.value,
            2: GameMove.PEDRA.value,
            3: GameMove.TESOURA.value
        }

        return moves[option]

    @staticmethod
    def machine_move():
        """
        Gera a jogada da máquina aleatoriamente.

        Este método escolhe uma jogada aleatória para a máquina entre Pedra, Papel e Tesoura.
        Utiliza um número aleatório entre 1 e 3 para determinar a jogada e retorna a jogada correspondente.

        Retorno:
        - str: A jogada escolhida pela máquina (Papel, Pedra ou Tesoura).

        Exemplo:
            machine_move() pode retornar "Pedra", "Papel" ou "Tesoura".
        """

        numero = random.randint(1, 3)
        return Game.get_move(numero)

    @staticmethod
    def check_move(player_option, player_score, machine_score):
        """
        Verifica o resultado de uma jogada no jogo Pedra, Papel e Tesoura.

        Args:
            player_option(str): A jogada do jogador ("Pedra", "Papel" ou "Tesoura").
            player_score(int): Pontuação atual do jogador.
            machine_score(int): Pontuação atual da máquina.

        Returns:
            tuple: Uma tupla contendo a nova pontuação do jogador e da máquina.
        """

        machine_move = Game.machine_move()
        player_move = Game.get_move(player_option)

        rules = {
            (GameMove.PEDRA.value, GameMove.TESOURA.value): ("Você Ganhou! Pedra quebra Tesoura", True),
            (GameMove.PAPEL.value, GameMove.PEDRA.value): ("Você Ganhou! Papel embrulha Pedra", True),
            (GameMove.TESOURA.value, GameMove.PAPEL.value): ("Você Ganhou! Tesoura corta Papel", True),
            (GameMove.TESOURA.value, GameMove.PEDRA.value): ("Você perdeu! Pedra quebra Tesoura", False),
            (GameMove.PEDRA.value, GameMove.PAPEL.value): ("Você perdeu! Papel embrulha Pedra", False),
            (GameMove.PAPEL.value, GameMove.TESOURA.value): ("Você perdeu! Tesoura corta Papel", False),
        }

        if player_move == machine_move:
            result = f"Empate! {player_move} empata com {machine_move}"
        else:
            result, player_won = rules.get((player_move, machine_move),  (None, None))

            if player_won is True:
                player_score = Game.update_score(player_score)
            elif player_won is False:
                machine_score = Game.update_score(machine_score)

        print(result)
        return player_score, machine_score

    @staticmethod
    def update_score(score):
        """
        Atualiza a pontuação adicionando um ponto.

        Este método recebe a pontuação atual e retorna a nova pontuação com um ponto a mais.

        Parâmetros:
        - score (int): A pontuação atual do jogador.

        Retorno:
        - int: A nova pontuação após adicionar um ponto.

        Exemplo:
            atualiza_pontuacao(3) retorna 4.
        """
        return score + 1

    @staticmethod
    def display_score(player_score, machine_score):
        """
        Exibe o placar atual do jogo.

        Este método exibe o placar atual do jogo no console, mostrando a pontuação da máquina
        e a pontuação do jogador de forma clara e formatada.

        Parâmetros:
        - player_score (int): A pontuação atual do jogador.
        - machine_score (int): A pontuação atual da máquina.

        Exemplo:
            mostra_placar(3, 2) imprime:
            ========================================
            MAQUINA: 2 | VOCÊ: 3
        """

        print("="*40)
        print(f"MAQUINA: {machine_score:<10} | VOCÊ: {player_score:<10}")
        print("="*40)

    def play_round():
        """
        Executa uma rodada do jogo de Pedra, Papel e Tesoura.

        Este método inicia uma rodada onde o jogador pode escolher entre Pedra (1),
        Papel (2) e Tesoura (3), ou encerrar a rodada (0). Para cada jogada, o placar
        do jogador e da máquina é atualizado com base na escolha feita. O jogo continua
        até que o jogador decida encerrar a rodada. Ao final, o placar da rodada é
        exibido.

        Retorno:
            Nenhum.
        """

        player_score = 0
        machine_score = 0

        while True:
            option = get_user_input(menu())

            if option in [1, 2, 3]:
                player_score, machine_score = Game.check_move(option, player_score, machine_score)
                Game.display_score(player_score=player_score, machine_score=machine_score)
            elif option == 0:
                print("@@@ Encerrando jogo!!! @@@")
                break
            else:
                print("@@@ Opção inválida. Tente novamente! @@@")

        clear_terminal()
        print("RESULTADO")
        Game.display_score(player_score=player_score, machine_score=machine_score)
