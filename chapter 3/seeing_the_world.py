# organazing a list.

places = ["New york","Sidney","Malibu","Iceland","China"]
print(places)

# the listed sorted without modifying the original list
print(sorted(places))

# showing the original list
print(places)

# in reverse without modifying the original
print(sorted(places,reverse=True))

# showing the original
print(places)

# change the order to reverse
places.reverse()
print(places)

# reverse it back to orignial state
places.reverse()
print(places)

# sorting in alphabetical order
places.sort()
print(places)

# in reverse alphabetical order
places.sort(reverse=True)
print(places)
