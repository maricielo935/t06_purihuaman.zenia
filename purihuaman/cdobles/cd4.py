import os
#EXCESO DE VELOCIDAD
#Declaracion de variables
velocidad_inicial,tiempo,aceleracion,velocidad_final=0,0,0,0

#INPUT
velocidad_inicial=float(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
aceleracion=int(os.sys.argv[3])

#PROCESSING
velocidad_final=velocidad_inicial+(aceleracion*tiempo)

#VERIFICADOR
exceso_de_velocidad=(velocidad_final>70)

#OUTPUT
print("##############################################")
print("#          EXCESO   DE   VELOCIDAD           #")
print("##############################################")
print(" #  Velocidad inicial  : ", velocidad_inicial, "m/s")
print(" #  Tiempo             : ", tiempo, "s")
print(" #  Aceleracion        : ", aceleracion, "m/s°")
print(" #  Velocidad final    : ", velocidad_final, "m/s")
print("##############################################")

#Condicion doble
#SI la velocidad es mayor a 70, mostrarle Exceso de Velocidad
if ( exceso_de_velocidad==True):
    print("EXCESO DE VELOCIDAD.")
#fin_if
else:
    print("Va demasiado rapido.")
#fin_else
