# 13.un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: 
# si trabaja 40 horas o menos se le paga $16 por hora. Si trabaja más de 40 horas se le paga $16 poe 
# cada una de las primeras 40 horas y $ 20 por cada hora extra.

horas_trabajo = int(input('cuantas horas trabajo? '))
horas_precio_hasta40 = 16
hora_extra = 20 

if horas_trabajo <= 40:
    sueldo = horas_trabajo * horas_precio_hasta40
    print('su sueldo es: ', sueldo)
else:
    horas_trabajo2 = horas_trabajo-40
    suledo2 = horas_trabajo2 * hora_extra
    sueldo_final = (40*horas_precio_hasta40) +suledo2
    print('su sueldo es: ', sueldo_final)


