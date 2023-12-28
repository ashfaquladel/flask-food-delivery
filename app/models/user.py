from uuid import uuid4

class User():
    def __init__(self, name, email):
        self.id = str(uuid4())
        self.name = name
        self.email = email