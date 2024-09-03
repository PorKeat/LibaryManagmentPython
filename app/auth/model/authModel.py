from db_connection import connect
import re
import hashlib

class AuthModel:
    def __init__(self):
        self.connection = connect
        
    def check_user(self, email, password):
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
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return None
        
    def create_user(self, username, first_name, last_name, email, password, phone_number,role):

        try:
            with self.connection.cursor() as cursor:
                    cursor.execute(
                    """
                    INSERT INTO users (username, first_name, last_name, email, password, phone_number, membership_date, role_id)
                    VALUES (%s, %s, %s, %s, %s, %s, NOW(),%s)
                    """,
                    (username, first_name, last_name, email, password, phone_number,role)
                )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False