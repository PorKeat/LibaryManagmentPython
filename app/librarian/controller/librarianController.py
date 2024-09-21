from app.librarian.model.librarianModel import LibrarianModel
import re
import hashlib

class LibrarianController:
    def __init__(self):
        self.librarian_model = LibrarianModel()
        
    def list_book(self):
        result = self.librarian_model.list_book()
        if result:
            return result
        else:
            return None
        
    def list_borrrow_book(self):
        result = self.librarian_model.list_borrow_book()
        if result:
            return result
        else:
            return None
        
    def borrow_book(self,user_id ,book_id):
        result = self.librarian_model.borrow_book(user_id ,book_id)
        if result:
            return "Borrow Book Successfully !"
        else:
            return "Failed to borrow book !"
        
    def return_book(self,book_id,user_id):
        result = self.librarian_model.return_book(book_id,user_id)
        if result:
            return "Return Book Successfully !"
        else:
            return "Failed to return book !"