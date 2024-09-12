from app.admin.controller.adminController import AdminController

class AdminView:
    def __init__(self):
        self.controller = AdminController() 
        
    def table_user(self,user):
        print(f"User ID: {user[0]}, Username: {user[1]}, Role: {user[2]}")
        
    def table_book(self,book):
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")
    
    def table_data(self,id,data):
        print(f"{id}\t{data}")
    
        
    def user_not_found(self):
        print("User not found !")
        
    def list_user(self):
        results = self.controller.list_user()
        if results:
            for user in results:
                self.table_user(user)
        else:
            self.user_not_found()
    
    def list_genre(self):
        results = self.controller.list_genre()
        print("ID\tGenre")
        if results:
            for id,genre in results:
                self.table_data(id,genre)
        else:
            self.user_not_found()
            
    def list_book(self):
        results = self.controller.list_book()
        if results:
            for book in results:
                self.table_book(book)
        else:
            self.user_not_found()
            
    def list_role(self):
        results = self.controller.list_role()
        print("ID\tRole")
        if results:
            for id,role in results:
                self.table_data(id,role)
        else:
            self.user_not_found()
            
    def search_user_by_id(self):
        id = input("Search ID: ")
        result = self.controller.search_user_by_id(id)
        if result:
            self.table_user(result)
        else:
            self.user_not_found()
    
    def search_user_by_name(self):
        name = input("Search Name: ")
        results = self.controller.search_user_by_name(name)
        if results:
            for result in results:
                self.table_user(result)
        else:
            self.user_not_found()
            
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
            self.user_not_found()
            
    def upgrade_role(self):
        self.show_all_role()
        id = input("Enter user ID: ")
        check = self.controller.search_user_by_id(id)
        print(check)
        if check:
            role = int(input("Enter role:"))
            result = self.controller.upgrade_role(role,id)
            print(result)
        else:
            self.user_not_found()
            
    def new_book(self):
        self.show_all_genre()
        title = input("Enter title: ")
        author = input("Enter author: ")
        publisher = input("Enter publisher: ")
        copies = int(input("Enter amount of copies: "))
        year = int(input("Enter year: "))
        genre_id = int(input("Enter genre id:"))
        result = self.controller.create_book(title,author,publisher,copies,year,genre_id)
        print(result)
        
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