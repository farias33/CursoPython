"""
Quantidade de caracteres
"""
usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario) #Com len não é necessario fazer typecasting
print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print("Voce precisa de pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")
    pass

string_1 = input("Digite algo: ")
string_2 = input("Digite mais: ")
print(f"A quantidade total de caracteres digitados foi {len(string_1)+len(string_2)}") #É ppossível fazer operações dentro das chaves
#Objetos do tipo int, boolean e float não possuem len().