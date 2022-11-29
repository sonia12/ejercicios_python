# 17.Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta. 
# suponiendo que todos los meses son de 30 días

dia = int(input('introduzca un dia'))
mes = int(input('introduzca un mes'))
año = int(input('introduzca un año'))

if dia <= 30:

    if mes <= 12:
     
        if año > 0:
            print('la fecha es correcta')
else:
    print('la fecha es incorrecta')


