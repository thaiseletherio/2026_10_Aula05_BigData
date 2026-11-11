#entrada
nota = float(input('Nota: '))
frequencia = float (input('Frequência: '))
mensalidade_cheia = 3000

if nota >= 7 and frequencia >= 75:
    bolsa = mensalidade_cheia * 0.20 
    print (f'Você recebeu uma bolsa de R$ {bolsa}')

else:
    print(f'Você não recebeu bolsa e pagará R$ {mensalidade_cheia}')