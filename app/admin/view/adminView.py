from app.admin.controller.adminController import AdminController
from app.admin.model.adminModel import AdminModel

class AdminView:
    def __init__(self):
        self.controller = AdminController()
        self.model = AdminModel()
        
    def show_all_use(self):
        results = self.controller.find_user()
        for user in results:
            print(f"User ID: {user[0]}, Username: {user[1]}, Role: {user[2]}")
            
    def found_use_by_id(self):
        id = input("Search ID: ")
        result = self.controller.search_user_id_to_update(id)
        if result:
            print(f"User ID: {result[0]}, Username: {result[1]}, Role: {result[2]}")
        else:
            print(result)