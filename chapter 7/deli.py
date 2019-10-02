sandwich_orders = ["chiken","vegetable", "tuna"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a "+sandwich+" sandwich!")
    finished_sandwiches.append(sandwich)

print("Here are the sandwiches I made:")
for sandwich in finished_sandwiches:
    print(sandwich)
