# 15.	pedir 3 numeros y mostrarlos ordenados de mayor a menor

numero1 = int(input('introducir primer numero'))
numero2 = int(input('introducir segundo numero'))
numero3 = int(input('introducir tercer numero'))

if numero1 > numero2 and numero2 > numero3:
    print(numero1, numero2, numero3)

elif  numero1> numero3 and numero3 >numero2:
    print(numero1 , numero3, numero2)

elif numero2 >numero3> numero1:
    print(numero2,numero3,numero1)

elif numero2 > numero1 and numero1 > numero3:
    print(numero2, numero1, numero3)

elif numero3 > numero1 and numero1 > numero2:
    print(numero3, numero1, numero2)

elif numero3 > numero2 and numero2> numero1:
    print (numero3 ,numero2, numero1)

elif numero1 == numero2 and numero2 > numero3:
    print(numero1 , numero2 , numero3)
elif numero2 == numero3 and numero2 > numero1:
    print(numero2, numero3, numero1)
elif numero1==numero3 and numero3 > numero2:
    print(numero1, numero2, numero3)
else: 
    print(numero1,numero2, numero3)