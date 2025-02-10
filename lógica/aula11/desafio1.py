'''

Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Pizza
Produto 'Pizza' adicionado ao carrinho!
Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Refrigerante
Produto 'Refrigerante' adicionado ao carrinho!
Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): finalizar

🛍️ Você comprou:
- Pizza
- Refrigerante

'''
pedido = ""
item_pedido =[]


while pedido.lower() != "sair":
    pedido = input("Escolha um item: ")
    if pedido != "sair":
        print(f"{pedido} adicionado ao seu carrinho!")
        item_pedido.append(pedido)
        
    elif pedido.lower() == "sair" :
        print("Pedido encerrado!")
        for item in item_pedido:
            print(f"- {item}")
    else:
        print("Erro inesperado.")
