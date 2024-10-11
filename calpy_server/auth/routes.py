from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.db_tinydb import TinyDBWrapper
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)
db = TinyDBWrapper()

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar la contraseña usando el método de la base de datos
        if db.verify_password(username, password):
            session['username'] = username
            flash('Login exitoso!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('auth.login'))

@auth_bp.route('/create_admin', methods=['POST'])
def create_admin():
    # Ruta para crear el usuario administrador. Asegúrate de protegerla adecuadamente.
    username = 'admin'
    password = 'chuschus'
    
    # Verificar si el usuario ya existe
    if db.get_user(username):
        flash('El usuario administrador ya existe.', 'warning')
    else:
        # Agregar el usuario con la contraseña cifrada
        db.add_user(username, password)
        flash('Usuario administrador creado con éxito.', 'success')
    
    return redirect(url_for('auth.login'))