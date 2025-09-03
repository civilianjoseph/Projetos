import os 

def clear_output(): 
    os.system('cls' if os.name == 'nt' else 'clear')

lista = []

adicionar_item = ''

inserir_item = ''

apagar_item = []


while lista != 0:
    
        funcao_lista = input('escolha uma opção'
                         '[I]nserir [A]pagar [L]istar ')
        try:
            if funcao_lista == 'i' or funcao_lista == 'I':
                adicionar_item = input('Qual o valor à ser adicionado? ')
                lista.append(adicionar_item) 
                clear_output()
                for indice, item in enumerate(lista):
                    print(indice, item)
                    continue

    
            if funcao_lista == 'a' or funcao_lista == 'A':
                apagar_item = int(input('Qual o item à ser excluído? '))
                item_apagado = lista.pop(apagar_item)
                clear_output()
                for indice, item in enumerate(lista):
                    print(indice, item)
                    continue
    
            
            if funcao_lista == 'l' or funcao_lista == 'L':
                clear_output()
                for indice, item in enumerate(lista):
                    print (indice, item)
                continue
        except:
            print('Esta não é uma opção válida')



        