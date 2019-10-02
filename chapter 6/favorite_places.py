favorite_places = {
    "Riley":['Morocco','New zealand'],
    "Leo":['Indonesia'],
    "Fredie":['China','Japan','Morocco']
}

for friend in favorite_places.keys():
    if len(favorite_places[friend]) == 1:
        print(friend+"'s favorite place is "+favorite_places[friend][0])
    else:
        print(friend+"'s favorite places are:")
        for place in favorite_places[friend]:
            print(place)