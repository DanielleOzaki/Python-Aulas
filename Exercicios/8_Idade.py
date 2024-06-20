# Autor: Danielle Ozaki
# Data: 04/06/2024
# Versão: 2.0
# Algoritimo: Classificação de idade
# Descrição: Escreva um programa que leia a idade de um indivíduo e escreva
#            a faixa etária a que pertence, de acordo com a tabela abaixo;

#           Faixa Etária        Classificação
#           <12                 Criança
#           13~17               Adolescente
#           18~59               Adulto
#================================================================================

#variável
idade = 0
classificacao = ''

#entrada
idade = int(input('Qual sua idade? ')) # int é numero inteiro

#processamento
if(idade >= 0 and idade <= 12):
    classificacao = 'Criança'

elif(idade >= 13 and idade <= 17):
    classificacao = 'Adolescente'

elif(idade >= 18 and idade <= 59):
     classificacao = 'Adulto'

elif(idade >= 59 and idade <= 120):
    classificacao = 'Idoso'

else: 
    classificacao = 'Idade inválida'

#saída
print(classificacao)