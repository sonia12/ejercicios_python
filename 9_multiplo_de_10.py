# 9.Hacer un programa que lea un numero entero y muestre si el numero es multiplo de 10.

numero = int(input('introducir un numero entero: '))

if numero % 10 == 0: # multiplo de 10 es numero / entre 10 el resto es cero
    print ('el numero ', numero, 'es multiplo de 10')
else: 
    print('el numero ', numero, 'no es multiplo de 10')
