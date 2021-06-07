"""
Usando fString
"""

nome = 'Thales Fortes'
idade = 20 #int
altura = 1.80 #float
e_maior = idade > 18
peso = 80
imc = peso/altura**2

#print(nome,'tem',idade,'anos de idade e seu imc é:', imc)
#print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
#print('{} tem {} anos  e seu imc é {:.2f}'.format(nome,idade,imc))
#print('{0} tem {1} anos  e seu imc é {2:.2f}'.format(nome,idade,imc))
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc))