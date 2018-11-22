# using for loops.
# copying a list, the pizza program
pizzas = ["italien pizza","mexican pizza","moroccan pizza"]

friend_pizzas = pizzas[:]
pizzas.append("quatre fromage")
friend_pizzas.append("fruit de mere")

print("my favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("my frined's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
