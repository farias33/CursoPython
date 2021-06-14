"""
Formatando valores com modificadores
:s - Texto(String)
:d - Inteiros(Int)
:f - Números de ponto flutuante(float)
:.(NÚMERO DE CASAS DECIMAIS)f - Quantidade de casas decimais(float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s,d ou f)
> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 1150
divisao = num_1 / num_2
print("{:.2f}".format(divisao)) # ou também: print(f"{divisao:.2f}")

nome = "Thales"
sobrenome = "Fortes"
ultimo_nome = "Ribeiro"
print(f"{nome:s}")
print(f"{num_1:0>10}")
print(f"{num_2:0<10}")
print(f"{num_2:0>10.2f}")
print((50 - len(nome))/2) #Mostrando como ficará dividido os caracteres no print abaixo
print(f"{nome:#^50}")
nome_formatado = "{:@>50}".format(nome)
print(nome_formatado)

nome_formatado_2 = "{n:0<20}".format(n=nome)
print(nome_formatado_2)

nome_formatado_3 = "{0:#^8} {1:%^8} {2:&^8}".format(nome, sobrenome, ultimo_nome)
print(nome_formatado_3)
nome = nome.ljust(20, "#")
nome = nome.rjust(20, "#")

name = "THalEs fOrTeS"
print(nome)
print(name.lower()) #Tudo minúscilo
print(name.upper()) #Tudo maiúsculo
print(name.title()) #Primeiras letras maiúsculas