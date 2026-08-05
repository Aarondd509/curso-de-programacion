print("🏝️ ¡BIENVENIDO A LA AVENTURA DE LA ISLA DESIERTA! 🏝️")
print("--------------------------------------------------")

# Nivel 1 (2 opciones)
p1 = input("Despiertas en una playa. ¿Quieres explorar la SELVA o la COSTA?: ")
# --- CAMINO DE LA SELVA ---
if p1 == "selva":
    print("Entras a la selva espesa y encuentras una enorme cueva oscura.")
    
    # Nivel 2 (Más de 2 opciones - 1)
    p2 = input("¿Qué haces? ¿ENTRAR a la cueva, RODEAR la cueva o VOLVER a la playa?: ")
    
    if p2 == "entrar":
        print("Dentro de la cueva encuentras un viejo baúl de pirata.")
        
        # Nivel 3 (Más de 2 opciones - 2)
        p3 = input("¿Cómo abres el baúl? ¿FUEGO, LLAVE o ROMPER?: ")
        
        if p3 == "fuego":
            print("El baúl tenía pólvora y explota. Fin del juego. 💥")
        elif p3 == "llave":
            print("¡El baúl se abre! Encuentras un mapa antiguo.")
            
            # Nivel 4 (2 opciones)
            p4 = input("El mapa marca dos rutas. ¿Vas al NORTE o al SUR?: ")
            if p4 == "norte":
                print("Al norte encuentras un helicóptero de rescate. ¡Ganaste! 🚁")
            elif p4 == "sur":
                print("Al sur caes en un pozo de arenas movedizas. Fin del juego. ⏳")
            else:
                print("Opción inválida. Te perdiste en la cueva.")
                
        elif p3 == "romper":
            print("Rompes el baúl, pero rompes también las pociones de valor que había dentro. Fin.")
        else:
            print("Opción inválida. El baúl desapareció.")

    elif p2 == "rodear":
        print("Al rodear la cueva encuentras un árbol con frutas exóticas.")
        
        # Nivel 5 (Más de 2 opciones - 3)
        p5 = input("Ves tres frutas. ¿Comes la ROJA, la AMARILLA o la VERDE?: ").strip().lower()
        
        if p5 == "roja":
            print("La fruta roja era venenosa. Fin del juego. ☠️")
        elif p5 == "amarilla":
            print("La fruta amarilla te da super fuerza para construir una balsa gigante y escapar. ¡Ganaste! ⛵")
        elif p5 == "verde":
            print("La fruta verde te duerme por cien años. Fin.")
        else:
            print("Opción inválida. Te moriste de hambre.")
            
    elif p2 == "volver":
        print("Regresas a la playa, pero un jaguar te embosca en el camino. Fin.")
    else:
        print("Opción inválida. Un coco te cayó en la cabeza.")

# --- CAMINO DE LA COSTA ---
elif p1 == "costa":
    print("Caminas por la orilla y encuentras un bote abandonado con herramientas.")
    
    # Nivel 6 (2 opciones)
    p6 = input("¿Prefieres REPARAR el bote o SEGUIR caminando por la arena?: ")
    
    if p6 == "reparar":
        print("Reparas el bote con éxito y navegas hacia el mar abierto.")
        
        # Nivel 7 (Más de 2 opciones - 4)strip
        p7 = input("Ves tres islas a lo lejos. ¿Viajas a la isla A, isla B o isla C?: ")
        
        if p7 == "isla a":
            print("La isla A está habitada por caníbales. Fin del juego. 🍖")
        elif p7 == "isla b":
            print("La isla B es un puerto comercial con barcos que te llevan a casa. ¡Ganaste! 🚢")
        elif p7 == "isla c":
            print("La isla C es solo un volcán activo que entra en erupción. Fin.")
        else:
            print("Opción inválida. El bote se hundió por no elegir un rumbo.")
            
    elif p6 == "seguir":
        print("Más adelante en la playa, encuentras a un anciano nativo pescando.")
        
        # Nivel 8 (Más de 2 opciones - 5)
        p8 = input("¿Qué le dices? ¿SALUDAR, ROBAR su caña o IGNORAR al anciano?: ")
        
        if p8 == "saludar":
            print("El anciano es amable y te ofrece comida en su cabaña.")
            
            # Nivel 9 (2 opciones)
            p9 = input("Te ofrece sopa de pescado. ¿Aceptas COMER o prefieres RECHAZAR?: ")
            if p9 == "comer":
                print("La sopa te da energía y el anciano te revela el camino secreto de salida. ¡Ganaste! 🗺️")
            elif p9 == "rechazar":
                print("El anciano se ofende y te echa de su cabaña bajo la tormenta. Fin.")
            else:
                print("Opción inválida. El anciano se cansó de esperar.")
                
        elif p8 == "robar":
            print("El anciano resulta ser un maestro de artes marciales y te derrota. Fin.")
            
        elif p8 == "ignorar":
            print("Lo ignoras y sigues caminando solo hasta que cae la noche.")
            
            # Nivel 10 (Más de 2 opciones - 6)
            p10 = input("Tienes frío. ¿Qué haces? ¿CANTAR, DORMIR oBUSCAR leña?: ")
            
            if p10 == "cantar":
                print("Tus cantos atraen a los lobos de la isla. Fin.")
            elif p10 == "dormir":
                print("Mueres de hipotermia por el frío de la noche. Fin.")
            elif p10 == "buscar":
                print("Encuentras leña, haces una fogata y un barco ve tu señal de humo. ¡Salvado! 🛳️🔥")
            else:
                print("Opción inválida. El frío terminó contigo.")
        else:
            print("Opción inválida. El anciano se marchó.")
    else:
        print("Opción inválida. Te arrastró una ola.")

else:
    print("Opción inválida. Te quedaste parado y te quemó el sol. Fin del juego.")

print("--------------------------------------------------")
print("🎮 ¡Fin de la partida! Gracias por jugar. 🎮")