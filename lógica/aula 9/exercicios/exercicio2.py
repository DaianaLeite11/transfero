# aluna: Daiana

# exercício 2

'''
Dado dois conjuntos de ingredientes, exiba os ingredientes comuns entre eles e os que estão disponíveis apenas em um conjunto.
'''
ingredientes_1 = {"mussarela", "calabresa", "catupiry"}
ingredientes_2 = {"mussarela", "frango", "catupiry"}

ingredientes_comuns = ingredientes_1.intersection(ingredientes_2)
ingredientes_disponiveis_1 = ingredientes_1.difference(ingredientes_2)
ingredientes_disponiveis_2 = ingredientes_2.difference(ingredientes_1)

print("Ingredientes comuns:", ingredientes_comuns)
print("Ingredientes disponíveis apenas no primeiro conjunto:", ingredientes_disponiveis_1)
print("Ingredientes disponíveis apenas no segundo conjunto:", ingredientes_disponiveis_2)