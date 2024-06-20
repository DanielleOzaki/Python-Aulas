# Autor: Danielle Ozaki
# Data: 04/06/2024
# Versão: 2.0
# Algoritimo: Multa de velocidade
# Descrição: Escreva um programa que leia a velocidade máxima permitida em
#           uma avenida e velocidade com que o motorista estava dirigindo nela
#           e  calcule a multa que uma pessoa vai receber;

#           Velocidade Ultrapassada             Valor da Multa
#           Até 10 km/h                             R$ 50,00
#           11 a 30 km/h                            R$ 100,00
#           Mais 31 km/h                            R$ 200,00
#================================================================================

#Variável
velocidade = 0
ultrapassado = 0
diferencaVelocidade = 0 
multa = ''

#Entrada
velocidade = int(input('Qual a velocidade permitida? '))
ultrapassado = int(input('Qual a velocidade do veículo? '))

#Processamento
diferencaVelocidade = ultrapassado - velocidade

if diferencaVelocidade > 0 and diferencaVelocidade <= 10:
    multa = 'R$ 50,00'
          
elif diferencaVelocidade >= 11 and diferencaVelocidade <= 30:
    multa = 'R$ 100,00'

elif diferencaVelocidade >= 31:
    multa = 'R$ 200,00'

else:
    multa = 'R$ 0,00'

#Saída
print('Valor da multa é de', multa)