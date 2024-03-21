menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor para depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"
        else:
            print("Erro! Valor não aceito.")

    elif opcao == "s":
        valor = float(input("Valor para saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro! Saldo insuficiente.")
        elif excedeu_limite:
            print("Erro! Saque ultrapassa o limite permitido.")
        elif excedeu_saques:
            print("Erro! Limite de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque efetuado: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Erro! Valor não aceito.")

    elif opcao == "e":
        print("\n========== EXTRATO DE MOVIMENTAÇÕES ==========")
        print("Nenhuma movimentação registrada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================================")

    elif opcao == "q":
        print("Sessão encerrada. Até logo!")
        break

    else:
        print("Seleção inválida, tente novamente.")
