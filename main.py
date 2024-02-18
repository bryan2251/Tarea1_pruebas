# main.py
from todo_list import TodoList
from task_manager import add_task, delete_task

def main():
    todo_list = TodoList()

    while True:
        # Menu de opciones por consola
        print("\n1. Agregar tarea")
        print("2. Modificar estado tarea")
        print("3. Eliminar tarea")
        print("4. Generar reporte")
        print("5. Mostrar lista de Tareas")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        # Creacion de tareas con el estado de nueva definida1
        if choice == "1":
            name = input("Ingrese el nombre de la nueva tarea: ")
            time = input("Ingrese la hora de la nueva tarea: ")
            state = "Nueva"
            add_task(todo_list, name, time, state)
            print("Tarea agregada con éxito.")
            
        # Cambio de estados de opciones predefinidas de tareas ya creadas
        elif choice == "2":
            index = int(input("Ingrese el índice de la tarea cambiar el estado: "))
            todo_list.change_state_task(index + 1)
            print("Tarea cambiada con exito.")
            
        #  Eliminacion de tareas con comprobante por estados aceptados
        elif choice == "3":
            index = int(input("Ingrese el índice de la tarea a eliminar: "))
            delete_task(todo_list, index + 1)
            print("Tarea eliminada.")
            
        # Reporte por estados con conteo y tareas definidas dentro de cada estado
        elif choice == "4":
            todo_list.generate_report()
            
        # Mostrar lista de las tareas en la consola
        elif choice == "5":
            todo_list.mostrar()
            
        # Cierre del programa
        elif choice == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
