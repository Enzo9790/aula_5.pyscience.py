import random

print('Seja bem vindo(a) site de jogos')
print('Este é o jogo da adivinhação de números:')



        
numero_aleatorio =  random.randint(1,10)
meu_chute = int(input('chute: '))
if meu_chute == numero_aleatorio:
    print('Acertou em cheio!O número é: ', numero_aleatorio)
else:
    print('Errou feio!O número é: ', numero_aleatorio)     

