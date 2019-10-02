cities = {
    "Marrakech":{
        'country':'Morocco',
        'population':'1.70 million',
        'fact':'Horse-drawn carriages represent an old tradition.',
    },
    "Osaka":{
        'country':'Japan',
        'population':'2.691 million',
        "fact":"Known as the Nation's kitchen."
    }
}

for city, info in cities.items():
    print(city)
    print(info['country'], info['population'],info['fact'])
    