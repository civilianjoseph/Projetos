velocidade_carro = int(input())
local_carro = int (input())

LOCAL_RADAR = int (100)
RADAR_RANGE = int (3)
RADAR_SPEED_LIMIT = int (100)

radar_range = velocidade_carro - RADAR_RANGE and velocidade_carro + RADAR_RANGE

multa_carro = velocidade_carro > RADAR_SPEED_LIMIT and radar_range

if multa_carro:
    print(f'o carro ultrapassou o limite de {RADAR_SPEED_LIMIT} e foi multado, na velocidade de {velocidade_carro}')

else:
    print (f'O carro estava à {velocidade_carro} e não ultrapassou o limite de {RADAR_SPEED_LIMIT}.')

