# 7.Construir un programa que, dado un numero total de horas, devuelve el numero de semanas, 
# días y horas equivalentes. Por ejemplo, dado un total de 1000 horas debe mostrar 5 semanas, 6 días y 16 horas

import math


horas = int(input('introducir numero total de horas'))

semanas = horas /(24 *7) 
semana_entera = math.trunc(semanas) 
semana_decimal =  semanas -semana_entera
dias = semana_decimal * 7
dia_entera = math.trunc(dias)
dia_decimal = dias-dia_entera
horas = dia_decimal * 24
hora_entero = math.trunc(horas)

print('son : ', semana_entera ,'semanas', 'y',dia_entera, 'dias',  'y', hora_entero, 'horas' )
