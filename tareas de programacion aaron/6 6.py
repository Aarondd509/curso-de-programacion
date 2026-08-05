nota = float(input("Introduce la nota del estudiante: (0 a 100): "))

if nota >= 60:
    print(f"El estudiante obtuvo una A con una nota de {nota}")
    print("¡Felicidades! Has aprobado el curso.")
else: 
    print("¡Que mal! Has reprobado el curso.")