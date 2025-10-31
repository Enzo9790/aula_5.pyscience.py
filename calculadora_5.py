def somar(a,b):
    print(a + b)


def subtrair(a,b):
    print(a - b)


def multiplicar(a,b):
    print(a * b)


def dividir(a,b):
    print(a / b)



def calculadora():
    while True:
        operacao =  input('Escolha a operação: + - * /')
        if operacao == '+':
            n1  =  float(input('='))
            n2  =  float(input('='))
            somar(n1, n2)    
        if operacao == '-':
            n1  =  float(input('='))
            n2  =  float(input('='))
            subtrair(n1, n2)              
        elif operacao == '*':
            n1  =  float(input('='))
            n2  =  float(input('='))
            multiplicar(n1, n2)                          
        elif operacao == '/':
            n1  =  float(input('='))
            n2  =  float(input('='))
            dividir(n1, n2)   


# calculadora()




def verificarO_indice(num,lista):
    indice  =  lista.index(num)
    print(indice)



lista  =  [102,35,5,6]
n  = int(input('numero: '))


verificarO_indice(n, lista)

def cal_val_hr(carga, salario):
    return salario / carga
