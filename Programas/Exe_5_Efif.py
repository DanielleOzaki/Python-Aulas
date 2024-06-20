''' Abertura Comentario

Autor: Danielle Ozaki
Data: 28/05/ 2024
Versão: 1.0
Descrição: Estudos do condicional IF ... ELIF

Fechamento Comentário
'''
#===================================================
#Condição:

#Variável
nota = 0

#Entrada
nota = int(input('Insira uma nota: '))

#Processamento
if (nota >= 6):
    print('ALUNO APROVADO')

 #else if (nota < 4): OU 
elif(nota < 4):
    print('ALUNO REPROVADO')

else:
    print('ALUNO EM RECUPERAÇÃO')

#Saída
print('Nota do aluno:', nota)
