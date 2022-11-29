# la calificacion final de un estudiante de informatica se calcula con base a las calificaciones de 4 aspectos
# de su rendimiento academico: participacion, primer examen parcial, segundo examen parcial y examen final.
#  Sabiendo que las calificaciones anteriores entran a la calificacion final con ponderaciones 
# del 10%, 25%, 25% y 40 %,  hacer un programa que calcule e imprima la calificacion final obtenida 
# por un estudiante.

nota_participacion =  (float(input('Introducir la nota de participacion')))*0.1
primer_parcial = (float(input('Introducir la nota primer parcial')))*0.25
segundo_parcial = (float(input('Introducir la nota segundo_parcial')))*0.25
examen_final = (float(input('Introducir la nota examen final')))*0.4

calificacion_final = nota_participacion + primer_parcial+segundo_parcial + examen_final
print(calificacion_final)
