# 11.	hacer un programa que lea un caracter por teclado y compruebe si es una letra mayuscula

letra = input('introducir un caracter: ')

if letra.isupper() == True: # issupper comprueba si es mayuscula o minuscula, lanzando true si es mayuscula y false sino es
    print(letra, 'la letra introducida es mayuscula ')
else:
    print(letra, 'la letra introducida es minuscula ')