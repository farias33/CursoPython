"""
Operadores Lógicos
and -> Vai realizar duas comparações
or
not
in
not in
"""
""""
comparacao_1 = 2
comparacao_2 = 3
# (Verdadeiro e Verdadeiro) = True , (Verdadeiro e Falso) = False
var = comparacao_1 and comparacao_2
#Basta 1 ser verdadeiro para que a expressao seja True
var2 = comparacao_1 or comparacao_2
"""
""" 
a=2
b=3
if not b > a:  #Será printado o que está no else
    print('b é maior que a')
else:
    print('a é maior que b')
"""
"""
a = "" #Se colocar algum valor a expressao do if não será mostrada
b = 0  #Funciona com o 0, pois em booleano 0 é false
if not a:
    print("Preencha o valor de A.")
"""
nome = "Thales"
if "T" in nome: #"Se 'T' está em "nome" "
    print("Existe no nome Thales")
else:
    print("Não existe")
    pass
if "gh" not in nome: #"Se 'gh' não está em "nome" "
    print("Não existe")
else:
    print("Existe o texto")
