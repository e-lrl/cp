from flask import Flask
from .routes import configure_routes

# Crear la instancia de Flask
app = Flask(__name__)

# Configurar las rutas (importando desde routes.py)
configure_routes(app)
