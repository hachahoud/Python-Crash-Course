class Restaurant():
    """ A class modeling a restaurant. """

    def __init__(self,restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print the restaurant info."""
        print("Name: " + self.name)
        print("Cuisine_type: " + self.cuisine_type)
    
    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print("The " + self.name + " is now open!")

okla = Restaurant("Okla","TYPE1")
seasons = Restaurant("Seasons","TYPE3")
chezvous = Restaurant("ChezVous","TYPE2")

okla.describe_restaurant()
seasons.describe_restaurant()
chezvous.describe_restaurant()
