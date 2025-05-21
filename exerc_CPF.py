"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_Digitado = '140.203.259-52'

cpf_formatado = cpf_Digitado.replace('-', '').replace('.', '')

comp_CPF = len(cpf_formatado)
resultado = 0
contagem = 10

for digitos in cpf_formatado[:9]:
    resultado += int(digitos) * contagem
    contagem -= 1
digito = (resultado * 10) % 11
digito = digito if digito <=9 else 0
print(digito)
    

# # while comp_CPF <= 11:
#     try:
#         digito1 = int(cpf_formatado[0]) * 10
#         digito2 = int(cpf_formatado[1]) * 9
#         digito3 = int(cpf_formatado[2]) * 8
#         digito4 = int(cpf_formatado[3]) * 7
#         digito5 = int(cpf_formatado[4]) * 6
#         digito6 = int(cpf_formatado[5]) * 5
#         digito7 = int(cpf_formatado[6]) * 4
#         digito8 = int(cpf_formatado[7]) * 3
#         digito9 = int(cpf_formatado[8]) * 2

#         soma_digitos = digito1 + digito2 + digito3 + digito4 + digito5 + digito6 + digito7 + digito8 + digito9
#         mult_digitos = soma_digitos * 10
#         resto_soma = mult_digitos % 11

#         if resto_soma > 9:
#             resultado1 = 0
#         else:
#             resultado1 = resto_soma
#         print(resultado1)
        
#         digito1 = int(cpf_formatado[0]) * 11
#         digito2 = int(cpf_formatado[1]) * 10
#         digito3 = int(cpf_formatado[2]) * 9
#         digito4 = int(cpf_formatado[3]) * 8
#         digito5 = int(cpf_formatado[4]) * 7
#         digito6 = int(cpf_formatado[5]) * 6
#         digito7 = int(cpf_formatado[6]) * 5
#         digito8 = int(cpf_formatado[7]) * 4
#         digito9 = int(cpf_formatado[8]) * 3
#         digito10 = int(cpf_formatado[9]) * 2

#         soma_digitos1 = digito1 + digito2 + digito3 + digito4 + digito5 + digito6 + digito7 + digito8 + digito9 + digito10
#         mult_digitos1 = soma_digitos1 * 10
#         resto_soma1 = mult_digitos1 % 11
        
#         if resto_soma1 > 10:
#             resultado1 = 0
#         else:
#             resultado1 = resto_soma1
#         print(resultado1)

#         break
#     except ValueError:
#         print('Digite um CPF válido.')
           


 



