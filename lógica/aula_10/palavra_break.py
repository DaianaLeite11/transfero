clientes = ["João", "Maria", "Carlos", "Ana", "Pedro"]

print("Atendendo Clientes")
for i, cliente in enumerate(clientes):
    if i > 2:
        print("Número de cliente excedidos")
        break
        