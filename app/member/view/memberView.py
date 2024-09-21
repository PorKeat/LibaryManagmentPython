from app.member.controller.memberController import MemberController

class MemberView:
    def __init__(self):
        self.controller = MemberController()
        
    def table_book(self,book):
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")
    
    def table_borrow_book(self,book):
        print(f"Borrow ID: {book[0]}, Username: {book[1]}, Title: {book[2]}, Borrow Date: {book[3]}, Due Date: {book[4]}, Status: {book[5]}")

    def not_found(self):
        print("Not found !")
        
    def list_book(self):
        results = self.controller.list_book()
        if results:
            for book in results:
                self.table_book(book)
        else:
            self.not_found()
            
    def list_borrow_book(self):
        results = self.controller.list_borrrow_book()
        if results:
            for borrow in results:
                self.table_borrow_book(borrow)
        else:
            self.not_found()

    def borrow_book(self,user_id):
        self.list_book()
        book_id = int(input("Enter Book ID: "))
        result = self.controller.borrow_book(user_id ,book_id)
        print(result)
        
    def return_book(self,user_id):
        self.list_borrow_book()
        book_id = int(input("Enter Book ID: "))
        result = self.controller.return_book(book_id,user_id)
        print(result)