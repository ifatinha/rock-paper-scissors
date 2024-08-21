"""
Este módulo define uma enumeração para representar os tipos de jogadas em um jogo de
Pedra, Papel e Tesoura.

A enumeração `TypesPlays` contém três membros:
- `PAPEL`: Representa a jogada "Papel".
- `TESOURA`: Representa a jogada "Tesoura".
- `PEDRA`: Representa a jogada "Pedra".

Este módulo pode ser usado para criar jogadas válidas e compará-las em um jogo de
Pedra, Papel e Tesoura.
"""


from enum import Enum


class GameMove(Enum):

    """
    Enumeração para representar os tipos de jogadas no jogo de Pedra, Papel e Tesoura.

    Membros:
    - `PAPEL`: Representa a jogada "Papel".
    - `TESOURA`: Representa a jogada "Tesoura".
    - `PEDRA`: Representa a jogada "Pedra".

    Cada membro da enumeração é associado a uma string que representa o nome da jogada.
    """

    PAPEL = "Papel"
    TESOURA = "Tesoura"
    PEDRA = "Pedra"
