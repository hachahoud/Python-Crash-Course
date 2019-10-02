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

class IceCreamStand(Restaurant):
    """Modeling a specific kind of restaurants, IceCreamStand."""

    def __init__(self, name, cuisine_type, flavors):
        """Initializing attributes of the parent class.
        Then inizialize attributes specific to an IceCreamStand."""

        super().__init__(name,cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        """Display the flavors."""
        for flavor in self.flavors:
            print(flavor)

mikey_stand = IceCreamStand("Mikey Stand","Type2",["flav1","flav2","flav3"])
mikey_stand.display_flavors()
