def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")

def obter_jogada():
    while True:
        try:
            linha = int(input("Escolha a linha (1, 2 ou 3): ")) - 1
            coluna = int(input("Escolha a coluna (1, 2 ou 3): ")) - 1
            if 0 <= linha < 3 and 0 <= coluna < 3:  # Verifica se os índices estão dentro dos limites do tabuleiro
                return linha, coluna
            else:
                print("Por favor, escolha valores válidos para linha e coluna.")
        except ValueError:
            print("Por favor, insira números inteiros para linha e coluna.")

def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador \
                or tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador \
            or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True
