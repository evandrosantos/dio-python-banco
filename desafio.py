import os
import time

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
SLEEP = 5


def limpar_tela():
    if os.name == "posix": 
        os.system("clear")
    else:
        os.system("cls")
        
def executar_menu(limpar_tela):
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    """
    
    limpar_tela()
    print(menu)
    
    return input("Escolha uma opção do menu: ")
   

def imprimir_extrato(limpar_tela, extrato):
    limpar_tela()
    print("Extrato\n")
    print(extrato)
    print("Saldo disponível: R$ {saldo}")
    time.sleep(SLEEP)
    

def executar_deposito(limpar_tela, saldo, extrato):
    limpar_tela()
    deposito = float(input("Digite o valor desejado para o depósito: "))
    if deposito <= 0:
        print("Impossível fazer o depósito. Valor inválido")
    else:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"

        print("Depósito efetuado com sucesso")
        print(f"Novo saldo: R$ {saldo:.2f}")
    
    return saldo, extrato

while True:
    opcao = executar_menu()
    if opcao == "d":
        saldo, extrato = executar_deposito(limpar_tela, saldo, extrato)
    elif  opcao == "s":
        limpar_tela()
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
        imprimir_extrato(limpar_tela, extrato)
    elif opcao == "q":
        break
    else:
        limpar_tela()
        print("Opção inválida")
        time.sleep(SLEEP)
        