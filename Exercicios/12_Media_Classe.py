# Autor: Danielle Ozaki
# Data: 011/06/2024
# Versão: 1.0
# Algorítmo: Média turma
# Descrição: Faça um programa que receba duas notas de 6 alunos.
#            Calcule e mostre:
#            A média aritmética das duas notas de cada aluno; e 
#            A mensagem que está na tabela a seguir:
#               Média aritmética    Mensagem
#               Até 3               Reprovado
#               Entre 4 e 7         Exame
#               De 8 para cima      Aprovado

#           O total de alunos aprovados:
#           O total de alunos de exame;
#           O total de alunos reprovados;
#           A média da classe.
#========================================================================

#Variáveis 
aluno = 0
quantidadeAluno = 6
aprovado = 0
reprovado = 0
exame = 0

while aluno < quantidadeAluno:
    aluno = aluno + 1

    nota1 = 0
    nota2 = 0
    media = 0 
    mediaFinal = 0
    somaMedia = 0
    
    #Entrada
    #nota1 = float(input(f'Digite a nota 1 do aluno {aluno}: ')) significa interpolação, misturar string com variaveis
    nome = input('insira o nome do aluno: ')
    nota1 = float(input(f'Digite a nota 1 do aluno {nome}: '))
    nota2 = float(input(f'Digite a nota 2 do aluno {nome}: '))

    media  = (nota1 + nota2)/2
    somaMedia = somaMedia + media     #

    #Processamento 
    if(media <= 3):
        print('Reprovado')
        reprovado += 1

    elif(media >= 4 and media <= 7):
        print('Exame')
        exame += 1

    else:
        print('Aprovado')
        aprovado += 1

mediaFinal = round(somaMedia / quantidadeAluno)

print(f'Quantidade de alunos aprovados: {aprovado}')
print(f'Quantidade de alunos em exame: {exame}')
print(f'Quantidade de alunos reprovados: {reprovado}')
print(f'Média final da turma: {mediaFinal} ')

