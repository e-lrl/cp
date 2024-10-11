# CalPy
Herramienta de Calibracion en Python

project/
│
├── calweb_server.py     # Archivo principal para ejecutar la aplicación Flask (antes app.py)
├── config.py            # Archivo de configuración
├── database/
│   ├── __init__.py      # Inicialización del módulo de base de datos
│   ├── db_tinydb.py     # Implementación de la base de datos utilizando TinyDB
│   └── db_interface.py  # Interfaz para la base de datos (abstracta)
├── auth/
│   ├── __init__.py      # Inicialización del módulo de autenticación
│   └── routes.py        # Rutas relacionadas con el inicio de sesión
├── templates/
│   ├── login.html       # Plantilla para la página de inicio de sesión
│   └── home.html        # Plantilla para la página principal
└── requirements.txt     # Dependencias del proyecto