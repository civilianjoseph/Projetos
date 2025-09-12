
while True:
    num_1 = input ('Digite um número: ')
    num_2 = input ('Digite um número: ') 
    operador = input ('Qual a operação? ')
    num_valid = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        num_valid = True
    except:
        num_valid = None
        
    if num_valid is None:
        print(f'Os valores {num_1} e {num_2} não são válidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print ('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '*':
        print (num_1_float * num_2_float)

    if operador == '+':
        print (num_1_float + num_2_float)

    if operador == '-':
        print (num_1_float - num_2_float)

    if operador == '/':
        print (num_1_float / num_2_float)
        

    
    
    
    
    
    
    
    
    
    
    sair = input('deseja sair? [s]im ').lower().startswith('s')

    if sair is True:
        print('Você saiu.')
        break

operador = input
