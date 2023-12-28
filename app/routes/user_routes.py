from app.models.user import User
from flask import request, jsonify
from app.repositories.user_repository import UserRepository

user_repository = UserRepository()
 
def add_user_routes(app):
    @app.route("/user/register", methods=["POST"])
    def register():
        body = request.json
        name = body.get("name", "")
        email = body.get("email", "")

        if not name and not email:
            return jsonify({"error":"Both name and email are required"}), 400
        
        new_user = User(name, email)
        user_repository.add_user(new_user)
        return jsonify({"message":"User registered successfully"}), 201

        