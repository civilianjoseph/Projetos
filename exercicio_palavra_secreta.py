"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'shadow'

tentativas = 0

letras_acertadas = ''

descobrindo_palavra = ''

input_user = ''


while (input_user != palavra_secreta and descobrindo_palavra != palavra_secreta):

    
    input_user = input ('Digite uma letra: ')
    tentativas += 1


    if len(input_user) > 1 and input_user != palavra_secreta:
        print('Digite apenas uma letra ')
        continue

    if tentativas > 4:
        print ('DICA!!!! Nome de desenho/Jogo')

    if input_user in palavra_secreta:
        letras_acertadas += input_user
        
    descobrindo_palavra = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            descobrindo_palavra += letra
            continue

        else:
            descobrindo_palavra += '*'
    print (f'a palavra secreta é {descobrindo_palavra}')
    
if tentativas > 10:
        print(f'Caraio ein doido, cê precisou de {tentativas} tentativas KKKKKKKKKKKKKKKKKKKKKKK')
else:
        print(f'Parabénsss!!, a palavra secreta era {palavra_secreta}. Você precisou de x{tentativas} tentativas.')
        
    

    







    