import os
#DERECHO A SUFRAGIO
#declaracion de variables
nombre,apellidos,ano_de_naciemiento,ano_actual="","",0,0

#INPUT
nombre=os.sys.argv[1]
apellidos=os.sys.argv[2]
ano_de_naciemiento=int(os.sys.argv[3])
ano_actual=int(os.sys.argv[4])

#PROCESSING
edad=(ano_actual-ano_de_naciemiento)

#VERIFICADOR
derecho_a_sufragio=(edad>18)

#OUTPUT
print("#########################################")
print("#         DERECHO  A  SUFRAGIO          #")
print("#########################################")
print(" #Nombre           : ", nombre)
print(" #Apellidos        : ", apellidos)
print(" #Ano de nacimiento: ", ano_de_naciemiento)
print(" #Ano actual       : ", ano_actual  )
print(" #Edad             : ", edad)
print("#########################################")

#Condicion doble
#SI la edad es mayor a 18, mostrarle Tiene derecho a sufragio
if ( derecho_a_sufragio==True):
    print("Ya puede sufragiar.")
#fin_if
else:
    print("Ya puede elegir a las autoridades politicas")
#fin_else
