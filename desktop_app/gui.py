import tkinter as tk
from tkinter import Canvas
import requests

# Función para obtener datos desde el servidor
def obtener_datos():
    try:
        response = requests.get("http://localhost:5000/")
        response.raise_for_status()  # Verifica si la solicitud tuvo éxito
        return response.json().get("message", "No hay datos disponibles")
    except requests.ConnectionError:
        return "Error: No se pudo conectar al servidor. Funcionando en modo local."
    except Exception as e:
        return f"Error inesperado: {e}"

# Función para verificar el estado del servidor
def verificar_estado():
    # Cambiar el color del LED a naranja mientras se verifica el estado
    led_canvas.itemconfig(led_circle, fill="orange")
    root.update_idletasks()  # Forzar actualización para que el cambio de color sea visible
    try:
        response = requests.get("http://localhost:5000/status")
        response.raise_for_status()  # Verifica si la solicitud tuvo éxito
        led_canvas.itemconfig(led_circle, fill="green")  # Cambiar el LED a verde si está conectado
        return response.json().get("status", "Estado no disponible")
    except requests.ConnectionError:
        led_canvas.itemconfig(led_circle, fill="red")  # Cambiar el LED a rojo si no está conectado
        return "Error: No se pudo conectar al servidor. Modo local activado."
    except Exception as e:
        led_canvas.itemconfig(led_circle, fill="red")  # Cambiar el LED a rojo en caso de error
        return f"Error inesperado: {e}"

# Función para mostrar datos en la interfaz gráfica
def mostrar_datos():
    datos = obtener_datos()
    resultado_label.config(text=datos)

# Función para mostrar el estado del servidor en la interfaz gráfica
def mostrar_estado():
    estado = verificar_estado()
    resultado_label.config(text=estado)

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

# Crear un frame para el botón "Verificar Estado" y el LED a su derecha
frame_verificar_estado = tk.Frame(frame_superior)
frame_verificar_estado.grid(row=0, column=1, padx=10, pady=5, sticky="e")

# Botón para verificar el estado del servidor
btn_estado = tk.Button(frame_verificar_estado, text="Verificar Estado", command=mostrar_estado)
btn_estado.pack(side="left", padx=5, pady=5)

# Canvas para dibujar el "LED" que indicará el estado del servidor
led_canvas = Canvas(frame_verificar_estado, width=20, height=20, highlightthickness=0)
led_circle = led_canvas.create_oval(2, 2, 18, 18, fill="red")  # Iniciar con LED rojo
led_canvas.pack(side="left", padx=5)

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
