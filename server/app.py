from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Pizza, RestaurantPizza, Restaurant, db
# Create a Flask application instance
app = Flask(__name__)

# Configure database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration objects

migrate = Migrate(app, db)

# db = SQLAlchemy(app)
db.init_app(app)






if __name__ == '__main__':
    app.run(port=5555, debug=True)