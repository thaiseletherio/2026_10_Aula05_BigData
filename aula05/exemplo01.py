#entrada
valor_pedido = float(input('Digite o valor do pedido: R$ '))
distancia = float(input('Digite a distância em Km: '))

if valor_pedido < 50 and distancia <= 3:
    frete = 0
    valor_final = valor_pedido + frete
    print (f'Frete Grátis. Valor_pedido = {valor_final}')

else:
    frete = 8 
    valor_final = valor_pedido + frete
    print (f'valor do pedido: {valor_final}') 