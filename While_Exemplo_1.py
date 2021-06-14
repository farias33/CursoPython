x = 0 #coluna
while x < 10:
    y = 0  # linha, o y tem que ser configurado para 0 a cada volta do nosso primeiro while
    while y < 5:
        print(f"({x},{y})")
        y += 1
    x += 1   #Mesma coisa que x = x + 1(pode ser usado com qualquer operador aritimético)
print("Acabou!")