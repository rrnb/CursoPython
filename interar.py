####################################
# AULA len
#
# INSTRUTOR: LUIZ OTÁVIO MIRANDA
# ENTIDADE: Udemy
# ALUNO: RICARDO C AMORIM
# git@rrnb.com.br
#
####################################
frase = input('Informe uma frase: ')
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = str(input('Qual a letra que deseja colocar em maiúscula? '))

#Interar
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
