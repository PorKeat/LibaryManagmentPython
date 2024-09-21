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

    def list_genre(self):
        result = self.librarian_model.list_genre()
        if result:
            return result
        else:
            return None

    # TODO SEARCH  
    def search_user_by_id(self, user_id):
        result = self.librarian_model.search_user_by_id(user_id)
        if result:
            return result
        else:
            return None
    
    def search_user_by_name(self, user_name):
        results = self.librarian_model.search_user_by_name(user_name)
        if results:
            return results
        else:
            return None
        
    def search_book_by_id(self, book_id):
        result = self.librarian_model.search_book_by_id(book_id)
        if result:
            return result
        else:
            return None
        
    # TODO CREATE & ADD
    def create_book(self,title,author,publisher,copies,year,genre_id):
        result = self.librarian_model.create_book(title,author,publisher,copies,year,genre_id)
        if result:
            return "Add New Book Successfully !"
        else:
            return "Failed to add new book !"
        
    # TODO UPDATE
    def update_book_data(self, title, author_name, publisher_name, copies_available, year_of_publisher, book_id):
        result = self.librarian_model.update_book_data(title, author_name, publisher_name, copies_available, year_of_publisher, book_id)
        if result:
            return "Updated Book Successfully"
        else:
            return "Update Failed"
        
    def change_genre(self,genre,id):
        result = self.librarian_model.change_genre(genre,id)
        if result:
            return "Genre Changed Successfully"
        else:
            return "Failed To Change Genre"

    # TODO REMOVE
    def remove_book(self,id):
        result = self.librarian_model.remove_book(id)
        if result:
            return "Removed Successfully"
        else:
            return "Fail to remove"

    def remove_borrow_book(self,id):
        result = self.librarian_model.remove_borrow_book(id)
        if result:
            return "Removed Successfully"
        else:
            return "Fail to remove"