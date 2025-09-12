"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero = (input('Digita um numero ae pae'))

try:

    numero_int = int (numero)
    numero_impar = int
    numero_par = int

    numero_par = numero_int % 2 == 0

    if numero_par and not numero_impar and numero_int:
        print (f'o {numero} é par')

    else:
        print (f'o {numero} é impar')

except:
    print (f'o {numero} não é um número inteiro')

    