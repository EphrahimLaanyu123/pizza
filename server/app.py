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

class Index(Resource):

    def get(self):

        response_dict = {
            "index": "Welcome to the Newsletter RESTful API",
        }

        response = make_response(
            jsonify(response_dict),
            200,
        )

        return response

api.add_resource(Index, '/')
class Pizzas(Resource):

    def get(self):
        
        response_dict_list = [n.to_dict() for n in Pizza.query.all()]

        response = make_response(
            jsonify(response_dict_list), 
            200
        )

        return response

api.add_resource(Pizzas, '/pizzas')
        



if __name__ == '__main__':
    api.add_resource(Pizzas, '/pizzas')
    app.run(port=5555, debug=True)