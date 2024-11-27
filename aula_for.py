"""
Iterável -> str, range, etc (__iter__)
Iterável -> quem sabe entregar um valor por vez
next -> me entrtegue o prox valor
iter -> me entregue seu iterador

"""

texto = 'José'
# iterador = iter(texto)

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break 
    
for letra in texto:
    print(letra)