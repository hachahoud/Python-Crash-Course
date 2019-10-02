class User():
    """Modeling a user."""

    def __init__(self,first_name, last_name, age):
        "Initialize attributes."
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        "describe the user."
        print("Name: " + self.first_name + " " + self.last_name + ".")
        print("Age: " + str(self.age))
    
    def greet_user(self):
        "greet the user."
        print("Hello, " + self.first_name)
    
    def increment_login_attempts(self):
        """increment the login attempts by one 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """reset the login attempts to 0."""
        self.login_attempts = 0


me = User("Hamza","Ashahoud",20)
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)
me.increment_login_attempts()
print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)
