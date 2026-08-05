temperatura = float(input("Introduce la temperatura en grados Celsius: "))

if temperatura >= 30:
    print(f"La temperatura es de {temperatura}°C, hace calor.")
elif temperatura >= 20:
    print(f"La temperatura es de {temperatura}°C, hace una temperatura agradable.")
else:
    print(f"La temperatura es de {temperatura}°C, hace frío.")