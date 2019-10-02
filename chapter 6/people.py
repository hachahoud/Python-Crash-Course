qtarantino = {
    'first_name':'Quentin',
    'last_name':'Tarantino',
    'city':'knoxville',
    'age':'56',
}
hachahoud = {
    'first_name':'hamza',
    'last_name':'achahoud',
    'city':'agadir',
    'age':'19',
}
people = [qtarantino, hachahoud]
for person in people:
    print("My name is "+person['first_name']+' '+
    person['last_name']+'.I am '+
    person['age']+' years old, and I live in '+person['city']+'.')
