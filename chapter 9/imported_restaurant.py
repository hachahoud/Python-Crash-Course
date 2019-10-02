from restaurant_module import Restaurant

my_restaurant = Restaurant("Mine",'TYPE8')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(7)
print(my_restaurant.number_served)
