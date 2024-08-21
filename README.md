# Jogo de Pedra, Papel e Tesoura

Este projeto é uma implementação simples do jogo Pedra, Papel e Tesoura em Python. O jogo permite que um jogador competia contra um oponente de computador e mantém o controle das pontuações.

## Estrutura do Projeto

- `functions/game.py`: Contém a lógica principal do jogo.
- `enums/game_move.py`: Define os movimentos possíveis usando uma enumeração.
- `util/menu.py`: Fornece as opções de menu para o jogo.
- `util/prompt.py`: Gerencia a entrada do usuário para o jogo.

## Recursos

- Jogador vs Máquina: Jogue contra um oponente de computador.
- Pontuação: Mantém o controle das pontuações do jogador e da máquina.
- Exibição Clara: Mostra a pontuação atual de forma formatada.

## Configuração

Para executar este projeto, certifique-se de ter o Python instalado. Não são necessárias bibliotecas externas além da Biblioteca Padrão do Python.

### Executando o Jogo

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/rock-paper-scissors.git

2. Navegue até o diretório do projeto:
    
    ``` cd rock-paper-scissors

3. Execute o script do jogo:
    
    ``` python game.py

## Uso

Após iniciar o jogo, siga o menu exibido para escolher sua jogada. A máquina fará uma jogada automaticamente, e o resultado será exibido junto com a pontuação atualizada.

### Exemplo de Menu

Escolha sua jogada:
1. Papel
2. Pedra
3. Tesoura
4. Sair

    ```
    ========================================
    MÁQUINA: 2          | VOCÊ: 3         
    ========================================

    ```

## Documentação do Código

- **`get_move(option)`**: Retorna o movimento correspondente à opção escolhida pelo jogador.
- **`machine_move()`**: Gera um movimento aleatório para a máquina.
- **`check_move(player_option, player_score, machine_score)`**: Verifica o resultado de uma jogada e atualiza a pontuação.
- **`update_score(score)`**: Atualiza a pontuação adicionando um ponto.
- **`display_score(player_score, machine_score)`**: Exibe a pontuação atual do jogo.

## Contribuindo

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.