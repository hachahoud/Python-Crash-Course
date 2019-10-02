def make_car(manufacturer,model,**features):
    info = {}
    info["manufacturer"] = manufacturer
    info["model"] = model

    for key, value in features.items():
        info[key] = value
    return info

mycar = make_car("MyCar","X574",color="black",
                self_drive=True)
print(mycar)