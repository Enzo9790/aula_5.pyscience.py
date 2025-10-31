# SISTEMA DE CALCULO HORAS 
# 1 -  calculo da hora normal
def cal_val_hr(carga, salario):
    return salario / carga


# 2 -  hora exta 
def hora_extra(valor_hora):
    return valor_hora * 1.5


# 3 -  quantas horas extrar realizadas
def quantidade_extra(quantidade, valor_hr_extra):
    return quantidade * valor_hr_extra


# 4 - total salário
def sal(total_extra, salario):
    return total_extra +  salario


def sistema():
    salario  =  float(input('Salario: '))
    quantidade_ex =  float(input('Hora extra: '))
    carga  = float(input('Carga: '))


    valor_hora  =  cal_val_hr(carga, salario)
    print('VALOR HORA R$', round(valor_hora, 2))
    print('----------------------')


    extra  =  hora_extra(valor_hora)
    print('VALOR DA HORA EXTRA R$:', round(extra,2))


    print('----------------------')
    quantidade_ = quantidade_extra(quantidade_ex,extra )
    print('TOTAL HORA EXTRA R$', round(quantidade_,2))
    print('----------------------')
    
    salario_t = sal(quantidade_,salario)
    print('Salario total: R$', round(salario_t,2))


    print('----------------------')
    
sistema()    




