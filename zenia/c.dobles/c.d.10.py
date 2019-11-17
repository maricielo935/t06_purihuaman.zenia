import os
#INPUT
frecuencia= float(os.sys.argv[1])

#PROCESSING
velocidad_angular= 2*frecuencia

#vVALIDADOR
validador_de_la_velocidad_angular=(velocidad_angular<10)

#OUTPUT
print("#################################################")
print("################## VELOCIDAD ANGULAR ############")
print("#################################################")
print("############# frecuencia:", frecuencia,"############")
print("############ velocidad angular:", velocidad_angular,"###########")
print("#################################################")

#CONDICION DOBBLE

#si el validador de la velocidad angular da 20 vueltas en un min mostrar ventilador en buen estado
if ( validador_de_la_velocidad_angular==True ):
    print("Ventilador excelente")

else:
    print("ventilador inservible")

#fin_if
