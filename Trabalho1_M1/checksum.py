import numpy as np

def somaUm(x3, x4):

    result2 = np.zeros(len(x3), dtype=int)
    aux3 = np.zeros(len(x3)+1, dtype=int)

    for i in range(len(x3)):
        if aux3[i] == 1:
            if x3[i] == 1 and x4[i] == 1:
                result2[i] = 1
                aux3[i + 1] = 1
            elif x3[i] != x4[i]:
                result2[i] = 0
                aux3[i + 1] = 1
            else:
                result2[i] = 1
        else:
            if x3[i] == 1 and x4[i] == 1:
                result2[i] = 0
                aux3[i + 1] = 1
            elif x3[i] != x4[i]:
                result2[i] = 1
            else:
                result2[i] = 0
    return result2


def soma(x1, x2):

    result = np.zeros(len(x1), dtype=int)
    aux = np.zeros(len(x1)+1, dtype=int)

    for i in range(len(x1)):
        if aux[i] == 1:
            if x1[i] == 1 and x2[i] == 1:
                result[i] = 1
                aux[i + 1] = 1
            elif x1[i] != x2[i]:
                result[i] = 0
                aux[i + 1] = 1
            else:
                result[i] = 1
        else:
            if x1[i] == 1 and x2[i] == 1:
                result[i] = 0
                aux[i + 1] = 1
            elif x1[i] != x2[i]:
                result[i] = 1
            else:
                result[i] = 0

    if aux[aux.size-1] == 1:
        aux[aux.size-1] = 0
        aux2 = np.zeros(len(x1), dtype=int)
        aux2[0] = 1
        return somaUm(result, aux2)
    else:
        return result


def monta_palavra(palavra1, palavra2, palavra3, palavra4):
    print("Montando a primeira soma...")

    print("Primeira palavra", palavra1)
    print("Segunda palavra ", palavra2)

    resultado1 = soma(palavra1, palavra2)
    resultado2 = soma(resultado1, palavra3)
    resultado3 = soma(resultado2, palavra4)

    print("primeira soma: ", resultado1, "\n\n")
    print("segunda soma: ", resultado2, "\n\n")
    print("terceira soma: ", resultado3, "\n\n")

    return resultado3


checksum = monta_palavra(np.asarray([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=int), np.asarray([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], dtype=int), np.asarray([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], dtype=int), np.asarray([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], dtype=int))
