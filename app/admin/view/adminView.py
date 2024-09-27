from app.admin.controller.adminController import AdminController
import pwinput
from prettytable import PrettyTable,SINGLE_BORDER

class AdminView:
    def __init__(self):
        self.controller = AdminController()
        
    # TODO TABLE OUTPUT
    def table_user(self,user):
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["ID","Username","Role"]
        for user in user:
            table.add_row(user)
        print(table)

    def table_book(self,book):
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["ID", "Title", "Author", "Genre","Publisher","Year", "Copies"]
        for book in book:
            table.add_row(book)
        print(table)
    
    def table_borrow_book(self,book):
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["ID", "Username", "Title", "Borrow Date", "Due Date", "Status"]
        for borrow in book:
            table.add_row(borrow)
        print(table)
    
        
    def not_found(self):
        print("Not found !")
    
    # TODO LIST
    def list_user(self):
        results = self.controller.list_user()
        if results:
            self.table_user(results)
        else:
            self.not_found()
    
    def list_genre(self):
        results = self.controller.list_genre()
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["ID", "Genre"]
        if results:
            for id, genre in results:
                table.add_row([id, genre])
            print(table)
        else:
            self.not_found()
            
    def list_book(self):
        results = self.controller.list_book()
        if results:
            self.table_book(results)
        else:
            self.not_found()
            
    def list_role(self):
        results = self.controller.list_role()
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["ID", "Role"]
        if results:
            for id, role in results:
                table.add_row([id, role])
            print(table)
        else:
            self.not_found()
            
    def list_borrow_book(self):
        results = self.controller.list_borrrow_book()
        if results:
            self.table_borrow_book(results)
        else:
            self.not_found()
      
    # TODO SEARCH
    def search_user_by_id(self):
        id = input("Search ID: ")
        result = self.controller.search_user_by_id(id)
        if result:
            self.table_user([result])
        else:
            self.not_found()
            
    def search_book_by_id(self):
        id = input("Search ID: ")
        result = self.controller.search_book_by_id(id)
        if result:
            self.table_book([result])
        else:
            self.not_found()
    
    def search_user_by_name(self):
        name = input("Search Name: ")
        results = self.controller.search_user_by_name(name)
        if results:
            self.table_user(results)
        else:
            self.not_found()
      
    # TODO UPDATE
    def update_user_data(self):
        id = input("Enter user ID: ")
        check = self.controller.search_user_by_id(id)
        if check:
            self.table_user([check])
            username = input("Enter username: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            result = self.controller.update_user_data(username, first_name, last_name, phone_number, id)
            print(result)
        else:
            self.not_found()
    
    def update_book_data(self):
        id = input("Enter book ID: ")
        check = self.controller.search_book_by_id(id)
        if check:
            self.table_book([check])
            title = input("Enter Title: ")
            author_name = input("Enter Author: ")
            publisher_name = input("Enter Publisher: ")
            copies_available = int(input("Enter Copies: "))
            year_of_publisher = int(input("Enter Year Of Publisher: "))
            result = self.controller.update_book_data(title, author_name, publisher_name, copies_available, year_of_publisher,id)
            print(result)
        else:
            self.not_found()
        
    def upgrade_role(self):
        self.list_role()
        id = input("Enter user ID: ")
        check = self.controller.search_user_by_id(id)
        if check:
            self.table_user([check])
            role = int(input("Enter role:"))
            result = self.controller.upgrade_role(role,id)
            print(result)
        else:
            self.not_found()
            
    def change_genre(self):
        self.list_genre()
        id = input("Enter user ID: ")
        check = self.controller.search_book_by_id(id)
        if check:
            self.table_book([check])
            genre = int(input("Enter role:"))
            result = self.controller.change_genre(genre,id)
            print(result)
        else:
            self.not_found()
        
    # TODO CREATE & ADD
    def create_book(self):
        self.list_genre()
        title = input("Enter title: ")
        author = input("Enter author: ")
        publisher = input("Enter publisher: ")
        copies = int(input("Enter amount of copies: "))
        year = int(input("Enter year: "))
        genre_id = int(input("Enter genre id:"))
        result = self.controller.create_book(title,author,publisher,copies,year,genre_id)
        print(result)
        
    def create_member(self):
        print("============|  Create Member  |============")
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
        self.controller.create_member(username, first_name, last_name, email, password, phone_number)
    
    def create_librarian(self):
        print("============|  Create Librarian  |============")
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
        self.controller.create_librarian(username, first_name, last_name, email, password, phone_number)

       
    # TODO REMOVE
    def remove_book(self):
        self.list_book()
        id = input("Enter id: ")
        result = self.controller.remove_book(id)
        print(result)
        
    def remove_user(self):
        self.list_user()
        id = input("Enter id: ")
        result = self.controller.remove_user(id)
        print(result)
        
    def remove_borrow_book(self):
        self.list_borrow_book()
        id = input("Enter id: ")
        result = self.controller.remove_borrow_book(id)
        print(result)