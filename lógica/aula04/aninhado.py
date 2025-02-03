motoboys_disponiveis = False
distancia_cliente = 8

# Verificar se a entrega pode ser feita com base na distância e se há motoboys disponíveis
# Se a distância for até 10km, a entrega é realizada
    # Se tivermos motoboys disponíveis, a entrega será realiza
    # Senão, não será realizada.
# Senão, não entregamos
if distancia_cliente <= 10:
    if motoboys_disponiveis:
        print("Entrega confirmada! Um motoboy está a caminho.") 
    else:
        print("Infelizmente, estamos sem motoboys disponíveis")   
else:
    print("Desculpe, não entregamos dessa distância")