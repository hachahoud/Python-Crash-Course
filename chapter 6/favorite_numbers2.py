data = {
    'billie':[7,13],
    'hamza':[8,23],
    'winston':[10,9,84],
}

for user in data.keys():
    print(user+"'s favorites numbers are:")
    for number in data[user]:
        print(number)
