saldo = 500
salario = float(input("Digite seu salário: "))
saldo += salario

while saldo > 0:
    print(f'Saldo disponível: R$ {saldo:.2f}')
    saque = input("Digite o valor para sacar ou 'sair' para encerrar: ")

    if saque.lower() == "sair":
        print("Operação encerrada")
        break
    saque = float(saque)
    if saque > saldo:
        print("❌ Saldo insuficiente!")
    else:
        saldo -= saque
        print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")






