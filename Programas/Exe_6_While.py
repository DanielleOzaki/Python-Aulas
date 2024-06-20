# Autor: Danielle Ozaki
# Data: 07/06/2024
# Versão: 1.0
# Descrição: Estudo da estrutura de repetição "While"

#========================================================

# Crescente
indice = 1
while indice <= 22:
    print('Danielle Ozaki', indice)
    indice += 1

#========================================================

# Decrescente
indice2 = 10
while indice2 > 0:
    print(indice2, 'Danielle Ozaki')
    indice2 = indice2 - 1

#========================================================

indice3 = 1
while True:
    print(indice3)
    indice3 = indice3 + 1
    if indice3 == 5:
        break

#========================================================

# indice4 = 1
while True:
    opcao = input('Digite S para finalizar esse programa')
    #indice4 = indice4 + 1
    if opcao == 'S':
        break