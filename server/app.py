from flask import Flask
from auth.routes import auth_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Registrar el blueprint para autenticación
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
    