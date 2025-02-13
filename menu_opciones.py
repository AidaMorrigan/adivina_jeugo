
"""Se muestra la elección de menu y dificultad y se comprueba que es váída"""

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Partida modo solitario")
    print("2. Partida 2 Jugadores")
    print("3. Estadística")
    print("4. Salir")

    opcion = input("¿Qué quieres hacer? ")
    while opcion not in ["1", "2", "3", "4"]:  # Solo acepta opciones válidas
        print("Opción inválida. Inténtalo de nuevo.")
        opcion = input("Elige una opción: ")

    return int(opcion)  # Convertimos a entero al final, ya que la opción es válida


def elegir_dificultad():
    print("\n--- Dificultad ---")
    print("1. Fácil (20 intentos)")
    print("2. Medio (12 intentos)")
    print("3. Difícil (5 intentos)")

    opcion = input("Elige una dificultad: ")
    while opcion not in ["1", "2", "3"]:  # Solo acepta opciones válidas
        print("Opción inválida. Inténtalo de nuevo.")
        opcion = input("Elige una dificultad: ")

    if opcion == "1":
        return 20
    elif opcion == "2":
        return 12
    elif opcion == "3":
        return 5

