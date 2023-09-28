from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Pizza, RestaurantPizza, Restaurant, db
from flask_restful import Api, Resource

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



migrate = Migrate(app, db)

# db = SQLAlchemy(app)
db.init_app(app)

api = Api(app)


class Pizzas(Resource):

    def get(self):
        pizzas = [] #Create an empty array to hold the pizzas 

        all_pizzas = Pizza.query.all() #Gets all pizzas

        for pizza in all_pizzas:
            pizzas.append(pizza.to_dict()) #Convert every pizza to dict

        response = make_response(
            jsonify(pizzas),
            200
        )

        return response 


api.add_resource(Pizzas, '/pizzas') #Gave it the endpoint

class Restaurants(Resource):

    def get(self):
        restaurants = [] #Create an empty array that holds all the restaursnts to be fetched
        all_restaurants = Restaurant.query.all() #Get all the restaurants through query

        for restaurant in all_restaurants:
            restaurants.append(restaurant.to_dict()) #loop through all the restaurants while adding themto the dictionary
        
        response  = make_response(
            jsonify(restaurants),
            200
        )

        return response

api.add_resource(Restaurants, '/restaurants') # GAVE IT AN ENDPOINT
        
class Restaurant_by_id(Resource):

    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first() #GET A RESTAURANT BY ID

        if restaurant is None: #IN CASE THERE IS NO RESTAURANT OF THAT ID FOUND IT BRINGS AN ERROR
            response_dict = {"error": "Restaurant not found"}
            response = make_response(
                jsonify(response_dict), #CONVERT THE ERROR RESPONSE TO DICTIONARY
                404
            )
            return response

        pizzas = RestaurantPizza.query.filter_by(restaurant_id=restaurant.id).all() #GET ALL THE PIZZAS ASSOCIATED WITH THAT SPECIFIC RESTAURANT


        pizzas_dict = [pizza.to_dict() for pizza in pizzas]# CONVERT THOSE PIZAS TO DICTTIONARY AND ADD THEM TO THE RESPONSE

        response_dict = {      #THIS IS THE RESPONSE THAT CONTAINS THE RESTAURANTS AND ALL THE PIZZAS ASSOCIATED WITH IT
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": pizzas_dict
        }

        response = make_response(  #GIVE BACK THE RESPONSE
            jsonify(response_dict),
            200
        )

        return response
    
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()  #GET A SPECIFIC RESTAUTRANT USING ITD ID

        if restaurant is None:
            response_dict = {"error": "Restaurant not found"} # ADDED AN ERORR MESSAGE IN CASE THE RESTURAURANT IS NOT FOUND
            response = make_response(
                jsonify(response_dict),#CONVERT THE ERROR RESPONSE TO DICTITONARY
                404
            )
            return response

        db.session.delete(restaurant) # DELETES THE RESTUARANT IF IT WAS GOTTENAT FIRST
        db.session.commit()

        response_dict = {"message":"Restaurant deleted succesfully"} # RETURNS AN RESPONSE IF THE RESTAURANT WAS FOUND
        response = make_response(
            jsonify(response_dict),
            200
        )

        return response


api.add_resource(Restaurant_by_id, '/restaurant/<int:id>') # GAVE IT AN ENDPOINT


class Restaurant_pizzas(Resource):

    def post(self): # CREATE A NEW RESTAURANT USING JSON FORMAT
        new_restaurant_pizza = RestaurantPizza(
            price=request.json['price'],
            pizza_id=request.json['pizza_id'],
            restaurant_id=request.json['restaurant_id']
        )

        if not new_restaurant_pizza.is_valid(): # IF THERE WAS AN ERROR IN POSTING THE RESPONSE
            response_dict = {"errors": ["validation errors"]}
            response = make_response(
                jsonify(response_dict),
                400
            )
            return response

        db.session.add(new_restaurant_pizza)#ADD THE RESTAURANTPIZZA
        db.session.commit()

        pizza = Pizza.query.get(new_restaurant_pizza.pizza_id) # GETS THE PIZZA ASSOCIATED WITH THE RESTAURANT PIZZA USING PIZZA_ID
        # CREATE A RESPONSE THAT SHOWS THE PIZZA DETAILS
        response_dict = {
            "id":pizza.id,
            "name":pizza.name,
            "ingredients": pizza.ingredients
        }

        response = make_response(
            jsonify(response_dict),
            201
        )

        return response

api.add_resource(Restaurant_pizzas, '/restaurant_pizzas') # GAVE IT AN ENDPOINT



if __name__ == '__main__':
    app.run(port=5555, debug=True)