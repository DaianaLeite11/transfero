'''
### **xibir o Cardápio 📜**

💡 **Enunciado:**

Crie uma função chamada `exibir_cardapio()` que exibe o cardápio da pizzaria.

📝 **Regras:**
O cardápio deve ser armazenado em um dicionário, onde as chaves são os sabores das pizzas e os valores são os preços.
A função deve exibir os itens do cardápio formatados corretamente.

 Exemplo esperado:

 🍕 Cardápio da Pizzaria Sabores:
1. Mussarela - R$ 30.00
2. Calabresa - R$ 32.00
3. Pepperoni - R$ 35.00
4. Quatro Queijos - R$ 38.00
5. Frango com Catupiry - R$ 40.00
'''

def exibir_cardapio():
    cardapio = {
        "mussarela": 30.00,
        "calabresa": 32.00,
        "pepperoni": 35.00,
        "quatro queijos": 38.00,
        "frango com catupiry": 40.00
    }

    print("🍕 Cardápio da Pizzaria Sabores:")
    for sabor, preco in cardapio.items():
        print(f"{sabor} - R$ {preco:.2f}")

exibir_cardapio()