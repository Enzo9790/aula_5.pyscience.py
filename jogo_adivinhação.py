import random


tentativas_totais = 0

def gerar_numero_secreto():
    """Gera um número secreto aleatório entre 1 e 100 (variável local)."""
    numero = random.randint(1, 100)
    return numero

def verificar_palpite(palpite, numero_secreto):
    """Verifica se o palpite do jogador está correto e retorna o resultado."""
    global tentativas_totais  
    tentativas_totais += 1

    if palpite < numero_secreto:
        return "Tente um número MAIOR!"
    elif palpite > numero_secreto:
        return "Tente um número MENOR!"
    else:
        return "Parabéns! Você acertou!"

def jogar():
    """Função principal do jogo."""
    print("Bem-vindo ao Jogo da Adivinhação!")
    numero_secreto = gerar_numero_secreto()
    acertou = False

    while not acertou:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            resultado = verificar_palpite(palpite, numero_secreto)
            print(resultado)

            if resultado == "Parabéns! Você acertou!":
                acertou = True
        except ValueError:
            print("Por favor, digite apenas números inteiros.")

    print(f"Você precisou de {tentativas_totais} tentativas para acertar!")


if __name__ == "__main__":
    jogar()
