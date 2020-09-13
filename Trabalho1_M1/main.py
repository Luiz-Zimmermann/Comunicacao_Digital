from Trabalho1_M1 import Hamming, checksum, CRC


if __name__ == '__main__':

    print("Hamming(1), CRC(2), Checksum(3)")
    metodo = input("Qual método deseja utilizar? Ex. 1: ")


    if int(metodo) == 1:
        print("7,4; 12,8; 15,11")
        tipo = input("Padrão de mensagem, Ex 7,4: ")
        mensagem = input("Insira os dados de acordo com o padrão escolhido acima: ")

        padrao1 = tipo.__contains__("7") and tipo.__contains__("4") and len(mensagem) == 4
        padrao2 = tipo.__contains__("12") and tipo.__contains__("8") and len(mensagem) == 8
        padrao3 = tipo.__contains__("15") and tipo.__contains__("11") and len(mensagem) == 11

        if padrao1 or padrao2 or padrao3:
            Hamming.hamming(mensagem, tipo)
        else:
            print("Padrão e mensagem incompativeis!!")


    elif int(metodo) == 2:
        pass
    elif int(metodo) == 3:
        print("Insira as 4 palavras de 12 bits para fazer o checksum: ")
        palavra1 = input("palavra1: ")
        palavra2 = input("palavra2: ")
        palavra3 = input("palavra3: ")
        palavra4 = input("palavra4: ")

        correto = len(palavra1) == 12 and len(palavra2) == 12 and len(palavra3) == 12 and len(palavra4) == 12

        if correto:
            checksum.iniciaChecksum(palavra1, palavra2, palavra3, palavra4)
        else:
            print("Palavras incompativeis!!")
    else:
        print("Opção invalida!!")
        exit(0)

