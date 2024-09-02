from app.auth.controller.authController import AuthController
import getpass

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
        while True:
            password = getpass.getpass('Enter your password: ')
            if self.controller.validatePass(password):
                break
            else:
                print("Invalid Input Password!")
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
