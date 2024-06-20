#Autor: Danielle Ozaki
#Data: 28/05/2024
#Versao: 1.0
#Descricao: Faça um algoritimo que receba o raio em metros 
#           de um circulo e apresente a sua area
#   ---------------------------------------------------------
#           Exemplo de execução:
#           Insira o raio em metros: 5
#           Area do circulo: 78.5m^2
#           A = pi * (r ^ 2)
#============================================================ 

#Variaveis
r = 0 
a = 0 
pi = 3.14

#Entrada
r = float(input('insira o valor do raio em metros:'))

#Processamento
pi = 3.14 
area  = pi * (r**2)
print(pi, ' * ', (r, ' ** ', 2), ' = ', area)

#Fim
print('a área do circulo é:', area, ' m^2 ')