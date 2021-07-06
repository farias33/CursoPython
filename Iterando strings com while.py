#        Índices
#        0123456789....................33   #Valores com índices são valores iteráveis
frase = "O rato roeu a ropa do rei de roma" #Essa string tem 34 índices, pois sempre começamos a contar do zero
tamanho_frase = len(frase)
contador = 0
nova_string = " "
"""
#Iteração
while contador < tamanho_frase:
    print(frase[contador], contador)
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
"""
#Iteração
input_do_usuario = input("Qual letra deseja colocar maiúscula: ")
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)

