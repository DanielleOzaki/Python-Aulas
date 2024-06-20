#Autor: Danielle Ozaki
#Data: 24/05/2024
#Versao: 1.0
#Descricao: Faca um algoritimo de um valor em Celsius para Fahrenheit e Kelvin
#           Kelvin: 273C
#           Fahrenheit: 32C
#           Celsius: 0C
#====================================================================================

#           Exemplo de execucao -
#           Kelvin: +273 (Celcius para Kelvin)
#           Fahrenheit: 1,8 * C + 32 (Celcius para Fahrenhait)
#           Celsius: 0C
#====================================================================================

#Inicio
celcius = float(input('inserir o valor do celcius:'))

#Processamento
kelvin = celcius + 273.15
print(celcius, ' + ', 273.15 , ' = ', kelvin)


fahrenhait = 1.8 * celcius + 32
print(celcius, ' * ', 1.8, ' + ', 32, ' = ', fahrenhait)

#Final
print(celcius, ' C equivalem ', kelvin, ' K ')
print(celcius, ' C equivalem ', fahrenhait, ' F ')
