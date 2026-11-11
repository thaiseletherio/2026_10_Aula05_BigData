#entrada
compra = float(input('Digite valor da conta: '))
fidelidade = input('Você tem nosso programa de fidelidade? [S / N] ').lower()[0]
mensagem = "frete grátis"
frete = 25

if compra > 200 or fidelidade == "s":
    print (mensagem)
    print (f' Valor da compra: R$ {compra}') 

else: 
    compra = compra + frete
    print (f'valor total: {compra}')

#constante é em MAIUSCULA e não deve alterar o valor.
