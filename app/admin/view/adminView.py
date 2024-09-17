from app.admin.controller.adminController import AdminController

class AdminView:
    def __init__(self):
        self.controller = AdminController() 
    # TODO TABLE OUTPUT
    def table_user(self,user):
        print(f"User ID: {user[0]}, Username: {user[1]}, Role: {user[2]}")
        
    def table_book(self,book):
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Copies: {book[4]}")
    
    def table_data(self,id,data):
        print(f"{id}\t{data}")
        
    def table_borrow_book(self,book):
        print(f"Borrow ID: {book[0]}, Username: {book[1]}, Title: {book[2]}, Borrow Date: {book[3]}, Due Date: {book[4]}, Status: {book[5]}")
    
        
    def not_found(self):
        print("Not found !")
    
    # TODO LIST
    def list_user(self):
        results = self.controller.list_user()
        if results:
            for user in results:
                self.table_user(user)
        else:
            self.not_found()
    
    def list_genre(self):
        results = self.controller.list_genre()
        print("ID\tGenre")
        if results:
            for id,genre in results:
                self.table_data(id,genre)
        else:
            self.not_found()
            
    def list_book(self):
        results = self.controller.list_book()
        if results:
            for book in results:
                self.table_book(book)
        else:
            self.not_found()
            
    def list_role(self):
        results = self.controller.list_role()
        print("ID\tRole")
        if results:
            for id,role in results:
                self.table_data(id,role)
        else:
            self.not_found()
            
    def list_borrow_book(self):
        results = self.controller.list_borrrow_book()
        if results:
            for borrow in results:
                self.table_borrow_book(borrow)
        else:
            self.not_found()
      
    # TODO SEARCH
    def search_user_by_id(self):
        id = input("Search ID: ")
        result = self.controller.search_user_by_id(id)
        if result:
            self.table_user(result)
        else:
            self.not_found()
            
    def search_book_by_id(self):
        id = input("Search ID: ")
        result = self.controller.search_book_by_id(id)
        if result:
            self.table_book(result)
        else:
            self.not_found()
    
    def search_user_by_name(self):
        name = input("Search Name: ")
        results = self.controller.search_user_by_name(name)
        if results:
            for result in results:
                self.table_user(result)
        else:
            self.not_found()
      
    # TODO UPDATE
    def update_user_data(self):
        id = input("Enter user ID: ")
        check = self.controller.search_user_by_id(id)
        print(check)
        if check:
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
        print(check)
        if check:
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
        print(check)
        if check:
            role = int(input("Enter role:"))
            result = self.controller.upgrade_role(role,id)
            print(result)
        else:
            self.not_found()
            
    def change_genre(self):
        self.list_genre()
        id = input("Enter user ID: ")
        check = self.controller.search_book_by_id(id)
        print(check)
        if check:
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
        
    def borrow_book(self,user_id):
        self.list_book()
        book_id = int(input("Enter Book ID: "))
        result = self.controller.borrow_book(user_id ,book_id)
        print(result)
        
    def return_book(self):
        self.list_borrow_book()
        book_id = int(input("Enter Book ID: "))
        result = self.controller.return_book(book_id)
        print(result)
       
    # TODO REMOVE
    def remove_book(self):
        self.show_all_book()
        id = input("Enter id: ")
        result = self.controller.remove_book(id)
        print(result)
        
    def remove_user(self):
        self.show_all_user()
        id = input("Enter id: ")
        result = self.controller.remove_user(id)
        print(result)