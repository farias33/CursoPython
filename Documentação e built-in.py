num_1 = input("Digite um numero: ")
num_2 = input("Digite um numero: ")
#isnumeric, isdigit,isdecimal : usadas quando eu quero saber se as str podem ser convertidas em int
#checar numeros posivitivos

#print(num_1.isnumeric())
#print(num_2.isnumeric())

if num_1.isnumeric() and num_2.isnumeric():
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1+num_2)
else:
    print("Não foi possivel converter os numeros")
    pass
#os dois funcionam igual
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)
except:
    print("Não foi possivel converter os numeros")

#docs.python no google