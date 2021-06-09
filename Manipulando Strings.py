"""
Manipulando Strings
*Strings indices
*Fatiamento de Strings[inicio:fim:passo]
*Funções built-in len,abs,type,print,etc...
Essas funções podem ser usadas diretamento em cada tipo.
Posso conferir tudo isso em:
 https://docs.python.org/3/library/stdtypes.html
 https://docs.python.org/3/library/functions.html
"""
#Cada caractere de uma string têm um índice
#positivos  [012345678]
texto     = "python_s2"
#negativos -[987654321]
print(texto[2])

url = "www.google.com.br/"
print(url[:-1])

nova_string = texto[7:] #Exemplos: texto[0:2] texto[-9:-3] texto[:-1] texto[:]
print(nova_string)

mais_string = texto[0::3] #Exemplos: texto[::]
print(mais_string)

print(len(texto))