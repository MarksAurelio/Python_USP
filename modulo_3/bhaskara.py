# Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros 
# e imprimir o resultado na saída da seguinte maneira:
# Quando não houver raízes reais imprima:
# esta equação não possui raízes reais
# Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:
# a raiz desta equação é X
# ou
# a raiz dupla desta equação é X
# onde X é o valor da raiz dupla
# Quando houver duas raízes reais imprima:
# as raízes da equação são X e Y
# onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:
# as raízes da equação são 1.0 e 2.0
# as raízes da equação são -2.0 e 0.0

import math

def numero_fornecido_usuario(label):
    return int(input('Número {}: '.format(label)))

def formula_de_bhaskara(a, b, c):
    delta = (b**2)-(4*a*c)

    if delta >= 0:
        raizes_do_calculo = (-b+ math.sqrt(delta)) / (2*a), (-b- math.sqrt(delta)) / (2*a)
        classificacao_raizes = tuple(sorted(raizes_do_calculo))

        if delta > 0:
            return 'as raízes da equação são {} e {}'.format(classificacao_raizes[0], classificacao_raizes[1])
        else:
            return 'a raiz desta equação é {}'.format(raizes_do_calculo[0])
    else:
        return 'esta equação não possui raízes reais'

numero = numero_fornecido_usuario ('a'), numero_fornecido_usuario ('b'), numero_fornecido_usuario ('c')
print(formula_de_bhaskara(numero[0], numero[1], numero[2]))
