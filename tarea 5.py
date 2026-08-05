saldo = 5000
opcion = 0

while opcion != 3:
    print("Bienvenido al cajero automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print(f"Su saldo actual es: ${saldo}")

    elif opcion == 2:
        monto = 0

        while monto <= 0 or monto % 100 != 0:
            monto = int(input("¿Cuánto quiere retirar? (múltiplo de 100): "))
            if monto <= 0 or monto % 100 != 0:
                print("Monto inválido. Debe ser un múltiplo de 100 y mayor que cero.")

        if monto <= saldo:
            saldo -= monto
            cantidad_billetes = monto // 100
            for i in range(cantidad_billetes):
                print("Entregando billete de $100")
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
        else:
            print("Error: Saldo insuficiente.")

    elif opcion == 3:
        print("Gracias por usar el cajero automático.")     

    else: 
        print("Opción inválida. Por favor, seleccione una opción válida.")