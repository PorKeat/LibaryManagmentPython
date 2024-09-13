from app.auth.model.authModel import AuthModel
import re
import hashlib

class AuthController:
    def __init__(self):
        self.user_model = AuthModel()

    def login(self, email, password):
        user_data = self.user_model.login(email, password)
        if user_data:
            user_role = user_data[8]
            if user_role == 1:
                return 'admin'
            elif user_role == 2:
                return 'librarian'
            else:
                return 'member'
        else:
            return 'error'
    
    def register(self, username, first_name, last_name, email, password, phone_number,role):
        encoded_password = password.encode()
        hashPassword = hashlib.sha256()
        hashPassword.update(encoded_password)
        hashedPass = hashPassword.hexdigest()
        result = self.user_model.register(username, first_name, last_name, email, hashedPass, phone_number,role)
        if result:
            print("Register successfully !")
        else:
            print("Failed to register")


    def validateEmail(self,email):
        if "@" not in email or "gmail" not in email or ".com" not in email:
            return False
        else:
            return True
    
    def validatePass(self,password):
        if len(password) <=5:
            return False
        if not re.search("[A-Z]",password):
            return False
        if not re.search("[a-z]",password):
            return False
        if not re.search("[0-9]",password):
            return False
        if not re.search("[!@#$%^&*]",password):
            return False
        return True
    
    def validatePhoneNumber(self,phone_number):
        if re.search("[A-Z]",phone_number):
            return False
        if re.search("[a-z]",phone_number):
            return False
        if re.search("[!@#$%^&*]",phone_number):
            return False
        return True