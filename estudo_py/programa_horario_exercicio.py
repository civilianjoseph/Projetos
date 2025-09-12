"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int(input('Qual o horário em que você está digitando isso? '))

if horario in (range(0, 11)):
    print ('BOM DIA FLOR DO DIA')

elif horario in (range(12, 17)):
    print ('BOA TARDE FLOR DA TARDE')

else:
    if horario in (range(18, 23)):
        print ('BOA NOITE FLOR DA NOITE')
    else:
        print ('FALA UM HORARIO CERTO IRMAO')