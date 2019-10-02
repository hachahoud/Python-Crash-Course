while True:
    age = input("Enter your age: ")

    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("Your ticket is free kiddo!")
    elif age <= 12:
        print("Your ticket is 10$")
    else:
        print("Your ticket is 15$")

