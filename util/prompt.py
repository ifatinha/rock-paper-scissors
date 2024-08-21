"""
Este módulo fornece uma função utilitária para solicitar e validar entradas do usuário.

Funções:
    - get_user_input(prompt): Solicita uma entrada numérica do usuário e a converte em um número inteiro.

    O módulo é projetado para simplificar a captura de entrada de usuário em forma de números inteiros,
    tratando de forma adequada os erros de conversão e fornecendo feedback ao usuário em caso de entradas inválidas.
"""


def get_user_input(prompt) -> int:
    """
    Solicita uma entrada numérica do usuário com base em um prompt.

    Args:
        prompt (str): O texto a ser exibido ao usuário.

    Returns:
        int or None: O número inteiro inserido pelo usuário ou None em caso de erro.
    """

    try:
        return int(input(prompt))
    except ValueError:
        print("@@@ Entrada inválida, por favor insira um número. @@@")
        return None
