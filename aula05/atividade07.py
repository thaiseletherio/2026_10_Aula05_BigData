venda = float (input('Valor da venda: '))
match venda:
    case venda if venda < 100:
        print ('venda pequena')
    case venda if 100 <= venda < 500:
        print ('venda média')
    case venda if venda >=500:
        print ('venda grande')
