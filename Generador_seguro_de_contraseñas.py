import random
import string

print("GENERADOR SEGURO DE CONTRASEÑAS")

longitud = int(input("Ingrese la longitud de la contraseña (1-100): "))

if longitud >= 1 and longitud <= 100:

    caracteres = string.ascii_letters + string.digits

    contraseña = ""

    for i in range(longitud):
        contraseña += random.choice(caracteres)

    print("Contraseña generada:", contraseña)

else:
    print("Error: La longitud debe estar entre 1 y 100.")
    