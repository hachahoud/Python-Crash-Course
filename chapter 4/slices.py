# slicing using the example from the odd_numbers program

# print odd numbers from one to twenty
odd = list(range(1,21,2))
print("The first three items in the list are:")
print(odd[:3])

# the list looks like this: [1,3,5,7,9,11,13,15,17,19]
#we want to get the numbers: 9,11,13
print("Three items from the middle of the list are:")
print(odd[4:7])

print("The last three items in the list are:")
print(odd[-3:])
