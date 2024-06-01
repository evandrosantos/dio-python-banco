menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input("Escolha uma opção do menu: ")
    if opcao == "d":
        deposito = float(input("Digite o valor desejado para o depósito: "))
        if deposito <= 0:
            print("Impossível fazer o depósito. Valor inválido")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

            print("Depósito efetuado com sucesso")
            print(f"Novo saldo: R$ {saldo:.2f}")
    elif  opcao == "s":
        saque = float(input("Digite o valor desejado para o saque: "))
        if saque > limite:
            print(f"Excedeu o limite de saque (R$ {limite:.2f})")
        elif numero_saques >= LIMITE_SAQUES: 
            print("Excedeu a limite de saques diários ({LIMITE_SAQUES})")
        elif saque > saldo:
            print(f"Sem limite disponível para o saque de R$ {saque:.2f}")
        elif saque <= 0:
            print("Impossível fazer o saque. Valor inválido")
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"

            print("Saque efetuado com sucesso")
            print(f"Novo saldo: R$ {saldo:.2f}")
    elif opcao == "e":
        print("Extrato\n")
        print(extrato)
        print("Saldo: R$ {saldo}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida")
        