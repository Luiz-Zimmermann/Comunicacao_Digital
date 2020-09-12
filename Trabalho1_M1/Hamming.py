import numpy as np

def check_pos(pos, tam):

    for i in range(tam):

        if 2**i == pos:
            return True

    return False

def format_vet(vet,p,min, max):
    # alterar o tamanho do aux
    aux = np.zeros(max)

    for i in range(1,len(aux)+1):
        # alterar o segundo valor
        if check_pos(i, min):
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

def hamming(message, tipo):
    vet = []
    paridade = 0
    tam = 0

    for x in message:
        vet.append(x)

    if tipo == "7,4":
        paridade = 3
        tam = 7
    elif tipo == "12,8":
        paridade = 4
        tam = 12
    elif tipo == "15,11":
        paridade = 4
        tam = 15

    vet = encode(vet,paridade, tam)
    opcao = input("Deseja simular um erro?(s ou n)")

    if opcao == "s":
        print("Mensagem atual: ",vet)
        erro = input("Insira a posição e o erro, Ex. 4,1: ")
        index, bit = erro.split(",")

        if int(index) not in range(len(vet)):
            print("Posição fora dos limites da mensagem!!")
        else:
            vet[int(index)] = bit

        decode(vet,paridade)
    elif opcao == "n":
        decode(vet,paridade)
    else:
        print("Opcao incorreta!!")


def encode(vet, tipo, tam):
    # alterar quantidade de bits paridade
    p = np.zeros(tipo)
    vet = format_vet(vet,p,tipo,tam)

    for i in range(len(p)):
        aux = redundant_values(i, vet)
        #print("i: ",i, aux)
        for j in aux[1:len(aux)]:
            p[i] = int(p[i])^int(j)

    for i in range(1,len(vet)+1):
        if check_pos(i, tipo):
            v = p[0]
            p = p[1:len(p)]
            vet[i-1] = v

    return vet


def decode(vet, tipo):
    # alterar quantidade de bits paridade
    k = np.zeros(tipo)

    for i in range(len(k)):
        aux = redundant_values(i, vet)
        for j in aux:
            #print("i: ",i, "valores: ",int(k[i]),int(j),int(k[i])^int(j))
            k[i] = int(k[i])^int(j)

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
        print("Mensagem: ", vet)


