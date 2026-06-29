import random
import string

print("======================================")
print(" GENERADOR SEGURO DE CONTRASEÑAS")
print("======================================")

while True:

    # Solicitar longitud
    longitud = int(input("Ingrese la longitud de la contraseña (1-100): "))

    # Validar longitud
    if longitud >= 1 and longitud <= 100:

        # Caracteres permitidos
        caracteres = string.ascii_letters + string.digits

        # Generar contraseña
        contraseña = ""

        for i in range(longitud):
            contraseña += random.choice(caracteres)

        # Mostrar contraseña
        print("\nContraseña generada:", contraseña)

    else:
        print("\nError: La longitud debe estar entre 1 y 100.")
        continue

    # Preguntar si desea generar otra contraseña
    respuesta = input("\n¿Desea generar otra contraseña? (S/N): ")

    if respuesta.upper() != "S":
        print("\nGracias por utilizar el Generador Seguro de Contraseñas.")
        break