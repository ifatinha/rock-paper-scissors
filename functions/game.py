from enums.game_move import GameMove
import random


class Game():

    @staticmethod
    def get_jogada(opcao):
        """
        Retorna a jogada correspondente à opção escolhida pelo jogador.

        Este método mapeia a opção numérica escolhida pelo jogador para a jogada
        correspondente no jogo de Pedra, Papel e Tesoura.

        Parâmetros:
        - opcao (int): A opção escolhida pelo jogador (1 para Papel, 2 para Pedra, 3 para Tesoura).

        Retorno:
        - str: A jogada correspondente (Papel, Pedra ou Tesoura).

        Exemplo:
            get_jogada(1) retorna "Papel".
        """

        jogadas = {
            1: GameMove.PAPEL.value,
            2: GameMove.PEDRA.value,
            3: GameMove.TESOURA.value
        }

        return jogadas[opcao]

    @staticmethod
    def jogada_maquina():
        """
        Gera a jogada da máquina aleatoriamente.

        Este método escolhe uma jogada aleatória para a máquina entre Pedra, Papel e Tesoura.
        Utiliza um número aleatório entre 1 e 3 para determinar a jogada e retorna a jogada correspondente.

        Retorno:
        - str: A jogada escolhida pela máquina (Papel, Pedra ou Tesoura).

        Exemplo:
            jogada_maquina() pode retornar "Pedra", "Papel" ou "Tesoura".
        """

        numero = random.randint(1, 3)
        return Game.get_jogada(numero)

    @staticmethod
    def verifica_jogada(opcao_jogador, pontos_jogador, pontos_maquina):
        """
        Verifica o resultado de uma jogada no jogo Pedra, Papel e Tesoura.

        Args:
            opcao_jogador (str): A jogada do jogador ("Pedra", "Papel" ou "Tesoura").
            pontos_jogador (int): Pontuação atual do jogador.
            pontos_maquina (int): Pontuação atual da máquina.

        Returns:
            tuple: Uma tupla contendo a nova pontuação do jogador e da máquina.
        """

        jogada_maquina = Game.jogada_maquina()
        jogada_usuario = Game.get_jogada(opcao_jogador)

        regras = {
            (GameMove.PEDRA.value, GameMove.TESOURA.value): ("Você Ganhou! Pedra quebra Tesoura", True),
            (GameMove.PAPEL.value, GameMove.PEDRA.value): ("Você Ganhou! Papel embrulha Pedra", True),
            (GameMove.TESOURA.value, GameMove.PAPEL.value): ("Você Ganhou! Tesoura corta Papel", True),
            (GameMove.TESOURA.value, GameMove.PEDRA.value): ("Você perdeu! Pedra quebra Tesoura", False),
            (GameMove.PEDRA.value, GameMove.PAPEL.value): ("Você perdeu! Papel embrulha Pedra", False),
            (GameMove.PAPEL.value, GameMove.TESOURA.value): ("Você perdeu! Tesoura corta Papel", False),
        }

        if jogada_usuario == jogada_maquina:
            resultado = f"Empate! {jogada_usuario} empata com {jogada_maquina}"
        else:
            resultado, jogador_ganhou = regras.get((jogada_usuario, jogada_maquina),  (None, None))

            if jogador_ganhou is True:
                pontos_jogador = Game.atualiza_pontuacao(pontos_jogador)
            elif jogador_ganhou is False:
                pontos_maquina = Game.atualiza_pontuacao(pontos_maquina)

        print(resultado)
        return pontos_jogador, pontos_maquina

    @staticmethod
    def atualiza_pontuacao(pontos):
        """
        Atualiza a pontuação adicionando um ponto.

        Este método recebe a pontuação atual e retorna a nova pontuação com um ponto a mais.

        Parâmetros:
        - pontos (int): A pontuação atual do jogador.

        Retorno:
        - int: A nova pontuação após adicionar um ponto.

        Exemplo:
            atualiza_pontuacao(3) retorna 4.
        """
        return pontos + 1

    @staticmethod
    def mostra_placar(pontos_jogador, pontos_maquina):
        """
        Exibe o placar atual do jogo.

        Este método exibe o placar atual do jogo no console, mostrando a pontuação da máquina
        e a pontuação do jogador de forma clara e formatada.

        Parâmetros:
        - pontos_jogador (int): A pontuação atual do jogador.
        - pontos_maquina (int): A pontuação atual da máquina.

        Exemplo:
            mostra_placar(3, 2) imprime:
            ========================================
            MAQUINA: 2 | VOCÊ: 3
        """

        print("="*40)
        print(f"MAQUINA: {pontos_maquina:<10} | VOCÊ: {pontos_jogador:<10}")
        print("="*40)
