import unicodedata

def normalizar_texto(texto):
    """Elimina acentos y convierte el texto a minúsculas para evitar errores."""
    texto = texto.strip().lower()
    # Eliminar diacríticos (acentos)
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                    if unicodedata.category(c) != 'Mn')
    return texto

def obtener_opcion(mensaje, opciones_validas):
    """Muestra el mensaje, lee la opción y valida que esté en las opciones permitidas."""
    while True:
        print("\n" + mensaje)
        entrada = input("👉 Tu elección: ")
        entrada_limpia = normalizar_texto(entrada)
        
        if entrada_limpia in opciones_validas:
            return entrada_limpia
        else:
            print("🚧 Opción no válida. Escribe una de las palabras en MAYÚSCULAS indicadas.")

def iniciar_juego():
    print("=" * 60)
    print("🌲🌌 AVENTURA EN EL BOSQUE OSCURO 🌌🌲")
    print("=" * 60)
    
    # --- NIVEL 1 ---
    m1 = "Estás caminando por un bosque oscuro y encuentras dos objetos.\n¿Te quedas con el FÓSFORO o la LINTERNA?"
    op1 = obtener_opcion(m1, ["fosforo", "linterna"])
    
    if op1 == "fosforo":
        # --- NIVEL 2 (Ruta Fósforo) ---
        m2 = "Coges el fósforo y lo enciendes 🔥. ¡Ves un gran oso grizzly! El fósforo se apaga.\n¿Quieres CORRER o ESCONDERSE detrás de un árbol?"
        op2 = obtener_opcion(m2, ["correr", "esconderse"])
        
        if op2 == "correr":
            # --- NIVEL 4 (Más de 2 opciones) ---
            m4 = "Corres a ciegas y tropiezas con la entrada de una cueva subterránea.\n¿Qué haces? ¿ENTRAR a la cueva, ESCALAR una roca cercana o GRITAR por ayuda?"
            op4 = obtener_opcion(m4, ["entrar", "escalar", "gritar"])
            
            if op4 == "entrar":
                # --- NIVEL 6 ---
                m6 = "Dentro de la cueva encuentras un cofre antiguo con un candado magnético.\n¿Intentas ROMPER el candado o BUSCAR la llave en el suelo?"
                op6 = obtener_opcion(m6, ["romper", "buscar"])
                if op6 == "romper":
                    print("\n💥 ¡El cofre tenía una trampa de gas! Quedas atrapado. FIN DE LA AVENTURA.")
                else:
                    print("\n🔑 ¡Encuentras la llave! El cofre se abre lleno de oro. ¡VICTORIA!")
                    
            elif op4 == "escalar":
                # --- NIVEL 7 (Más de 2 opciones) ---
                m7 = "Desde lo alto de la roca divisas tres luces en el horizonte.\n¿Hacia dónde bajas? ¿Hacia la luz ROJA, la luz AZUL o la luz VERDE?"
                op7 = obtener_opcion(m7, ["roja", "azul", "verde"])
                if op7 == "roja":
                    print("\n🏡 Era la fogata de unos aldeanos amigables. ¡Estás a salvo! ¡VICTORIA!")
                elif op7 == "azul":
                    print("\n⚡ Era un fuego fatuo que te hechiza profundamente. FIN DE LA AVENTURA.")
                else:
                    print("\n🐊 Era el reflejo de los ojos de un caimán mutante en el pantano. FIN DE LA AVENTURA.")
                    
            else: # gritar
                print("\n🦁 Tus gritos atraen a una manada de lobos hambrientos. FIN DE LA AVENTURA.")
                
        else: # esconderse
            # --- NIVEL 5 (Más de 2 opciones) ---
            m5 = "Te escondes. El oso pasa de largo, pero dejas caer tu billetera al suelo.\n¿Qué haces ahora? ¿RECOGER la billetera, AVANZAR en silencio o VOLVER por donde viniste?"
            op5 = obtener_opcion(m5, ["recoger", "avanzar", "volver"])
            
            if op5 == "recoger":
                print("\n🐍 Al agacharte, una serpiente venenosa te muerde el brazo. FIN DE LA AVENTURA.")
            elif op5 == "avanzar":
                # --- NIVEL 8 ---
                m8 = "Llegas a un río caudaloso con un puente de madera viejo.\n¿Cruzas el PUENTE o decides NADAR por el río?"
                op8 = obtener_opcion(m8, ["puente", "nadar"])
                if op8 == "puente":
                    print("\n🎉 El puente resiste y al otro lado encuentras la carretera principal. ¡VICTORIA!")
                else:
                    print("\n🌊 La corriente es demasiado fuerte y te arrastra río abajo. FIN DE LA AVENTURA.")
            else: # volver
                print("\n🐻 Regresas directo a las garras del oso que había cambiado de rumbo. FIN DE LA AVENTURA.")
                
    else: # linterna
        # --- NIVEL 3 (Ruta Linterna) ---
        m3 = "Enciendes la linterna 💡 y ves un camino. Oyes un crujido extraño entre las ramas.\n¿Quieres SEGUIR el camino recto o BUSCAR entre los árboles el origen del ruido?"
        op3 = obtener_opcion(m3, ["seguir", "buscar"])
        
        if op3 == "seguir":
            # --- NIVEL 9 (Más de 2 opciones) ---
            m9 = "El camino te lleva ante un extraño monje encapuchado que custodia un portal mágico.\nTe pide que elijas un elemento: ¿FUEGO, AGUA o TIERRA?"
            op9 = obtener_opcion(m9, ["fuego", "agua", "tierra"])
            
            if op9 == "fuego":
                print("\n🔥 El portal te quema las manos y te expulsa del bosque desorientado. FIN DE LA AVENTURA.")
            elif op9 == "agua":
                # --- NIVEL 10 ---
                m10 = "El portal de agua te teletransporta a una isla flotante. Hay un mapa y una brújula.\n¿Santas usando el MAPA o confías en la BRÚJULA?"
                op10 = obtener_opcion(m10, ["mapa", "brujula"])
                if op10 == "mapa":
                    print("\n🗺️ El mapa te guía por un sendero invisible seguro hasta tu hogar. ¡VICTORIA!")
                else:
                    print("\n🧭 La brújula se vuelve loca por el magnetismo y caes al vacío. FIN DE LA AVENTURA.")
            else: # tierra
                print("\n🗿 Te conviertes en una estatua de piedra para decorar el jardín del monje. FIN DE LA AVENTURA.")
                
        else: # buscar
            # --- NIVEL 11 (Más de 2 opciones) ---
            m11 = "Al buscar, descubres un búnker militar abandonado con tres puertas de colores.\n¿Qué puerta abres? ¿La puerta BLANCA, la NEGRA o la DORADA?"
            op11 = obtener_opcion(m11, ["blanca", "negra", "dorada"])
            
            if op11 == "blanca":
                print("\n🌌 La puerta te lleva a una dimensión paralela sin salida. FIN DE LA AVENTURA.")
            elif op11 == "negra":
                # --- NIVEL 12 (Más de 2 opciones) ---
                m12 = "Dentro de la sala negra encuentras un panel de control con tres botones.\n¿Presionas el botón UNO, el DOS o el TRES?"
                op12 = obtener_opcion(m12, ["uno", "dos", "tres"])
                if op12 == "uno":
                    print("\n🚀 El búnker se transforma en una nave espacial y despegas. ¡VICTORIA INTERGALÁCTICA!")
                elif op12 == "dos":
                    print("\n🚨 Se activa el sistema de autodestrucción del búnker. FIN DE LA AVENTURA.")
                else:
                    print("\n🤖 Aparece un robot de limpieza que te saca a escobazos del bosque. ¡VICTORIA... extraña!")
            else: # dorada
                print("\n🦁 La habitación dorada era la jaula de un león hambriento. FIN DE LA AVENTURA.")

# Ejecutar el juego
if __name__ == "__main__":
    iniciar_juego()
    