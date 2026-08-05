compra = float(input("Introduce el precio de la compra: $"))

if compra >= 400:
    descuento = compra * 0.30                                   #se aplica un descuento del 30% si la compra es mayor o igual a $400
    total = compra - descuento                                  #se aplica el descuento al total de la compra (multiplicar por 0.30 y restar al total de la compra)
    print(f"El precio de la compra es: ${compra:.2f}")
    print(f"Se aplicó un descuento del 30%: ${descuento:.2f}")
    print(f"El total a pagar es: ${total:.2f}")

else:
    print(f"El precio de la compra es: ${compra:.2f}")
    print("No se aplicó ningún descuento.")
    print(f"El total a pagar es: ${compra:.2f}")    