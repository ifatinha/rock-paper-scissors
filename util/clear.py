"""
Este módulo fornece uma função para limpar o terminal.

Atualmente, suporta a limpeza de terminal em sistemas Windows.

Funções:
- clear_terminal: Limpa o terminal do sistema operacional Windows.
"""

import os


def clear_terminal():
    """
    Limpa o terminal no sistema operacional Windows.

    Esta função executa o comando 'cls' para limpar o terminal em sistemas Windows.
    Para sistemas Linux e macOS, o comando correspondente seria 'clear', mas não está incluído nesta função.

    Não retorna nenhum valor.
    """
    os.system("cls")
