# aluna: Daiana

# exercício 1
'''
Crie um dicionário para o cardápio e adicione um novo sabor com preço. Atualize o preço de um sabor existente e remova um sabor do cardápio.

'''
cardapio = {
    "mussarela": 25.90
}

cardapio["calabresa"] = 27.90
cardapio["frango com catupiry"] = 29.90

cardapio["mussarela"] = 30.90

# del para remover um item 

del cardapio["calabresa"]

print(cardapio)