from app.auth.controller.authController import AuthController

class AuthView:
    def __init__(self):
        self.controller = AuthController()

    def login_role(self):
        while True:
            email = input("Enter your email: ")
            if self.controller.validateEmail(email):
                break
            else:
                print("Invalid Input Email!")
        password = input("Enter your password: ")
        status = self.controller.login(email, password)
        if status == 'admin':
            print("You are Admin")
            print("Successfully logged in")
        elif status == 'librarian':
            print("You are Librarian")
            print("Successfully logged in")
        elif status == 'member':
            print("You are Member")
            print("Successfully logged in")
        else:
            print("Incorrect Email or Password!")
