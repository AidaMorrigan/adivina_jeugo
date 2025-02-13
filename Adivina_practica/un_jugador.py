import random

import estadisticas

"""Partida en solitario donde el jugador indica la dificultad
    intenta adividar el numero elegido de manera aleatoria """

def partida_solitario(intentos_maximos):

    numero_secreto = random.randint(1, 1000)
    intentos_realizados = 0

    nombre_jugador = input("\nDime tu nombre: ")
    print(nombre_jugador + " Adivina el número entre 1 y 1000.")

    while intentos_realizados < intentos_maximos:
        try:
            intento = int(input(f"Intento {intentos_realizados + 1} de {intentos_maximos}: "))
            intentos_realizados += 1

            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.\n")
                #Guardamos el resultado de la partida ganada
                estadisticas.registrar_resultado(nombre_jugador, ganada=True, dificultad=intentos_maximos, intentos=intentos_realizados)
                return  # La partida termina si gana
        except ValueError:
            print("Por favor, ingresa un número válido.\n")

    # Si llega aquí, ha agotado los intentos sin adivinar
    print(f"Lo siento, has perdido. El número era {numero_secreto}.\n")
    #guardamos el resultado de la partida perdida
    estadisticas.registrar_resultado(nombre_jugador, ganada=False, dificultad=intentos_maximos, intentos=intentos_realizados)
    # devolvemos el nombre del jugador
    return nombre_jugador