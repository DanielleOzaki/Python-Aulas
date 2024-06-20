# Autor: Danielle Ozaki
# Data: 04/06/2024
# Versão: 2.0
# Algoritimo: Aumento salário
# Descrição: Faça um programa que receba o salário de um funcionário, 
#           calcule e mostre o novo salário, sabendo-se que:

#           Salário < R$ 1000,00 aumento de 25%
#           Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%
#           Salário >= R$ 2000,00 aumento de 10%
#==========================================================================

#Variável
salario = 0
salario_aumento = 0
porcentagem = ''

#Entrada
salario = float(input('Insira o valor do salario: ')) #float é numoero quebrado

#Processamento
if (salario < 1000):
    salario_aumento = salario * 1.25
    porcentagem = '25%'

elif (salario >= 1000 and salario < 2000):
    salario_aumento = salario * 1.15
    porcentagem = '15%'

elif (salario >= 2000):
    salario_aumento = salario * 1.10
    porcentagem = '10%'

salario_aumento = round(salario_aumento, 2) #round = arredondar valores

#Saída
print('Seu salário de', salario, 'sofreu um aumento de', porcentagem, ', salário atual é', salario_aumento)