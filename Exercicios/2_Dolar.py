#Autor: Danielle Ozaki
#Data: 24/05/2024
#Versão: 1.0
#Descriçaõ: Faça um algoritimo que um valor na moeda real (R$).
#           a cotação da conversão REAL para DÓLAR, e apresente
#           a quantidade desse valor em dólar ($) 
#=================================================================

#           Exemplo de execucao:
#           Insira o valor em real = 5000
#           Insira a cotação do dia = 5
#           R$5000,00 esquivale a $1000,00
#==================================================================
#Inicio
#necessario fazer o casting (conversao de tipos de dados)
#float <= string
#5000,00 <= '5000'
dolar = float(input('insira o valor do dólar:'))
real = float(input('insira o valor do real:' ))

#Processamento
resultado = real / dolar
print(real, ' / ', dolar, ' = ', resultado)

#Saída
print('O valor do dolar equivale á:', resultado)
