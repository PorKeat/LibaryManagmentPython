from app.auth.controller.authController import AuthController
from app.admin.view.adminView import AdminView
from app.member.view.memberView import MemberView
import getpass
import pwinput

class AuthView:
    def __init__(self):
        self.controller = AuthController()
        self.adminView = AdminView()
        self.memberView = MemberView()

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
            self.admin_feature()
        elif status == 'librarian':
            print("You are Librarian")
            print("Successfully logged in")
        elif status == 'member':
            print("You are Member")
            print("Successfully logged in")
        else:
            print("Incorrect Email or Password!")
            
    def register(self):
        print("============|  Become Our Member Ship  |============")
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
            print("2. Login To Join Us")
            print("3. Register To Become A Member")
            print("0. Exit !")
            print("====================================================")
            op = int(input("Choose your option: "))
            if op == 1:
                self.memberView.list_book()
            elif op == 2:
                self.login()
            elif op == 3:
                self.register()
            elif op == 0:
                break
            else:
                print("Invalid Input !")
    
    def admin_feature(self):
        while True:
            print("============| Admin Feature |============")
            print("1. List Features")
            print("2. Add Features")
            print("3. Search Features")
            print("4. Update Features")
            print("5. Remove Features")
            print("0. Sign Out !")
            print("=========================================")
            op = int(input("Choose your option: "))
            if op == 1:
                print("============| List Features |============")
                print("1. List User")
                print("2. List Book")
                print("3. List Role")
                print("4. List Genre")
                print("0. Back !")
                print("=========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.adminView.list_user()
                elif subOp == 2:
                    self.adminView.list_book()
                elif subOp == 3:
                    self.adminView.list_role()
                elif subOp == 4:
                    self.adminView.list_genre()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 0:
                break
            else:
                print("Invalid Input !")