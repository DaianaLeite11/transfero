sabores = ["Mussarela","Calabresa", "Pepperoni," "Quatro Queijos", "Frango com Catupiry"]

print("Faça seu pedido (digite 'sair' para encerrar)")
pedido = ""

while pedido.lower() != "sair":
    pedido = input("Escolha um sabor")
    if pedido in sabores:
        print(f"{pedido} adicionado ao seu pedido!")
    elif pedido.lower() == "sair":
        print("Pedido encerrado")
    else:
        print("Esse sabor não está no cardápio. Escolha outro")

print("Você saiu do Sistema!")
