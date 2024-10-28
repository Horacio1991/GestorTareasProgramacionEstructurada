""" 
    TP01 - Gestor de Tareas
    
    Un programa que permite al usuario agregar, listar, eliminar y marcar tareas como completadas.
    Las tareas se guardan en un archivo de txt para persistencia de datos.
    
"""

import os
from datetime import datetime

# Archivo donde se van a guardar las tareas
ARCHIVO_TAREAS = "tareas.txt"

# Agregar Tarea y crear archivo si no existe


def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ").strip()
    fecha_limite = input("Ingrese la fecha límite (DD-MM-YYYY): ").strip()

    if not descripcion:
        print("Error: La descripción no puede estar vacía.")
        return

    try:
        # Convertir la fecha ingresada al formato de dd-mm-aaaa
        fecha_obj = datetime.strptime(fecha_limite, "%d-%m-%Y")
        fecha_formateada = fecha_obj.strftime("%d-%m-%Y")
    except ValueError:
        print("Error: La fecha debe estar en formato DD-MM-YYYY.")
        return

    # Guardar la tarea en el archivo
    try:
        with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{descripcion} - {fecha_formateada} - Pendiente\n")
        print("Tarea agregada con éxito.")
    except IOError:
        print("Error: No se pudo escribir en el archivo.")

# Mostrar la lista de tareas


def listar_tareas():
    """Lee y muestra todas las tareas guardadas en el archivo de tareas."""
    if not os.path.exists(ARCHIVO_TAREAS):
        print("No hay tareas guardadas.")
        return

    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()
            if not tareas:
                print("No hay tareas para mostrar.")
            else:
                print("\nListado de Tareas:")
                for idx, tarea in enumerate(tareas, 1):
                    print(f"{idx}. {tarea.strip()}")
    except IOError:
        print("Error: No se pudo leer el archivo.")


def eliminar_tarea():
    if not os.path.exists(ARCHIVO_TAREAS):
        print("No hay tareas guardadas.")
        return

    listar_tareas()  # Mostrar las tareas para que el usuario elija cual borrar

    try:
        numero = int(input("Ingrese el numero de la tarea a eliminar: "))

        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()

        if numero < 1 or numero > len(tareas):
            print("Error: Número de tarea no válido.")
            return

        # le resto uno para que  el numero del usuario coincida con el indice de la lista
        tareas.pop(numero - 1)

        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)

        print("Tarea eliminada con éxito.")
    except ValueError:
        print("Error: Ingrese un número válido.")
    except IOError:
        print("Error: No se pudo modificar el archivo.")


def marcar_completada():
    if not os.path.exists(ARCHIVO_TAREAS):
        print("No hay tareas guardadas.")
        return

    listar_tareas()  # Mostrar las tareas para que el usuario elija cual completar

    try:
        numero = int(
            input("Ingrese el número de la tarea a marcar como completada: "))

        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()

        if numero < 1 or numero > len(tareas):
            print("Error: Número de tarea no válido.")
            return

        descripcion, fecha_limite, _ = tareas[numero - 1].rsplit(" - ", 2)
        tareas[numero - 1] = f"{descripcion} - {fecha_limite} - Completada\n"

        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)

        print("Tarea marcada como completada.")
    except ValueError:
        print("Error: Ingrese un número válido.")
    except IOError:
        print("Error: No se pudo modificar el archivo.")


def menu():
    ejecutando = True
    while ejecutando:
        print("\nLista de Tareas")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Eliminar Tarea")
        print("4. Marcar Tarea como Completada")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            marcar_completada()
        elif opcion == "5":
            print("Saliendo del gestor de tareas.")
            ejecutando = False  # Actualizamos la variable para salir del bucle
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    menu()
