# task_manager.py

def add_task(todo_list, name, time, state):
    new_task = {"name": name, "time": time, "state": state}
    
    # Convertir la hora de la nueva tarea a minutos para facilitar la comparacion
    # Conversion de Horas a minutos y sumatoria total de minutos
    new_time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(":"))))
    
    # Buscar la posicion correcta para insertar la nueva tarea según su hora (Cantidad total de minutos)
    index_to_insert = 0
    for index, task in enumerate(todo_list.tasks):
        task_time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(task["time"].split(":"))))
        if new_time >= task_time:
            index_to_insert = index + 1
        else:
            break
    
    # Insertar la nueva tarea en la posición correcta
    todo_list.tasks.insert(index_to_insert, new_task)


def delete_task(todo_list, index):
    if 0 <= index < len(todo_list.tasks):
        # Revisar estado para la eliminacion 
        task_state = todo_list.tasks[index].get("state", None)
        # Solo los estados de Nueva y En curso son eliminables
        if task_state in ["Nueva", "En curso"]:
            del todo_list.tasks[index]
            print("Tarea eliminada.")
        else:
            print("No se puede eliminar la tarea. El estado no es 'Nueva' o 'En curso'.")
    else:
        print("Índice de tarea inválido")
