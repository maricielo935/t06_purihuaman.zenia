import os
#INPUT
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
kg_de_manzanas=int(os.sys.argv[3])
precio_por_cada_kg_de_manzana=float(os.sys.argv[4])

#PROCESSING
pago_total=(kg_de_manzanas*precio_por_cada_kg_de_manzana)

#VALIDADOR
comprador_moderado=(pago_total<=16)

#OUTPUT
print("#############################################################################################")
print("################# BOLETA DE COMPRA ##########################################################")
print("########### cliente:" , cliente , "##########################################################")
print("########### cajero:" , cajero , "############################################################")
print("########### kd de manzanas", kg_de_manzanas , "##############################################")
print("########### precio por cada kg de manzana: s/.", precio_por_cada_kg_de_manzana, "############")
print("#############################################################################################")
print("###### pago total:", pago_total , "##########################################################")
print("#############################################################################################")

#CONDICION SIMPLE
#si el comprador es moderado mostrar un premio al pagar
if (comprador_moderado==True):
    print("FELICIDADES")
#fin_if
