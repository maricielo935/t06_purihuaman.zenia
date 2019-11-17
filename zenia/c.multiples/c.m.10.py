import os
#INPUT
frecuencia= float(input("FRECUENCIA: "))

#PROCESSING
velocidad_angular= 2*frecuencia

#VALIDADOR
validador_de_la_velocidad_angular=(velocidad_angular<10)

#OUTPUT
print("#################################################")
print("################## VELOCIDAD ANGULAR ############")
print("#################################################")
print("############# frecuencia:", frecuencia,"############")
print("############ velocidad angular:", velocidad_angular,"###########")
print("#################################################")

#CONDICION MULTIPLE
if ( validador_de_la_velocidad_angular==True ):
    print("Ventilador excelente")
#fin_if

if ( validador_de_la_velocidad_angular)
