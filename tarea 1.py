numero = 0
while numero <=0:
    numero = int(input("Introduce un numero entero positivo: "))
    if numero <= 0:
        print("El numero debe ser mayor que cero. Intenta de nuevo.")

suma_pares = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        suma_pares += i

print(f"La suma de los numeros pares desde 1 hasta {numero} es: {suma_pares}")