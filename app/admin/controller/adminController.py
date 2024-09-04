from app.admin.model.adminModel import AdminModel

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()
        
    def find_user(self):
        result = self.admin_model.list_user()
        if result:
            return result
        else:
            return None
            
    def search_user_id_to_update(self, user_id):
        result = self.admin_model.search_user_by_id(user_id)
        if result:
            return result
        else:
            return None
    
    def search_user_name_to_update(self, user_name):
        results = self.admin_model.search_user_by_name(user_name)
        if results:
            return results
        else:
            return None
        
    def user_to_update(self, username, first_name, last_name, phone_number, user_id):
        result = self.admin_model.update_user_data(username, first_name, last_name, phone_number, user_id)
        if result:
            return "Updated Successfully"
        else:
            return "Update Failed"
        
    def user_to_upgrade(self,role,id):
        result = self.admin_model.upgrade_role(role,id)
        if result:
            return "Upgraded User Successfully"
        else:
            return "Upgraded User Fail"