# extending the people exercise.
qtarantino = {
    'first_name':'quentin',
    'last_name':'tarantino',
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

for person in people:
    if person['first_name'] == 'hamza':
        person['profession'] = 'programming'
    elif person['first_name'] == 'quentin':
        person['profession'] = 'film making'
for person in people:
    print(person['first_name'], person['profession'],'.')