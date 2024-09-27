from app.member.controller.memberController import MemberController
from prettytable import PrettyTable,SINGLE_BORDER

class MemberView:
    def __init__(self):
        self.controller = MemberController()
        
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
        table.field_names = ["ID", "Username", "Title", "Borrow Date", "Due Date","Return Date", "Status"]
        for borrow in book:
            table.add_row(borrow)
        print(table)
    
    def table_fines(self,fines):
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["ID","Amount","Date","Status"]
        for fine in fines:
            table.add_row(fine)
        print(table)
    

    def not_found(self):
        print("Not found !")
        
    def list_book(self):
        results = self.controller.list_book()
        if results:
            self.table_book(results)
        else:
            self.not_found()
            
    def list_borrow_book(self,login_id):
        results = self.controller.list_borrrow_book(login_id)
        if results:
            self.table_borrow_book(results)
        else:
            self.not_found()
            
    def list_fines(self,login_id):
        results = self.controller.list_fines(login_id)
        if results:
            self.table_fines(results)
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