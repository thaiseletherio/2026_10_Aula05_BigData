num = int(input(f'Diga um número, considere qualquer número: '))

match num:
    case num if num >= 0:
        print ('positivo')
    case num if num <= 0:
        print ('negativo')
    case num if num == 0:
        print ('zero')