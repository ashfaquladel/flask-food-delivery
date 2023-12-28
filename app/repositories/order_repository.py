from app.util.json_util import read_json, write_json

ORDER_DATA = read_json("data/order_data.json")

class OrderRepository():
    def create_order(self, order):
        ORDER_DATA.append({
            "id": order.id,
            "foods": order.foods,
            "user_id": order.user_id,
            "address": order.address,
            "phone": order.phone,
            "total": order.total
        })
        write_json("data/order_data.json", ORDER_DATA)