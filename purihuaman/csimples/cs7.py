import os
#PRESENTACION DE EJERCICIOS EN MATEMATICA BASICA
#Declaracion de variables
alumno,nro_de_ejercicios,puntos_por_ejercicio="",0,0

#INPUT
alumno=os.sys.argv[1]
nro_de_ejercicios=int(os.sys.argv[2])
puntos_por_ejercicio=int(os.sys.argv[3])

#PROCESSING
nota=(nro_de_ejercicios*puntos_por_ejercicio)

#VERIFICADOR
aprobar=(nota>=11)

#OUTPUT
print("#################################################")
print("#PRESENTACION DE EJERCICIOS EN MATEMATICA BASICA#")
print("#################################################")
print(" #  Alumno                    :", alumno)
print(" #  N° de ejercicios resueltos:", nro_de_ejercicios)
print(" #  Puntos por ejercicio      :", puntos_por_ejercicio, "puntos")
print(" #  Nota                      :", nota)
print("#################################################")

#Condicion simple
#SI la nota es igual o mayor a 11 , mostrarle Aprobo Matematica Basica
if ( aprobar==True):
    print("Aprobo Matematica Basica.")
#fin_if
