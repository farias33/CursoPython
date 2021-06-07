"""
Tipos do dados:
String -> (str) : textos 'Assim' ou "Assim"
inteiro -> (int) : 0123456 -1 -2 -3 -15000
Float -> (real/ponto flutuante) : 1.2 2.6 50.456 -10.50 -48.68
bool -> (booleano/lógico) : True/False 10 == 10
"""
"""
print(('Luiz', type('Luiz')))
print((10, type(10)))
print((25.23, type(25.23)))
print(('L'=='L', type('L'=='L')))
print(('l'=='L', type('l'=='L')))
print(('', type('')))
"""


#print(bool([])) #Lista vazia

"""
TypeCasting: Conversão de pimitivos
"""
#print('10', type('10'), type(int('10')))
#print('Luiz', int('Luiz')) Casos impossíveis
#print('Luiz', int(10))
#print('Luiz', float(10.5))
#print(10, float(10)) #Vira 10.0
#print(10+10)
#print(10.5+10)
"""
Exercício da aula
"""
#String: nome
print('Thales Fortes', type('Thales Fortes'))
#Idade: Int
print(20, type(20))
#Altura: Float
print(1.80, type(1.80))
#Maior de idade
print(20 > 18, type(20 > 18))