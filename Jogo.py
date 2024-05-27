from Funcoes import *


def main():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        print(f"Vez do jogador {jogador_atual}")
        linha, coluna = obter_jogada()

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns! O jogador {jogador_atual} venceu!")
                break

            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")


if __name__ == "__main__":
    main()

