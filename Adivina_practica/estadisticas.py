import pandas as pd
import openpyxl
from openpyxl import Workbook
import os
from tabulate import tabulate


# Archivo para almacenar los datos de las partidas
archivo_excel = "estadisticas_partidas.xlsx"

# Diccionario para almacenar cada partida con su resultado
partidas = {}
id_partida = 1

def registrar_resultado(nombre_jugador, ganada, dificultad, intentos):
    """Registra los resultados de una partida en el diccionario 'partidas'."""
    #variable global de id_partida para podeer hacer la tabla
    global id_partida
    # diccionario de resultado con diferentes variables
    resultado = {
        "Jugador": nombre_jugador,
        "Ganada": "Sí" if ganada else "No",
        "Dificultad": dificultad,
        "Intentos": intentos
    }
    
    partidas[id_partida] = resultado
    id_partida += 1
    guardar_en_excel()  # Guardar automáticamente en el archivo Excel cada vez que se registra un resultado

def mostrar_resultados():
    """Muestra los resultados de todas las partidas en formato de tabla."""
    tabla = [
        [id_partida, datos["Jugador"], datos["Ganada"], datos["Dificultad"], datos["Intentos"]]
        for id_partida, datos in partidas.items()
    ]
    #Uso de tabulate para el formato de tabla
    print(tabulate(tabla, headers=["ID Partida", "Jugador", "Ganada", "Dificultad", "Intentos"]))


def guardar_en_excel():
    """Guarda las estadísticas en un archivo de Excel y lo abre."""
    if not os.path.exists(archivo_excel):
        # Crear un nuevo archivo de Excel si no existe
        wb = Workbook()
        ws = wb.active
        ws.title = "Estadisticas"
        # Crear encabezados
        ws.append(["ID Partida", "Jugador", "Ganada", "Dificultad", "Intentos"])
    else:
        # Abrir el archivo existente
        wb = openpyxl.load_workbook(archivo_excel)
        ws = wb["Estadisticas"]

    # Agregar los datos de cada partida al archivo 
    # Recorremos un for para rellenar todos los items del diccionario
    for id_partida, datos in partidas.items():
        ws.append([
            id_partida,
            datos["Jugador"],
            datos["Ganada"],
            datos["Dificultad"],
            datos["Intentos"]
        ])

    # Guardar los cambios en el archivo Excel
    wb.save(archivo_excel)

    # Abrir el archivo Excel automáticamente para los diferentes sistemas operativos
    if os.name == 'nt':  # Windows
        os.startfile(archivo_excel)
    else:  # macOS y Linux
        os.system(f"open {archivo_excel}" if os.uname().sysname == 'Darwin' else f"xdg-open {archivo_excel}")

