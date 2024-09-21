from app.admin.model.adminModel import AdminModel
import re
import hashlib

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()
    
    # TODO List
    def list_user(self):
        result = self.admin_model.list_user()
        if result:
            return result
        else:
            return None
    
    def list_genre(self):
        result = self.admin_model.list_genre()
        if result:
            return result
        else:
            return None
    
    def list_role(self):
        result = self.admin_model.list_role()
        if result:
            return result
        else:
            return None
    
    def list_book(self):
        result = self.admin_model.list_book()
        if result:
            return result
        else:
            return None
        
    def list_borrrow_book(self):
        result = self.admin_model.list_borrow_book()
        if result:
            return result
        else:
            return None
    
    # TODO REMOVE
    def remove_book(self,id):
        result = self.admin_model.remove_book(id)
        if result:
            return "Removed Successfully"
        else:
            return "Fail to remove"
        
    def remove_user(self,id):
        result = self.admin_model.remove_user(id)
        if result:
            return "Removed Successfully"
        else:
            return "Fail to remove"
        
    def remove_borrow_book(self,id):
        result = self.admin_model.remove_borrow_book(id)
        if result:
            return "Removed Successfully"
        else:
            return "Fail to remove"
            
    # TODO SEARCH  
    def search_user_by_id(self, user_id):
        result = self.admin_model.search_user_by_id(user_id)
        if result:
            return result
        else:
            return None
    
    def search_user_by_name(self, user_name):
        results = self.admin_model.search_user_by_name(user_name)
        if results:
            return results
        else:
            return None
        
    def search_book_by_id(self, book_id):
        result = self.admin_model.search_book_by_id(book_id)
        if result:
            return result
        else:
            return None
    
    # TODO UPDATE
    def update_user_data(self, username, first_name, last_name, phone_number, user_id):
        result = self.admin_model.update_user_data(username, first_name, last_name, phone_number, user_id)
        if result:
            return "Updated User Successfully"
        else:
            return "Update Failed"
        
    def update_book_data(self, title, author_name, publisher_name, copies_available, year_of_publisher, book_id):
        result = self.admin_model.update_book_data(title, author_name, publisher_name, copies_available, year_of_publisher, book_id)
        if result:
            return "Updated Book Successfully"
        else:
            return "Update Failed"
        
        
    def upgrade_role(self,role,id):
        result = self.admin_model.upgrade_role(role,id)
        if result:
            return "Upgraded User Successfully"
        else:
            return "Upgraded User Fail"
        
    def change_genre(self,genre,id):
        result = self.admin_model.change_genre(genre,id)
        if result:
            return "Genre Changed Successfully"
        else:
            return "Failed To Change Genre"
    
    # TODO CREATE & ADD
    def create_book(self,title,author,publisher,copies,year,genre_id):
        result = self.admin_model.create_book(title,author,publisher,copies,year,genre_id)
        if result:
            return "Add New Book Successfully !"
        else:
            return "Failed to add new book !"

    def create_member(self, username, first_name, last_name, email, password, phone_number):
        encoded_password = password.encode()
        hashPassword = hashlib.sha256()
        hashPassword.update(encoded_password)
        hashedPass = hashPassword.hexdigest()
        result = self.admin_model.create_member(username, first_name, last_name, email, hashedPass, phone_number)
        if result:
            print("Member created successfully !")
        else:
            print("Failed to create member")
            
    def create_librarian(self, username, first_name, last_name, email, password, phone_number):
        encoded_password = password.encode()
        hashPassword = hashlib.sha256()
        hashPassword.update(encoded_password)
        hashedPass = hashPassword.hexdigest()
        result = self.admin_model.create_librarian(username, first_name, last_name, email, hashedPass, phone_number)
        if result:
            print("Librarian created successfully !")
        else:
            print("Failed to create librarian")


    def validateEmail(self,email):
        if "@" not in email or "gmail" not in email or ".com" not in email:
            return False
        else:
            return True
    
    def validatePass(self,password):
        if len(password) <=5:
            return False
        if not re.search("[A-Z]",password):
            return False
        if not re.search("[a-z]",password):
            return False
        if not re.search("[0-9]",password):
            return False
        if not re.search("[!@#$%^&*]",password):
            return False
        return True
    
    def validatePhoneNumber(self,phone_number):
        if re.search("[A-Z]",phone_number):
            return False
        if re.search("[a-z]",phone_number):
            return False
        if re.search("[!@#$%^&*]",phone_number):
            return False
        return True