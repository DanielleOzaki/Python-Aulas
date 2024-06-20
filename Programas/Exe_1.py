#Autor: Danielle Ozaki
#Data: 23/05/2024
#Versão: 1.0
#Descrição: Algoritmo que recebe o nome do usuário
#           e exibe uma frase de saudação concatenada com
#           a entrada do usuário.
#===========================================================
#Observações:
#           a) para iniciar um comentário utiliza-se '#'
#           b) no visual studio utilizar o comando 'cntrl' + ';' ou 3 aspas no inicio e no fim
#            => para comentar o bloco de código
#===========================================================
#Início

#Linha de comentário
var_vazia = '' #var atribuída com um valor vazio
#ENTRADA
nome = input('Qual o seu nome?')
#PROCESSAMENTO
mensagem = 'Óla, seja bem-vindo!'
frase = mensagem + nome
#SAIDA
print(frase)

#Fim