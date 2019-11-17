import os
#AREA DE UN TERRENO
#Declaracion de variables
largo,ancho,area=0,0,0

#INPUT
largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])

#PROCESSING
area=largo*ancho

#VERIFICADOR
area_para_sembrar=(area<120)

#OUTPUT
print("############################")
print("#   AREA  DE  UN  TERRENO  #")
print("############################")
print(" #  Largo      :  ",  largo, "metros")
print(" #  Ancho      :  ",  ancho, "metros")
print(" #  Area       :  ",  area , "metros cuadrados")
print("############################")

#Condicion simple
#SI el  area para sembrar es menor a 120, mostrarle Esta area esta adecuada para sembrar
if ( area_para_sembrar==True):
    print("Esta area esta adecuada para sembrar.")
#fin_if
