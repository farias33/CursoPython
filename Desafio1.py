"""
Desafio 1
"""
nome = "Thales Fortes"
idade = 18
altura = 1.80
peso = 100
ano = 2021
ano_de_nascimento = ano - idade
IMC = peso/altura**2

print('{} tem {} anos,{} de altura e pesa {}Kg'.format(nome,idade,altura,peso))
print('O IMC de {} é {:.2f}'.format(nome,IMC))
print('{} naceu em {}'.format(nome,ano_de_nascimento))