class User():
    """Modeling a user."""

    def __init__(self,first_name, last_name, age):
        "Initialize attributes."
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        "describe the user."
        print("Name: " + self.first_name + " " + self.last_name + ".")
        print("Age: " + str(self.age))
    
    def greet_user(self):
        "greet the user."
        print("Hello, " + self.first_name)

admin = User("admin","admin",0)
me = User("hamza","achahoud",20)

admin.describe_user()
admin.greet_user()

me.describe_user()
me.greet_user()
