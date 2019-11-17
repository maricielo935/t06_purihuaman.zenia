import os
#INPUT
fuerza=int(os.sys.argv[1])
distancia=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

#PROCESSING
potencia=(fuerza*distancia)/tiempo

#VALIDADOR
validador_de_la_potencia=(potencia<56)

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
#si la potencia es mayor que 20 mostrar maquina en buen estado
if ( validador_de_la_potencia ):
    print("MAQUINA EFICAZ")
#fin_if
