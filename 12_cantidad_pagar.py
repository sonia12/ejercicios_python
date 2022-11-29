# 12.En MegaPlaza se hace un 20% de descuento a los clientes cuya compra supere los $300.
#  ¿cual sera la cantidad que pagara una persona por su compra?

compra = float(input(' introducir de que valor es su compra ? '))

if compra >= 300:
    compra_total = compra - (compra*0.2)
    print('su compra es: ', compra_total, 'con el 20% de descuento')
else:
    print ('su compra es: ', compra)