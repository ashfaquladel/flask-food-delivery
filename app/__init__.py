from flask import Flask
from app.routes.food_routes import add_food_routes

from app.routes.user_routes import add_user_routes

app = Flask(__name__)

add_user_routes(app)
add_food_routes(app)