from app.member.controller.memberController import MemberController

class MemberView:
    def __init__(self):
        self.controller = MemberController()
        
    def table_book(self,book):
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Copies: {book[4]}")
    
    def table_fines(self,fines):
        print(f"Fine ID: {fines[0]}, Amount: {fines[1]}, Date: {fines[2]}, Status: {fines[3]}")
    
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
            
    def list_borrow_book(self,login_id):
        results = self.controller.list_borrrow_book(login_id)
        if results:
            for borrow in results:
                self.table_borrow_book(borrow)
        else:
            self.not_found()
            
    def list_fines(self,login_id):
        results = self.controller.list_fines(login_id)
        if results:
            for fine in results:
                self.table_fines(fine)
        else:
            self.not_found()

    def borrow_book(self,user_id):
        self.list_book()
        book_id = int(input("Enter Book ID: "))
        result = self.controller.borrow_book(user_id ,book_id)
        print(result)
        
    def return_book(self,user_id):
        self.list_borrow_book(user_id)
        book_id = int(input("Enter Book ID: "))
        result = self.controller.return_book(book_id,user_id)
        print(result)
        
    def pay_back_fine(self,user_id):
        self.list_fines(user_id)
        fine_id = int(input("Enter Fines ID: "))
        result = self.controller.pay_back_fine(fine_id,user_id)
        print(result)