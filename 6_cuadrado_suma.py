#6.	Hacer un programa que calcule el cuadrado de una suma (a+b)^2= a^2+b^2+2ab

valor_a = float (input('introducir el valor de a: '))
valor_b = float (input('introducir el valor de b: '))

cuadrado_suma = float (valor_a**2)+(valor_b**2)+ 2*(valor_a*valor_b)
print (' el cuadrado de la suma es:  ', cuadrado_suma)