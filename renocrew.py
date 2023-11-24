import random

class Restaurant:
    def __init__(self, name, cuisine, rating, proximity):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.proximity = proximity

def populate_data_structure():
    # Populate the data structure with sample restaurants
    restaurants = [
        Restaurant("Restaurant1", "Italian", 4.5, 2),
        Restaurant("Restaurant2", "Chinese", 3.8, 1),
        Restaurant("Restaurant3", "Mexican", 4.0, 3),
        Restaurant("Restaurant4", "Indian", 4.2, 3),
        Restaurant("Restaurant5", "Maharastrian", 4.3, 1),
        Restaurant("Restaurant6", "panjabi", 4.6, 2),

        
    ]
    return restaurants

def recommend_restaurants(user_input, restaurants):
    # Filter restaurants based on user input
    matching_restaurants = [r for r in restaurants if r.cuisine.lower() == user_input.lower()]

    # Sort by rating and proximity
    matching_restaurants.sort(key=lambda x: (x.rating, -x.proximity), reverse=True)

    return matching_restaurants

def main():
    # Step 3: Populate the data structure
    restaurant_data = populate_data_structure()

    while True:
        try:
            # Step 1: User input
            user_input = input("Enter a type of food: ")

            if not user_input:
                break

            # Step 6: Error handling for invalid or unavailable type of food
            if not any(r.cuisine.lower() == user_input.lower() for r in restaurant_data):
                print("Sorry, no restaurants found for that type of food. Try again.")
                continue

            # Step 4: Recommendation function
            recommendations = recommend_restaurants(user_input, restaurant_data)

            # Step 7: Display recommendations
            if recommendations:
                print("Recommendations:")
                for i, restaurant in enumerate(recommendations):
                    print(f"{i + 1}. {restaurant.name} - Cuisine: {restaurant.cuisine}, Rating: {restaurant.rating}, Proximity: {restaurant.proximity} km")
            else:
                print("No matching restaurants found.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Step 8: Write test cases
    test_restaurant_data = populate_data_structure()
    assert recommend_restaurants("Italian", test_restaurant_data)
    assert recommend_restaurants("Chinese", test_restaurant_data)
    assert recommend_restaurants("Mexican", test_restaurant_data)
    assert recommend_restaurants("Maharastrian", test_restaurant_data)
    assert recommend_restaurants("Indian", test_restaurant_data)
    assert recommend_restaurants("Panjabi", test_restaurant_data)

    assert not recommend_restaurants("Japanese", test_restaurant_data)
    assert not recommend_restaurants("", test_restaurant_data)

    # Run the main program
    main()
