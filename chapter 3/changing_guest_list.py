# a program printing a message to each person on the list. after replacing one of the guests

invited = ["Nickola Tesla","Fyodor Dostoyevsky","Frank Kafka"]
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])
# one of the guest couldn't make it so let's think of someone else.
# print a message saying his name.
out_guest = invited.pop(1)
print(out_guest, "couldn't make the dinner!")

# inviting the new guest
new_guest = "Victor Hugo"
invited.insert(1,new_guest)
# inviting. printing the messages.
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])
