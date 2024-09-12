from app.member.controller.memberController import MemberController

class MemberView:
    def __init__(self):
        self.controller = MemberController()
        
    def table_book(self,book):
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")
    
    def user_not_found(self):
        print("User not found !")
        
    def list_book(self):
        results = self.controller.list_book()
        if results:
            for book in results:
                self.table_book(book)
        else:
            self.user_not_found()