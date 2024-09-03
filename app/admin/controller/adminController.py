from app.admin.model.adminModel import AdminModel

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()
        
    def find_user(self):
        result = self.admin_model.listUser()
        if result:
            return result
        else:
            print("No users found !")
            
    # def search_user_id_to_update(self,id):
    #     results = self.admin_view.found_use_by_id()
    #     if results:
    #         print("Found User !")
    #         return results
    #     else:
    #         print(f"User not found ID:{id} !")
            
    def search_user_id_to_update(self, user_id):
        result = self.admin_model.searchUserByID(user_id)
        if result:
            return result
        else:
            return "User not found !"