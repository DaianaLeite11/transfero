
sabores = ["mussarela", "calabresa","frango com catupiry", "portuguesa"]
daddos_pizza = ['mussarela', 26.9]
daddos_pizza2 = ['mussarela', 26.9, sabores]

print("InformaçÕes sobre os sabores da pizza: ", daddos_pizza[0], "que custa ", daddos_pizza[1])
print(daddos_pizza2)

# append
sabores.append("margherita")
print("Os sabores disponiveis sao: ", sabores)

# remove
sabores.remove("calabresa")
print("Os sabores disponiveis sao: ", sabores)

#acessando items da lista

print(sabores[0])
print(sabores[1])
print(sabores[2])
print(sabores[3])
print(sabores[-1])

#tupla

tamanhos = ("pequena", "media", "grande")
print("tamanhos disponiveis sao: ",tamanhos)

#acessando items da tupla

print(tamanhos[0])
print(tamanhos[1])
print(tamanhos[2])
print(tamanhos[-1])



