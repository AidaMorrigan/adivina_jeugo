import getpass
import estadisticas

# Pedir el numero secreto que no se muestra y comprueba que está en el rango
def pedir_numero_secreto():
    """Solicita al jugador 1 que introduzca un número secreto dentro del rango permitido."""
    while True:
        try:
            numero_secreto = int(getpass.getpass("Introduce el número secreto entre 1 y 1000: "))
            if 1 <= numero_secreto <= 1000:
                return numero_secreto
            else:
                print("Número fuera de rango. Debe estar entre 1 y 1000.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

# Funcion que entra en el bucle del numero a adivinar
def adivinar_numero(numero_secreto, intentos_maximos):
    """Permite al jugador 2 intentar adivinar el número secreto."""
    intentos_realizados = 0
    while intentos_realizados < intentos_maximos:
        try:
            intento = int(input(f"Intento {intentos_realizados + 1} de {intentos_maximos}: "))
            intentos_realizados += 1

            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
                return True, intentos_realizados
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return False, intentos_realizados


def partida_dos_jugadores(intentos_maximos):
    """Función principal para el modo de juego de dos jugadores."""
    print("\nEstás jugando al Modo dos jugadores.")

    # Jugador 1 define el número secreto
    jugador_uno = input("\nJugador 1, introduce tu nombre: ")
    numero_secreto = pedir_numero_secreto()

    # Jugador 2 intenta adivinar
    nombre_jugador = input("\nJugador 2, introduce tu nombre: ")
    print(f"{nombre_jugador}, intenta adivinar el número secreto entre 1 y 1000.\n")

    # Adivinanza por Jugador 2
    ganada, intentos_realizados = adivinar_numero(numero_secreto, intentos_maximos)

    # Registrar resultado en las estadísticas
    estadisticas.registrar_resultado(
        nombre_jugador,
        ganada=ganada,
        dificultad=intentos_maximos,
        intentos=intentos_realizados
    )

    # Mensaje final según el resultado
    if not ganada:
        print(f"Lo siento, {nombre_jugador}, has perdido. El número era {numero_secreto}.")

    return nombre_jugador

