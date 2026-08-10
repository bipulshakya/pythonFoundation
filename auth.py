class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def get_info(self):
        print(f"Name: {self.name}, Email: {self.email}")
        return self.name, self.email

    def match_password(self, password):
        if self.password == password:
            return True
        else: 
            return False
        

u1 = User("Alice", "alice@example.com", "password1")
u2 = User("Bob", "bob@example.com", "password2")
u3 = User("Charlie", "charlie@example.com", "password3")
users = [u1, u2, u3]

class Login:
    @staticmethod
    def authenticate(email, password):
        found = False
        for user in users:
            if user.email == email and user.password == password:
                found = True
            if found:
                print("Login successful!")
        else:
            print("Invalid email or password.")
    
email = input("Enter your email: ")
password = input("Enter your password: ")
Login.authenticate(email, password)