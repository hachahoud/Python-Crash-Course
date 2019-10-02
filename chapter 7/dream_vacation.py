results = {}
active = True
while active:
    name = input("Give your name: ")
    dream = input("what's your dream vacation? ")

    results[name] = dream

    print("continue taking the poll? (yes/no)")
    repeat = input().lower()
    if repeat == 'no':
        active = False

for name, response in results.items():
    print(name, ":", response)
