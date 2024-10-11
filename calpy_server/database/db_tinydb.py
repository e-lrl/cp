from tinydb import TinyDB, Query
from config import Config
from .db_interface import DatabaseInterface

class TinyDBWrapper(DatabaseInterface):
    def __init__(self):
        self.db = TinyDB(Config.DATABASE_PATH)
        self.users_table = self.db.table('users')

    def get_user(self, username):
        User = Query()
        return self.users_table.get(User.username == username)

    def add_user(self, username, password):
        self.users_table.insert({'username': username, 'password': password})