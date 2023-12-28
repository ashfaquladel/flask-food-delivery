from app.models.food import Food
from flask import request, jsonify
from app.repositories.food_repository import FoodRepository

food_repository = FoodRepository()
 
def add_food_routes(app):
    @app.route("/food/view", methods=["GET"])
    def view_food():
        result = food_repository.get_foods()
        return jsonify({"data": result, "count": len(result)}), 200
        

    @app.route("/food/search", methods=["GET"])
    def search_food():
        params = request.args
        name = params.get("name", "")
        category = params.get("category", "")

        if (not name and not category) or (name and category):
            return jsonify({"error":"Only one parameter is required"}), 400
        
        result = food_repository.search_food(name, category)
        return jsonify({"data": result, "count": len(result)}), 200


        