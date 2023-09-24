from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Pizza, RestaurantPizza, Restaurant, db
from flask_restful import Api, Resource
# Create a Flask application instance
app = Flask(__name__)

# Configure database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration objects

migrate = Migrate(app, db)

# db = SQLAlchemy(app)
db.init_app(app)

api = Api(app)


class Pizzas(Resource):

    def get(self):
        pizzas = []

        all_pizzas = Pizza.query.all()

        for pizza in all_pizzas:
            pizzas.append(pizza.to_dict()) 

        response = make_response(
            jsonify(pizzas),
            200
        )

        return response


api.add_resource(Pizzas, '/pizzas')

class Restaurants(Resource):

    def get(self):
        restaurants = []
        all_restaurants = Restaurant.query.all()

        for restaurant in all_restaurants:
            restaurants.append(restaurant.to_dict())
        
        response  = make_response(
            jsonify(restaurants),
            200
        )

        return response

api.add_resource(Restaurants, '/restaurants')
        
class Restaurant_by_id(Resource):

    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        restaurant_dict  = restaurant.to_dict()

        response = make_response(
            jsonify(restaurant_dict),
            200
        )

        return response

api.add_resource(Restaurant_by_id, '/restaurant/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)