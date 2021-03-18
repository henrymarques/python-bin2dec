def decToBin(number):
    bin = ""
    remainders = []

    while number > 0:
        remainder = number % 2
        remainders.append(str(remainder))
        number = int(number / 2)

    remainders.reverse()
    bin = bin.join(remainders)
    print(bin+"\n\n")

def binToDec(number):
    dec = 0
    parts = []
    counter = len(number)-1

    for bin in number:
        if int(bin) == 0:
            parts.append(0)
        else:
            part = 2 ** counter
            parts.append(part)
        counter-=1

    for part in parts:
        dec += part

    print(dec)

while True:
    opcao = int(input("Digite uma opção: \n1. Decimal para binário\n2. Binário para decimal\n\n0. Sair\n"))
    if(opcao == 1):
        dec = int(input("Digite um número decimal: "))
        decToBin(dec)
    elif(opcao == 2):
        bin = str(input("Digite um número binário: "))
        binToDec(bin)
    else:
        print("Você escolheu sair")
        break;
