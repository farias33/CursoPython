horas = input("Digite um horário entre (0-23): ")

if horas.isnumeric():
    horas= int(horas)
    if horas >= 0 and horas <= 11:
        print("Bom dia")
    elif horas >= 12 and horas <= 17:
        print("Boa tarde")
    elif horas >= 18 and horas <= 23:
        print("Boa noite")