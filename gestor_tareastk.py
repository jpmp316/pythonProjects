import tkinter as tk
from tkinter import messagebox

# Función para añadir tareas
def añadir_tarea(tareas, frame):
    def guardar_tarea():
        clave = entry_id.get()
        titulo = entry_titulo.get()
        descripcion = entry_descripcion.get()
        estado = entry_estado.get()

        if clave and titulo and descripcion and estado:
            tareas[clave] = {
                "titulo": titulo,
                "descripcion": descripcion,
                "estado": estado
            }
            messagebox.showinfo("Añadir tarea", f"Tarea '{clave}' añadida.")
            entry_id.delete(0, tk.END)
            entry_titulo.delete(0, tk.END)
            entry_descripcion.delete(0, tk.END)
            entry_estado.delete(0, tk.END)
        else:
            messagebox.showwarning("Añadir tarea", "Todos los campos son obligatorios.")
    
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="ID de la tarea:").pack()
    entry_id = tk.Entry(frame)
    entry_id.pack()

    tk.Label(frame, text="Título de la tarea:").pack()
    entry_titulo = tk.Entry(frame)
    entry_titulo.pack()

    tk.Label(frame, text="Descripción de la tarea:").pack()
    entry_descripcion = tk.Entry(frame)
    entry_descripcion.pack()

    tk.Label(frame, text="Estado de la tarea:").pack()
    entry_estado = tk.Entry(frame)
    entry_estado.pack()

    tk.Button(frame, text="Guardar tarea", command=guardar_tarea).pack(pady=10)
    tk.Button(frame, text="Volver al menú", command=lambda: mostrar_menu(frame)).pack(pady=10)

# Función para ver tareas
def ver_tareas(tareas, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    if not tareas:
        tk.Label(frame, text="No hay tareas registradas.").pack()
    else:
        for id, tarea in tareas.items():
            tk.Label(frame, text=f"ID: {id}").pack()
            tk.Label(frame, text=f"Título: {tarea['titulo']}").pack()
            tk.Label(frame, text=f"Descripción: {tarea['descripcion']}").pack()
            tk.Label(frame, text=f"Estado: {tarea['estado']}").pack()
            tk.Label(frame, text="-" * 20).pack()

    tk.Button(frame, text="Volver al menú", command=lambda: mostrar_menu(frame)).pack(pady=10)

# Función para marcar tarea como completada
def marcar_completada(tareas, frame):
    def completar():
        clave = entry_id.get()
        if clave in tareas:
            tareas[clave]['estado'] = "completada"
            messagebox.showinfo("Marcar completada", f"Tarea '{clave}' marcada como completada.")
        else:
            messagebox.showwarning("Error", f"No se encontró la tarea con ID '{clave}'.")

    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Ingrese el ID de la tarea a marcar como completada:").pack()
    entry_id = tk.Entry(frame)
    entry_id.pack()

    tk.Button(frame, text="Marcar completada", command=completar).pack(pady=10)
    tk.Button(frame, text="Volver al menú", command=lambda: mostrar_menu(frame)).pack(pady=10)

# Función para eliminar tarea
def eliminar_tarea(tareas, frame):
    def eliminar():
        clave = entry_id.get()
        if clave in tareas:
            del tareas[clave]
            messagebox.showinfo("Eliminar tarea", f"Tarea '{clave}' eliminada.")
        else:
            messagebox.showwarning("Error", f"No se encontró la tarea con ID '{clave}'.")

    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Ingrese el ID de la tarea a eliminar:").pack()
    entry_id = tk.Entry(frame)
    entry_id.pack()

    tk.Button(frame, text="Eliminar tarea", command=eliminar).pack(pady=10)
    tk.Button(frame, text="Volver al menú", command=lambda: mostrar_menu(frame)).pack(pady=10)

# Función para ver estadísticas
def ver_estadisticas(tareas, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    total = len(tareas)
    completadas = sum(1 for tarea in tareas.values() if tarea['estado'] == 'completada')
    pendientes = total - completadas

    tk.Label(frame, text=f"Total de tareas: {total}").pack()
    tk.Label(frame, text=f"Tareas completadas: {completadas}").pack()
    tk.Label(frame, text=f"Tareas pendientes: {pendientes}").pack()

    tk.Button(frame, text="Volver al menú", command=lambda: mostrar_menu(frame)).pack(pady=10)

# Función para mostrar el menú
def mostrar_menu(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Button(frame, text="Añadir tarea", command=lambda: añadir_tarea(tareas, frame)).pack(fill='x', pady=5)
    tk.Button(frame, text="Ver tareas", command=lambda: ver_tareas(tareas, frame)).pack(fill='x', pady=5)
    tk.Button(frame, text="Marcar tarea como completada", command=lambda: marcar_completada(tareas, frame)).pack(fill='x', pady=5)
    tk.Button(frame, text="Eliminar tarea", command=lambda: eliminar_tarea(tareas, frame)).pack(fill='x', pady=5)
    tk.Button(frame, text="Ver estadísticas", command=lambda: ver_estadisticas(tareas, frame)).pack(fill='x', pady=5)
    tk.Button(frame, text="Salir", command=root.quit).pack(fill='x', pady=5)

# Función principal
def main():
    global root
    root = tk.Tk()
    root.title("Gestor de Tareas")
    root.geometry("1280x720")

    global tareas
    tareas = {}

    frame = tk.Frame(root)
    frame.pack(pady=20)

    mostrar_menu(frame)
    root.mainloop()

if __name__ == "__main__":
    main()
