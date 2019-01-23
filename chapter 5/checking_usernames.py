# checking usernames.
current_users = ["hamza","eric",'jennifer','gabrielle','frank']
new_users = ['gabrielle','thomas','haruki', 'eric','mark']
for name in new_users:
    if name in current_users:
        print("This name already taken! try another!")
    else:
        print("Name is available.")

