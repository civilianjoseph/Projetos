nome = input('Digite aqui um nome: ')
encontrar = input('Digite aqui o que você quer encontrar: ')

if encontrar in nome:
    print (f'{encontrar} está em {nome}')

else:
    print (f'Cara, {encontrar} não está em {nome} não :/')