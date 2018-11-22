# a program printing a message to each person on the list. and adding more guests.

invited = ["Nickola Tesla","Fyodor Dostoyevsky","Franz Kafka"]
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])

# informing the guests that we've found a bigger table.
print("hey, we have found a bigger table, so we're inviting new people")
# add a new guest to the beginning of the list.
invited.insert(0,"Victor Hugo")
# add another one to the middle of the list.
invited.insert(2,"Richard Faynman")
# add another to the end of the list.
invited.append("Isaac Newton")

# printing the inviting message.
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])
print("You are welcomed to dinner at my house this afternoon,", invited[3])
print("You are welcomed to dinner at my house this afternoon,", invited[4])
print("You are welcomed to dinner at my house this afternoon,", invited[5])
