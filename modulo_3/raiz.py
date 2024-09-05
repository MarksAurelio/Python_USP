import math

def entrada (label):
    return int(input('Digite o valor de {}:'.format(label)))

def bhaskara (a, b, c):
    delta = (b ** 2) - (4 * a* c)

    if delta >= 0:
        raizes = (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)

        if delta > 0:
            return "[Delta > 0] - raizes reais: {} e {}".format(raizes[0], raizes[1])
        else:
            return "[Delta == 0] - raiz real: {}".format(raizes[0])
    else:
        return "[Delta < 0] - raizes reais: Não Possui!"

entradas = entrada('a'), entrada('b'), entrada('c')
print(bhaskara(entradas[0], entradas[1], entradas[2]))