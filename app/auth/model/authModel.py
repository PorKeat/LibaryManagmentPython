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