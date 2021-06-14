#Questão 1
num_1 = input("Digite um número inteiro: ")

if num_1.isnumeric():
    num_1 = int(num_1)
    print("O número é inteiro")
    if num_1%2 == 0:
        print(f"{num_1} é par")
    else:
        print(f"{num_1} é ímpar")

else:
    print("O número não é inteiro")
    pass


#Checagem invertida:
if not num_1.isnumeric():
    print("Isso nao é um número inteiro")
else:
    num_1 = int(num_1)
    print("Isso é um número inteiro")
    if not num_1 % 2 == 0:
        print(f"{num_1} é ímpar ")
    else:
        print(f"{num_1} é par")






