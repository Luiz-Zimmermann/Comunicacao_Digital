import numpy as np

# Funcao que inverte os bits
def comp1(palavra):
    aux = np.zeros(len(palavra), dtype=int)
    for i in range(len(palavra)):
        # Se for zero, vale 1
        if palavra[i] == 0:
            aux[i] = 1
        else: # Se for 1, vale 0
            aux[i] = 0
    return aux

# Essa funcao tem o mesmo proposito que a anterior
# Ela foi criada para não ter uma funcao recursiva
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


# Funcao de soma
def soma(x1, x2):
    # Cria vetor zerado do tamanho do vetor por parametro
    result = np.zeros(len(x1), dtype=int)
    # Cria um vetor auzxiliar de tamanho + 1
    aux = np.zeros(len(x1)+1, dtype=int)
    # Laco de repeticao fazer a soma entre todas as posicoes
    for i in range(len(x1)):
        # Se posicao do vetor auxiliar estiver 1(vai um)
        if aux[i] == 1:
            # Se ambos palavras valerem 1
            if x1[i] == 1 and x2[i] == 1:
                result[i] = 1
                aux[i + 1] = 1
            # Se um deles valerem um e o outro zero
            elif x1[i] != x2[i]:
                result[i] = 0
                aux[i + 1] = 1
            # Se os dois forem zero
            else:
                result[i] = 1
        else:   # Se vetor auxiliar estiver zero(vai um)
            # Se ambos valerem 1
            if x1[i] == 1 and x2[i] == 1:
                result[i] = 0
                aux[i + 1] = 1
            # Se um deles valer 1 e o outro zero
            elif x1[i] != x2[i]:
                result[i] = 1
            else:   # Se ambos valerem zero
                result[i] = 0

    # Se a ultima posicao do vetor auxiliar valer 1
    # Significa que deu overflow
    # Com isso terá que somar 1 ao resultado final
    if aux[aux.size-1] == 1:
        aux2 = np.zeros(len(x1), dtype=int)
        aux2[0] = 1
        # Retorna o resultado com soma de 1
        return somaUm(result, aux2)
    else:
        # Caso nao der overflow, retorna o resultado final apenas
        return result


# Funcao que descobre o EDC
def monta_palavra(palavra1, palavra2, palavra3, palavra4):
    # Faz a soma da primeira com a terceira palavra
    resultado1 = soma(palavra1, palavra2)
    # Soma resultado com a terceira palavra
    resultado2 = soma(resultado1, palavra3)
    # Soma resultado com a quarta palavra
    resultado3 = soma(resultado2, palavra4)
    # Chama funcao de complemento de 1 para descobrir o EDC
    EDC = comp1(resultado3)
    print("EDC: ", EDC, "\n")
    # Monta o Tx
    Tx = str(palavra1) + " " + str(palavra2) + " " + str(palavra3) + " " + str(palavra4) + ":" + str(EDC)
    print("Tx", Tx.replace("[", "").replace("]", " "))
    # Retorna EDC
    return EDC


# funcao que verifica erro
def verificaErro(palavra1, palavra2, palavra3, palavra4, EDC):

    # Soma primeira com segunda palavra e salva no vetor
    resultado1 = soma(palavra1, palavra2)
    # Faz a soma do vetor com a terceira palavra
    resultado2 = soma(resultado1, palavra3)
    # Faz a soma do vetor com a quarta palavra
    resultado3 = soma(resultado2, palavra4)
    # Faz a soma do vetor com o EDC para verificacao de erro
    resultadoFinal = soma(resultado3, EDC)
    # Monta o RX
    Rx = str(palavra1) + str(palavra2) + str(palavra3) + str(palavra4) + ":" + str(EDC)
    print("Rx", Rx.replace("[", "").replace("]", " "))
    # Printa o resultado final
    print("resultado final: ", resultadoFinal, "\n")

    # Retorna o resultado para verificacao de erro
    return resultadoFinal

def iniciaChecksum(palavra1, palavra2, palavra3, palavra4):
    vet1 = []
    for x in palavra1:
        vet1.append(x)
    vet2 = []
    for x in palavra2:
        vet2.append(x)
    vet3 = []
    for x in palavra3:
        vet3.append(x)
    vet4 = []
    for x in palavra4:
        vet4.append(x)

    # Chama funcao para fazer as contas e descobrir o EDC
    EDC = monta_palavra(vet1, vet2, vet3, vet4)

    opcao = input("Deseja simular um erro?(s ou n)")

    if opcao == "s":
        print("Insira as 4 palavras: ")
        palavraErro1 = input("palavra1: ")
        palavraErro2 = input("palavra2: ")
        palavraErro3 = input("palavra3: ")
        palavraErro4 = input("palavra4: ")

        correto = len(palavraErro1) == 12 and len(palavraErro2) == 12 and len(palavraErro3) == 12 and len(palavraErro4) == 12

        if correto:
            vetAux1 = []
            for x in palavraErro1:
                vetAux1.append(x)
            vetAux2 = []
            for x in palavraErro2:
                vetAux2.append(x)
            vetAux3 = []
            for x in palavraErro3:
                vetAux3.append(x)
            vetAux4 = []
            for x in palavraErro4:
                vetAux4.append(x)

            # Chama funcao de verifica erro passando 4 palavras e o EDC como parametro
            VerificaErroFinal = verificaErro(vetAux1,
                                             vetAux2,
                                             vetAux3,
                                             vetAux4,
                                             EDC)
        else:
            print("Erro em algumas da palavras!!!")

    elif opcao == "n":
        pass
    else:
        print("Opcao incorreta!!")


    testa = 0
    # Laco de repeticao para verificacao de erro
    for i in range(len(VerificaErroFinal)):
        # Se existe algum erro
        if VerificaErroFinal[i] == 0:
            testa += 1

    # Se nao tem erro, printa que esta tudo ok
    if testa == 0:
        print("Sem erro")
    else:   #se tem erro printa que algo deu errado
        print("Com erro")
