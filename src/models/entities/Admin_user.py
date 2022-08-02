from werkzeug.security import check_password_hash

class Admin_user():
    
    def __init__(self, id, name, password) -> None:
        self.id = id        
        self.name = name        
        self.password = password
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)