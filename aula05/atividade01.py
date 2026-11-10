#entrada
nota_1 = float(input(f'Qual foi a sua nota na primeira prova? '))
nota_2 = float(input(f'Qual foi a sua nota na segunda prova? '))
nota_3 = float(input(f'Qual foi a sua nota na terceira prova? '))
nota_4 = float(input(f'Qual foi a sua nota na quarta prova? '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7:
    print (f'Parabéns, sua média é {media:.1f}. Até ano que vem!')
elif media >= 5:
    print (f'Sua média é {media:.1f}. Estude para a recuperação!')
else:
    print (f'Infelizmente, você ficou com média {media:.1f} e não teve nota suficiente para passar. Sinto muito.')