"""
For in em Python
Iterando strings com for
Função range(start = 0, stop, step = 1)
"""
"""
texto = "Python"
c = 0                     #Maneira mais complicada
while c < len(texto):
    print(texto[c])
    c += 1


texto = "Python"

for letra in texto:
    print(letra)
    
    for n in range(20, 10, -1): #Forma decrescente
    print(n)
    
    for n in range(0, 100, 8): #Múltiplos de 8
    print(n)

for n in range(5, 10, 1):
    print(n)

print("############################") #Dividindo os laços apenas

for n in range(100):
    if n % 8 == 0:
        print(n)
"""
texto = "python"
nova_string = " "
#continue: pula para o próximo laço
#breake: termina o laço
for letra in texto:
    if letra == "t":
        nova_string += letra.upper()
    elif letra == "h":
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)


















