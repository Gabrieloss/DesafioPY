saldo = 0
limite_saque_dia = 3
limite_saque = 500
saques_realizados = 0


print('''
        MENU:

        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [0] - Sair
    ''')

while True:
        
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou. O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if saldo >= valor and valor <= limite_saque and saques_realizados < limite_saque_dia:
            saldo -= valor
            saques_realizados += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            if saldo < valor:
                print("Operação falhou. Você não tem saldo suficiente.")
            elif valor > limite_saque:
                print("Operação falhou. O valor do saque excede o limite.")
            elif saques_realizados >= limite_saque_dia:
                print("Operação falhou. Limite diário de saques atingido.")

    elif opcao == "3":
        if saldo == 0 and saques_realizados == 0:
            print("Não foram realizadas movimentações.")
        else:
            print(f"Extrato:\nSaldo Atual: R$ {saldo:.2f}\nSaques realizados: {saques_realizados}")

    elif opcao == "0":
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida.")
