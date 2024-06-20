#Autor: Danielle Ozaki
#Data: 24/05/2024
#Versão: 1.0
#Descriçaõ: Faça um algoritmo que receba 5 notas e imprima a média final do aluno
#           Exemplo:
#           Nota 1: 10 
#           Nota 2: 10
#           Nota 3: 10
#           Nota 4: 10
#           Nota 5: 10
#           Média final: 10

#======================================================================================
#Entrada
nota1 = int(input('insira a nota 1:'))
nota2 = int(input('insira a nota 2:'))
nota3 = int(input('insira a nota 3:'))
nota4 = int(input('insira a nota 4:'))
nota5 = int(input('insira a nota 5:'))

#Processamento
#Soma
somatória = nota1 + nota2 + nota3 + nota4 + nota5
print(nota1, ' + ', nota2, ' + ', nota3, ' + ', nota4, ' + ', nota5, ' = ', somatória) # =35

#Divisão
Média = somatória / 5
print(somatória, ' / ', 5, ' = ', Média)

#Saída 
print('A média do aluno é:', Média)
