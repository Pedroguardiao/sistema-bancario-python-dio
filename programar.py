# deposito, saque e extrato, depositar valores positivos na conta, todos os depositos devem ser armazenados em uma
# variável e exibidos na operação extrato, sistema deve permitir realizar 3 saques diarios com limite de R$ 500 po saque
# se nao tem saldo, deve emitir msg dizendo q ñ tem saldo, todos os saques dever ser armazenados em uma variável e
# e exibidos na operação extrato


menu = """
    [d] - Depositar 
    [s] - Saque 
    [e] - Extrato 
    [q] - Sair
    
    
    
    =>>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Desposito: R$ {valor:.2f}\n"

        else:
            print("Valor informado não é valido!!")
    if opcao == "s":
        valor = float(input("Informe valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente")
        elif excedeu_limite:
            print(" O saque execede o limite de R$ {}".format(limite))
        elif excedeu_saque:
            print("Você atingiu limite de saque diário!!")

        elif valor > 0:
            saldo -= valor
            extrato -= f"Saque: R$ {valor:.2f}\n"
            numero_saque +=1

        else:
            print("Valor informado invalido")

    elif opcao == "e":
        print("\n************EXTRATO************")
        print("Não foram realizdadas operações." if not extrato else extrato)
        print(f"\n Saldo de R${saldo:.2f}")
        print("*******************************")

    elif opcao =="q":
        break

    else:
        print("opção invalida, escolha as opções do menu..")









