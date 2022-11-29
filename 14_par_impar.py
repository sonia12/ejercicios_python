# 14.	hacer un programa que tome dos numeros y diga si ambos son pares o impares.
'''
numero1= int(input('introducir el primer numero'))
numero2 = int(input(' introducir el segundo numero'))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print('ambos numero son pares')
elif numero1 % 2 != 0 and numero2 % 2 != 0:
    print('ambos numeros son impares')
else:
   print('un numero es par y el otro es impar' )
'''

## otra forma

numero1 = int(input('introducir el primer numero'))
numero2 = int(input(' introducir el segundo numero'))

if numero1 % 2 == 0 and numero2 % 2== 0:
        print('Ambos son pares')
else:
    if(numero1 % 2 != 0 and numero2 % 2!=0):
        print('Ambos son impares')
    else:
        if numero1 % 2 == 0:
            print( numero1, 'es par')
        else:
            print(numero1, 'es impar')
            
        if numero2 % 2== 0:
            print( numero2, 'es par')
        else:
            print( numero2, 'es par')
'''
numero1 = int(input('introducir el primer numero'))
numero2 = int(input(' introducir el segundo numero'))

if numero1 % 2 == 0 and numero2 % 2== 0:
        print('Ambos son pares')
else:
    if(numero1 % 2 != 0 and numero2 % 2!=0):
        print('Ambos son impares')
    else:
        n1 = 'es par' if numero1 % 2 == 0 else 'es impar'
        n2 = 'es par' if numero2 % 2 == 0 else 'es impar'
    print (n1, n2 ) 
'''
        

    
   

