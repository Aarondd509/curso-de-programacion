jugar = "si"

while jugar == "si":
    numero_secreto = 7

    print("Adivina el número secreto entre 1 y 10. Tienes 3 intentos.")

    for intento in range(3):
        intento_usuario = int(input("Introduce el número: "))

        if intento_usuario == numero_secreto:
            print("¡Felicidades! Has adivinado el número secreto.")
            break
        elif intento_usuario < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

        jugar = input("¿Quieres jugar de nuevo? (si/no): ")

    print("Gracias por jugar.")