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
        print("------------")
        print("Metodo CRC.")
        print("Montar uma mensagem (1), Verificar mensagem (2)")

        func = input("Qual função você deseja executar? Ex. 1: ")

        if int(func) == 1:
            print("Montar mensagem")
            palavra_str = input("Digite a palavra a ser enviada: (Ex.: 10101101)")
            polinom_str = input("Digite o polinômio de grau 3: (Ex.: 1101)")
            crc = CRC.monta_palavra(palavra_str, polinom_str)

            print("Validando mensagem com o mesmo polinômio...")
            CRC.detecta_erro(crc, polinom_str)

        elif int(func) == 2:
            print("Verificar mensagem")
            mensagem_str = input("Insira a mensagem recebida para verificação de erro: (Ex.: 10101101010)")
            polinomi_str = input("Insira o polinômio de grau 3 utilizado: (Ex.: 1101)")
            print(CRC.detecta_erro(mensagem_str, polinomi_str))

    elif int(metodo) == 3:
        pass
    else:
        print("Opção invalida!!")
        exit(0)
