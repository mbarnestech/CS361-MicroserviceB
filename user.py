class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Users:
    public = "public"
    def __init__(self):
        self.users = []
        self.active = public

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
        self.active = public