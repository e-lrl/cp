import tkinter as tk
from tkinter import messagebox
from controller import obtener_datos, verificar_estado

# Función para obtener datos desde el servidor y mostrarlos en la interfaz
def mostrar_datos():
    try:
        datos = obtener_datos()
        resultado_label.config(text=datos)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener datos: {e}")

# Función para verificar el estado del servidor
def mostrar_estado():
    try:
        estado = verificar_estado()
        resultado_label.config(text=estado)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo verificar el estado: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Cliente de Escritorio - Flask")
root.state('zoomed')  # Pantalla completa al iniciar la aplicación
root.grid_columnconfigure(0, weight=1)  # Expande columnas en la ventana principal
root.grid_rowconfigure(2, weight=1)  # Expande la fila inferior donde están las 4 áreas

# Crear el frame superior para los botones y la etiqueta de resultados
frame_superior = tk.Frame(root)
frame_superior.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# Botón para obtener datos del servidor
btn_datos = tk.Button(frame_superior, text="Obtener Datos", command=mostrar_datos)
btn_datos.grid(row=0, column=0, padx=5, pady=5)

# Botón para verificar el estado del servidor
btn_estado = tk.Button(frame_superior, text="Verificar Estado", command=mostrar_estado)
btn_estado.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta para mostrar los resultados de los botones, colocada al lado de los botones
resultado_label = tk.Label(frame_superior, text="", bd=1, relief="solid", anchor="w")
resultado_label.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

# Línea de separación gráfica que ocupa todo el ancho de la ventana
separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

# Crear un frame inferior para dividir en cuatro partes
frame_inferior = tk.Frame(root)
frame_inferior.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

# Configurar columnas y filas en el frame inferior
frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(1, weight=1)

# Crear las cuatro áreas en la parte inferior, sin líneas separadoras
label_osciloscopio = tk.Label(frame_inferior, text="Osciloscopio", bd=1, relief="solid")
label_osciloscopio.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

label_generador = tk.Label(frame_inferior, text="Generador de Funciones", bd=1, relief="solid")
label_generador.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

label_atenuador = tk.Label(frame_inferior, text="Atenuador", bd=1, relief="solid")
label_atenuador.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

label_multimetro = tk.Label(frame_inferior, text="Multímetro", bd=1, relief="solid")
label_multimetro.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Iniciar el bucle principal de Tkinter
root.mainloop()
