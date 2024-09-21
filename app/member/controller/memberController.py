from app.member.model.memberModel import MemberModel

class MemberController:
    def __init__(self):
        self.member_model = MemberModel()
    
    # ! List Book
    def list_book(self):
        result = self.member_model.list_book()
        if result:
            return result
        else:
            return None
        
    def list_borrrow_book(self,login_id):
        result = self.member_model.list_borrow_book(login_id)
        if result:
            return result
        else:
            return None
        
    def list_fines(self,login_id):
        result = self.member_model.list_fines(login_id)
        if result:
            return result
        else:
            return None
        
    def borrow_book(self,user_id ,book_id):
        result = self.member_model.borrow_book(user_id ,book_id)
        if result:
            return "Borrow Book Successfully !"
        else:
            return "Failed to borrow book !"
        
    def return_book(self,book_id,user_id):
        result = self.member_model.return_book(book_id,user_id)
        if result:
            return "Return Book Successfully !"
        else:
            return "Failed to return book !"
        
    def pay_back_fine(self, fine_id,user_id):
        result = self.member_model.pay_back_fine(fine_id,user_id)
        if result:
            return "Paid Successfully !"
        else:
            return "Failed to paid fines !"