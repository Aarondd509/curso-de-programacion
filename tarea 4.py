palabra = ""
while palabra != "":
    palabra = input("Introduce una palabra: ")
    if palabra == "":
     print("Has introducido una palabra vacía.")

vocales = "aeiouAEIOU"

print("resultados de la transformacion: ")

for posicion, letra in enumerate(palabra):
    if letra in vocales:

       valor = posicion * 3
else:
       valor = posicion // 2

print(f"Letra: {letra}, Posición original: {posicion}, Valor final: {valor}")
