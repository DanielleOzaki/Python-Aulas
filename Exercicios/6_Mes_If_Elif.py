'''
Autor: Danielle Ozaki
Data: 02/06/2024
Versão: 1.0
Descrição: Escreva um algoritmo para exibir o nome do mês por extenso
           de acordo com o número que o representa:
                        1	    Janeiro
                        2	    Fevereiro
                        3	    Março
                        4	    Abril
                        5	    Maio
                        6	    Junho
                        7	    Julho
                        8	    Agosto
                        9	    Setembro
                        10	    Outubro
                        11	    Novembro
                        12	    Dezembro

'''

#Variável
mes = 0

#Entrada
print(' 1. Janeiro \n 2. Fevereiro \n 3. Março \n 4. Abril \n 5. Maio \n 6. Junho \n 7. Julho \n 8. Agosto \n 9. Setembro \n 10. Outubro \n 11. Novembro \n 12. Dezembro ')
mes = int(input( 'Qual o numero do mes: '))

#Processamento
if mes == 1:                # OU mes = ''
    print('Janeiro')        # if mes == '1':
elif mes == 2:              # mes = 'Janeiro'
    print('Fevereiro')
elif mes == 3:
    print('Março')
elif mes == 4:
    print('Abril')
elif mes == 5:
    print('Maio')
elif mes == 6:
    print('Junho')
elif mes == 7:
    print("Julho") 
elif mes == 8:
    print('Agosto')
elif mes == 9:
    print('Setembro')
elif mes == 10:
    print('Outubro')
elif mes == 11:
    print('Novembro')
elif mes == 12:
    print('Dezembro')
else:
    print('Opção Inválida')

#Saída
