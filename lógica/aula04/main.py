# Pizzaria Sabores
NOME_CLIENTE = "jose"

pizza_calabresa = "calabresa"
pizza_frango = "frango"
pizza_queijo = "queijo"

pizza_pequena = 10
pizza_media = 15
pizza_grande = 20

estoque = 10
# IF -> Obrigatório
if estoque > 0:
    print("Pedido aceito! Temos pizzas disponíveis")

# IF ELSE -> Opcional
if estoque > 0:
    print("Pedido aceito! Temos pizzas disponíveis")
else:
    print("Desculpe, estamos sem esse sabor no momento.")

# IF ELIF ELSE -> Opcional, e pode ser repetido
distancia_cliente = 8 # 8 quilômetros
# Se o cliente morar até 5KM da pizzaria, a entrega será em 20m
# Se o cliente morar acima de 5KM E ATÉ 10KM, a entrega será em 40m
# Senão, não entregamos nessa região.
if distancia_cliente <= 5:
    print("O tempo estimado de entrega é de 20 minutos.")
elif distancia_cliente <= 10:
    print("O tempo estimado de entrega é de 40 minutos ")
else:
    print("Infelizmente, não entregamos nessa região.")
