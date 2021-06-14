"""
while em Python
Utilizado para realizar ações enquanto uma condição for verdadeira
Requisitos: Entender condições e operadores
"""
x = 0
while x < 10:
    if x == 3:    #Se eu quiser por exemplo tirar o 3 do meu loop
        x = x+1
        continue
    print(x)
    x = x+1

print("Acabou!")

x = 0
while x < 10:
    if x == 3:
        x = x+1
        break     #O comando break para o loop instantaneamente
    print(x)
    x = x+1

print("Acabou!")
