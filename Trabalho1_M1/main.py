import numpy as np



def check_pos(pos, tam):

    for i in range(tam):

        if 2**i == pos:
            return True

    return False

def format_vet(vet,p):
    # alterar o tamanho do aux
    aux = np.zeros(12)
    for i in range(1,len(aux)+1):
        # alterar o segundo valor
        if check_pos(i, 4):
            #print("p: ", p)
            v = p[0]
            p = np.delete(p,0)
            aux[i-1] = v

        else:
            v = vet[0]
            vet = np.delete(vet,0)
            aux[i-1] = v


    return aux

def redundant_values(i, vet):
    aux = []
    x = 0
    y = 2**i

    for j in range((2**i)-1,len(vet)):
        if x < 2**i:
            aux.append(vet[j])
            x += 1
        elif y > 1:
            y -= 1
        else:
            x = 0
            y = 2**i

    return aux

def encode(vet):
    # alterar quantidade de bits paridade
    p = np.zeros(4)
    vet = format_vet(vet,p)

    for i in range(len(p)):
        aux = redundant_values(i, vet)
        #print("i: ",i, aux)
        for j in aux[1:len(aux)]:
            p[i] = int(p[i])^int(j)

    for i in range(1,len(vet)+1):
        if check_pos(i, 4):
            v = p[0]
            p = p[1:len(p)]
            vet[i-1] = v

    return vet


def decode(vet):
    # alterar quantidade de bits paridade
    k = np.zeros(4)

    for i in range(len(k)):
        aux = redundant_values(i, vet)
        for j in aux:
            #print("i: ",i, "valores: ",int(k[i]),int(j),int(k[i])^int(j))
            k[i] = int(k[i])^int(j)

    print(k)
    if k.__contains__(1):
        pos = 0
        for i in range(len(k)):
            if k[i] == 1:
                pos+=2**i

        print("há erro na posição: ",pos)
        print("Mensagem com erro: ", vet)
        vet[pos-1] = 0
        print("Mensagem corrigida: ", vet)

    else:
        print("Não há erro")

if __name__ == '__main__':
    vet = np.array([1,0,1,0,1,0,1,0])
    #vet = np.array([1,0,0,1])
    vet = encode(vet)
    vet[9] = 1
    decode(vet)


