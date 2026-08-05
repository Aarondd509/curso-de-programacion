num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

operacion = input("Introduce la operación a realizar (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")

else:
    print("Operación no válida. Por favor, introduce una operación correcta (+, -, *, /).")    