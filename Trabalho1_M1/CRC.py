import numpy as np


def bitwise(x1, x2):
    result = np.zeros(len(x1))
    result[x1 != x2] = 1
    return result


def string2array(a):
    vet = []
    for x in a:
        vet.append(int(x))
    return np.asarray(vet, dtype=np.uint8)


def detecta_erro(palavra, polinomio):
    print("\nVerificando se ha erro...")

    print("Palavra recebida", palavra)
    print("Polinomio divisor", polinomio)

    if isinstance(palavra, str):
        px = string2array(palavra)
    else:
        px = palavra

    cx = string2array(polinomio)
    k = len(cx) - 1

    i = 0
    while i < len(px) - k:
        if px[i] == 0:
            i += 1
            continue

        print(px, "/", cx)

        xor = bitwise(px[i:i + k + 1], cx)
        px[i:i + k + 1] = xor
        i = 0

    print("Resto divisao ", px)

    for x in px:
        if x == 1:
            return "Mensagem com erro\n\n"

    return "Mensagem sem erro"


def monta_palavra(palavra, polinomio):
    print("Montando mensagem para envio...")

    print("Palavra", palavra)
    print("Polinomio C(x)", polinomio, "de grau", len(polinomio)-1)

    mx = string2array(palavra)
    cx = string2array(polinomio)
    k = len(cx)-1    # grau do polinomio

    # polinomio p(x) = palavra + k bits
    px = np.concatenate((mx, np.zeros(k))).astype(np.uint8)
    print("p(x) =", px)

    i = 0
    while i < len(px) - k:  # percorre a mensagem para fazer a divisao
        if px[i] == 0:      # loop até encontrar 1
            i += 1
            continue

        print(px, "/", cx)
        # funcao que retorna o xor da posicao i da palavra ate posicao k+1 e o polinomio
        xor = bitwise(px[i:i + k + 1], cx)
        # atribui o resultado do bitwise na mesma posicao em que foi feito
        px[i:i + k + 1] = xor
        i = 0

    print("Resto divisao ", px)
    # concatenacao da mensagem com o resto da divisao, resto da divisao sao os ultimos k bits
    crc = np.concatenate((mx, px[len(px)-k:len(px)])).astype(np.uint8)

    print("Mensagem para envio ", crc, "\n\n")
    return crc


if __name__ == "__main__":
    # palavra e polinomio de divisao como parametro
    crc = monta_palavra(np.asarray([1, 0, 0, 1, 1, 0, 1, 0], dtype=np.uint8), np.asarray([1, 1, 0, 1]))
    # palavra recebida e polinomio de divisao
    detecta_erro(crc, np.asarray([1, 1, 0, 1]))
