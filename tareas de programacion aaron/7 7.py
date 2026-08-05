numero1 = float(input("introduce el primer numero: "))
numero2 = float(input("introduce otro numero: "))

if numero1 > numero2: 
    print(f"El primer numero ({numero1}) es el mayor. ")
elif numero1 < numero2: 
    print("El segundo numero ({numero2}) es el mayor. ")
elif numero1 == numero2: 
    print(f"Los numeros son iguales ({numero1}) y ({numero2}). ")

