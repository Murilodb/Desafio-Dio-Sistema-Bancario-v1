menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
deposito = 0
limit = 500
numero_saques = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("'Depósito'")
        deposito = float(input("Digite o valor do seu depósito: "))
        if deposito > 0:
            print(f"\nSeu depósito foi de: {deposito:.2f}") 
            saldo += deposito
            extrato += f"\nDepósito de {deposito:.2f}"
        else:
            print("Não é possível depositar valores negativos")

    elif opcao == "s":
        print("'Saque'\n")
        if saldo > 0 and numero_saques < LIMITE_SAQUE:
            saque = float(input("Quanto você deseja retirar: "))
            if saque > 0:
                if saque <= saldo:
                    saldo -= saque
                    extrato += f"\nSeu saque foi de {saque:.2f}"
                    numero_saques += 1
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo insuficiente para o saque.")
            else:
                print("Não é possível sacar valores negativos.")
        else: 
            print("Opção de saque não disponível pois não há saldo em conta ou limite de saques atingido.")

    elif opcao == "e":
        print("""""""""""""Extrato""""""""""""")
        print(extrato)


    elif opcao == "q":
        break

    else:
        print("Opção inválida")
