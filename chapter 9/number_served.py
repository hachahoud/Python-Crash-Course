class Restaurant():
    """ A class modeling a restaurant. """

    def __init__(self,restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print the restaurant info."""
        print("Name: " + self.name)
        print("Cuisine_type: " + self.cuisine_type)
    
    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print("The " + self.name + " is now open!")

    def set_number_served(self, number):
        "set the number of customers served."
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't decrement the number served!")
    
    def increment_number_served(self, number):
        "increment the number of customers served."
        self.number_served += number

restaurant = Restaurant("Okla","TYPE1")
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(2)
print(restaurant.number_served)