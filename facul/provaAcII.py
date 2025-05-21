idades = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
numeroCriancas =0
numeroAdultos = 0

for idade in idades:
    if idade >= 18:
        numeroAdultos += 1
        print(f'{idade} é Maior de idade')

    elif idade< 18:
        numeroCriancas += 1
        print(f'{idade} é MENOR de idade')
