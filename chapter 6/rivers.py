rivers = {
    "Nile":"Egypt",
    "Mississippi River":"USA",
    "Yangtze":"China",
}

for k,v in rivers.items():
    print(k,"runs through",v,end='.\n')

# name of each river
for k in rivers.keys():
    print(k)

# name of each country
for v in rivers.values():
    print(v)
