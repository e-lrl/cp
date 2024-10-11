from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.db_tinydb import TinyDBWrapper

auth_bp = Blueprint('auth', __name__)
db = TinyDBWrapper()

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.get_user(username)

        if user and user['password'] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('auth.login'))