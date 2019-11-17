import os
#DIETA DE UNA PERSONA
#Declaracion de variables
nombre,peso_inicial,peso_final,tiempo="",0,0,0

#INPUT
nombre=os.sys.argv[1]
peso_inicial=float(os.sys.argv[2])
peso_final=float(os.sys.argv[3])
tiempo=int(os.sys.argv[4])

#PROCESSING
reduccion_de_peso=peso_inicial-peso_final

#VERIFICADOR
peso_luego_de_la_dieta=(reduccion_de_peso<8)

#OUTPUT
print("#################################")
print("#    DIETA  DE  UNA  PERSONA    #")
print("#################################")
print(" #  Nombre      :  ", nombre)
print(" #  Peso inicial:  ", peso_inicial, "kilos")
print(" #  Peso final  :  ", peso_final, "kilos")
print(" #  Tiempo      :  ", tiempo, "meses")
print(" #  Redujo      :  ", reduccion_de_peso,"kilos")
print("#################################")

#Condicion multiple
#SI el peso de la persona a reducido hasta menos de 8 kilos, mostrarle La dieta fue efectiva
if ( peso_luego_de_la_dieta==True):
    print("La dieta fue efectiva.")
#fin_if
if ( peso_luego_de_la_dieta>8):
    print("La dieta dio resultados favorables.")
#fin_if

