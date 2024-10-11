from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def get_user(self, username):
        pass

    @abstractmethod
    def add_user(self, username, password):
        pass