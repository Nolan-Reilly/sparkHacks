from flask_login import UserMixin
from flask import flash

class User(UserMixin):
    def __init__(self, username, password, active=True):
        self.username = username
        self.password = password
        self.active = active

    def write_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.username} {self.password}\n")
    
    def is_active(self):
        return self.active
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.username
    