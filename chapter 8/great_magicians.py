def show_magicians(magicians):
    for name in magicians:
        print(name)

def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magician = "The Great " + current_magician
        great_magicians.append(great_magician)
    

magicians = ["Messi","Zidane","Pirlo","Ronaldo"]
great_magicians = []
make_great(magicians,great_magicians)
show_magicians(great_magicians)
