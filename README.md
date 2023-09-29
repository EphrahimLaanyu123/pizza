<<<<<<< HEAD
## Pizza Restaurant API
This is a Flask-based API for managing pizza restaurants, their pizzas, and prices. It allows you to perform various operations, including retrieving a list of pizzas, restaurants, and adding restaurant-specific pizzas.

# Table of Contents
Installation
Usage
Running the Application
API Endpoints
Database
Seed Data
Models
Contributing
License
# Installation
To run this application, you'll need to have Python and Flask installed. Follow these steps to set up the environment:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/pizza-restaurant-api.git
Navigate to the project directory:

bash
Copy code
cd pizza-restaurant-api
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Running the Application
You can run the application using the following command:

bash
Copy code
python app.py
The application will be accessible at http://localhost:5555.

# API Endpoints
Here are the available API endpoints:

GET /pizzas: Retrieve a list of all pizzas.
GET /restaurants: Retrieve a list of all restaurants.
GET /restaurant/{id}: Retrieve information about a specific restaurant by its ID.
DELETE /restaurant/{id}: Delete a restaurant by its ID.
POST /restaurant_pizzas: Add a new restaurant-specific pizza.
To use these endpoints, you can use tools like curl, Postman, or your preferred API client.

Database
This application uses SQLite as its database, and the database file is named pizza.db. You can configure the database URI in the app.py file.

Seed Data
To populate the database with sample data, you can run the seed_database.py script. It will generate random pizzas, restaurants, and restaurant-pizza associations and add them to the database.

To seed the database, run the following command:

bash
Copy code
python seed_database.py
Models
Pizza: Represents a pizza with attributes such as name, ingredients, and timestamps.
RestaurantPizza: Represents the relationship between a restaurant and a pizza, including the price.
Restaurant: Represents a restaurant with attributes like name and address.
Contributing
If you'd like to contribute to this project, please follow the contributing guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

=======
# Pizza Restaurant API
This is a basic Flask-based API for managing pizza restaurants, their pizzas, and prices. It offers essential functionality for listing pizzas, restaurants, retrieving restaurant details by ID, deleting restaurants, and adding restaurant-specific pizzas.

## Endpoints

- **GET /pizzas**: Retrieve a list of all available pizzas.
- **GET /restaurants**: Get a list of all registered restaurants.
- **GET /restaurant/{id}**: Retrieve details of a specific restaurant by its ID.
- **DELETE /restaurant/{id}**: Delete a restaurant by its ID.
- **POST /restaurant_pizzas**: Add a new pizza to a restaurant's menu.
## Usage
Clone this repository.
Access the API at http://localhost:5555.
## Models
Pizza: Each pizza has attributes like name and ingredients.
RestaurantPizza: Represents a pizza offered by a restaurant, including its price.
Restaurant: Describes a restaurant with attributes like name and address.
## Seed Data
To populate the database with sample data, execute seed_database.py. It will create random pizzas, restaurants, and their associations in the database.

Run the following command to seed the database:

bash
Copy code
python seed.py
Contributing
Feel free to contribute to this project. Fork the repository and submit a pull request.

License
This project is open-source and licensed under the MIT License. Please see the LICENSE file for details.
>>>>>>> 103330e324c16db4e714388e74345cd5c7ea93bd



