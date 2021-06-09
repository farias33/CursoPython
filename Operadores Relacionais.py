"""
Operadores Relacionais
== igualdade
> maior que
< menor que
>= maior ou igual
<= menor ou igual
!= diferente
"""
"""
num_1 = 2
num_2 = 2
expressao = num_1 == num_2
"""

"""
print(expressao)

num_1 = 3
num_2 = 2
expressao = num_1 > num_2

print(expressao)
"""

"""
print(expressao)

num_1 = 3
num_2 = 2
expressao = num_1 >= num_2

print(expressao)
"""
"""
var_1 = 'Thales'
var_2 = 'Fortes'
expressao = var_1 != var_2
print(expressao)
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
idade = int(idade) #Converter a idade que será recebida em str para int, afim de fazer os cáculos com este valor
idade_limite = 30
idade_minima = 20
if idade >= idade_minima and idade <= idade_limite:  #O and diminui o tamanho da estrutura If Else
    print(f"{nome} pode pegar o empréstimo")
else:
    print(f"{nome} não pode pegar o empréstimo")