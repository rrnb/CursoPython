####################################
# AULA LACO WHILE
#
# INSTRUTOR: LUIZ OTÁVIO MIRANDA
# ENTIDADE: Udemy
# ALUNO: RICARDO C AMORIM 
# git@rrnb.com.br
#
####################################



print("===================================================================")
print("=    Bem vindo!                                                   ="
      "\n=  Isso é um loop infinito, caso queira sair dele digite        ="
      "\n= 'Sair' quando solicitaro o operador                           =")
print("===================================================================")
while True:
    print()
    num1 = int(input('Digite um numero: '))
    operador = input('Digite um operador: ')
    num2 = int(input('Digite outro numero: '))

    # + - / *
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    if operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == 'Sair':
        exit(print("Voce encerrou o programa"))
else:
        print("Operador invalido")
        exit()

