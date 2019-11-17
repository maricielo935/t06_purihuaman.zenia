import os
#BOLETA DE LA BOTICA SBCH
#declaracion de variables
cliente,producto,laboratorio,cantidad,precio="","","",0,0.0

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
laboratorio=os.sys.argv[3]
cantidad=int(os.sys.argv[4])
precio=float(os.sys.argv[5])

#PROCESSING
monto_final=(precio*cantidad)

#VERIFICADOR
puntos_bonus=(monto_final>40)

#OUTPUT
print("##############################################")
print("#BOTICA SOCIEDAD DE BENEFICIENCIA DE CHICLAYO#")
print("##############################################")
print(" #  Cliente       :  ",  cliente)
print(" #  Producto      :  ",  producto)
print(" #  Laboratorio   :  ",  laboratorio)
print(" #  Cantidad      :  ",  cantidad)
print(" #  Precio        :  ",  precio)
print(" #  Subtotal      :  ",  monto_final)
print("##############################################")

#Condicion multiple
#SI el monto final es mayor a 40, mostrarle Gano 10 puntos bonus
if ( puntos_bonus==True):
    print("Gano 10 puntos Bonus, que puede utilizar en su proxima compra.")
#fin_if
if ( puntos_bonus<40):
    print("Gano 5 puntos Bonus, que puede utilizar en su proxima compra.")
#fin_if
