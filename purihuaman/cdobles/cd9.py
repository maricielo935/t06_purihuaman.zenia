import os
#CREACION DE CUENTA EN FACEBOOK
#Declaracion de variables
nombre,apellido_paterno,apellido_materno,anio_nacimiento,edad,correo,sexo,contraseña="","","",0,0,"","",""

#INPUT
nombre=os.sys.argv[1]
apellido_paterno=os.sys.argv[2]
apellido_materno=os.sys.argv[3]
anio_nacimiento=int(os.sys.argv[4])
edad=int(os.sys.argv[5])
correo=os.sys.argv[6]
sexo=os.sys.argv[7]
contraseña=os.sys.argv[8]


#VERIFICADOR
cuenta_creada=(edad>18)

#OUTPUT
print("###################################")
print("# CREACION DE CUENTA  EN FACEBOOK #")
print("###################################")
print(" # Nombre            :", nombre)
print(" # Apellido paterno  :", apellido_paterno)
print(" # Apellido materno  :", apellido_materno)
print(" # Anio de nacimiento:", anio_nacimiento)
print(" # Edad              :", edad)
print(" # Correo            :", correo)
print(" # Sexo              :", sexo)
print(" # Contrasenia       :", contraseña)
print("###################################")

#Condicion doble
#SI la persona tiene mas de 18 anios , mostrarle YA CUENTA CON CUENTA DE FACEBOOK
if ( cuenta_creada==True):
    print("YA CUENTA CON CUENTA DE FACEBOOK.")
#fin_if
else:
    print("Cuenta creada")
#fin_else
