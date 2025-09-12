def media_vendas(vendas):
    soma = sum(vendas)
    tamanho = len(vendas)
    media = soma / tamanho
    return media

vendas = [(100, 150, 200), (50, 75, 100), (200, 300, 400)]

media_vendas(vendas[2])
