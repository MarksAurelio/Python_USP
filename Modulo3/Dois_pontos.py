# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, 
# respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. 
# Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro
# ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

# longe

# na saída. Caso o contrário, quando a distância for menor que 10, imprima

# perto

import math

def entrada(coordenada, cartesiano):
    return float(input('Digite a coordenada {} para o plano Cartesiano {}:'.format(coordenada, cartesiano)))

cartesianoA = entrada('A', 'X'), entrada('A', 'Y')
cartesianoB = entrada('B', 'X'), entrada('B', 'Y')
formula = (cartesianoA[0] - cartesianoB[0]) ** 2 + (cartesianoA[1] - cartesianoB[1]) ** 2
distancia = math.sqrt(formula)

print('longe' if distancia >= 10 else 'perto')