imc = 0         
situacao = ""    

def ler_dados():
    """Lê peso e altura do usuário."""
    print("\n=== Entrada de Dados ===")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    return peso, altura 

def calcular_imc(peso, altura):
    """Calcula o IMC com base no peso e altura."""
    global imc  
    imc = peso / (altura ** 2)
    return imc

def definir_situacao():
    """Define a situação corporal com base no IMC."""
    global situacao  #
    if imc < 18.5:
        situacao = "Abaixo do peso"
    elif imc < 25:
        situacao = "Peso normal"
    elif imc < 30:
        situacao = "Sobrepeso"
    elif imc < 35:
        situacao = "Obesidade Grau I"
    elif imc < 40:
        situacao = "Obesidade Grau II"
    else:
        situacao = "Obesidade Grau III (mórbida)"

def exibir_resultado():
    """Mostra o resultado final do cálculo."""
    print("\n=== Resultado do IMC ===")
    print(f"IMC calculado: {imc:.2f}")
    print(f"Classificação: {situacao}")


def main():
    peso, altura = ler_dados()
    calcular_imc(peso, altura)
    definir_situacao()
    exibir_resultado()


main()
