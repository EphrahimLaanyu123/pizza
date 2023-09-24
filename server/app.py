from flask import Flask, make_response, jsonify, request
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

        if restaurant is None:
            response_dict = {"error": "Restaurant not found"}
            response = make_response(
                jsonify(response_dict),
                404
            )
            return response

        pizzas = RestaurantPizza.query.filter_by(restaurant_id=restaurant.id).all()


        pizzas_dict = [pizza.to_dict() for pizza in pizzas]

        response_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": pizzas_dict
        }

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response
    
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant is None:
            response_dict = {"error": "Restaurant not found"}
            response = make_response(
                jsonify(response_dict),
                404
            )
            return response

        db.session.delete(restaurant)
        db.session.commit()

        response_dict = {"message":"Restaurant deleted succesfully"}
        response = make_response(
            jsonify(response_dict),
            200
        )

        return response


api.add_resource(Restaurant_by_id, '/restaurant/<int:id>')


class Restaurant_pizzas(Resource):

    def post(self):
        new_restaurant_pizza = RestaurantPizza(
            price=request.json['price'],
            pizza_id=request.json['pizza_id'],
            restaurant_id=request.json['restaurant_id']
        )

        if not new_restaurant_pizza.is_valid():
            response_dict = {"errors": ["validation errors"]}
            response = make_response(
                jsonify(response_dict),
                400
            )
            return response

        db.session.add(new_restaurant_pizza)
        db.session.commit()

        pizza = Pizza.query.get(new_restaurant_pizza.pizza_id)

        response_dict = {
            "id":new_restaurant_pizza.id,
            "name":pizza.name,
            "ingredients": pizza.ingredients
        }

        response = make_response(
            jsonify(response_dict),
            201
        )

        return response

api.add_resource(Restaurant_pizzas, '/restaurant_pizzas')



if __name__ == '__main__':
    app.run(port=5555, debug=True)