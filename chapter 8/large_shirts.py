def make_shirt(size="large", message="I love python"):
    print("A '"+message+"' on a "+size+" sized t-shirt.")

# a large shirt with the default message.
make_shirt()
# a meduim with the default text.
make_shirt(size="medium")
# a large with another message.
make_shirt(message="<I know HTML/>")
