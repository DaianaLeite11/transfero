
# Crie um programa que permita adicionar produtos a um carrinho de compras. O programa deve continuar pedindo produtos 
# até que o usuário digite "finalizar". No final, exiba todos os produtos comprados.
# 📝 Regras:
# O usuário digita o nome do produto e ele é adicionado a uma lista.
# Se o usuário digitar "finalizar", o programa encerra e mostra os produtos comprados.

lista_de_compras = []


for i, itens in enumerate(lista_de_compras):
    itens = input("Digite o produto ou 'finalizar' para encerrar: ")
    if itens.lower() != "finalizar":
        break
    lista_de_compras.append(itens) 


print(f'''
    Você comprou:
      {lista_de_compras}
''')

