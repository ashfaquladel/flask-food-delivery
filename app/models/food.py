from uuid import uuid4

class Food():
    def __init__(self, name, price, category):
        self.id = str(uuid4())
        self.name = name
        self.price = price
        self.category = category