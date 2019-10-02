java = {
    'species':'dog',
    'owner':'jolie',
    'name':'java',
}
lina = {
    'name':'lina',
    'species':'cat',
    'owner':'jules',
}

pets = [java,lina]
for pet in pets:
    print(pet['name'].title()+' is a '+pet['species']+', and it belongs to '+
        pet['owner'].title()+'.')