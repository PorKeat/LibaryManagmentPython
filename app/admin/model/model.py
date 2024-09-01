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
                        print("User Success:", results[5])
                    elif results[8] == 2:
                        print("You are Librarian")
                        print("Successfully")
                        print("User Success:", results[5])
                    else:
                        print("You are Member")
                        print("Successfully")
                        print("User Success:", results[5])
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
    
    def validatePhoneNumber(self,phone_number):
        if re.search("[A-Z]",phone_number):
            return False
        if re.search("[a-z]",phone_number):
            return False
        if re.search("[!@#$%^&*]",phone_number):
            return False
        return True
    
    def listUser(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Users.user_id, Users.username, Roles.role_name
                    FROM Users 
                    JOIN Roles ON Users.role_id = Roles.role_id;
                    """
                )
                results = cursor.fetchall()
                if results:
                    for row in results:
                        print(f"User ID: {row[0]}, Username: {row[1]}, Role: {row[2]}")
                else:
                    print("No users found !")
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
    def searchUserByID(self,id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Users.user_id, Users.username, Roles.role_name
                    FROM Users
                    JOIN Roles ON Users.role_id = Roles.role_id
                    WHERE Users.user_id = %s
                    """,
                    (id,)
                )
                result = cursor.fetchone()
                if result:
                    print(f"User ID: {result[0]}, Username: {result[1]}, Role: {result[2]}")
                else:
                    print("No user found !")
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
    def searchUserByName(self,name):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Users.user_id, Users.username, Roles.role_name
                    FROM Users
                    JOIN Roles ON Users.role_id = Roles.role_id
                    WHERE Users.username LIKE %s
                    """,
                    (f'%{name}%',)
                )
                results = cursor.fetchall()
                if results:
                    for result in results:
                        print(f"User ID: {result[0]}, Username: {result[1]}, Role: {result[2]}")
                else:
                    print("No user found !")
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()