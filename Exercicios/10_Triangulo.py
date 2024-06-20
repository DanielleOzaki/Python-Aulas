# Autor: Danielle Ozaki
# Data: 06/06/2024
# Versão: 1.0
# Algoritimo: Tipo de Triângulo
# Descrição: Faça um programa que receba 3 valores e verifique se
#           eles podem representar os lados em um triângulo;

#           Triângulo escaleno: triângulo que possui todos os lados com medidas diferentes.
#           Triângulo isósceles: triângulo que possui 2 lados com medidas iguais.
#           Triângulo equilátero: triângulo que possui todos os lados iguais.

#           Lembrando que a soma das medidas de 2 lados de um triângulo é sempre maior 
#           que a medida do terceiro lado.
#==============================================================================================

#variável
lado1 = 0
lado2 = 0
lado3 = 0
triangulo = ''

#entrada
lado1 = int(input('Qual o valor do lado 1 do triângulo? '))
lado2 = int(input('Qual o valor do lado 2 do triângulo? '))
lado3 = int(input('Qual o valor do lado 3 do triângulo? '))

#processamento
if ((lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2 and
    (lado1 > 0 and lado2 > 0 and lado3 > 0)):          
    print('O triângulo existe')

    if lado1 == lado2 and lado2 == lado3:       # OU lado1 == lado2 == lado3:
        triangulo = 'triângulo Equilátero'

    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        triangulo = 'triângulo Isóceles'

    elif lado1 != lado2 != lado3:
        triangulo = 'triângulo Escaleno'

    print('O triângulo é um', triangulo)

else:
    print('Triângulo não existe')
