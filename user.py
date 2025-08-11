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
        self.users.append(User(username, password))
        self.active = username

    def login(self, username, password):
        for user in self.users:
            if user.username == username:
                if user.password == password:
                    self.active = username
                    return True
                else:
                    return False
            return False
    
    def logout(self):
        self.active = universal