
def añadir_tarea(tareas):
    while True:
        clave = input("Ingrese el ID de la tarea (o presione Enter para terminar): ")
        if clave == "":
            break
        titulo = input(f"Ingrese el título de la tarea '{clave}': ")
        descripcion = input(f"Ingrese la descripción de la tarea '{clave}': ")
        estado = input(f"Ingrese el estado actual de la tarea '{clave}': ")
        tareas[clave] = {"titulo": titulo,
                         "descripcion": descripcion,
                         "estado": estado
                         }
    return tareas


def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for id, tarea in tareas.items():
            print(f"ID: {id}")
            print(f"Título: {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Estado: {tarea['estado']}")
            print("-" * 20)


def marcar_completada(tareas):
    # Implementa la lógica para marcar una tarea como completada
    if not tareas:
        print("No hay tareas registradas.")
        return tareas

    print("Tareas actuales:")
    for id, tarea in tareas.items():
        print(f"ID: {id}, Título: {tarea['titulo']}, Estado: {tarea['estado']}")

    clave = input("Ingrese el ID de la tarea que quiera marcar como completada: ")

    if clave in tareas:
        tareas[clave]['estado'] = "completada"
        print(f"La tarea '{tareas[clave]['titulo']}' ha sido marcada como completada.")
    else:
        print("ID de tarea no encontrado.")

    return tareas




def eliminar_tarea(tareas):
    # Implementa la lógica para eliminar una tarea
    if not tareas:
        print("No hay tareas registradas.")
        return tareas
    for id, tarea in tareas.items():
        print(f"ID: {id}, Título: {tarea['titulo']}, Estado: {tarea['estado']}")

    clave = input("Ingrese el ID de la tarea que quiere eliminar ")

    if clave in tareas:
        titulo_tarea = tareas[clave]['titulo']
        del tareas[clave]
        print(f"La tarea '{titulo_tarea}' ha sido eliminada")
    else:
        print("ID de tarea no encontrado.")

    return tareas



def ver_estadisticas(tareas):
    # Implementa la lógica para mostrar estadísticas
    contador_completadas = 0

    # Recorrer el diccionario y verificar el estado de cada tarea
    for clave, valor in tareas.items():
        if valor['estado'] == 'completada':
            contador_completadas += 1

    # Imprimir el resultado
    print(f"Número de tareas completadas: {contador_completadas}")


    



def main():
    opcion = 0
    tareas = {}
    while opcion != 6:

        print("\n--- Gestor de Tareas ---")
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Ver estadísticas")
        print("6. Salir")
        while True:
                try:
                    opcion = int(input("Seleccione una opción: "))
                    
                    break
                except ValueError:
                    print("Ingrese un numero entero")
            
       
        # Implementa la lógica para manejar las opciones del usuario
        if opcion == 1:
            tareas=añadir_tarea(tareas)
        elif opcion == 2:
            ver_tareas(tareas)
        elif opcion == 3:
            marcar_completada(tareas)
        elif  opcion ==4:
            eliminar_tarea(tareas)
        elif opcion == 5:
            ver_estadisticas(tareas)
      
if __name__ == "__main__":
    main()