try:
    
    numeroAlunos = float(input("Quantos alunos? "))
    cont = 1
    soma = 0
    while cont <= numeroAlunos:
            nota = float(input("Digite uma nota: "))
            soma = soma + nota
            cont = cont + 1
            print(f'A nota: ', nota, 'e a nota somada: ', soma)

    media = soma / numeroAlunos        
    print(f'MÉDIA DOS ALUNOS:', media)

    if media < 5.0:
        print("REPROVADOS. SALA, ESTUDEM MAIS")
            
    else:
        print("APROVADOS. MUITO BEM, TURMA")

except ValueError:
    print("Digite dados corretos, por favor. Comece de novo")