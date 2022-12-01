# 18.	Pedir el dia , mes y año de una fecha e indicar si la fecha es correcta.
#  con meses de 28,30 y 31 días. sin años bisiestos.

dia, mes, año = map(int,input('introducir una fecha con formato dia/mes/año: ').split('/'))


if mes==1 or mes==3 or mes==5 or mes==7 or mes ==8 or mes==10 or mes==12:
    if (dia<=31):
        if(año>0):
            print(f"la fecha: {dia}/{mes}/{año} es correcta.")
elif mes==4 or mes==6 or mes==9 or mes==11:
    if (dia<=30):
        if(año>0):
            print(f"la fecha: {dia}/{mes}/{año} es correcta.")
elif mes==2:
    if(dia<=28):
        if(año>0):
            print(f"la fecha: {dia}/{mes}/{año} es correcta.")
else:
    print('la fecha es incorrecta')




    
  