from app.models.order import Order
from app.models.user import User
from flask import request, jsonify
from app.repositories.order_repository import OrderRepository

order_repository = OrderRepository()
 
def add_order_routes(app):
    @app.route("/order/create", methods=["POST"])
    def create_order():
        body = request.json
        foods = body.get("foods", "")
        user_id = body.get("user_id", "")
        address = body.get("address", "")
        phone = body.get("phone", "")
        total = body.get("total", "")

        if not foods and not user_id and not address and not phone and not total:
            return jsonify({"error":"Incorrect parameter"}), 400
        
        new_order = Order(foods, user_id, address, phone, total)
        order_repository.create_order(new_order)
        return jsonify({"message":"Order created successfully"}), 201

        