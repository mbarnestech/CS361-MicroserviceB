universal = "Public"

class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

class Users:
    def __init__(self, user=User(universal)):
        self.users = [user]
        self.active = user.username

    def addUser(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
        self.active = username

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.active = username
                return True
        return False
    
    def logout(self):
        self.active = universal