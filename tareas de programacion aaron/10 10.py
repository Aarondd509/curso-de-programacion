dividiendo = int(input("Introduce un número para dividir: "))
divisor = int(input("Introduce el divisor: "))

if divisor == 0:
    print("Error: El divisor no puede ser cero.")
else:
    resultado = dividiendo / divisor
    print(f"El resultado de {dividiendo} dividido por {divisor} es: {resultado}")