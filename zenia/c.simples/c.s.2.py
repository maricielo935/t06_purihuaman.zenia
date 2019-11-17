import os
#INPUT
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
pantalones=int(os.sys.argv[3])
precio_por_cada_pantalon=float(os.sys.argv[4])

#PROCESSING
compra_total=(pantalones*precio_por_cada_pantalon)
IGV=(compra_total*0.18)
pago_total=(compra_total+IGV)

#VALIDADOR
validador_del_pago_total=(pago_total<118)

#OUTPUT
print("#############################################################################################")
print("################# BOLETA DE VENTA ###########################################################")
print("########### cliente:" , cliente , "##########################################################")
print("########### cajero:" , cajero , "############################################################")
print("########### pantalones", pantalones , "######################################################")
print("########### precio por cada pantalon: s/.", precio_por_cada_pantalon, "######################")
print("#############################################################################################")
print("###### compra total:", compra_total , "######################################################")
print("###### IGV:", IGV , "########################################################################")
print("#############################################################################################")
print("###### pago total:", pago_total , "##########################################################")
print("#############################################################################################")

#CONDICION SIMPLE
#si el validador del pago total es superior a 200 soles, mostrarle gran comprador
if (validador_del_pago_total==False):
    print("REGRESE PRONTO GRAN COMPRADOR")
#fin_if
