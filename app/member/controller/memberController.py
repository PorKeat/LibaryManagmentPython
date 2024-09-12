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