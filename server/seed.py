from faker import Faker
from app import app, db, Pizza, RestaurantPizza, Restaurant

fake = Faker()

def generate_pizza():
    return {
        'name': fake.word(),
        'ingredients': ', '.join(fake.words(nb=5)),
    }

def generate_restaurant():
    return {
        'name': fake.company(),
        'address': fake.address(),
    }

def seed_database():
    with app.app_context():
        pizzas = []
        restaurants = []

        for _ in range(50): 
            pizza_data = generate_pizza()
            pizza = Pizza(**pizza_data)
            pizzas.append(pizza)
            db.session.add(pizza)

        for _ in range(20): 
            restaurant_data = generate_restaurant()
            restaurant = Restaurant(**restaurant_data)
            restaurants.append(restaurant)
            db.session.add(restaurant)

        for pizza in pizzas:
            for restaurant in restaurants:
                price = fake.random_int(min=1, max=30)
                restaurant_pizza = RestaurantPizza(restaurant=restaurant, pizza=pizza, price=price)
                db.session.add(restaurant_pizza)

        db.session.commit()

if __name__ == '__main__':
    seed_database()



