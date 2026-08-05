cantidad = 0
while cantidad < 5: 
    cantidad = int(input("cuantos numeros quieres ingresar?"))
    if cantidad < 5:
        print("debes ingresar al menos 5 numeros")

positivos = 0
negativos = 0
ceros = 0

for i in range(cantidad):
    numero = int(input(f"Ingresa un número"))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")