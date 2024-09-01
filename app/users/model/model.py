from db_connection import connect
import re
import hashlib

class UserModel:
    def __init__(self) -> None:
        self.connection = connect
        
    def register(self, username, first_name, last_name, email, password, phone_number,role):
        encoded_password = password.encode()
        hashPassword = hashlib.sha256()
        hashPassword.update(encoded_password)
        hashedPass = hashPassword.hexdigest()
        try:
            with self.connection.cursor() as cursor:
                    cursor.execute(
                    """
                    INSERT INTO users (username, first_name, last_name, email, password, phone_number, membership_date, role_id)
                    VALUES (%s, %s, %s, %s, %s, %s, NOW(),%s)
                    """,
                    (username, first_name, last_name, email, hashedPass, phone_number,role)
                )
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
    def login(self, email, password):
        encoded_password = password.encode()
        hashPassword = hashlib.sha256()
        hashPassword.update(encoded_password)
        hashedPass = hashPassword.hexdigest()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                """
                SELECT * FROM users WHERE email = %s AND password = %s
                """,
                (email, hashedPass)
                )
                results = cursor.fetchone()
                if results:
                    if results[8] == 1:
                        print("You are Admin")
                        print("Successfully")
                        print("User Success:", results)
                    elif results[8] == 2:
                        print("You are Librarian")
                        print("Successfully")
                        print("User Success:", results)
                    else:
                        print("You are Member")
                        print("Successfully")
                        print("User Success:", results)
                else:
                    print("Incorrect Email or Password!")
                    
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
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