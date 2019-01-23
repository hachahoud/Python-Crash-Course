# conditional tests.

# tests evaluating to True.
car = 'tesla'
print("Is car == 'tesla'? I predict True.")
print(car == 'tesla')

car = 'tesla'
print("Is car.upper() != 'tesla'? I predict True.")
print(car.upper != 'tesla')

user = 'Admin'
print("Is user.lower() == 'admin'? I predict True.")
print(user.lower() == 'admin')

user = 'Admin'
print("Is user != 'admin'? I predict True.")
print(user != 'admin')

user = 'admin'
print("Is user == 'admin'? I predict True.")
print(user == 'admin')

# tests evaluating to False.
stock = 13
print("Is stock < 10? I predict False.")
print(stock < 10)

stock = 13
print("Is stock != 13? I predict False.")
print(stock != 13)

sells = 8
print("Is (sells > 10) or (stock < 10) I predict False.")
print((sells>10)or(stock<10))

print("Is (sells > 10) and (stock > 10)? I predict False.")
print((sells>10)and(stock>10))

user = 'User'
print("Is user == 'user'? I predict False.")
print(user == 'user')


