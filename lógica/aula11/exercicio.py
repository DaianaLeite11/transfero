'''
### **Fazer um Pedido 🛒**

💡 **Enunciado:**

Crie uma função chamada `fazer_pedido()` que permite ao cliente escolher pizzas do cardápio.

📝 **Regras:**
A função deve receber o cardápio como argumento.
O cliente pode escolher quantas pizzas quiser.
O pedido deve ser armazenado em uma lista.
Se o cliente digitar "sair", o pedido deve ser finalizado.
e o sabor digitado não existir no cardápio, exibir um erro e pedir outra escolha.
Retornar a lista com os sabores escolhidos.

🔍 Exemplo esperado:

Digite o sabor da pizza (ou 'sair' para finalizar): Mussarela
✅ Mussarela adicionada ao pedido!
Digite o sabor da pizza (ou 'sair' para finalizar): Quatro Queijos
✅ Quatro Queijos adicionada ao pedido!
Digite o sabor da pizza (ou 'sair' para finalizar): Chocolate
❌ Esse sabor não está disponível. Escolha outro.
Digite o sabor da pizza (ou 'sair' para finalizar): sair

📦 Pedido finalizado! Pizzas escolhidas: ['Mussarela', 'Quatro Queijos']

'''

def fazer_pedido(cardapio):
    pedido = []

    while True:
        sabor = input("Digite o sabor da pizza que deseja (ou 'sair' para finalizar): ")
        if sabor.lower() == "sair":
            break
        elif sabor in cardapio:
            print(f"✅ {sabor} adicionada ao pedido!")
            pedido.append(sabor)
        else:
            print(f"❌ Esse sabor não está disponível. Escolha outro.")
    return pedido

cardapio = ["mussarela", "quatro queijos", "calabresa", "frango com catupiry"]
pedido_cliente =fazer_pedido(cardapio)
print(f"📦 Pedido finalizado! Pizzas escolhidas: {pedido_cliente}")
