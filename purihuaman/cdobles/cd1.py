import os
#BOLETA DE NOTAS
#declaracion de variables
nota1,nota2,nota3,nota4=0,0,0,0

#INPUT
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
nota4=int(os.sys.argv[4])

#PROCESSING
promedio_final=(nota1+nota2+nota3+nota4)/4

#VERIFICADOR
aprobar=(promedio_final>=11)

#OUTPUT
print("#####################################")
print("#  BOLETA   DE   NOTAS  DE  FISICA  #")
print("#####################################")
print("  # Nota 1        :  ", nota1)
print("  # Nota 2        :  ", nota2)
print("  # Nota 3        :  ", nota3)
print("  # Nota 4        :  ", nota4)
print("  #Promedio final :  ", promedio_final)
print("#####################################")

#Condicion doble
#SI el promedio es mayor o igual 11, mostrarle Aprobado
if ( aprobar==True):
    print("Curso Aprobado")
#fin_if
else:
    print("Sigue esforzandote")
#fin_else
