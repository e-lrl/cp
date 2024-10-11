from tinydb import TinyDB, Query
from config import Config
from .db_interface import DatabaseInterface
from werkzeug.security import generate_password_hash, check_password_hash

class TinyDBWrapper(DatabaseInterface):
    def __init__(self):
        self.db = TinyDB(Config.DATABASE_PATH)
        self.users_table = self.db.table('users')

    def get_user(self, username):
        User = Query()
        return self.users_table.get(User.username == username)

    def add_user(self, username, password):
        # Generar un hash de la contraseña antes de almacenarla
        hashed_password = generate_password_hash(password)
        self.users_table.insert({'username': username, 'password': hashed_password})

    def verify_password(self, username, password):
        user = self.get_user(username)
        if user:
            # Comparar la contraseña almacenada (hash) con la proporcionada
            return check_password_hash(user['password'], password)
        return False   