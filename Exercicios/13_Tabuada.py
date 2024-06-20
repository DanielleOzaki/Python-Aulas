'''
Autor: Danielle Ozaki
Data: 13/06/2024
Versão: 1.0
Algoritmo: Tabuada
Descrição: Faça um algoritmo que calcule a tabuada de um
            número digitado pelo usuário.
'''
#=============================================================
#No 'FOR" não precisa de variável

multiplicador = int(input('Digite o número: '))
for numero in range(11):
    resultado = multiplicador * numero
    print(multiplicador, 'x', numero, '=', resultado)       
    #OU print(f'{multiplicador} x {numero} = {resultado}')      #interpolação     #f(format)
    #OU print(f'{multiplicador} x {numero} = {multiplicador * numero}')