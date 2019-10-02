favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

names = ["sarah", "hamza", "jesse","phil","edward"]

for name in names:
    if name in favorite_languages.keys():
        print("Thank you for taking the poll "+name+"!")
    else:
        print("Welcome "+name+"! Would you please take the poll!")
