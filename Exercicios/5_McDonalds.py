# Autor: Danielle Ozaki
# Data: 02/06/2024
# Versão: 2.0
# Descrição: Escreva um algoritmo para exibir o nome do lanche de acordo
#             do número inserido pelo usuário, seguindo a tabela abaixo:
#
#                        Nr. 	Lanche
#                        1	    Big Mac
#                        2	    Quarteirão
#                        3	    McChicken
#                        4	    Cheddar McMelt
#                        5	    McFish
#===============================================================================

# Variavel 
lanche = 0
lanche_escolhido = ''

# Entrada
print('Nr. Lanche \n 1. Big Mac \n 2. Quarteirão \n 3. McChicken \n 4. Cheddar McMelt \n 5. McFish')
lanche = int(input('Insira o número do lanche: '))

# Processamento
if lanche == 1:
    lanche_escolhido = 'Big Mac'
elif lanche == 2:
    lanche_escolhido = 'Quarteirão'
elif lanche == 3:
    lanche_escolhido = 'McChicken'
elif lanche == 4:
    lanche_escolhido = 'Cheddar McMelt'
elif lanche == 5:
    lanche_escolhido = 'Mc Fish'
else:
    print('Opção inválida')

# Saída
print(lanche_escolhido)