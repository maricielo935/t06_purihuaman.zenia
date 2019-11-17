import os
#PREMIO POR NUMERO DE ETIQUETAS DE LECHE GLORIA
#Declaracion de variables
nombre,apellidos,nro_etiquetas="","",0

#INPUT
nombre=os.sys.argv[1]
apellidos=os.sys.argv[2]
nro_etiquetas=int(os.sys.argv[3])

#VERIFICADOR
reclamar_premio=(nro_etiquetas>10)

#OUTPUT
print("############################################")
print("#PREMIO POR N° DE ETIQUETAS DE LECHE GLORIA#")
print("############################################")
print(" # Nombre        :", nombre)
print(" # Apellidos     :", apellidos)
print(" # N°de etiquetas:", nro_etiquetas)
print("############################################")

#Condicion doble
#SI la persona logro juntar mas de 10 etiquetas , mostrarle RECLAMAR 3 TARROS DE LECHE GLORIA GRATIS
if ( reclamar_premio==True):
    print("RECLAMAR 3 TARROS DE LECHE GLORIA GRATIS.")
#fin_if
else:
    print("Sigue intentando")
#fin_else
