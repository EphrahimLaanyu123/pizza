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



