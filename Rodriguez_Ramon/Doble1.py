#PROGRAMA_01
import os
producto_1,cant_1="",0

#INPUT VIA OS
producto_1=os.sys.argv[1]
cant_1=int(os.sys.argv[2])

#PROCESSING
#Si el numero de producto supera 180, mostrar "Calidad de algodon"
#Caso contrario mostar "Mala calidad"
if(cant_1 > 180 ):
    print(producto_1, "Calidad de algodon")
else:
    print(producto_1,"Mala calidad")
#fin_if
