# 1.pedir un numero entre 0 y 99999 y decir cuantas cifras tiene

cifra = int(input('introducir un numero'))

if cifra <= 9: 
    print(cifra, 'tiene una cifra')
elif cifra <=99:
    print(cifra, 'tiene 2 cifra')
elif cifra <=999:
    print(cifra, 'tiene 3 cifra')
elif cifra <= 9999:
    print(cifra, 'tiene 4 cifra')
elif cifra <= 99999:
    print(cifra, 'tiene 5 cifra')
elif cifra <= 999999:
    print(cifra, 'tiene 6 cifra')
else:
    print('tiene 7 o mas cifras')