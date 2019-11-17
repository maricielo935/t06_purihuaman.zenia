import os
#INPUT
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
cemento=int(os.sys.argv[3])
precio_por_cada_cemento=float(os.sys.argv[4])

#PROCESSING
compra_total=(cemento*precio_por_cada_cemento)
IGV=(compra_total*0.18)
pago_total=(compra_total+IGV)

#VALIDADOR
validador_del_pago_total=(pago_total>=50)

#OUTPUT
print("#############################################################################################")
print("################# BOLETA DE VENTA ###########################################################")
print("########### cliente:" , cliente , "##########################################################")
print("########### cajero:" , cajero , "############################################################")
print("########### cemento", cemento , "############################################################")
print("########### precio por cada cemento: s/.", precio_por_cada_cemento, "########################")
print("#############################################################################################")
print("###### compra total:", compra_total , "######################################################")
print("###### IGV:", IGV , "########################################################################")
print("#############################################################################################")
print("###### pago total:", pago_total , "##########################################################")
print("#############################################################################################")

#CONDICION MULTIPLE
if ( validador_del_pago_total<80 and validador_del_pago_total<70 ):
    print("GRACIAS POR SU COMPRA")
#fin_if

if ( validador_del_pago_total<20 and validador_del_pago_total<15):
    print("REGRESE PRONTO")
#fin_if
