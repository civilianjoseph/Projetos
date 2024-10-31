print('Vamos descobrir seu IMC!')
print('Preencha corretamente com seus dados pessoais, por favor.')

nome = input('Qual seu nome?')
peso = int(input('Qual seu peso?'))
altura_metros = float(input('E qual tua altura?'))
calculo_imc = peso / (altura_metros * altura_metros)

print('Nome:', nome)
print('Peso:', peso, "KG")
print('Altura:', altura_metros, "M")
print(f'Seu IMC: {calculo_imc:.2f}')
#preciso utilizar o f no inicio de uma str (começa com ' e termina com '), e colocar em chaves, ex: {calculo_imc}. O F de function permite uma string utilizar variáveis. Genial
