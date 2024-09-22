import requests

# URL base del servidor Flask
BASE_URL = "http://localhost:5000"

# Función para obtener datos del servidor
def obtener_datos():
    try:
        response = requests.get(f"{BASE_URL}/")
        response.raise_for_status()  # Verificar si hubo errores
        return response.json()["message"]
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# Función para verificar el estado del servidor
def verificar_estado():
    try:
        response = requests.get(f"{BASE_URL}/status")
        response.raise_for_status()  # Verificar si hubo errores
        return response.json()["status"]
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
