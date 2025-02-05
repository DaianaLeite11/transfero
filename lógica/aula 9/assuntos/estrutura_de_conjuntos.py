

ingredientes= {"mussarela", "calabresa", "tomate", "azeitona"}
print("Ingredientes:", ingredientes)

ingredientes.add("oregano")
print("Ingredientes atualizados:", ingredientes)

# união dos conjuntos
adicionais= {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("Todos os ingredientes:", todos_ingredientes)

# interseção dos conjuntos
pizza_vegana ={ "tomate", "azeitona", "rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("Ingredientes comuns:", comuns)