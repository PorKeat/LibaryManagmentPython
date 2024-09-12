from app.auth.controller.authController import AuthController
from app.admin.view.adminView import AdminView
import getpass
import pwinput

class AuthView:
    def __init__(self):
        self.controller = AuthController()
        self.adminView = AdminView()

    def login(self):
        while True:
            email = input("Enter your email: ")
            if self.controller.validateEmail(email):
                break
            else:
                print("Invalid Input Email!")
        while True:
            password = pwinput.pwinput('Enter your password: ')
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
            
    def register(self):
        username = input("Username: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        while True:
            email = input("Email: ")
            if self.controller.validateEmail(email):
                break
            else:
                print("Invalid Input Email!")
        while True:
            password = pwinput.pwinput('Password: ')
            if self.controller.validatePass(password):
                break
            else:
                print("Invalid Input Password!")
        while True:
            phone_number = input("PhoneNumber: ")
            if self.controller.validatePhoneNumber(phone_number):
                break
            else:
                print("Invalid Input !")
        while True:
            role = int(input("Role [1.Admin 2.Librarian 3.Member]: "))
            if role in [1, 2, 3]:
                break
            else:
                print("Please enter a valid number for role (1, 2, 3)")
        self.controller.register(username, first_name, last_name, email, password, phone_number,role)

    def normal_user(self):
        while True:
            print("============| Libary Management System |============")
            print("1. List All Book")
            print("3. Register To Become A Member")
            print("0. Exit !")
            print("====================================================")
            op = int(input("Choose your option: "))
            if op == 1:
                self.adminView.list_book()
            elif op == 2:
                pass
            elif op == 3:
                pass
            elif op == 0:
                break
            else:
                print("Invalid Input !")
    
    def register_to_become_member(self):
        print("============|  Become Our Member Ship  |============")