from uuid import uuid4

class Order():
    def __init__(self, foods, user_id, address, phone, total):
        self.id = str(uuid4())
        self.foods = foods
        self.user_id = user_id
        self.address = address
        self.phone = phone
        self.total = total