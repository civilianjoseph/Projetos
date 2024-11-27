senha = '123456'

repeticoes = 0
senha_escrita_atual = ''

while senha != senha_escrita_atual:
    senha_escrita_atual = input(f'Senha [{repeticoes}x]: ')
    repeticoes += 1

    if repeticoes >= 3:
        print (f'Você excedeu a quantidade de {repeticoes}x. Valide suas credenciais novamente.')
        break

