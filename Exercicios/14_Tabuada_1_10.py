'''
Autor: Danielle Ozaki
Data: 13/06/2024
Versão: 1.0
Algoritmo: Tabuada de 1 a 10
Descrição: Faça um algoritmo que calcule a tabuada de 1 a 10.
'''
#================================================================
#No "FOR" não precisa de variáveis

for multiplicador in range(11):
    print(f'-> TABUADA {multiplicador}')
    for numero in range (11):
        resultado = multiplicador * numero
        print(f'{multiplicador} x {numero} = {resultado}')
    