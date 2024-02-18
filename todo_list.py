# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = []

    
    # Cambio de estado de las tareas
    def change_state_task(self, index):
        # Definir el estado por defecto en casos de error
        state = "Nueva"
        if 0 <= index < len(self.tasks):
            # Cerrar las opciones a solo los estados definidos para que el usuario no salga de los estados predefinidos
            while True:
                print("\n1. Completado")
                print("2. Pendiente")
                print("3. En curso")
                choice = input("Seleccione una opción de estadosa: ")

                if choice == "1":
                    state = "Completado"
                    break
                elif choice == "2":
                    state = "Pendiente"
                    break
                elif choice == "3":
                    state = "En curso"
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
            # Actualizacion del estado    
            self.tasks[index]["state"] = state      
        else:
            print("Índice de tarea inválido")

    
    # Funcion de Debugging para mostrar las tareas 
    # TO-DO: Mejorar como se ve
    def mostrar(self):
        print("Lista de tareas:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. Nombre: {task['name']}, Hora: {task['time']}, Estado: {task['state']}")
    
    def generate_report(self):
    # Filtrar las tareas por estado en listas separadas
        pending_tasks = [task for task in self.tasks if task["state"] == "Pendiente"]
        completed_tasks = [task for task in self.tasks if task["state"] == "Completado"]
        oncourse_tasks = [task for task in self.tasks if task["state"] == "En curso"]

        # Mostrar el reporte
        # TO-DO: Mejorar formato de Reporte
        print("Tareas pendientes:")
        for task in pending_tasks:
            print("- Nombre:", task["name"], "| Hora:", task["time"], "| Estado:", task["state"])
            
        print("\nTareas en curso:")
        for task in oncourse_tasks:
            print("- Nombre:", task["name"], "| Hora:", task["time"], "| Estado:", task["state"])
            
        print("\nTareas completadas:")
        for task in completed_tasks:
            print("- Nombre:", task["name"], "| Hora:", task["time"], "| Estado:", task["state"])
