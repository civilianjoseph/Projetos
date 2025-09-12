"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Fala seu nome ai doidao: ')

nome_comp = len(nome)
tamanho_nome_menor = nome_comp < 4

print (nome_comp)

if nome_comp > 1 and nome_comp <= 4:
    print(f'nome curto com {nome_comp} letras ein')

elif nome_comp >= 5 and nome_comp <= 6:
    print('nome normal')

else:
    if nome_comp > 6:
        print('nome grande do caraio ein')



