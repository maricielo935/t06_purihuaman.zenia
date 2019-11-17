import os
#PREMIO POR COMPRAS EN PLAZA VEA
#Declaracion de variables
cliente,producto,cantidad,precio_producto="","",0,0.0

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cantidad=int(os.sys.argv[3])
precio_producto=float(os.sys.argv[4])

#PROCESSING
monto=(cantidad*precio_producto)

#VERIFICADOR
monto=(monto>50)

#OUTPUT
print("###################################")
print("# PREMIO POR COMPRAS EN PLAZA VEA #")
print("###################################")
print(" # Cliente          :", cliente)
print(" # Producto         :", producto)
print(" # Precio por unidad:", precio_producto,"soles")
print(" # Cantidad         :", cantidad,"unidades")
print("###################################")

#Condicion doble
#SI el monto resulta mayor a 5o soles , mostrarle Gano un descuento del 50% en Hamburgesas BEMBOS
if ( monto==True):
    print("Gano un descuento del 50% en Hamburgesas BEMBOS.")
#fin_if
else:
    print("DISFRUTA LA OFERTA Y VUELVA A COMPRAR.")
#fin_else
