import os
#INPUT
masa=int(os.sys.argv[1])
calor_especifico=float(os.sys.argv[2])
variacion_de_la_temperatura=int(os.sys.argv[3])

#PROCESSING
calor=(masa*calor_especifico*variacion_de_la_temperatura)

#VALIDADOR
validador_del_calor=(calor<=120)

#OUTPUT
print("##################################################################################")
print("##########  FORMULA DEL CALOR ####################################################")
print("##################################################################################")
print("############ masa:", masa , "#####################################################")
print("############ calor especifico", calor_especifico , "##############################")
print("############ variacion de la temperatura", variacion_de_la_temperatura , "########")
print("##################################################################################")
print("############### calor", calor , "#################################################")
print("##################################################################################")

#CONDICION MULTIPLE
if ( validador_del_calor>=100 and validador_del_calor>101  ):
    print("PUNTO DE EBULLICION")
#fin_if

if ( validador_del_calor<1 and validador_del_calor==0)
    print("PUNTO DE FUSION")
#fin_if
