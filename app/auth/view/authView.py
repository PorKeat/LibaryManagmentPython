from app.auth.controller.authController import AuthController
from app.admin.view.adminView import AdminView
from app.member.view.memberView import MemberView
from app.librarian.view.librarianView import LibrarianView
import pwinput

class AuthView:
    def __init__(self):
        self.controller = AuthController()
        self.adminView = AdminView()
        self.memberView = MemberView()
        self.librarianView = LibrarianView()
        self.login_id = []

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
        status,user_id = self.controller.login(email, password)
        if status == 'admin':
            print("You are Admin")
            print("Successfully logged in")
            self.login_id.append(user_id)
            self.admin_feature()
        elif status == 'librarian':
            print("You are Librarian")
            print("Successfully logged in")
            self.login_id.append(user_id)
            self.librarian_feature()
        elif status == 'member':
            print("You are Member")
            print("Successfully logged in")
            self.login_id.append(user_id)
            print(self.login_id)
            self.member_feature()
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
        self.controller.register(username, first_name, last_name, email, password, phone_number)

    def normal_user(self):
        while True:
            print("============| Libary Management System |============")
            print("1. View Book")
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
                
    
    def member_feature(self):
        while True:
            print("============| Member Feature |============")
            print("1. View Book")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Pay Fines")
            print("0. Sign Out !")
            print("=========================================")
            op = int(input("Choose your option: "))
            if op == 1:
                self.memberView.list_book()
            elif op == 2:
                self.memberView.borrow_book(self.login_id[0])
            elif op == 3:
                self.memberView.return_book(self.login_id[0])
            elif op == 4:
                self.memberView.pay_back_fine(self.login_id[0])
            elif op == 0:
                self.login_id.clear()
                break
            else:
                print("Invalid Input !")
                
    def librarian_feature(self):
        while True:
            print("============| Librarian Feature |============")
            print("1. List Feature")
            print("2. Add Book")
            print("3. Search Feature")  
            print("4. Update Book")
            print("5. Change Book Genre")
            print("6. Remove Feature")
            print("0. Sign Out !")
            print("============================================")
            op = int(input("Choose your option: "))
            if op==1:
                print("============| List Features |============")
                print("1. List Book")
                print("2. List Borrow Book")
                print("0. Back !")
                print("=========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.librarianView.list_book()
                elif subOp == 2:
                    self.librarianView.list_borrow_book()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 2:
                self.librarianView.create_book()
            elif op == 3:
                print("============| Search Features |============")
                print("1. Search User By ID")
                print("2. Search User By Name")
                print("3. Search Book By ID")
                print("0. Back !")
                print("===========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.librarianView.search_user_by_id()
                elif subOp == 2:
                    self.librarianView.search_user_by_name()
                elif subOp == 3:
                    self.librarianView.search_book_by_id()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 4:
                self.librarianView.update_book_data()
            elif op == 5:
                self.librarianView.change_genre()
            elif op == 6:
                print("============| Remove Features |============")
                print("1. Remove Book")
                print("2. Remove Borrow Book")
                print("0. Back !")
                print("===========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.librarianView.remove_book()
                elif subOp == 2:
                    self.librarianView.remove_borrow_book()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 0:
                self.login_id.clear()
                break
            else:
                print("Invalid Input !")
    
    def admin_feature(self):
        while True:
            print("============| Admin Feature |============")
            print("1. List Features")
            print("2. Create Features")
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
                print("5. List Borrow Book")
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
                elif subOp == 5:
                    self.adminView.list_borrow_book()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 2:
                print("============| Create Features |============")
                print("1. Create Member")
                print("2. Create Librarian")
                print("3. Create Book")
                print("0. Back !")
                print("===========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.adminView.create_member()
                elif subOp == 2:
                    self.adminView.create_librarian()
                elif subOp == 3:
                    self.adminView.create_book()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 3:
                print("============| Search Features |============")
                print("1. Search User By ID")
                print("2. Search User By Name")
                print("3. Search Book By ID")
                print("0. Back !")
                print("===========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.adminView.search_user_by_id()
                elif subOp == 2:
                    self.adminView.search_user_by_name()
                elif subOp == 3:
                    self.adminView.search_book_by_id()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 4:
                print("============| Update Features |============")
                print("1. Update User")
                print("2. Update Book")
                print("3. Upgrade Role")
                print("4. Change Book Genre")
                print("0. Back !")
                print("===========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.adminView.update_user_data()
                elif subOp == 2:
                    self.adminView.update_book_data()
                elif subOp == 3:
                    self.adminView.upgrade_role()
                elif subOp == 4:
                    self.adminView.change_genre()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 5:
                print("============| Remove Features |============")
                print("1. Remove User")
                print("2. Remove Book")
                print("3. Remove Borrow Book")
                print("0. Back !")
                print("===========================================")
                subOp = int(input("Choose your option: "))
                if subOp == 1:
                    self.adminView.remove_user()
                elif subOp == 2:
                    self.adminView.remove_book()
                elif subOp == 3:
                    self.adminView.remove_borrow_book()
                elif subOp == 0:
                    continue
                else:
                    print("Invalid Input !")
            elif op == 0:
                self.login_id.clear()
                break
            else:
                print("Invalid Input !")