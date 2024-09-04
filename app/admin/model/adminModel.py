from db_connection import connect
import hashlib

class AdminModel:
    def __init__(self):
        self.connection = connect
        
    # ! REGISTER
    # def register(self, username, first_name, last_name, email, password, phone_number,role):
    #     encoded_password = password.encode()
    #     hashPassword = hashlib.sha256()
    #     hashPassword.update(encoded_password)
    #     hashedPass = hashPassword.hexdigest()
    #     try:
    #         with self.connection.cursor() as cursor:
    #                 cursor.execute(
    #                 """
    #                 INSERT INTO users (username, first_name, last_name, email, password, phone_number, membership_date, role_id)
    #                 VALUES (%s, %s, %s, %s, %s, %s, NOW(),%s)
    #                 """,
    #                 (username, first_name, last_name, email, hashedPass, phone_number,role)
    #             )
    #         self.connection.commit()
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback()
            
    # ! LOGIN
    # def login(self, email, password):
    #     encoded_password = password.encode()
    #     hashPassword = hashlib.sha256()
    #     hashPassword.update(encoded_password)
    #     hashedPass = hashPassword.hexdigest()
    #     try:
    #         with self.connection.cursor() as cursor:
    #             cursor.execute(
    #             """
    #             SELECT * FROM users WHERE email = %s AND password = %s
    #             """,
    #             (email, hashedPass)
    #             )
    #             results = cursor.fetchone()
    #             if results:
    #                 if results[8] == 1:
    #                     print("You are Admin")
    #                     print("Successfully")
    #                     print("User Success:", results[5])
    #                 elif results[8] == 2:
    #                     print("You are Librarian")
    #                     print("Successfully")
    #                     print("User Success:", results[5])
    #                 else:
    #                     print("You are Member")
    #                     print("Successfully")
    #                     print("User Success:", results[5])
    #             else:
    #                 print("Incorrect Email or Password!")
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback() 
    
    # ! List User
    def list_user(self):
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
                return results

        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
    def search_user_by_id(self,id):
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
                return result
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
             
    def search_user_by_name(self,name):
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
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    
    def user_exist(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM Users WHERE user_id = %s;
                    """,
                    (user_id,)
                )
                return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error: {e}")
            return False

            
    def update_user_data(self, username, first_name, last_name, phone_number, user_id):
        try:
            if self.user_exists(user_id):
                with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Users
                        SET username = %s, first_name = %s, last_name = %s, phone_number = %s
                        WHERE user_id = %s;
                        """,
                        (username, first_name, last_name, phone_number, user_id)
                    )
                    self.connection.commit()
                    return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
            
    def upgrade_role(self,role,id):
        self.listUser()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                """
                SELECT * FROM Users WHERE user_id = %s;
                """,
                (id,)
                )
                user = cursor.fetchone()
                if user:
                    cursor.execute(
                        """
                        UPDATE Users
                        SET role_id = %s
                        WHERE user_id = %s;
                        """,
                        (role,id)
                    )
                    self.connection.commit()
                    print("Role upgraded successfully !")
                else:
                    print("Failed to upgrade role !")
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()