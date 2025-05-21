# Exercicio 1 - Votação
Cleber = 0
João = 0
Maria = 0
Ana = 0
Nulo = 0
Branco = 0
voto = 0

print("===========REGRAS DE VOTAÇÃO===========" \
    "\n"
    "1 - Cleber" \
    "\n"
    "2 - João" \
    "\n"
    "3 - Maria" \
    "\n"
    "4 - Ana" \
    "\n"
    "5 - Nulo" \
    "\n"
    "6 - Branco" \
    "\n"
    "=======================================")

for votos in range(1, 10):
    
    voto = int(input('Digite o número do candidato escolhido:'))
    if voto == 1:
        Cleber = Cleber + 1
    elif voto == 2:
        João = João + 1
    elif voto == 3:
        Maria = Maria + 1
    elif voto == 4:
        Ana = Ana + 1
    elif voto == 5:
        Nulo = Nulo + 1
    elif voto == 6:
        Branco = Branco + 1
    else:
        print("Voto inválido. Tente novamente.")

votos_validos = 10 - Nulo

print("===========RESULTADO DA VOTAÇÃO==========="
    "\n"
    "Candidato Cleber: ", Cleber, "votos" \
    "\n"
    "Candidato João: ", João, "votos" \
    "\n"
    "Candidata Maria: ", Maria, "votos" \
    "\n"
    "Candidata Ana: ", Ana, "votos" \
    "\n"
    "Votos Nulos: ", Nulo, "votos" \
    "\n"
    "Votos em Branco: ", Branco, "votos" \
    "\n"
    "média de votos nulos e brancos: ",Branco + Nulo, " %" "de votos" \
    "\n"
    "média de votos válidos: ", votos_validos, " %" "de votos"  
    "\n"
    "=========================================")

    