from app.admin.controller.adminController import AdminController

class AdminView:
    def __init__(self):
        self.controller = AdminController() 
        
    def table_user(self,user):
        print(f"User ID: {user[0]}, Username: {user[1]}, Role: {user[2]}")
    
    def table_data(self,id,data):
        print(f"{id}\t{data}")
    
        
    def user_not_found(self):
        print("User not found !")
        
    def show_all_user(self):
        results = self.controller.find_user()
        if results:
            for user in results:
                self.table_user(user)
        else:
            self.user_not_found()
    
    def show_all_genre(self):
        results = self.controller.find_genre()
        print("ID\tGenre")
        if results:
            for id,genre in results:
                self.table_data(id,genre)
        else:
            self.user_not_found()
            
    def show_all_role(self):
        results = self.controller.find_role()
        print("ID\tRole")
        if results:
            for id,role in results:
                self.table_data(id,role)
        else:
            self.user_not_found()
            
    def found_user_by_id(self):
        id = input("Search ID: ")
        result = self.controller.search_user_id_to_update(id)
        if result:
            self.table_user(result)
        else:
            self.user_not_found()
    
    def found_user_by_name(self):
        name = input("Search Name: ")
        results = self.controller.search_user_name_to_update(name)
        if results:
            for result in results:
                self.table_user(result)
        else:
            self.user_not_found()
            
    def updated_user(self):
        id = input("Enter user ID: ")
        check = self.controller.search_user_id_to_update(id)
        print(check)
        if check:
            username = input("Enter username: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            result = self.controller.user_to_update(username, first_name, last_name, phone_number, id)
            print(result)
        else:
            self.user_not_found()
            
    def upgrade_user(self):
        self.show_all_role()
        id = input("Enter user ID: ")
        check = self.controller.search_user_id_to_update(id)
        print(check)
        if check:
            role = int(input("Enter role:"))
            result = self.controller.user_to_upgrade(role,id)
            print(result)
        else:
            self.user_not_found()