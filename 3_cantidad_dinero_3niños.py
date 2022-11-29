# 3.Guillermo tiene N dolares. Luis tiene la mitad de lo que posee Guillermo. 
# Juan tiene la mitad de lo que posee  Luis  y Guillermo juntos. Hacer un programa que calcule e imprima
# la cantidad de dinero que tienen entre los tres

dinero_guillermo = int(input(' cuanto tiene guillermo? '))
dinero_luis = dinero_guillermo/2
dinero_juan = (dinero_guillermo + dinero_luis) / 2

total_de_los_tres = dinero_guillermo + dinero_luis + dinero_juan
print (' los tres niños tienen una cantidad de: ', total_de_los_tres)