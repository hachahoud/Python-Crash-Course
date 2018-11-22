# a program printing a message to each person on the list.

invited = ["Nickola Tesla","Fyodor Dostoyevsky","Franz Kafka"]
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])

# informing the guests that we've found a bigger table.
print("hey, we have found a bigger table, so we're inviting new people")
# add a new guest to the beginning of the list.
invited.insert(0,"Victor Hugo")
# add another one to the middle of the list.
invited.insert(2,"Jim Carry")
# add another to the end of the list.
invited.append("Isaac Newton")

# printing the inviting message.
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])
print("You are welcomed to dinner at my house this afternoon,", invited[3])
print("You are welcomed to dinner at my house this afternoon,", invited[4])
print("You are welcomed to dinner at my house this afternoon,", invited[5])

# there's only place for two people.
print("I can only invite two people.")
# let's leave only 'Jim Carry' and 'Kafka'.
# the list looks now like this:
# ['Hugo','Tesla','Carry','Dostoyvsky','Kafka','Newton']
fyodor = invited.pop(3)
print("I am sorry I can't invite you to dinner.",fyodor)
# after the value with index 3 is removed:
# ['Hugo','Tesla','Carry','Kafka','Newton']
hugo = invited.pop(0)
print("I am sorry I can't invite you to dinner.",hugo)
# now looks like this: ['Tesla','Carry','Kafka','Newton']
tesla = invited.pop(0)
print("I am sorry I can't invite you to dinner.",tesla)
# now it looks like this: ['Carry','Kafka','Newton']
newton = invited.pop(2)
print("I am sorry I can't invite you to dinner.",newton)

# now there's only two people ['carry','kafka']
print("you are still invited,", invited[0])
print("you are still invited,", invited[1])

# emptying the list at the end of the program.
del invited[0]
del invited[0]
# making sure the list is actually empty.
print(invited)
