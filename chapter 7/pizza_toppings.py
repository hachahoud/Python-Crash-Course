active = True
while active:
    topp = input("Enter a topping: ")
    
    if topp == 'quit':
        active = False
    else:
        print("Adding "+topp+" to the pizza toppings.")