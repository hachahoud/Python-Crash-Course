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


class Privileges():
    """Representation of the privileges of an admin."""
    def __init__(self):
        """Initialize the privileges' attributes."""
        self.privileges = ["delete","add","modify","close"]

    def show_privileges(self):
        """show the privileges of an admin."""
        for pr in self.privileges:
            print(pr)


class Admin(User):
    """Modeling an admin."""

    def __init__(self,first_name, last_name,age):
        """Initialize te parent class then the subclass."""
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()
    

admin = Admin("Hamza","Ach",20)
admin.greet_user()
admin.privileges.show_privileges()