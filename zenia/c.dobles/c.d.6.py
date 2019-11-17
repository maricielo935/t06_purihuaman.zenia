import os
#INPUT
alumno=os.sys.argv[1]
tesorera=os.sys.argv[2]
cursos=int(os.sys.argv[3])
precio_por_cada_curso=int(os.sys.argv[4])

#PROCESSING
pago_total=(cursos*precio_por_cada_curso)

#VALIDADOR
validador_del_pago_total=(pago_total<60)

#OUTPUT
print("#####################################################################################")
print("################# BOLETA DE PAGO ####################################################")
print("########### alumno:" , alumno , "####################################################")
print("########### tesorera:" , tesorera , "################################################")
print("########### cursos", cursos , "######################################################")
print("########### precio por cada curso: s/.", precio_por_cada_curso, "####################")
print("#####################################################################################")
print("###### pago total:", pago_total , "##################################################")
print("#####################################################################################")

#CONDICION DOBLE
#si el alumno logra pagar los cursos mostrar alumno responsables
if (validador_del_pago_total==True):
    print("Alumno responsable")

else:
    print("Alumno irresponsable")

#fin_if
