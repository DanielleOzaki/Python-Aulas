'''
Autor: Danielle Ozaki
Data: 13/06/2024
Versão: 1.0
Algoritmo: Prova
Descrição: Faça um programa que receba dois valores, sendo que o 
            primeiro deve ser menor que o segundo.
            O programa deve apresentar todos os números ímpares
            contidos nestas sequências.
            (Modulo %  //  Exemplo: 7%2 = 1)    #Para descobrir o impar tem q dividir por 2, X % 2
'''
#=====================================================================
numero1 = 0
numero2 = 0

numero1 = int(input('Digite o valor inicial do seu range: '))
numero2 = int(input('Digite o valor final do seu range: '))

for numRange in range(numero1, numero2):
    resto = numRange % 2            #0 é par // 1 impar
    # print(f'{numRange} % 2 = {resto}')
    if resto == 1:
        print(numRange)