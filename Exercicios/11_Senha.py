# Autor: Danielle Ozaki
# Data: 06/06/2024
# Versão: 2.0
# Algoritimo: Senha
# Descrição: Faça um programa que solicite para o usuário a senha
#           de acesso ao sistema, ele terá no máximo 3 tentativas para 
#           inserir a senha cadastrada, caso passe desse limite uma
#           mensagem uma mensagem de erro deve aparecer.
#           senha: senai115

#=========================================================================

# Variavel 
senha = ''                                  #para receber a senha do usuario
senhaPadrao = 'senai115'
tentativas = 3                              #numero de tentativas de acesso ao sistema

while True:
    senha = input('Digite sua senha: ')     #senai115 = numeros com letras entao sem casting   
        
    if senha == senhaPadrao:
        print('Acesso liberado!')
        break                                #quebra o loop while, finaliza o programa

    else:
        tentativas = tentativas - 1          #OU tentativas -= 1
        print('Você possui mais', tentativas, 'tentativas')

    if(tentativas <= 0):
        print('Sua senha está bloqueada')
        break

     
    