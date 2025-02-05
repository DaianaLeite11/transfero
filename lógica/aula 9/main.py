#criar um sistema de pedido de pizzas

cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90
}

pedido =[]

pedido.append("mussarela")
pedido.append("calabresa")

print(pedido)

#sum () -> soma

total = sum(cardapio[sabor] for sabor in pedido)
print(total)
print("Resumo dos pedidos:")
for sabor in pedido:
    print(f"- {sabor}: R$ {cardapio[sabor]:.2f}")