import os
#INPUT
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])
generatriz=float(os.sys.argv[3])

#PROCESSING
area=(pi*radio*generatriz)

#VALIDADOR
validador_del_area=(area>=60)

#OUTPUT
print("##############################################")
print("# AREA TOTAL DE UN CONO")
print("##############################################")
print("#")
print("############pi:", pi , "######################")
print("############radio", radio , "#################")
print("###########generatriz", generatriz , "########")
print("###############area del cono", area , "#######")
print("##############################################")

#CONDICION SIMPLE
if ( validador_del_area==False ):
    print("AREA DEL CONO ")
#fin_if
