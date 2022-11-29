

'''
cantidad_carro_vendido= int(input('cuantos carros vendio en este mes? '))
precio_carro= int(input('a cuanto vendio los carros?  '))

salario_mensual = 1000
comision_por_carro = 150
comision_precio_carro = 0.5

salario_total = salario_mensual + (150 * cantidad_carro_vendido ) + ((precio_carro*0.05)*cantidad_carro_vendido)

print (salario_total)

'''
'''
# con for primera opcion
cantidad_carro_vendido= int(input('cuantos carros vendio?  '))

salario_mensual = 1000
comision_por_carro = 150
comision_precio_porcarro = 0.05
total_comision = 0

for i in range(cantidad_carro_vendido):
    precio_carro= int(input('a cuanto vendio los carros?  '))
    total_comision += (precio_carro*0.05)+ comision_por_carro
total= salario_mensual + total_comision
print(total)

# segunda option

cantidad_carro_vendido= int(input('cuantos carros vendio?  '))

salario_mensual = 1000
comision_por_carro = 150
comision_precio_porcarro = 0.05

total_comision = 0

for i in range(cantidad_carro_vendido):
    precio_carro= int(input('a cuanto vendio los carros?  '))
    comision_por_carro_total = (precio_carro*0.05)+ comision_por_carro
    total_comision = total_comision + comision_por_carro_total
   
total= salario_mensual + total_comision
print(total)
'''

##  

carros_vendido= int(input('cuantos carros vendio? '))

saliorio_mensual = 1000 
comision_por_carro_vendido= 150
comision_valor_carro = 0.005

comision_total= 0

for i in range(carros_vendido):
    text = 'introduzca el valor del carro '+str(i +1) + ': '
    valor_carro = int(input(text))
    comision_total +=  (valor_carro*comision_valor_carro)+ comision_por_carro_vendido
total_sueldo = comision_total + saliorio_mensual
print (total_sueldo)




     


