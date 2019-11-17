import os
#INPUT
masa=int(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
altura=int(os.sys.argv[3])

#PROCESSING
energia_potencial=(masa*gravedad*altura)

#VALIDADOR
validador_energia_potencial=(energia_potencia>160)

#OUTPUT
print("#######################################################################################")
print("##########  FORMULA DE LA ENERGIA POTENCIAL ###########################################")
print("#######################################################################################")
print("############ masa:", masa , "##########################################################")
print("############ gravedad", gravedad , "###################################################")
print("############ altura", altura , "#######################################################")
print("#######################################################################################")
print("############ energia potencial ", energia_potencial , "################################")
print("#######################################################################################")

#CONDICION MULTIPLE
if ( validador_energia_potencial>=160 and validador_energia_potencial>150):
    print("ENERGIA NECESARIA")
#fin_if

if ( validador_energia_potencial<160 and validador_energia_potencial<150 ):
    print("FALTA DE ENERGIA")
#fin_if
