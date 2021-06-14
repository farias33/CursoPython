nome = input("Digite o nome do usuário: ")
qtd_letras = len(nome)

if qtd_letras <= 4:
    print("Seu nome é curto")
elif qtd_letras >= 5 and qtd_letras <= 6:
    print("Seu nome é normal")
elif qtd_letras > 6:
    print("Seu nome é muito grande")


