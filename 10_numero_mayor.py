# 10.	pedir dos numeros y decir cual es el mayor o si son iguales
numero1 = int(input('introducir el primer numero'))
numero2 = int(input('introducir el segundo numero'))

if numero1 > numero2:
    print ('el numero mayor es: ', numero1)
elif numero2 > numero1:
    print('el numero mayor es: ', numero2)
else:
    print('son iguales', numero2, numero1)