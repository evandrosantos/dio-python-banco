import os

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
SLEEP = 5
lista_clientes = []
lista_contas = []
numero_conta = 1
AGENCIA = "001"

def limpar_tela():
    if os.name == "posix": 
        os.system("clear")
    else:
        os.system("cls")

def encontrou_erro(limpar_tela, mensagem):
    limpar_tela()
    print(mensagem)
    input("\n\nPressione enter para continuar")

        
def executar_menu(limpar_tela):
    menu = """

    [c] Criar cliente
    [cc] Criar conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    """
    
    limpar_tela()
    print(menu)
    
    return input("Escolha uma opção do menu: ")
   

def imprimir_extrato(limpar_tela, saldo, /, *, extrato):
    limpar_tela()
    print("Extrato\n")
    print(extrato)
    print(f"Saldo disponível: R$ {saldo}")

    input("\n\npressione qualquer tecla para continuar")
    

def executar_deposito(limpar_tela, saldo, extrato, /):
    limpar_tela()
    deposito = float(input("Digite o valor desejado para o depósito: "))
    if deposito <= 0:
        encontrou_erro(limpar_tela, "Impossível fazer o depósito. Valor inválido")
    else:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"

        apresentar_saldo(limpar_tela, saldo, "Depósito efetuado com sucesso")
    
    return saldo, extrato

def apresentar_saldo(limpar_tela, saldo, texto):
    limpar_tela()
    print(texto)
    print(f"Novo saldo: R$ {saldo:.2f}")

    input("\n\npressione qualquer tecla para continuar")

def efetuar_saque(*, limpar_tela, encontrou_erro, apresentar_saldo, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    limpar_tela()
    saque = float(input("Digite o valor desejado para o saque: "))
    if saque > limite:
        encontrou_erro(limpar_tela, f"Excedeu o limite de saque (R$ {limite:.2f})")
    elif numero_saques >= LIMITE_SAQUES: 
        encontrou_erro(limpar_tela, f"Excedeu a limite de saques diários ({LIMITE_SAQUES})")
    elif saque > saldo:
        encontrou_erro(limpar_tela, f"Sem limite disponível para o saque de R$ {saque:.2f}")
    elif saque <= 0:
        encontrou_erro(limpar_tela, "Impossível fazer o saque. Valor inválido")
    else:
        saldo -= saque
        numero_saques += 1
        extrato += f"Saque: R$ {saque:.2f}\n"

        apresentar_saldo(limpar_tela, saldo, "Saque efetuado com sucesso")

    return saldo, numero_saques, extrato

def criar_cliente(encontrou_erro, limpar_tela, lista_clientes):
    limpar_tela()
    cpf = input("digite o CPF do cliente: ")

    encontrados = [cliente for cliente in lista_clientes if cliente["cpf"] == cpf]

    if len(encontrados) > 0:
        encontrou_erro(limpar_tela, f"Não foi possível realiazar o cadastro - cliente de cpf {cpf} já estava cadastrado")
    else:
        cliente = dict()

        cliente["cpf"] = cpf
        cliente["nome"] = input("Digite o nome do cliente: ")
        cliente["data_nascimento"] =  input("Digite a data de nascimento do cliente: ")
        cliente["endereco"] = input("Digite o endereço do cliente: s")

        lista_clientes.append(cliente)

        print("\n\nCliente cadastrado com sucesso")
        input("Pressione qualquer tecla para continuar")

    return lista_clientes
        

def criar_conta(encontrou_erro, limpar_tela, numero_conta, lista_contas, lista_clientes, AGENCIA):
    limpar_tela()
    cpf = input("digite o CPF do cliente: ")

    encontrados = [cliente for cliente in lista_clientes if cliente["cpf"] == cpf]
    if len(encontrados) < 1:
        encontrou_erro(f"Não é possivel cadastrar a conta, cliente {cpf} não existe")
    else:
        conta = dict()

        conta["cpf"] = cpf
        conta["numero"] = numero_conta
        conta["agencia"] = AGENCIA

        lista_contas.append(conta)
        numero_conta += 1
        
        print("\n\nConta cadastrada com sucesso")
        input("Pressione qualquer tecla para continuar")

    return numero_conta, lista_contas


while True:
    opcao = executar_menu(limpar_tela)
    if opcao == "c":
        lista_clientes = criar_cliente(encontrou_erro, limpar_tela, lista_clientes)
    elif opcao == "cc":
       numero_conta, lista_contas =  criar_conta(encontrou_erro, limpar_tela, numero_conta, 
                                                 lista_contas, lista_clientes, AGENCIA)
    elif opcao == "d":
        saldo, extrato = executar_deposito(limpar_tela, saldo, extrato)
    elif  opcao == "s":
        saldo, numero_saques, extrato = efetuar_saque(limpar_tela = limpar_tela, 
                                                      encontrou_erro = encontrou_erro, 
                                                      apresentar_saldo = apresentar_saldo, 
                                                      saldo = saldo, 
                                                      limite = limite, 
                                                      extrato = extrato, 
                                                      numero_saques = numero_saques, 
                                                      LIMITE_SAQUES = LIMITE_SAQUES)
    elif opcao == "e":
        imprimir_extrato(limpar_tela, saldo, extrato = extrato)
    elif opcao == "q":
        break
    else:
        limpar_tela()
        encontrou_erro(limpar_tela ,"Opção inválida")
