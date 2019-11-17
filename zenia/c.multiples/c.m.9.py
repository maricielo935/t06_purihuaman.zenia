import os
#INPUT
fuerza=int(os.sys.argv[1])
distancia=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

#PROCESSING
potencia=(fuerza*distancia)/tiempo

#VALIDADOR
validador_de_la_potencia=(potencia>=56)

#OUTPUT
print("##################################################################################")
print("##########  FORMULA DE LA POTENCIA ###############################################")
print("##################################################################################")
print("############ fuerza:", fuerza , "#################################################")
print("############ distancia", distancia , "############################################")
print("############ tiempo", tiempo , "##################################################")
print("##################################################################################")
print("############### potencia", potencia , "###########################################")
print("##################################################################################")

#CONDICION SIMPLE
if ( validador_de_la_potencia>50 and validador_de_la_potencia>56 ):
    print("MAQUINA EFICAZ")
#fin_if

if ( validador_de_la_potencia<50 and validador_de_la_potencia<40 ):
    print("MAQUINA EN MAL ESTADO")
#fin_if
