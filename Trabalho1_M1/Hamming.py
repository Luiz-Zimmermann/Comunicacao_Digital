import numpy as np

# Função para descobrir onde irão os bits de paridade
def check_pos(pos, tam):

    for i in range(tam):

        if 2**i == pos:
            return True

    return False

# Cria o corpo do vetor da mensagem final, de acordo com o padrão escolhido
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

# Coloca em um vetor, os bits que o bit de paridade cobre
# Ex: p0 = b0^b1^b3
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

# Cria a mensagem final que será enviada.
# dados + bits de paridade
def encode(vet, tipo, tam):

    p = np.zeros(tipo)
    vet = format_vet(vet,p,tipo,tam)

    # Calcula o valor do bit de paridade
    for i in range(len(p)):
        aux = redundant_values(i, vet)
        for j in aux[1:len(aux)]:
            p[i] = int(p[i])^int(j)

    # Adiciona o bit de paridade no vetor
    for i in range(1,len(vet)+1):
        if check_pos(i, tipo):
            v = p[0]
            p = p[1:len(p)]
            vet[i-1] = v

    return vet

# Decodifica a mensagem recebida
def decode(vet, tipo):
    # variáveis para verificação de erro
    k = np.zeros(tipo)

    # Calcula o valor das variáveis de erro
    for i in range(len(k)):
        aux = redundant_values(i, vet)
        for j in aux:
            k[i] = int(k[i])^int(j)

    # Se o conjunto das variáveis conter pelo menos um valor 1, então há um erro na mensagem.
    # Calcula a posição do erro e o corrige.
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
        print("Mensagem recebida: ", vet)


