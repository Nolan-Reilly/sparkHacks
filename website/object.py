class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
