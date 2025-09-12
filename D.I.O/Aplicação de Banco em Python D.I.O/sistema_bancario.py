from datetime import date, time, datetime

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
current_datetime = datetime.now()

def deposito(saldo, valor):
    return valor + saldo
    

def saque(saldo, valor):
    return saldo - valor

def menu():
    return print("""
            SEJA MUITO BEM-VINDO!!
          
          O que deseja fazer hoje?
                 
          (E) Extrato;

          (D) Depositar;
                 
          (S) Sacar;

          (Q) Sair do sistema.

            AGRADECEMOS A PREFERENCIA, COMO SEMPRE!
""")
print(current_datetime)
    
while True:
    menu()
    opcao = input("Digite aqui a opcao desejada: ")

    if opcao == "d":
        valor = float(input("Qual o valor para depósito? "))
        if valor > 0:
            extrato += f'Depósito de R${valor} feito em: {current_datetime}\n'
            saldo = deposito(saldo, valor)
            print(f"Depósito de R${valor} feito. Saldo atual: R${saldo}!")

    
    if opcao == "s":
        print(f"Seu número atual de saques diários está em: {numero_saques}")
        valor = float(input("Qual o valor para o saque? "))

        if valor > saldo:
            print(f"Valor de R${valor} não permitido, saldo de apenas R${saldo}!")
            continue
        else:
            if numero_saques >= LIMITE_SAQUES:
                print(f"Desculpe! Mas seu número de saques diários está em {numero_saques}! Só amanhã agora parceiro :/")
            else:
                extrato += f'Saque de R${valor} feito em: {current_datetime}\n'
                numero_saques += 1
                saldo = saque(saldo, valor)
                print(f"Saque de R${valor} feito. Saldo atual: R${saldo}!")


    if opcao == "e":
        print("========== EXTRATO ==========")
        print("Não foram feitas transações durante essa sessão") if not extrato else extrato
        print(extrato)
        print(f'Saldo disponível: R${saldo:.2f} - {current_datetime}')
        print("=============================")

    if opcao == "q":
        print("Agradecemos, e nos vemos na próxima!")
        break
                

    

