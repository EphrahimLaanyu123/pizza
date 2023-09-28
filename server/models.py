from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from flask import Flask


db = SQLAlchemy()

# Create Pizza model
class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Add relationship to RestaurantPizza class
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients,
        }

# Cretaed RestaurantPizza model
class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer, CheckConstraint('price >= 1 AND price <= 30'), nullable=False) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Add relationships to Restaurant and Pizza
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    

    def to_dict(self):
        return {
            "price": self.price,
            "pizza_id": self.pizza_id,
            "restaurant_id": self.restaurant_id,
        }
    def is_valid(self):
        if self.price < 0: # Check if the price of the RestaurantPizza is less than 0
            return False
        return True   # If the price is not less than 0, it is valid


# Added Restaurant class
class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String)
    
    # Define a relationship to RestaurantPizza
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
    




