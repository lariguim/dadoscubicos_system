class AuthManager:
    def __init__(self, storage):
        self.storage = storage
        
    def login(self, username, password):
        user = self.storage.get_user(username)
        if user and user["password"] == password:  # In production, use proper password verification
            return user
        return None
        
    def register(self, username, password, role="customer"):
        if self.storage.get_user(username):
            return False
        user = User(username, password, role)
        self.storage.save_user(user)
        return True