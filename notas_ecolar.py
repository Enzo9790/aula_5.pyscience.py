situacao = "" 
media_geral = 0  
def ler_notas():
    """Lê as notas do aluno e retorna uma lista."""
    print("\n=== Entrada de Notas ===")
    notas = []  
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    """Calcula e retorna a média das notas."""
    global media_geral  
    media_geral = sum(notas) / len(notas)
    return media_geral

def definir_situacao():
    """Define a situação do aluno com base na média."""
    global situacao 
    if media_geral >= 7:
        situacao = "Aprovado"
    elif media_geral >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

def exibir_resultado():
    """Exibe o resultado final."""
    print("\n=== Resultado Final ===")
    print(f"Média: {media_geral:.2f}")
    print(f"Situação: {situacao}")


def main():
    notas = ler_notas()
    calcular_media(notas)
    definir_situacao()
    exibir_resultado()


main()
