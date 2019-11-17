import os
#INPUT
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])
generatriz=float(os.sys.argv[3])

#PROCESSING
area=(2*pi*radio*generatriz)

#VALIDADORES
validador_area=(area<40)

#OUTPUT
print("###########################################################")
print("# AREA TOTAL DE UN CILINDRO################################")
print("###########################################################")
print("############pi:", pi , "###################################")
print("############radio", radio , "##############################")
print("###########generatriz", generatriz , "#####################")
print("###########################################################")
print("###############area del cilindro", area , "################")
print("###########################################################")

#CONDICION SIMPLE
#si el validador area es mayor a 20  mostrar la nota aprovatoria
if ( validador_area==False ):
    print("APROBASTE EL CURSO")
#fin_if
