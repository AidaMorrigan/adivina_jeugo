import pandas as pd
import dos_jugadores
import estadisticas
import menu_opciones
from menu_opciones import mostrar_menu
import un_jugador




def main():
    while True:
        opcion = mostrar_menu()

        if opcion in [1, 2]:  # Modo solitario o 2 jugadores
            intentos_maximos = None
            while intentos_maximos is None:
                intentos_maximos = menu_opciones.elegir_dificultad()
            if opcion == 1:
                un_jugador.partida_solitario(intentos_maximos)
                estadisticas.mostrar_resultados()

            elif opcion == 2:
                dos_jugadores.partida_dos_jugadores(intentos_maximos)
                estadisticas.mostrar_resultados()
                

        elif opcion == 3:
            estadisticas.mostrar_resultados()
            

        elif opcion == 4:
            
            print("¡Gracias por jugar! Guardando resultados y saliendo.")

            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")



main()

