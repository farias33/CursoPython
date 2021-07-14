"""
Operador ternário em python
"""
logged_user = False
msg = "Usuario logado." if logged_user else "Usuario precisa logar."

print(msg)

idade = input("Qual a sua idade? ")

if not idade.isnumeric():
    print("Voce precisa digitar apenas numeros")
else:
    idade = int(idade)
    maior = (idade>=18)
    msg = "Pode acessar" if maior else "Nao pode acessar"

print(msg)
































