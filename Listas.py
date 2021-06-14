"""
Listas em python
fatiamento
append, isert, pop, del, clear, extend, +
min, max
range
"""
"""
#    +       0         1         2         3          4
lista = ["Ameixa", "Bacana", "Carlos", "Doutor", "Expressao"]
#     -      5         4         3         2          1

string = "ABCDE"
print(lista[3])
print(lista)

lista = ["A", "B", "C", "D", "E", 10.5]
lista[5] = "Qualquer outra coisa."
print(lista[5])

#Fatiamento
lista = ["A", "B", "C", "D", "E", 10.5]
print(lista[::-1])
#Concatenando listas
l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1)
print(l2)
l3 = l1 + l2
print(l3)

#Extendendo lista
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
l1.extend("a")
print(l1)
print(l2)
print()

#Outra forma de adicionar algo na lista
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l2.append(True)
print(l1)
print(l2)

#Inserindo
l1 = [1, 2, 3]
l2 = [4, 5, 6]
#Dentro do () será o índice em que será colocado a informação, seguido dela mesma
l2.insert(0,"banana")
print(l1)
print(l2)

#Deletando o ultimo elemento da lista
l2 = [4, 5, 6]
print(l2)
l2.insert(0,"banana")
print(l2)
l2.pop()
print(l2)

#Deletando fatias selecionadas
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
del(l2[0])
print(l2)

#Valor maximo e minimo de uma lista
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2))
print(min(l2))

#Função built-in: list
l2 = list(range(1, 10))
print(l2)

for valor in l2:
    print(valor)

l2 = list(range(0, 100, 8))
soma = 0
for valor in l2:
    soma = soma + valor

print(soma)


l2 = ["String", True, 10, -20.5]

for element in l2:
    print(f"O tipo de element é {type(element)} e seu valor é: {element}")
"""

secreto = "perfume"
digitadas = []
while True:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Ah isso não vale, digite apenas uma letra.")
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f"Uhuull, a letra '{letra}' existe na palavra!")
    else:
        print(f"A letra '{letra}' não existe na palavra secreta")
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra
        else:
            secreto_temporario += "*"
        print(secreto_temporario)








