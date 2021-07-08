"""
* Split - Dividir uma string #str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list
"""
"""
string = "O brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(" ") #O comando .split transforma a string em uma lista separando a varialvel pelo o que está existente na lista e o que for colocado no parênteses
# Nesse caso com espaço, fica assim: ['O', 'brasil', 'é', 'o', 'país', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta.']
lista_2 = string.split(",")
# Nesse caso com vígulas, fica assim: ['O brasil é o país do futebol', ' o Brasil é penta.']
print(lista_1)
print(lista_2)
"""
"""
string = "O brasil é o país do futebol, o Brasil é penta."             
lista_1 = string.split(" ")
lista_2 = string.split(",")

for valor in lista_1:
    print(valor)
"""
"""
string = "O brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(" ")
lista_2 = string.split(",")

for valor in lista_1:
    print(f"A palavra {valor} apareceu {lista_1.count(valor)}x na frase.") # O comando .count conta quantas vezes um valor específico apareceu na lista, ele faz a contagem de todos os valores automaticamente neste caso
"""
"""
string = "O brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(" ")
lista_2 = string.split(",")
palavra = ""
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é {palavra}({contagem}x)")
"""
"""
string = "O brasil é penta."
lista = string.split(" ")
string2 = ",".join(lista) # Junta os elementos da lista usando usando o que está entre aspas
print(string)
print(lista)
print(string2)
"""
"""
string = "O brasil é penta."
lista = string.split(" ")

for indice, valor_real in enumerate(lista): #Visto posteriormente em desempacotamento
    print(indice,valor_real, lista[indice])
"""
"""
lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in lista:
    print(v[0], v[1]) # Checa-se cada índice de cada lista
"""
"""
lista = [
    [0, 'Luiz'],
    [1, 'Joao'],
    [2, 'Maria'],
]
                               # Isso que a função enumerate faz
for indice, nome in lista:
    print(indice, nome)
"""
"""
lista = ['Luiz','Joao','Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)
"""
lista = ['Luiz', 'Joao', 'Maria']
n1, n2, n3 = lista
print(n2)

