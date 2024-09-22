from flask import jsonify

def configure_routes(app):
    
    @app.route('/')
    def home():
        return jsonify({"message":"Bienvenido al servidor web"})

    @app.route('/status')
    def status():
        return jsonify({"status":"El servidor esta corriendo correctamente"})
